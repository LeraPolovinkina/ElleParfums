import datetime
from calendar import month

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from blog import req
from blog.models import UserVictory, StaticValueVictory
from blog.models import UserEnglishDistrict, StaticValueEnglishDistrict


def home(request):
    # Данные, которые вы хотите передать на страницу
    my_variable_value = StaticValueVictory.objects.first()
    employee = UserVictory.objects.filter(is_active=True).order_by('-profit')

    new_api_users = req.get_all_employees()
    today = req.get_today_statistic()
    month = req.get_global_statistic()

    # Обновление или создание пользователей в базе данных Django
    users = UserVictory.objects.all()
    for user in users:
        flag = False
        api_user = None
        for api_user in new_api_users:
            if user.user_id == (api_user['user_id']):
                flag = True
                api_user = api_user
                break
        if flag:
            user.profit = int(api_user['profit'])
            user.save()
            new_api_users.remove(api_user)
        else:
            user.profit = 0
            user.save()
    print(new_api_users)
    for api_user in new_api_users:
        user = UserVictory(
            name=api_user['name'],
            profit=int(api_user['profit']),
            user_id=int(api_user['user_id'])
            # ... и так далее
        )
        user.save()
    # Сохранение нового пользователя


    current_date = datetime.date.today()

    # Преобразовать текущую дату в формат "дд.мм.гггг"
    formatted_date = current_date.strftime("%d.%m.%Y")
    # Передача данных в шаблон
    context = {'first': employee[0],
                'users': employee[1:],
                'variable': my_variable_value,
                'current_date': formatted_date,
                'today': today,
                'month': month}

    # Возврат отрендеренного представления с передачей контекста
    return render(request, 'index.html', context)

class Update(View):
    def get(self, request, *args, **kwargs):
        employee = UserVictory.objects.filter(is_active=True).order_by('-profit')

        new_api_users = req.get_all_employees()
        today = req.get_today_statistic()
        month = req.get_global_statistic()

        # Обновление или создание пользователей в базе данных Django
        users = UserVictory.objects.all()
        for user in users:
            flag = False
            api_user = None
            for api_user in new_api_users:
                if user.user_id == (api_user['user_id']):
                    flag = True
                    api_user = api_user
                    break
            if flag:
                user.profit = int(api_user['profit'])
                user.save()
                new_api_users.remove(api_user)
            else:
                user.profit = 0
                user.save()
        print(new_api_users)
        for api_user in new_api_users:
            user = UserVictory(
                name=api_user['name'],
                profit=int(api_user['profit']),
                user_id=int(api_user['user_id'])
                # ... и так далее
            )
            user.save()
        # Сохранение нового пользователя

        my_variable_value = StaticValueVictory.objects.first()

        current_date = datetime.date.today()

        # Преобразовать текущую дату в формат "дд.мм.гггг"
        formatted_date = current_date.strftime("%d.%m.%Y")
        # # Преобразование QuerySet в список словарей
        employee_data = serializers.serialize('json', employee)
        static_v = {'global_goal': my_variable_value.global_goal,
                    'employee_goal': my_variable_value.employee_goal,
                    'today_goal': my_variable_value.today_goal,
                    'success_color': my_variable_value.success_color,
                    'show_users_15_and_20_percent': my_variable_value.show_users_15_and_20_percent,
                    'pizza_sound': my_variable_value.pizza_sound.name,
                    'sale_sound': my_variable_value.sale_sound.name,
                    'current_date': formatted_date,
                    'date_turn_on': my_variable_value.date_turn_on}
        print(static_v)
        # Логика обработки AJAX-запроса и формирования данных для отправки клиенту
        data = {'users': employee_data,
                'variable': static_v,
                'today': today,
                'month': month}
        return JsonResponse(data)

# Личные кабинеты для пользователей
class UserPersonalView(View):
    template_name = 'personal_page.html'

    def get(self, request, name):
        try:
            user = UserVictory.objects.get(name=name)
        except UserVictory.DoesNotExist:
            return render(request, 'user_not_found.html', {'name': name})

        my_variable_value = StaticValueVictory.objects.first()
        today = req.get_today_statistic()
        month = req.get_global_statistic()

        context = {
            'user': user,
            'variable': my_variable_value,
            'today': today,
            'month': month
        }

        return render(request, self.template_name, context)

