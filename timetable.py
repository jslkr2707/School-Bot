import requests
import json
import rawJson

key = "8ac24597df1b4f379534042401554d00"

def subjects(date):
    subjects = '오늘 수업 과목은'.split()
    for i in rawJson.raw('hisTimetable', key, {'AY': 2022, 'SEM': 2, 'ALL_TI_YMD': date, 'GRADE': 1, 'CLASS_NM': 8}):
        subjects.append("**" + i['ITRT_CNTNT'] + "**")

    for j in range(3, len(subjects) - 1):
        subjects[j] += ', '
    subjects.extend('입니다.\n 수업을 잘 듣나 돌아다니며 감시를 할 예정이므로, 잘 들으면 좋겠습니다.'.split())
    return subjects

