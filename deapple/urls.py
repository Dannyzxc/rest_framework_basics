from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    # path('select/<int:pk>', views.select, name='select'),
    # path('studentlist', views.student_list, name='student-list'),
    # path('studentlistjson', views.student_list_json, name='student-list-json'),
]
