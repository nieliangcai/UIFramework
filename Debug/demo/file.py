# f = open(r"C:\Users\HP\Desktop\Git.txt",'r',encoding="GBK")
# for i in f:
#     print(i)
# print(f.tell())
# f.seek(0)
# print(list(f))
# f.seek(0)
# print(f.readlines())
# print(f.tell())
# f.close()
"""
小客服:小甲鱼，有个好评很好笑哈.
小甲鱼:哦？
小客服:有了小甲鱼，以后妈妈再也不用担心我的学习了~
小甲鱼:哈哈哈，我看到呀，我还发微博了呢~31231313231
小客服:嗯嗯，我看了你的微博丫~
小甲鱼:OK
小客服:那个有条回复"左手拿着小甲鱼,右手拿着打火机,哪里不会点哪里
"""
f = open(r"C:\Users\HP\Desktop\record.txt",'r',encoding='GBK')
# f.write("小客服：小甲鱼，有个好评很好笑哈\n小甲鱼:哦？\n小客服:有了小甲鱼，以后妈妈再也不用担心我的学习了~\n小甲鱼:哈哈哈，我看到呀，我还发微博了呢~31231313231\n小客服:嗯嗯，我看了你的微博丫~\n小甲鱼:OK\n小客服:那个有条回复'左手拿着小甲鱼,右手拿着打火机,哪里不会点哪里'")
# f.writelines(["小客服：小甲鱼，有个好评很好笑哈\n","小甲鱼:哦？\n"])

list = f.readlines()
girl_list = []
boy_list = []
for i in range(len(list)):
    split = str(list[i]).split(":")
    for j in range(len(split)):

        if split[j]=="小客服":
            girl_list.append(split[1])
        if split[j] == "小甲鱼":
            boy_list.append(split[1])
print(girl_list)
            # f = open(r"C:\Users\HP\Desktop\boy_1.txt",'w')
            # f.writelines(list1.append(split[1]))

print(boy_list)
f = open(r"C:\Users\HP\Desktop\boy_1.txt",'w')
f.writelines(boy_list)
f.close()
f = open(r"C:\Users\HP\Desktop\girl_1.txt",'w')
f.writelines(girl_list)
f.close()

