from django.shortcuts import render

from blog import req
from blog.models import User, StaticValue


def home(request):
    # Данные, которые вы хотите передать на страницу
    employee = User.objects.filter(is_active=True)

    new_api_users = req.get_all_employees()
    today = req.get_today_statistic()
    month = req.get_global_statistic()

    # Обновление или создание пользователей в базе данных Django
    for api_user in new_api_users:
        # Попытка найти пользователя по email в базе данных
        try:
            user = User.objects.get(user_id=int(api_user['user_id']))
            user.profit = int(api_user['profit'])
            user.save()
        except User.DoesNotExist:
            user = User(
                name=api_user['name'],
                profit=int(api_user['profit']),
                user_id=int(api_user['user_id'])
                # ... и так далее
            )
            user.save()
    # Сохранение нового пользователя

    my_variable_value = StaticValue.objects.first()
    # Передача данных в шаблон
    context = {'employee': employee,
               'variable': my_variable_value,
               'today': today,
               'month': month}

    # Возврат отрендеренного представления с передачей контекста
    return render(request, 'index.html', context)

