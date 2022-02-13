from django.apps import apps
from django.contrib import admin

app = apps.get_app_config("app")
for model in app.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
