import os

from django.contrib import admin

import blog
from blog.models import StaticValueVictory
from django.contrib.auth.models import User, Group
from blog.models import StaticValueEnglishDistrict

# Отключаем отображение модели User и Group в административной панели
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
class StaticValueVictoryAdmin(admin.ModelAdmin):

    # Определение отображаемых полей и других настроек

    def has_add_permission(self, request):
        # Запрет на добавление новых объектов
        return False

    def has_delete_permission(self, request, obj=None):
        # Запрет на удаление объектов
        return False

class  StaticValueEnglishDistrictAdmin(admin.ModelAdmin):

    # Определение отображаемых полей и других настроек

    def has_add_permission(self, request):
        # Запрет на добавление новых объектов
        return False
    #
    def has_delete_permission(self, request, obj=None):
        # Запрет на удаление объектов
        return False

class UsersVictoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'profit', 'is_active', 'goal')  # Поля, отображаемые в списке пользователей
    list_filter = ('is_active',)  # Фильтр по активному/неактивному статусу
    search_fields = ('name', 'profit')  # Поля, по которым можно искать пользователей
    list_editable = ('is_active', 'goal')  # Добавляем атрибут list_editable для редактирования is_active

class UsersEnglishDistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'profit', 'is_active', 'goal')  # Поля, отображаемые в списке пользователей
    list_filter = ('is_active',)  # Фильтр по активному/неактивному статусу
    search_fields = ('name', 'profit')  # Поля, по которым можно искать пользователей
    list_editable = ('is_active', 'goal')  # Добавляем атрибут list_editable для редактирования is_active

admin.site.register(blog.models.UserVictory, UsersVictoryAdmin)
admin.site.register(blog.models.UserEnglishDistrict, UsersEnglishDistrictAdmin)
admin.site.register(StaticValueVictory, StaticValueVictoryAdmin)
admin.site.register(StaticValueEnglishDistrict,  StaticValueEnglishDistrictAdmin)
