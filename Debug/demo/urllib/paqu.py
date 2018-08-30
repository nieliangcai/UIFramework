# coding=utf-8
from urllib import request
from urllib import parse
from bs4 import BeautifulSoup
import re,sys


def main():
    url = 'https://baike.baidu.com/search/word?%s'
    keyword = input("请输入关键字，便于查找:")
    keyword = parse.urlencode({'word':keyword})
    response = request.urlopen((url) %keyword)
    html =response.read().decode("utf-8")
    soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    for a in soup.find_all(href=re.compile("viewPage")):
        # print(a.text)
        content = ''.join(a.text)
        # print(content)
        url2 = ''.join(["http://baike.baidu.com",a["href"]])#"http://baike.baidu.com",
        # print(url2)
        response2 = request.urlopen(url2)

        html2 = response2.read().decode("utf-8")
        soup2 = BeautifulSoup(html2,"html.parser")
        # print(soup2)
        if soup2.h2:
            content = ''.join([content,soup2.h2.text])
        content = ''.join([content,"->",url2])
        print(content)
    # url = "http://baike.baidu.com/view/284853.htm"
    # response = request.urlopen(url)
    # html = response.read().decode("utf-8")
    # # print(html)
    # soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    # all = soup.find_all(href=re.compile("view"))
    # for a in all:
    #     print(a.text,"->",''.join(["http://baike.baidu.com",a["href"]]))
    # \d{2, 3}\.\d{0, 3}\.\d{0, 3}\.\d{0, 3}    获取IP地址，正则表达式
    #(<)?(\w+@\w+(?:\.\w{0,3})+)(>)?    邮件格式   [a-zA-Z0-9]{0,15}@[a-zA-Z0-9]{0,10}\.[a-zA-Z0-9]{0,11}
    #[a-zA-Z0-9]{0,15}@[a-zA-Z0-9]{0,10}\.[a-zA-Z0-9]{0,11} a-z或者A-Z或者0-9取0-15个值加上“@”再取0-10个值加上“.”再取0-11个值
if __name__=="__main__":
    main()