class UpdatePersonalView(View):
    def get(self, request, name):
        try:
            user = UserVictory.objects.get(name=name)
        except UserVictory.DoesNotExist:
            return JsonResponse({'error': f'Сортудник {name} не найден'})

        # Ваша логика обновления данных для конкретного пользователя

        my_variable_value = StaticValueVictory.objects.first()
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%d.%m.%Y")

        today = req.get_today_statistic()
        month = req.get_global_statistic()

        static_v = {
            'global_goal': my_variable_value.global_goal,
            'employee_goal': my_variable_value.employee_goal,
            'today_goal': my_variable_value.today_goal,
            'success_color': my_variable_value.success_color,
            'show_users_15_and_20_percent': my_variable_value.show_users_15_and_20_percent,
            'pizza_sound': my_variable_value.pizza_sound.name,
            'sale_sound': my_variable_value.sale_sound.name,
            'current_date': formatted_date,
            'date_turn_on': my_variable_value.date_turn_on,
        }

        # Логика обработки AJAX-запроса и формирования данных для отправки клиенту
        user_data = serializers.serialize('json', [user])
        data = {
            'users': user_data,
            'variable': static_v,
            'today': today,
            'month': month
        }

        return JsonResponse(data)

def elle2(request):
    # Данные, которые вы хотите передать на страницу
    my_variable_value = StaticValueEnglishDistrict.objects.first()
    employee = UserEnglishDistrict.objects.filter(is_active=True).order_by('-profit')

    new_api_users = req.get_all_employees()
    today = req.get_today_statistic()
    month = req.get_global_statistic()

    # Обновление или создание пользователей в базе данных Django
    users = UserEnglishDistrict.objects.all()
    for user in users:
        flag = False
        api_user = None
        for api_user in new_api_users:
            if user.user_id == (api_user['user_id']):
                flag = True
                api_user = api_user
                break
        if flag:
            user.profit = int(api_user['profit'])
            user.save()
            new_api_users.remove(api_user)
        else:
            user.profit = 0
            user.save()
    print(new_api_users)
    for api_user in new_api_users:
        user = UserEnglishDistrict(
            name=api_user['name'],
            profit=int(api_user['profit']),
            user_id=int(api_user['user_id'])
            # ... и так далее
        )
        user.save()
    # Сохранение нового пользователя


    current_date = datetime.date.today()

    # Преобразовать текущую дату в формат "дд.мм.гггг"
    formatted_date = current_date.strftime("%d.%m.%Y")
    # Передача данных в шаблон
    context = {'first': employee[0],
                'users': employee[1:],
                'variable': my_variable_value,
                'current_date': formatted_date,
                'today': today,
                'month': month}

    # Возврат отрендеренного представления с передачей контекста
    return render(request, 'english_district.html', context)

class UpdateSecondPage(View):
    def get(self, request, *args, **kwargs):
        employee = UserEnglishDistrict.objects.filter(is_active=True).order_by('-profit')

        new_api_users = req.get_all_employees_elle2()
        today = req.get_today_statistic_elle2()
        month = req.get_global_statistic_elle2()

        # Обновление или создание пользователей в базе данных Django
        users = UserEnglishDistrict.objects.all()
        for user in users:
            flag = False
            api_user = None
            for api_user in new_api_users:
                if user.user_id == (api_user['user_id']):
                    flag = True
                    api_user = api_user
                    break
            if flag:
                user.profit = int(api_user['profit'])
                user.save()
                new_api_users.remove(api_user)
            else:
                user.profit = 0
                user.save()
        print(new_api_users)
        for api_user in new_api_users:
            user = UserEnglishDistrict(
                name=api_user['name'],
                profit=int(api_user['profit']),
                user_id=int(api_user['user_id'])
                # ... и так далее
            )
            user.save()
        # Сохранение нового пользователя

        my_variable_value = StaticValueEnglishDistrict.objects.first()

        current_date = datetime.date.today()

        # Преобразовать текущую дату в формат "дд.мм.гггг"
        formatted_date = current_date.strftime("%d.%m.%Y")
        # # Преобразование QuerySet в список словарей
        employee_data = serializers.serialize('json', employee)
        static_v = {'global_goal': my_variable_value.global_goal,
                    'employee_goal': my_variable_value.employee_goal,
                    'today_goal': my_variable_value.today_goal,
                    'success_color': my_variable_value.success_color,
                    'show_users_15_and_20_percent': my_variable_value.show_users_15_and_20_percent,
                    'pizza_sound': my_variable_value.pizza_sound.name,
                    'sale_sound': my_variable_value.sale_sound.name,
                    'current_date': formatted_date,
                    'date_turn_on': my_variable_value.date_turn_on}
        print(static_v)
        # Логика обработки AJAX-запроса и формирования данных для отправки клиенту
        data = {'users': employee_data,
                'variable': static_v,
                'today': today,
                'month': month}
        return JsonResponse(data)