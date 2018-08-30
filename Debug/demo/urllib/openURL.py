# from urllib import request
from urllib import parse
import requests
import urllib.request,json
import urllib.parse
#
# response = request.urlopen("http://www.fishc.com")
# html = response.read()
# html = html.decode("utf-8")
# print(html)
# response = request.urlopen("http://placekitten.com/g/200/300")
# cat_img = response.read()
# with open("cat200_300.jpg",'wb') as f:
#     f.write(cat_img)

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionfrom=http://fanyi.youdao.com/"
data = {
    "i": "i love fishc.com",
    "from":"AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1534138727699",
    "sign": "ddd046bade7b544577ccf01991223fa0",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
    "typoResult": "false"
}
# data = {
#     "type":"AUTO",
#     "i":"i love fishc.com",
#     "doctype":"json",
#     "xmlVersion":"1.6",
#     "keyfrom":"fanyi web",
#     "ue":"true",
# }
data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.urlopen(url,data)
html = response.read().decode("utf-8")
a = json.loads(html)
print(a)
# data = parse.urlencode(data).encode("utf-8")
# response = request.urlopen(url,data)
# html = response.read().decode("utf-8")
# print(html)
# response = requests.post(url,data)
# print(response.json())