from collections import Counter
def problem1(l):
    ctr=0
    for i in l:
        a=set(i)
        if '\n' in a:
            ctr+=len(a)-1
        else:
            ctr+=len(a)
        # print(a,ctr)
    print(ctr)

def problem2(l):
    ctr=0
    for i in range(len(l)):
        a=Counter(l[i])
        for j in a:
            if '\n' not in a:
                ctr+=len(l[i])
                break
            elif a[j]>a['\n']:
                ctr+=1
    print(ctr)

def main():
    a=open('day6_input.txt','r')
    s=a.read()
    s=s.strip('\n')
    s=s.split('\n\n')
    # l = [i.split('\n') for i in s]
    ch=int(input('Enter 1-Problem 1 , 2-Problem 2 : '))
    if ch==1:
        problem1(s)
    elif ch==2:
        problem2(s)
main()
