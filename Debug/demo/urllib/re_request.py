import re,time
from urllib import request

url = "http://tieba.baidu.com/p/3823765471"
response = request.urlopen(url)
html = response.read().decode('utf-8')

r = r'<img class="BDE_Image" .*? src="([^"]*\.jpg)".*?>'
img_list = re.findall(r,html)
for img_url in img_list:
    print(img_url)
    response = request.urlopen(img_url)
    img = response.read()
    now = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
    with open('img_list%s.jpg'%now,'wb') as f:
        f.write(img)
