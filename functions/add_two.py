li1=[2,4,3]
li2=[5,6,4]
emp1=[]
emp2=[]
for i in li1:
    emp1.append(str(i))
print(type(emp1))
print(emp1)
string1="".join(emp1)
print(type(string1))
k=int(string1)
print(type(k))

for i in li2:
    emp2.append(str(i))
print(type(emp2))
print(emp2)
string2="".join(emp2)
print(type(string2))
j=int(string2)
print(type(j))

rev=0
while(k>0):
    digit=k%10
    rev=rev*10+digit
    k=k//10
print(rev)
str1=rev
rev=0
while(j>0):
    digit=j%10
    rev=rev*10+digit
    j=j//10
print(rev)
str2=rev
sum=str1+str2
print(sum)


