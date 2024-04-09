
import pandas as pd
import gspread

def load_spreadsheet_data(json_file_path, spreadsheet_url, sheetname):
    # Load data from google spreadsheet
    gc = gspread.service_account(json_file_path)
    doc = gc.open_by_url(spreadsheet_url)
    worksheet = doc.worksheet(sheetname)
    cell_data = worksheet.get('A1:C100')

    # Construct Data Frame
    max_columns = len(cell_data[0])
    formatted_data = [row + [None] * (max_columns - len(row)) for row in cell_data]     # Customized the length of all rows of all rows
    patient_data = pd.DataFrame(formatted_data[1:], columns=formatted_data[0])

    first_empty_row = patient_data[patient_data['Group'].isnull()].iloc[0]['ID']
    # Column of Factor
    last_col = 'B' + str(int(first_empty_row) + 1)
    last_col2 = 'A' + str(int(first_empty_row) + 1)
    factor_value = worksheet.acell(last_col).value
    num_value = worksheet.acell(last_col2).value

    return num_value, factor_value, patient_data
