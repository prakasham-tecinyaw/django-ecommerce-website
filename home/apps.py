from django.apps import AppConfig
from django.contrib.admin.appss import AdminConfig

class HomeConfig(AppConfig):
    name = 'home'

class AppAdminConfig(AdminConfig):
    default_site = 'home.admin.AppAdminArea'