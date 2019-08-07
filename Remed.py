# # soal 1
# def ascending(a):
#     for item in range(len(a)):
#         for item1 in range(item+1,len(a)):
#             if a[item]>a[item1]:
#                 a[item],a[item1]=a[item1],a[item]
#     print(a)

#     print(a)
# def find(x):
#     x=x.split(' ')
#     b=[]
#     print(x)
#     for item in (x):
#         b.append(len(item))
#     ascending(b)
#     print(b[0])



# find('saya akan pergi kemana saja tes a')


# soal 2

def persistence(n):
    n=str(n)
    c=[]
    count=0
    while len(n) !=1:
        x='1'
        b=[]
        for item in n:
            b.append (item)
        for item in range (len(b)):
            x=int(x)*int(b[item])
        count+=1
        n=str(x)
    print(count)

    

persistence(39)


# # soal 3
# def table(a,b): 
#     c=[]
#     for item in range(1,a+1):
#         o=''
#         for item1 in range(1,b+1):
#             z=0
#             z+=item*item1
#             c.append(z)
#             o+=str(z) +' '
#         print(o)
# table(5,3)



# # soal 4

def alphabet(h):
    b={}
    a='abcdefghijklmnopqrstuvwxyz'
    k=''
    for item in range (len(a)):
        b[a[item]]=item+1
    for item1 in range(len(h)):
        if h[item1] in b:
            k+=str((b[str(h[item1])]))+' '
        else:
            k+='  '
    print(k)

alphabet('The sunset sets at twelve o')



# # Soal Bonus
# def prima1(num):
#     a=[]
#     b=[]
#     if num<0:
#         num=num*-1
#     for item in range(2,num):
#         a.append(item)
#     for item1 in range(len(a)):
#         if num%a[item1] ==0:
#             b.append(False)
#         else:
#             b.append(True)
#     if num==1 or num==-1:
#         print(False)
#     elif False in b:
#         print(False)
#     else:
#         print(True)
# prima1(1)
# prima1(1)
# prima1(2)
# prima1(-15)
# prima1(-5099)
# prima1(-11)