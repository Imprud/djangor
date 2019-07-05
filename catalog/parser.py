import django
import os
import sys
from requests_html import HTMLSession
from time import sleep

P = os.path.abspath(__file__)
P = os.path.dirname(os.path.dirname(P))

sys.path.append(P)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangor.settings")
django.setup()


from catalog.models import Agency, Category

categories = Category.objects.all()
print(categories)

with open('urls.txt', 'r') as f:
    all_cats = f.read().split('\n')


session = HTMLSession()


for cat in all_cats[:1]:
    url = 'https://www.goodfirms.co'+cat+'?page=1'
    resp = session.get(url)
    if resp.status_code == 200:
        links = resp.html.xpath('//div[@class="autowidth overflow clear bstars"]/a/@href')
        resp = session.get('https://www.goodfirms.co'+links[0])
        agency_name = resp.html.xpath('//h1[1]/text()')
        image = resp.html.xpath('//div[@class="service-logo"]//img/@src[1]')[0]
        description = resp.html.xpath('//div[@id="services-main"]/div[2]/div[2]//text()')
        rates = resp.html.xpath('//div[@class="firm-pricing"]/text()')
        location = resp.html.xpath('//div[@class="firm-location"]/text()')
        year = resp.html.xpath('//div[@class="firm-founded"]/text()')
        employees = resp.html.xpath('//div[@class="firm-employees"]/text()')
        email = resp.html.xpath('//div[@class="firm-employees"]/text()')
        address = resp.html.xpath('//div[@class="firm-employees"]/text()')
        phone


        result = {
            'name': agency_name,
            'origin_image': image,
            'description': description,
            'rates': rates,
            'location': location,
            'year': year,
            'employees': employees,
            'contacts': contacts,
            'email': email,





        }
        #
        # services = resp.html.xpath("//*[name()='svg'][1]//*[@class='highcharts-legend'][1]/text()")
        #
        #
        # print(image)
        # print('Services!!!!: \n', services)



    else:
        raise NameError("Google Response Error: " + str(resp.status_code))
