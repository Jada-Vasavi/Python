num=int(input())
rev_num=0
for i in str(num):
    rev_num=rev_num*10 + num%10
    num=num//10
print(rev_num)