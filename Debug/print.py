import time
print(time.ctime())
now_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
print('report%s.html' %now_time)

x = str(time.time())
ntime = now_time.split('.')[0]
actime = time.strptime(ntime,'%Y%m%d%H%M%S')        #把ntime变为元组
bctime = time.strftime('%Y%m%d%H%M%S')
print(x,actime,bctime)
etime = int(time.mktime(actime))
print(etime)
y = time.strftime('%Y%m%d%H%M%S')
print(y)

str1 = "id=1,name='one plus 3 event',status=True,limit=20,address='上海闵行',start_time='2018-07-27 17:06:00'"
str2 = str1.replace('=',':')
print(str2)