# i = 5 
# while i>=1:
#     print(i)
#     i -= 1

# i = 1
# while i<=100:
#     print(i)
#     i +=1

# i = 100
# while i>=1:
#     print(i)
#     i -= 1

# num = [1,4,9,16]
# i = 0
# while i < len(num):
#  print(num[i])
#  i += 1


# num =(1, 4, 9, 16, 25, 36)
# x = 36
# i = 0
# while i < len(num):
#  if(num[i] == x):
#     print("found")
#     break
#  i += 1

# print this patten from 1-100
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# j = 1
# i = 1
# val = []
# while j <= 100:
#   val.append(j)
#   j = j +(i*2)
#   i+=1
#   j+=1
# print(val)


# num = [1,4,9,16,25,36]
# x = 16
# i = 0
# for val in num:
#     if(val == x):
#       print('found',i)
#     i+=1



# for i in range(5):
#     print(i)



# for i in range(1,5):
#     print(i)

    
# for i in range(1,6,2):
#     print(i)

# n = int(input('enter number:'))
# for i in range(1,11):
#     print(i*n)

# n = int(input("Enter a positive integer: "))
# sum = 0
# count = 1
# while count <= n:
#         sum = sum + count
#         count = count + 1
# print(sum)      
         
# n = int(input("Enter a positive integer: "))
# sum = 0
# for i in range(1,n):
#         sum += i

# print(sum)


# n = int(input('enter a number:'))
# fac = 1
# i = 1
# while i <= n:
#     fac *= i
#     i+= 1
# print(fac)

# n = int(input('enter a number:'))
# fac=1
# for i in range(1,n):
#     fac *= i
# print(fac)

# def sum(a,b):
#     s=a+b
#     print(s)
  
# sum(2,3)
# sum(5,10)


# def avg(a,b,c):
#      sum = a+b+c
#      avrage = sum/2
#      return avrage


# output = avg(2,2,2)
# print(output)
# list = [1,2,3,4,5,6]

# def lis(a):
#     for i in a:
#         print(i,end=' ')

# lis(list)
# lis([1,2,3,4,5])

# def fact(n):
#    fac=1
#    for i in range(1 , n+1):
#     fac *= i
#    print(fac)

# fact(3)

# def usd(n):
#     print(n*float(133.47))

# usd(2)

# def inp(n):
#     if(n%2==0):
#         print('even')
#     else:
#         print('odd')

# data = int(input('enter a number:'))
# inp(data)

# def show(n):
#     if(n==10):
#         return
#     print(n)
#     show(n+1)

# show(1)

# def fac(n):
#     if(n==1 or n==0):
#         return 1
#     return fac(n-1)*n
# print(fac(5))

# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1) + n

# s = sum(5)
# print(s)
 
# hey = ['ajay',2,3,4,5,6]

# def lis(list,idx=0):
#     if(idx == len(list)):
#         return 0
#     print(list[idx])
#     lis(list,idx+1)

# lis(hey)


# with open('hello.txt', 'r') as f:
#   data = f.read()


# new_data = data.replace('java','python')
# print(new_data)
    
# with open('hello.txt','w') as f:
#    f.write(new_data)

# def search():
#     with open('hello.txt','r') as f:
#        data = f.read()
#        if(data.find('python') != -1):
#           print('found')
#        else:
#           print('not found')
 
# search()

# def line():
#     word = 'ajay'
#     data = True
#     i=1
#     with open('hello.txt','r') as f:
#          while data:
#               data = f.readline()
#               if(word in data):
#                    print(i)
#                    return
#               i+=1
#     return -1
# line()
# i= 0
# with open('hello.txt','r') as f:
#     data = f.read()
#     number = data.split(',')
   
#     for val in number:
#         if(int(val)%2==0):
#              i+=1
# print(i)

# class students:
#     name = ['Ajay']
#     roll = 5

# s1 = students()
# s1.name.append('hari')
# print(s1.name[0])


# class student:
#     def __init__(self,fullname,roll):
#         self.name = fullname
#         self.rol = roll


# s1 = student('ajay',25)

# class student:


#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def getavg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             avg = sum/len(self.marks)
#         print(self.name,avg)

# s1=student('ajay',[98,99,97])
# s1.getavg()
# class Ajay:
#     def __init__(self,name,age):    
#         self.name=name
#         self.age= age

# s1=Ajay('ajay',25) 
# print(s1.name,s1.age)
