from django.contrib import admin
from django.template.context_processors import static
from django.urls import path

from blog.views import home, Update
from blog.views import UserPersonalView
from blog.views import UpdatePersonalView
from blog.views import elle2
from blog.views import UpdateSecondPage

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('update/', Update.as_view(), name='update'),
    path('user/<str:name>/', UserPersonalView.as_view(), name='user'),
    path('user/<str:name>/update/', UpdatePersonalView.as_view(), name='update'),
    path('elle2/', elle2, name='elle2'),
    path('elle2/update/', UpdateSecondPage.as_view(), name='update'),
]
