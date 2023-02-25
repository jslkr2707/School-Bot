import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'schoolbot-378901-78d53f5eb0f2.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1EG5qTBC6zOIRAlEbKgUON-MyNr6tSbehXgCHemPuKYw/edit#gid=0'
# 스프레스시트 문서 가져오기 
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('시트1')

# region get

def getWorksheet():
    return worksheet

def getRow(row) -> list:
    return worksheet.row_values(row)

def getCol(col) -> list:
    return worksheet.col_values(col)

def getCell(col: str, row: int):
    cell = col+str(row)
    return worksheet.acell(cell).value

# endregion

# region write

def addRow(values: list): # add a row to the end of the sheet
    worksheet.append_row(values)

# endregion

def userIndex(id):
    return worksheet.find(str(id)).row

def userRow(id):
    return worksheet.row_values(userIndex(id))

def userValid(id):
    arr = worksheet.col_values(1)
    return str(id) in arr

def gradeValid(id):
    return userRow(id)[2] != 0