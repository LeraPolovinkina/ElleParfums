from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

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
    context = {'users': employee,
               'variable': my_variable_value,
               'today': today,
               'month': month}

    # Возврат отрендеренного представления с передачей контекста
    return render(request, 'index.html', context)

class Update(View):
    def get(self, request, *args, **kwargs):
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

        # # Преобразование QuerySet в список словарей
        employee_data = serializers.serialize('json', employee)
        static_v = {'global_goal':my_variable_value.global_goal, 'employee_goal': my_variable_value.employee_goal, 'today_goal' : my_variable_value.today_goal}

        # Логика обработки AJAX-запроса и формирования данных для отправки клиенту
        data = {'users': employee_data,
                'variable': static_v,
                'today': today,
                'month': month}
        print(data)
        return JsonResponse(data)