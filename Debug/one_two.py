#随便输入一个list，把它拆分为2个list，2个list的差最小
import random
import itertools

#生成一个随机的list
a = input("请输入list的长度:")
test_list = []
for i in range(int(a)):
    list1 = random.randint(1,10)
    test_list.append(list1)
print(sorted(test_list))
#计算list的和，取中间数
# sum = 0
list = sorted(test_list)
def sumall(list_test):
    sum = 0
    for j in range(len(list_test)):
        sum += list_test[j]
    return sum
# for j in range(len(list)):
#     sum += list[j]
mid = sumall(list)//2
mid_sum = 0
list2 = []
for k in range(len(list)):
    mid_sum += list[k]
    if mid_sum < mid:
        list2.append(list[k])
        list3 = list[k+1:]
    else:
        break
# print(list2,list3)
# def div(test_list1 ,test_list2):
#     div_num = abs(sumall(test_list1)-sumall(test_list2))
#     return div_num
div = lambda list1,list2 : abs(sumall(list1)-sumall(list2))  #匿名函数，2个参数，abs()为计算方法，会return结果
print(div(list2,list3))
print("list2 的值为：",sumall(list2))
print("list3 的值为：",sumall(list3))

