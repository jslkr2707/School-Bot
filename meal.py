import requests
import json
import rawJson

key = "17e7a88580d24bb4b3485fa2fd37cdad"

def meal_list(date):
    meal = '오늘 급식은'.split() + rawJson.raw('mealServiceDietInfo', key, {'MLSV_YMD': '20221230'})[0]['DDISH_NM'].split()

    for i in range(2, len(meal)):
        arr = list(meal[i])
        while "(" in arr or "<" in arr:
            if "(" in arr:
                del arr[arr.index('('):arr.index(')')+1]
            if "<" in arr:
                del arr[arr.index('<'):arr.index('>')+1]

        meal[i] = ''.join(arr).replace("☆", "")
        if meal[i] == '':
            continue
        meal[i] = "**" + meal[i] + "**"

    for j in range(2, len(meal)-1):
        meal[j] += ', '
    
    meal.extend('입니다.\n 맛있게 드시기 바랍니다.\n\n'.split())
    return meal

print(meal_list(20221229))