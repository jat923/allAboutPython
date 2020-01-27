data={'ns' : 'green' , 'ew': 'red'}

def switchLights(var):
    for key in var.keys():
        if var[key]=='red':
            var[key]=='yellow'
        elif var[key]=='yellow':
            var[key]=='red'
        elif var[key]=='red':
            var[key]=='green'
    assert 'red' in var.values(), 'neighther is red'+str(data)
    return data
print(data)
data=switchLights(data)
print(data)
"""
**************
***        ***
**************

import traceback
import os
print(os.getcwd())
def boxPrint(symbol,height,width):
    if len(symbol) >1:
        try:
            raise Exception("symbol needs to have len 1")
        except:
            errorfile=open("errorfile.txt",'a')
            errorfile.write(traceback.format_exc())
            errorfile.close()

    for i in range(height):
            if i==0:
                print(symbol*width)
            elif i!=0 and i!=height-1:
                print(symbol+" "*(width-2)+symbol)
            else:
                print(symbol*width)
boxPrint("* ",4,4)
"""