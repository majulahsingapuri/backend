from django.urls import Resolver404, resolve

from .models import Request


def request_logger(get_response):
    def middleware(request):
        method = request.method
        try:
            match = resolve(request.path)
        except Resolver404:
            pass
        else:
            if request.user.is_authenticated:
                Request.objects.create(
                    user=request.user,
                    method=method,
                    route=match.route,
                    kwargs=match.kwargs,
                )
        return get_response(request)

    return middleware
