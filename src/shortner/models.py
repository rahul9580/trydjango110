from django.db import models

from .utils import create_shortcode

from django.conf import settings

SHORTCOCE_MAX = getattr(settings, 'SHORTCOCE_MAX', 15)


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=False)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            if q.shortcode == 'abc':
                q.shortcode = create_shortcode(q)
                print (q.shortcode)
                q.save()
                new_codes += 1
        return "New code made: {i}".format(i=new_codes)


class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(
        max_length=SHORTCOCE_MAX, default='abc', blank=True, )
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    def save(self, *args, **kwargs):
        if not self.shortcode or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(args, kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)


'''
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
'''
