from oauth2client.service_account import ServiceAccountCredentials
import gspread
def updateTosheet(json_file_path, spreadsheet_url,sheetname, assigned_group, num):
    # Automatically updating the Google Spreadsheet with results
    # Google Sheets API 인증
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_file_path, scope)
    client = gspread.authorize(creds)

    # Open spreadsheet
    spreadsheet = client.open_by_url(spreadsheet_url)  # 스프레드시트 이름으로 열기
    worksheet = spreadsheet.worksheet(sheetname)  # 워크시트 이름으로 열기

    # Update result to Google spreadsheet
    row_num = int(num)+1
    col_num = 3
    cell = worksheet.cell(row_num, col_num)
    worksheet.update_cell(row_num, col_num, assigned_group)

    return print("Done")
