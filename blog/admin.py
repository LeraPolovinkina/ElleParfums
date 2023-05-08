import os

from django.contrib import admin

import blog
from blog.models import StaticValue
from django.contrib.auth.models import User, Group

# Отключаем отображение модели User и Group в административной панели
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
class StaticValueAdmin(admin.ModelAdmin):
    # Определение отображаемых полей и других настроек

    def has_add_permission(self, request):
        # Запрет на добавление новых объектов
        return False

    def has_delete_permission(self, request, obj=None):
        # Запрет на удаление объектов
        return False

    def save_model(self, request, obj, form, change):
        # Получаем новый файл из формы
        new_file = form.cleaned_data.get('pizza_sound')

        # Получаем объект модели и путь к текущему файлу
        obj = form.save(commit=False)
        old_file_path = obj.pizza_sound.path

        # Удаляем текущий файл перед сохранением нового
        if os.path.exists(old_file_path):
            os.remove(old_file_path)

        # Сохраняем новый файл и модель
        obj.pizza_sound = new_file
        obj.save()
        form.save_m2m()

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'profit', 'is_active', 'goal')  # Поля, отображаемые в списке пользователей
    list_filter = ('is_active',)  # Фильтр по активному/неактивному статусу
    search_fields = ('name', 'profit')  # Поля, по которым можно искать пользователей
    list_editable = ('is_active', 'goal',)  # Добавляем атрибут list_editable для редактирования is_active


admin.site.register(blog.models.User, UserAdmin)


admin.site.register(StaticValue, StaticValueAdmin)
