from collections import Counter

def problem1(l):
    c=0
    for i in l:
        min = i[0].split('-')[0]
        max = i[0].split('-')[1]
        letter = i[1].split(':')[0]
        word = i[2]
        ctr = Counter(word)
        if ctr[letter]>=int(min) and ctr[letter]<=int(max):
            c+=1
    print (c)

def problem2(l):
    c=0
    for i in l:
        min = i[0].split('-')[0]
        max = i[0].split('-')[1]
        letter = i[1].split(':')[0]
        word = i[2]
        if word[int(min)-1]==letter and word[int(max)-1]==letter:
            pass
        elif word[int(min)-1]!=letter and word[int(max)-1]!=letter:
            pass
        else:
            c+=1
    print (c)

def main():
    t=0
    l=[]
    a=open('day2_input.txt','r')
    s=a.read()
    l=s.split('\n')
    l=[i.split(' ') for i in l]
    l.pop(-1)
    # d={}
    # for i in l:
    #     d[i]=True
    z=int(input('Enter 1-Problem 1 , 2-Problem 2: '))
    if z==1:
        problem1(l)
    elif z==2:
        problem2(l)
main()
