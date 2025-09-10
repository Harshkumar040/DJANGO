from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),                     # /
    path('inc/', views.include_page, name="inc_page"),     # /inc/
    path('hello/', views.hello, name="hello"),             # /hello/
    path('var/', views.var),                               # /var/
    path('sum/', views.sum),                               # /sum/
    path('func/', views.func),                             # /func/
    path('getval/<int:a>/<int:b>/', views.getval),         # /getval/10/20/
    path('query/', views.query),                           # /query/?name=John&roll=12204666
    path('jsonVal/', views.jsonVal),                       # /jsonVal/
    path('first/', views.image),                           # /first/
    path('student/', views.student_list, name='student_list'),
    
]
