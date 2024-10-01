import add as c
import number
from multi import*
from sub import sub
import div as d


# def add:
while True:
    print('''
1.Add
2.subtract
3.multiplication
4.division''')
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        a,b=number.num()
        c.add(a,b)
    elif ch==2:
        a,b=number.num()
        sub(a,b)
    elif ch==3:
        a,b=number.num()
        multi(a,b)  
    elif ch==4:
        a,b=number.num()
        d.div(a,b)          


    


