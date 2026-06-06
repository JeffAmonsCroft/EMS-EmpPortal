from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcomepage_view, name='index'),
    path('emp_portal/login', views.login_view, name='login'),
    path('emp_portal/home', views.homepage_view, name='home'),
    # path('emp_portal/complaints', views.complaint_view, name='complaints'),
    path('emp_portal/logout', views.logout_view, name='logout'),
]