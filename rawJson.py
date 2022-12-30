import requests
import json

key = "8ac24597df1b4f379534042401554d00"

def raw(field, key, dict):
    url = f"https://open.neis.go.kr/hub/{field}?KEY={key}&Type=json&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7010137"
    for i in dict:
        url += "&" + i + "=" + str(dict[i])
    try:
        row = json.loads(requests.get(url).text)[field][1]['row']
        return row
    except:
        return '없습니다'

