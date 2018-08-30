import tkinter
# root = tkinter.Tk()
# root.title("Fishc Demo")
# theLabel = tkinter.Label(root,text="我的第二个窗口程序")
# theLabel.pack()
# root.mainloop()
class App:
    def __init__(self,root):
        frame = tkinter.Frame(root)
        frame.pack()
        self.hi_there = tkinter.Button(frame,text="打招呼",command=self.say_hi)
        self.hi_there.pack(side=tkinter.LEFT)

    def say_hi(self):
        print("我是mac，大家好")

root = tkinter.Tk()
app = App(root)

root.mainloop()