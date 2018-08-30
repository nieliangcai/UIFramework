#coding:utf-8
# string  =  "aaasssadasdasdasdssahggggggggggggggggggggggggggggggggggggdhsagdjg3213asadasdazxczxcsaydwqte"
# list1 = []
# dict_null = {}
# for i in range(len(string)):
#     list1.append([string[i],string.count(string[i])])
#     dict_null[string[i]] = string.count(string[i])
# # print(list1)
# print(dict(list1))
# print(dict_null)
# max_count = sorted(list(dict_null.values()),reverse=True)
# # print(max_count)
# print(list(dict_null.keys())[list(dict_null.values()).index(max_count[0])])
# print(dict_null.items())
#
# list1 = [1,2,3,4]
# list2 = [2,3,4,5]
# list1.extend(list2)
# print(list1)

# with open(r"C:\Users\HP\Desktop\girl_1.txt",'rb') as f:
#     n = 1
#     for line in f.readlines():
#         # print(line.decode("gb2312"))
#         n +=1
#         while n==6:
#             print(line.decode("gb2312"))
#             break

# array = [1,1,2,2,3,3,3,4,2,3]
# dict = {}
# for item in set(array):
#     dict[str(item)] = array.count(item)
# print(sorted(dict.items(),key=lambda a:a[1],reverse=False))
# for i in reversed(sorted(dict.items(),key=lambda d:d[1],reverse=False)[-3:]):
#     print(i)
# import hashlib
# '''2中常见的加密算法'''
# string = "nieliangcai"
# hash_string = hashlib.md5()
# # hash_string = hashlib.sha1()
# hash_string.update(string.encode())
# print(hash_string.hexdigest())
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").is_displayed()

WebDriverWait(driver,10).until(EC.visibility_of)
driver.execute_script()