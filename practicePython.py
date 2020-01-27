raise Exception('error msg')


'''

new=open(r"E:\allAboutPython\New Text Document.txt")
content=new.readlines()
new.close()
import shelve
shelfFile=shelve.open(r"E:\allAboutPython\New Text Document.txt")
shelfFile['cats']=['1','2']
shelfFile.close()

import os
totalSize=0
for foldername,subfolder,filename in os.listdir("D:\TCarto"):
    if os.path.isfile(os.path.join("D:\TCarto",filename)):
        totalSize=totalSize+os.path.getsize(os.path.join("D:\TCarto",filename))
print("totalsize is",totalSize)


print(type(os.getcwd())) # getting directory, returns string
print(os.chdir('D:\TCarto\weather_16'))  # getting changing directory
print(os.getcwd()) # after changing it getting it as string
a,b=3,2
if a<b:
    min=a
else:
    min=b
min=a if a<b else b
print("hi") if a<b else print("bye")

mylist=[0,1,2,3,4]
print(mylist[-1])
name="jisaSAKIB"
name.upper()
def func(*args):
    pass

a+=1
import copy
roots={x**2:x for x in range(5,0,-1)}
print(roots)
my_dict={'pair1':'landsat1'}
my_dict1={'pair1':'landsat2'}

name="Jarin Tasnim 1jisa"
print(name[name.isdigit()])

complex(3.5,4)
eval('print(max(100,200)*2)')
newList=['1','2','3','4','5']
for i in zip(mylist,newList):#list of  tuples
    print(type(i))
newName=[l for l in name if l=='T' ]
print(newName)
#newName=[ while name[i]!='t']
new=[x*int(y) for x in mylist for y in newList]
print(new)
'''