from django.contrib import admin
from .views import test_view, test_view_final
from django.urls import path

urlpatterns = [
    path('test', test_view), тестовый путь на котором есть форма отправки
    path('test2', test_view_final, name='test_final'),
]
