##module.py

#even or odd function
def even(a):
    if a%2==0:
        return "even"
    else:
        return "odd"

    
#Leap year within range
def leapyear(start,end):
    for i in range(start,end+1): 
        if i%400 == 0 or (i %100 != 0 and i % 4 == 0):
            print(i,end=" ")

            
##Unique elements
def unique(l):
    li=[]
    for i in l:
        if l.count(i)==1:
            li.append(i)
    return li