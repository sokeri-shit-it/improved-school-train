from django.urls import path, include
from App import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('personal_area', views.personal_area, name='pres_area'),
    path('register', views.register, name='register_me'),
    path('pay', views.pay, name='pay'),

    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
]
