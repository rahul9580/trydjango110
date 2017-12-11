from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import KirrURL


# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    # import ipdb
    # ipdb.set_trace()
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponse('hello {sc}'.format(sc=obj.url))


class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse('hello {sc}'.format(sc=obj.url))
