import time
# def add(a,b):
#     """简单的加法运算"""
#     s = a+b
#     return s
# # print(add(1,2))
# help(add)
#
# def odd(x):
#     return x*2
#     # return x%2
#
# temp = filter(odd,range(10))        #1或者True返回
# print(temp)
# print(list(temp))
# print(list(filter(lambda x:x%2,range(100))))
# print(list(map(lambda x:x*2,range(10))))
# print(list(map(odd,range(10))))
#
# def recursion(n):
#     course = n
#     for i in range(1,course):
#         course = course*i
#     return course
# print(recursion(5))
# def factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*factorial(n-1)
#
# print(factorial(5))
#
# def fab(n):
#     a1 =1
#     a2 =1
#     a3 =1
#     if n <1:
#         print("input error")
#         return n
#     while n>2:
#         a3 = a1+a2
#         a1 = a2
#         a2 = a3
#         n -=1
#     return a3
# start_time = time.time()
# print(start_time)
# print(fab(255))
# end_time = time.time()
# print(end_time)
# times = lambda x,y:abs(x-y)
# print(times(int(start_time),int(end_time)))
# print(fab(55))
# def fab(n):
#     if n<1:
#         print("input error")
#         return n
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fab(n-1)+fab(n-2)
# print(fab(20))
# #
# start_time = time.strftime("%Y-%m-%d %H:%M:%S")
# print(start_time)
#
# print(fab(32))
#
# end_time = time.strftime("%Y-%m-%d %H:%M:%S")
# print(end_time)

# print(int(end_time)-int(start_time))

# def hanoi(n,x,y,z):
#     if n==1:
#         print(x,"-->",z)
#     else:
#         hanoi(n-1,x,z,y)
#         print(x,'-->',z)
#         hanoi(n-1,y,x,z)
#
# hanoi(3,"x","y","z")

def  func(n):
    if n<=0:
        return ("你输入有误")
    elif n==1:
        return n
    else:
        return func(n-1)*n

# print(func(6))
def fab(n):
    if n<1:
        print("input error")
        return n
    elif n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)
print(fab(20))
i,s=0,1
a = int(input("请输入你要记录的斐波拉切数列的个数："))
for n in range(a):
    print("第%d个=%d"%(n+1,s))
    sum = s+i
    i = s
    s = sum