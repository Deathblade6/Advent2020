def problem2(l):
    seats = [[0]*8 for i in range(128)]
    for i in l:
        ur=127
        lr=0
        for j in range(7):
            if i[j]=='F':
                if (ur+lr)%2==1:
                    ur=(ur+lr)//2
                else:
                    ur=(ur+lr)//2
            elif i[j]=='B':
                if (ur+lr)%2==1:
                    lr=((ur+lr)//2)+1
                else:
                    lr=(ur+lr)//2
            # print(lr,ur)
        r=0
        if i[6]=='F':
            r=lr
        else:
            r=ur
        uc=7
        lc=0
        for j in range(7,10):
            if i[j]=='L':
                if (uc+lc)%2==1:
                    uc=(uc+lc)//2
                else:
                    uc=(uc+lc)//2
            elif i[j]=='R':
                if (uc+lc)%2==1:
                    lc=((uc+lc)//2)+1
                else:
                    lc=(uc+lc)//2
            # print(lc,uc)
        c=0
        if i[9]=='L':
            c=lc
        else:
            c=uc
        seats[r][c]=r*8+c

    flag=1
    for i in range(128):
        for j in range(8):
            if seats[i][j]==0:
                if j==0 and i!=0:
                    if seats[i][j+1]!=0 and seats[i-1][7]!=0:
                        print(i*8+j)
                        flag=0
                        break
                elif j==7 and i!=128:
                    if seats[i][j-1]!=0 and seats[i+1][0]!=0:
                        print(i*8+j)
                        flag=0
                        break
                else:
                    if seats[i][j-1]!=0 and seats[i][j+1]!=0:
                        print(i*8+j)
                        flag=0
                        break
        if flag==0:
            break
            # print(seats[i][j],end=' ')
        # print()

def problem1(l):
    sid=[]
    for i in l:
        ur=127
        lr=0
        for j in range(7):
            if i[j]=='F':
                if (ur+lr)%2==1:
                    ur=(ur+lr)//2
                else:
                    ur=(ur+lr)//2
            elif i[j]=='B':
                if (ur+lr)%2==1:
                    lr=((ur+lr)//2)+1
                else:
                    lr=(ur+lr)//2
            # print(lr,ur)
        r=0
        if i[6]=='F':
            r=lr
        else:
            r=ur
        uc=7
        lc=0
        for j in range(7,10):
            if i[j]=='L':
                if (uc+lc)%2==1:
                    uc=(uc+lc)//2
                else:
                    uc=(uc+lc)//2
            elif i[j]=='R':
                if (uc+lc)%2==1:
                    lc=((uc+lc)//2)+1
                else:
                    lc=(uc+lc)//2
            # print(lc,uc)
        c=0
        if i[9]=='L':
            c=lc
        else:
            c=uc
        sid.append(r*8+c)
    #     print()
    # print(sid)
    print(max(sid))
def main():
    a=open('day5_input.txt','r')
    s=a.read()
    s=s.split('\n')
    s.pop(-1)
    ch=int(input('Enter 1-Problem 1 , 2-Problem 2 : '))
    if ch==1:
        problem1(s)
    elif ch==2:
        problem2(s)
main()
