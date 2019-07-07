import django
import os
import sys
from requests_html import HTMLSession
import json

P = os.path.abspath(__file__)
P = os.path.dirname(os.path.dirname(P))

sys.path.append(P)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangor.settings")
django.setup()


from catalog.models import Agency, Category

categories = Category.objects.all()
cats_dir = {c.name: c for c in Category.objects.all()}

with open('urls.txt', 'r') as f:
    all_cats = f.read().split('\n')


session = HTMLSession()


for cat in all_cats[18:]:
    for page in range(1, 4):
        print(f'Category name to parse: {cat}')
        url = f'https://www.goodfirms.co{cat}?page={page}'
        print("Url to parse (page): "+url)
        resp = session.get(url)
        if resp.status_code == 200:
            links = resp.html.xpath('//div[@class="autowidth overflow clear bstars"]/a/@href')
            for link in links:
                resp = session.get('https://www.goodfirms.co'+link)
                agency_name = resp.html.xpath('//h1[1]/text()')[0]
                try:
                    image = resp.html.xpath('//div[@class="service-logo"]//img/@src[1]')[0]
                except:
                    image = ''
                    print(link, " none image")
                try:
                    description = resp.html.xpath('//div[@id="services-main"]/div[2]/div[2]//text()')[0]
                except:
                    description = ''
                    print(link, " none description")
                try:
                    rates = resp.html.xpath('//div[@class="firm-pricing"]/text()')[0]
                except:
                    rates = '$10+'
                    print(link, " none rates")
                try:
                    location = resp.html.xpath('//div[@class="firm-location"]/text()')[0]
                except:
                    location = ''
                    print(link, " none location")
                try:
                    year = resp.html.xpath('//div[@class="firm-founded"]/text()')[0]
                except:
                    year= ''
                    print(link, " none year")
                try:
                    employees = resp.html.xpath('//div[@class="firm-employees"]/text()')[0]
                except:
                    employees = '10+'
                    print(link, " none employees")
                try:
                    phone = resp.html.xpath('//span[@class="postal_phone"]/text()')[0]
                except:
                    phone = ''
                    print(link, " none phone")
                try:
                    email = resp.html.xpath('//div[@class="right_common_info"]/div')[0].text
                except:
                    email = ''
                    print(link, " none email")
                try:
                    address = resp.html.xpath('//div[@itemprop="address"]/div/span//text()')[:-1]
                    address = '\n'.join(address)
                except:
                    address = ''
                    print(link, " none address")

                agency_cats = []
                script_string = resp.html.xpath('//script')
                js_string = ''
                try:
                    js_string = script_string[-9].text
                    firs = js_string.find("data:")
                    js_string = js_string[firs + 6:]
                    end = js_string.find("]")
                    js_string = js_string[:end + 1]
                    jsok = json.loads(js_string)
                except:
                    print('js_string not found' +link)

                for cater in jsok:
                    agency_cats.append(cater['name'])

                try:
                    agen = Agency.objects.create(
                        name=agency_name,
                        origin_image=image,
                        description=description,
                        rates=rates,
                        location=location,
                        year=year,
                        employees=employees,
                        phone=phone,
                        email=email,
                        address=address,
                    )



                    for categ in agency_cats:
                        try:
                            category = cats_dir[categ]
                            agen.cats.add(category)
                        except:
                            print("exeption in" + category)
                except Exception as e:
                    print("!MAX! Error while saving: ", e)


        else:
            raise NameError("Google Response Error: " + str(resp.status_code))
