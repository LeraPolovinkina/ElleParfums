import datetime

import requests

from blog.models import StaticValue


def get_all_employees():
    result = {}
    start_of_month = StaticValue.objects.first().date

    # Форматирование даты в строку в формате "ггггммдд"
    formatted_start_of_month = start_of_month.strftime("%Y%m%d")
    data = {
        'token': StaticValue.objects.first().token,
        'dateFrom': formatted_start_of_month
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getWaitersSales', params=data)
    list_of_dicts = response.json()['response']
    result = [{'name': d['name'], 'profit': int(int(d['profit']) / 100), 'user_id': int(d['user_id'])} for d in
              list_of_dicts if 'profit' in d]
    result.sort(key=lambda x: x['profit'], reverse=True)
    return result


def get_global_statistic():
    now = datetime.datetime.now()

    # Получение даты начала текущего месяца
    start_of_month = datetime.datetime(now.year, now.month, 1)

    # Форматирование даты в строку в формате "ггггммдд"
    formatted_start_of_month = start_of_month.strftime("%Y%m%d")

    data = {
        'token': StaticValue.objects.first().token,
        # 'format': 'json',
        # 'interpolate': 'month',
        'dateFrom': formatted_start_of_month,
        'spot_id': 2
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getSpotsSales', params=data)

    result = {'profit': int(float(response.json()['response']['revenue']))}
    max_value = int(StaticValue.objects.first().global_goal)
    result['percent'] = int(result['profit'] * 100 / max_value)
    return result


def get_today_statistic():
    current_date = datetime.datetime.now()

    # Преобразование даты в формат "ггггммдд"
    formatted_date = current_date.strftime('%Y%m%d')

    data = {
        'token': StaticValue.objects.first().token,
        'dateFrom': formatted_date
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getSpotsSales', params=data)
    result = response.json()['response']
    result['profit'] = int(result['revenue'])
    return result
