from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('var/', views.var),
    path('sum/', views.sum,),
    path('func/', views.func,),
]
