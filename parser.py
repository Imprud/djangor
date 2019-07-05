from requests_html import HTMLSession
from time import sleep

with open('urls.txt', 'r') as f:
    all_cats = f.read().split('\n')


session = HTMLSession()


for cat in all_cats[:1]:
    url = 'https://www.goodfirms.co'+cat+'?page=1'
    resp = session.get(url)
    if resp.status_code == 200:
        links = resp.html.xpath('//div[@class="autowidth overflow clear bstars"]/a/@href')
        resp = session.get('https://www.goodfirms.co'+links[0])
        print(links)
        agency_name = resp.html.xpath('//h1[1]/text()')
        image = resp.html.xpath('//div[@class="service-logo"]//img/@src[1]')[0]

        services = resp.html.xpath("//*[name()='svg'][1]//*[@class='highcharts-legend'][1]/text()")

        print(image)
        print('Services!!!!: \n', services)



    else:
        raise NameError("Google Response Error: " + str(resp.status_code))

