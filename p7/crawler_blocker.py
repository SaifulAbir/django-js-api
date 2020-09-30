import json
import string
from random import choice, Random

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render


class P7CrawlerBlockerMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/staff"):
            return self.get_response(request)
        # get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        # unique key for each IP
        ip_cache_key = "django_bot_crawler_blocker:ip_rate" + ip

        ip_hits_timeout = settings.IP_HITS_TIMEOUT if hasattr(settings, 'IP_HITS_TIMEOUT') else 60
        max_allowed_hits = settings.MAX_ALLOWED_HITS_PER_IP if hasattr(settings, 'MAX_ALLOWED_HITS_PER_IP') else 2000

        # get the hits by this IP in last IP_TIMEOUT time
        this_ip_hits = cache.get(ip_cache_key)

        if not this_ip_hits:
            this_ip_hits = 1
            cache.set(ip_cache_key, this_ip_hits, ip_hits_timeout)
        else:
            this_ip_hits += 1
            cache.set(ip_cache_key, this_ip_hits)

        print(f"{ip}: {this_ip_hits} of {max_allowed_hits}")

        if this_ip_hits > max_allowed_hits and request.path != "/api/captcha":
            if request.path == "/api/resolve-captcha/":
                data = json.loads(request.body.decode('utf-8'))
                if data.get("captcha") and  cache.get("captcha") and \
                    data.get("captcha").upper() == cache.get("captcha").upper():
                    this_ip_hits = 0
                    cache.set(ip_cache_key, this_ip_hits, ip_hits_timeout)
                    response = self.get_response(request)
                    return response
            return render(request, 'captcha.html')
        else:
            return self.get_response(request)


def get_captcha(request):
    w_box, h_box = 100, 100
    offset = 60
    w_canvas, h_canvas = 500, 100
    im = Image.new('RGB', (w_canvas, h_canvas))
    char_length = 5

    letters = string.ascii_letters + "23456789"
    text = ''.join(choice(letters) for i in range(char_length))
    cache.set("captcha", text)
    rand = Random()
    print(text)
    for i in range(char_length):
        box = Image.new("RGB", (w_box, h_box), (245,217,29))
        draw = ImageDraw.Draw(box)
        x = rand.randint(offset/2, w_box - offset)
        y = rand.randint(offset/2, h_box - offset)
        r = rand.randint(50, 150)
        g = rand.randint(50, 150)
        b = rand.randint(50, 150)
        font_size = rand.randint(50, 60)
        font = ImageFont.truetype('resources/Westmeath.otf', font_size)
        draw.text(
            (x, y),
            text[i],
            fill=f'rgb({r}, {g}, {b})',
            font=font
        )
        blurred = box.filter(ImageFilter.BLUR)
        degree = rand.randint(-60, 60)
        rotated = blurred.rotate(degree, fillcolor=(50,50,50))

        im.paste(rotated, (i * w_box, 0 , (i+1) * w_box, h_box))

    for i in range(20):
        x1 = rand.randint(0, w_canvas)
        y1 = rand.randint(0, h_canvas)
        x2 = rand.randint(0, w_canvas)
        y2 = rand.randint(0, h_canvas)
        r = rand.randint(50, 150)
        g = rand.randint(50, 150)
        b = rand.randint(50, 150)
        draw = ImageDraw.Draw(im)
        draw.line((x1, y1, x2, y2),width=2 , fill=f'rgb({r}, {g}, {b})')

    response = HttpResponse(content_type="image/png")
    im.save(response, "PNG")
    return response