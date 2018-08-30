import easygui as gui
import sys
gui.msgbox("欢迎来到easygui页面！","欢迎页面")
msg = "请问你过来是想要干什么呢？"
title = "互动小游戏。"
choices = ["tank","小心走火","养甲鱼"]
choice = gui.choicebox(msg,title,choices)
gui.msgbox("你的选择是："+str(choice),"结果")
msg = "你希望再选一次吗？"
title = "请选择"
if gui.ccbox(msg,title):
    pass
else:
    sys.exit(0)