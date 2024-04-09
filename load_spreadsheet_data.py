
import pandas as pd
import gspread

def load_spreadsheet_data(json_file_path, spreadsheet_url, sheetname):
    # Load data from google spreadsheet
    gc = gspread.service_account(json_file_path)
    doc = gc.open_by_url(spreadsheet_url)
    worksheet = doc.worksheet(sheetname)
    cell_data = worksheet.get('A1:C100')

    # Construct Data Frame
    import pandas as pd

    # 셀 데이터
    # 모든 행의 길이를 헤더의 길이와 동일하게 맞춤
    max_columns = len(cell_data[0])
    formatted_data = [row + [None] * (max_columns - len(row)) for row in cell_data]
    patient_data = pd.DataFrame(formatted_data[1:], columns=formatted_data[0])

    #patient_data = pd.DataFrame(cell_data[1:], columns=cell_data[0])
    first_empty_row = patient_data[patient_data['Group'].isnull()].iloc[0]['ID']
    # Column of Factor
    last_col = 'B' + str(int(first_empty_row) + 1)
    factor_value = worksheet.acell(last_col).value

    return factor_value, patient_data
