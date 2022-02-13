from django.conf import settings
from ninja import NinjaAPI, Query
from ninja.security import django_auth

from .schema import Auth, Error

# disable docs and openapi endpoints by default
api_options = {"docs_url": None, "openapi_url": None}
if settings.DEBUG:
    api_options = {}
api = NinjaAPI(auth=django_auth, csrf=True, **api_options)
Query = Query(...)


@api.get("/auth", auth=None, response={200: Auth, 401: Error})
def auth(request):
    if not request.user.is_authenticated:
        return 401, Error(error="There is no user currently authenticated")
    return 200, Auth(email=request.user.email, first_name=request.user.first_name)
