import pandas as pd
import spreadHandler as spread

sinfo = pd.read_csv('schoolInfo.csv', encoding='cp949')

def schoolValid(name):
    return name in sinfo.values

def register(id, school):
    spread.addRow([str(id), school, 0, 0])

def getSchool(id):
    return spread.userRow(id)[1]