import os
import shutil
x = os.listdir(r"C:\Users\hp\Downloads")

main = 'C:\\Users\hp\Downloads\\'
target = 'D:\PDF'
file = '.pdf'

def mover(original, final, directory, type):
    for i in x:
        try:
            if i.endswith(type):
                first = main + i
                shutil.move(first, target)
        except:
            if i.endswith(type):
                first = main + i
                shutil.move(first, 'D:\\')
