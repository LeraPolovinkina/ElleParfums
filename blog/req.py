import datetime

import requests

from blog.models import StaticValueVictory, StaticValueEnglishDistrict


def get_all_employees():
    result = {}
    start_of_month = StaticValueVictory.objects.first().date
    isStart = StaticValueVictory.objects.first().use_start_of_month
    if isStart:
        now = datetime.datetime.now()

        # Получение даты начала текущего месяца
        start_of_month = datetime.datetime(now.year, now.month, 1)
    # Форматирование даты в строку в формате "ггггммдд"
    formatted_start_of_month = start_of_month.strftime("%Y%m%d")
    print(formatted_start_of_month)
    data = {
        'token': StaticValueVictory.objects.first().token,
        'dateFrom': formatted_start_of_month
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getWaitersSales', params=data)
    list_of_dicts = response.json()['response']
    result = [{'name': d['name'], 'profit': int(int(d['profit']) / 100), 'user_id': int(d['user_id'])} for d in
              list_of_dicts if 'profit' in d]
    result.sort(key=lambda x: x['profit'], reverse=True)
    print(result)
    return result


def get_global_statistic():
    now = datetime.datetime.now()

    # Получение даты начала текущего месяца
    start_of_month = datetime.datetime(now.year, now.month, 1)

    # Форматирование даты в строку в формате "ггггммдд"
    formatted_start_of_month = start_of_month.strftime("%Y%m%d")

    data = {
        'token': StaticValueVictory.objects.first().token,
        'dateFrom': formatted_start_of_month,
        'spot_id': 2
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getSpotsSales', params=data)

    # result = {'profit': int(float(response.json()['response']['revenue']))}
    result = {'profit': int(float(response.json()['response']['profit']))}
    max_value = int(StaticValueVictory.objects.first().global_goal)
    result['percent'] = int(result['profit'] * 100 / max_value)
    print(result)
    print(response)
    return result


def get_today_statistic():
    current_date = datetime.datetime.now()

    # Преобразование даты в формат "ггггммдд"
    formatted_date = current_date.strftime('%Y%m%d')

    data = {
        'token': StaticValueVictory.objects.first().token,
        'dateFrom': formatted_date
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getSpotsSales', params=data)
    result = response.json()['response']
    result['profit'] = int(result['revenue'])
    # result['profit'] = int(result['profit'])
    print(result)
    return result


def get_all_employees_elle2():
    result = {}
    start_of_month = StaticValueEnglishDistrict.objects.first().date
    isStart = StaticValueEnglishDistrict.objects.first().use_start_of_month
    if isStart:
        now = datetime.datetime.now()

        # Получение даты начала текущего месяца
        start_of_month = datetime.datetime(now.year, now.month, 1)
    # Форматирование даты в строку в формате "ггггммдд"
    formatted_start_of_month = start_of_month.strftime("%Y%m%d")
    print(formatted_start_of_month)
    data = {
        'token': StaticValueEnglishDistrict.objects.first().token,
        'dateFrom': formatted_start_of_month
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getWaitersSales', params=data)
    list_of_dicts = response.json()['response']
    result = [{'name': d['name'], 'profit': int(int(d['profit']) / 100), 'user_id': int(d['user_id'])} for d in
              list_of_dicts if 'profit' in d]
    result.sort(key=lambda x: x['profit'], reverse=True)
    print(result)
    return result

def get_global_statistic_elle2():
    now = datetime.datetime.now()

    # Получение даты начала текущего месяца
    start_of_month = datetime.datetime(now.year, now.month, 1)

    # Форматирование даты в строку в формате "ггггммдд"
    formatted_start_of_month = start_of_month.strftime("%Y%m%d")

    data = {
        'token': StaticValueEnglishDistrict.objects.first().token,
        'dateFrom': formatted_start_of_month,
        'spot_id': 1
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getSpotsSales', params=data)
    result = {'profit': int(float(response.json()['response']['profit']))}
    max_value = int(StaticValueVictory.objects.first().global_goal)
    result['percent'] = int(result['profit'] * 100 / max_value)
    print(result)
    return result


def get_today_statistic_elle2():
    current_date = datetime.datetime.now()

    # Преобразование даты в формат "ггггммдд"
    formatted_date = current_date.strftime('%Y%m%d')

    data = {
        'token': StaticValueEnglishDistrict.objects.first().token,
        'dateFrom': formatted_date,
        'spot_id': 1
    }
    response = requests.get(
        'https://joinposter.com/api/dash.getSpotsSales', params=data)
    result = response.json()['response']
    result['profit'] = int(result['revenue'])
    # result['profit'] = int(result['profit'])
    print(result)
    return result
