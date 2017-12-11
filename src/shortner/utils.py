import random
import string
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)


def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    klass = instance.__class__
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    while qs_exists:
        new_code = create_shortcode(size=size)
        qs_exists = klass.objects.filter(shortcode=new_code).exists()
    return new_code
