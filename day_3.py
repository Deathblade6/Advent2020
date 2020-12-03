def problem(l,incx,incy):
    curx = 0
    cury = 0
    ctr = 0
    hor = len(l[0])
    while (cury<len(l)):
        if (l[cury][curx]=='#'):
            ctr+=1
        curx+=incx
        cury+=incy
        curx = curx % hor
    return ctr

def main():
    t=0
    l=[]
    a=open('day3_input.txt','r')
    s=a.read()
    l=s.split('\n')
    l1=[]
    for i in l:
        l2=[]
        for j in i:
            l2.append(j)
        l1.append(l2)
    l1.pop(-1)
    z=int(input('Enter 1-Problem 1 , 2-Problem 2: '))
    if z==1:
        print (problem(l1,3,1))
    elif z==2:
        print(problem(l1,3,1)*problem(l1,1,1)*problem(l1,5,1)*problem(l1,7,1)*problem(l1,1,2))
main()
