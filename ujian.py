# # SOAL 1

# import math
# def calculate_years(principal,interest,tax,desired):
#     k=0
#     while desired>principal:
#         a=principal*interest
#         z=a*tax
#         d=a-z
#         b=principal+d
#         principal=b
#         k+=1
#     print(k)

# calculate_years(1000,0.05,0.18,1100)
# calculate_years(1200,0.17,0.05,2000)
# calculate_years(1500,0.07,0.6,5000)

# SOAL 2
def expandedform(x):
    for item in range(1,x+1):
        angka=10
        if item<100:
            angka=angka
        elif item>100:
            angka=angka*10
        elif item>1000:
            angka=angka*100
        elif item>10000:
            angka=angka*1000
        if item %angka==0:
            a=item
        elif item%angka>0:
            b=item
    z=b-a
    print('{}+{}'.format(str(a),str(z)))


expandedform(7020)


# SOAL 3

# def tower_builder(x,a):
#     d,e=a
#     k=''
#     for item2 in range(x):
#         for  item in range(e):
#             k+=' '
#             for item1 in range(e):
#                 for item3 in range(d):
#                  k+='*'
#                 k+='\n'     
#     print(k)



# tower_builder(3,(2,3))
    


