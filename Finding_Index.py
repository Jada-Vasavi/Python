string=input()
char=input()
i_value=[]
for i in range(len(string)):
    if string[i]==char:
        i_value.append(i)
if i_value:
    print("char found in:",i_value)
else:
    print("char not found",i_value)