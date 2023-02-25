import requests
import json
import pandas as pd
import datetime
import numpy as np
import dataframe_image as dfi

def toDate(num):
    return num.isoformat().replace("-", "")

key = "8ac24597df1b4f379534042401554d00"
start = datetime.date.today() - datetime.timedelta(days = datetime.date.today().weekday())
end = start + datetime.timedelta(days=4)

def getMonday():
    return start.isoformat()

def timetable(grade, class_no):
    url = f"https://open.neis.go.kr/hub/hisTimetable?KEY={key}&Type=json&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7010137&GRADE={grade}&CLASS_NM={class_no}&AY=2022&TI_FROM_YMD={toDate(start)}&TI_TO_YMD={toDate(end)}"

    try:
        row = np.array(json.loads(requests.get(url).text)['hisTimetable'][1]['row'])
    except:
        return '없습니다'
    days = np.array([i for i in range(len(row)) if row[i]['PERIO'] == '1'] + [len(row)])
    subjects = [[i['ITRT_CNTNT'] for i in row[days[j]:days[j+1]]] for j in range(len(days)-1)]
    for i in subjects: 
        if len(i) < 7: i.append('X')
    weekdays = ['월', '화', '수', '목', '금']
    timetable = pd.DataFrame(dict([(k, v) for k, v in zip(weekdays, subjects)])); timetable.index += 1

    dfi.export(timetable, f'image/{start.isoformat()}.png', max_cols=-1, max_rows=-1)
