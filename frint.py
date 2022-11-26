#frint
import gc

global ram
global cur
global buff

ram = []
cur = 0
buff = []


def frint(data):
    global ram
    global cur
    if type(data) is type(None):
        if cur != 0:
            return printram(0-cur)
    elif type(data) == str:
        ram.append(data)
        cur += 1
        return ram[-1]
    elif type(data) == list:
        for i in data:
            frint(i)
        return printram(0-cur)
    elif type(data) == int or type(data) == bool or type(data) == float:
        ram.append(str(data))
        cur += 1
        return ram[-1]
    
def printram(ammount):
    global ram
    global buff
    buff.append(ram)
    ram = []
    return(buff[-1])

def getram():
    global buff
    return(buff[-1])
    
        
