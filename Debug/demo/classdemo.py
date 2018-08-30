import sys

class BB:
    def printBB(self):
        print("gsafdgasdhjsa")

bb = BB()
bb.printBB()
print(BB.__dict__)
for i in sys.path:
    print(i,end='\n')