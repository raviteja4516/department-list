from django.urls import path
from . import views
app_name = 'testapp'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('apply/',views.application,name='apply'),
    path('index/', views.index, name='index'),
    path('detail/<int:department_id>/',views.detail,name='detail'),
    path('detailing/<int:department_id>/',views.detailing,name='detailing'),

]

