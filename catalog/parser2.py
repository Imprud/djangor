import django
import os
import sys
from requests_html import HTMLSession
from pprint import pprint

P = os.path.abspath(__file__)
P = os.path.dirname(os.path.dirname(P))

sys.path.append(P)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangor.settings")
django.setup()


from catalog.models import Agency, Category

# categories = Category.objects.all()
# print(categories)


session = HTMLSession()
resp = session.get('https://www.goodfirms.co/directories')

all_cats = {}
cats_text = resp.html.xpath('//div[@class="explore-page-left"]//li//a/text()')
cats_links = resp.html.xpath('//div[@class="explore-page-left"]//li//a/@d-href')

for n, cat_text in enumerate(cats_text):
    print(cat_text)
    print(cats_links[n])
    resp = session.get('https://www.goodfirms.co'+cats_links[n])
    cat_descr = resp.html.xpath('//div[@class="clear whitebg"]//p//text()')[0]

    cat = Category.objects.create(
        name=cat_text,
        text=cat_descr
    )



