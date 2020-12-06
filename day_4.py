import re

def problem1(l):
    ctr=0
    for i in l:
        if len(i)==8:
            ctr+=1
        elif len(i)==7 and 'cid' not in i:
            ctr+=1
    print (ctr)

def problem2(l):
    ctr=0
    print(len(l))
    c=0
    for i in l:
        # print(i)
        if len(i)==8:
            if not(int(i['byr'])>=1920 and int(i['byr'])<=2002):
                continue
            if not(int(i['iyr'])>=2010 and int(i['iyr'])<=2020):
                continue
            if not(int(i['eyr'])>=2020 and int(i['eyr'])<=2030):
                continue
            print(i['byr'],i['iyr'],i['eyr'])
            regex = r"(cm|in)$"
            matches = re.search(regex, i['hgt'])
            if matches:
                if 'in' in i['hgt']:
                    if not(int(i['hgt'].split('i')[0])>=59 and int(i['hgt'].split('i')[0])<=76):
                        continue
                elif 'cm' in i['hgt']:
                    if not(int(i['hgt'].split('c')[0])>=150 and int(i['hgt'].split('c')[0])<=193):
                        continue
            else:
                continue
            regex = r"#[a-f0-9]{6}"
            matches = re.search(regex, i['hcl'])
            if not(matches):
                continue
            if not(i['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                continue
            if not(len(i['pid'])==9):
                continue
            ctr+=1
        elif len(i)==7 and 'cid' not in i:
            if not(int(i['byr'])>=1920 and int(i['byr'])<=2002):
                continue
            if not(int(i['iyr'])>=2010 and int(i['iyr'])<=2020):
                continue
            if not(int(i['eyr'])>=2020 and int(i['eyr'])<=2030):
                continue
            print(i['byr'],i['iyr'],i['eyr'])
            regex = r"(cm|in)$"
            matches = re.search(regex, i['hgt'])
            if matches:
                if 'in' in i['hgt']:
                    if not(int(i['hgt'].split('i')[0])>=59 and int(i['hgt'].split('i')[0])<=76):
                        continue
                elif 'cm' in i['hgt']:
                    if not(int(i['hgt'].split('c')[0])>=150 and int(i['hgt'].split('c')[0])<=193):
                        continue
            else:
                continue
            regex = r"#[a-f0-9]{6}"
            matches = re.search(regex, i['hcl'])
            if not(matches):
                continue

            if not(i['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                continue
            if not(len(i['pid'])==9):
                continue
            ctr+=1
        c+=1
    print (ctr)
def main():
    a=open('day4_input.txt','r')
    s=a.read()
    l=s.split('\n\n')
    l=[i.replace('\n',' ') for i in l]
    l=[i.split(' ') for i in l]
    l1=[]
    for i  in l:
        l2={}
        for j in i:
            if j!='':
                l2[j.split(':')[0]]=j.split(':')[1]
        l1.append(l2)
    # print(l1)

    ch=int(input('Enter 1-Problen 1 , 2-Problem 2 : '))
    if ch==1:
        problem1(l1)
    elif ch==2:
        problem2(l1)
main()
