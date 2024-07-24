from django.contrib import admin
from .models import ExtendUser
from django.apps import apps # imports the apps object, allows you to access the configuration of installed Django apps

admin.site.register(ExtendUser)

# Getting the config objects for the graphql_auth app. Contains metadata including models.
app = apps.get_app_config('graphql_auth')

# This loop iterates over all the models defined in the `graphql_auth` app.
for model_name, model in app.models.items():
    admin.site.register(model)


# app.models is a dictionary where the keys are the model names and the values are the model classes.