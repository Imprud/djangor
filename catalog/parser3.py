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


session = HTMLSession()

url = "https://www.goodfirms.co/company/solulab"
resp = session.get(url)
agency_cats = []
if resp.status_code == 200:
    script_string = resp.html.xpath('//script')
    js_string = script_string[-9].text
    firs = js_string.find("data:")
    js_string = js_string[firs+6:]
    end = js_string.find("]")
    js_string = js_string[:end+1]
    jsok = json.loads(js_string)
    for cat in jsok:
        print(cat['name'])
        agency_cats.append(cat['name'])

    print(agency_cats)

else:
    raise NameError("Google Response Error: " + str(resp.status_code))
