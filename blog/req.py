import datetime

import requests

from blog.models import StaticValue

token = StaticValue.objects.first().token


def get_all_employees():
    result = {}
    data = {
        'token': token,
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getWaitersSales', params=data)
    list_of_dicts = response.json()['response']
    result = [{'name': d['name'], 'profit': int(int(d['profit']) / 100), 'user_id': int(d['user_id'])} for d in
              list_of_dicts if 'profit' in d]
    result.sort(key=lambda x: x['profit'], reverse=True)
    return result


def get_global_statistic():
    data = {
        'token': token,
        'format': 'json',
        'interpolate': 'month',
        'select': 'profit'
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getAnalytics', params=data)

    result = {'profit': int(float(response.json()['response']['data'][-1]))}
    max_value = int(StaticValue.objects.first().global_goal)
    result['percent'] = int(result['profit'] * 100 / max_value)
    return result


def get_today_statistic():
    current_date = datetime.datetime.now()

    # Преобразование даты в формат "ггггммдд"
    formatted_date = current_date.strftime('%Y%m%d')

    data = {
        'token': token,
        'dateFrom': formatted_date
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getSpotsSales', params=data)
    result = response.json()['response']
    result['profit'] = int(result['profit'])
    return result
