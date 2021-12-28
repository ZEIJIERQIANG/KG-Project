import requests
import urllib.request
from lxml import etree

def Replace_Space(str):
    str_result = str.replace("\t", "")
    str_result = str_result.replace("\r", "")
    str_result = str_result.replace("\n","")
    return str_result

url_list = [
            "http://std.samr.gov.cn/gb/search/gbDetailed?id=CA6C0E542CE9C983E05397BE0A0AED11"]

wb = """
        <html><body><div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </li></ul>
         </div>
        </body></html>
        """

for url in url_list:
    result = []
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request, timeout=5)
    res = response.read().decode('utf-8')

    html = etree.HTML(res)


    html_data = html.xpath('/html/body/div[@class="container main-body"]/div/div/div/div[@class="page-header"]/h4//text()')
    for i in range (len(html_data)):
        print(html_data[i])

