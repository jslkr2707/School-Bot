import requests
import json
import rawJson

key = "cd33b878c36e408fa240f12cbb6f4cca"

def addGrade(arr):
    result = "("
    for i in range(len(arr)):
        if arr[i] == "Y":
            result += str(i+1) + "/" if i != 2 else str(i+1)
    result += ")"

    return result

def event_list(date):
    raw = rawJson.raw('SchoolSchedule', key, {'AA_YMD': date})
    print(len(raw))
    events = '오늘 학사일정은'.split()
    grades = []

    for i in range(len(raw)):
        grades.append([raw[i]["ONE_GRADE_EVENT_YN"], raw[i]["TW_GRADE_EVENT_YN"], raw[i]["THREE_GRADE_EVENT_YN"]])
        str = "**" + raw[i]["EVENT_NM"]
        if "/" not in raw[i]["EVENT_NM"]: str += addGrade(grades[i])
        str += "**"
        if i != len(raw)-1: str += ', '
        events.append(str)
    
    events.extend('가 있습니다.\n 오늘 하루 좋은 하루 잘 보내시기 바랍니다.\n'.split())
    return events

print(event_list(20221230))
