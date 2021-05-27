# codeup 1번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print('Hello')

# codeup 2번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print('Hello World')

# codeup 3번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print('Hello\nWorld')

# codeup 4번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print('\'Hello\'')

# codeup 5번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print('\"Hello World\"')

# codeup 6번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print('"!@#$%^&*()"')

# codeup 7번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print('"C:\\Download\\hello.cpp"')

# codeup 8번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# print("\u250C\u252C\u2510")
# print("\u251C\u253C\u2524")
# print("\u2514\u2534\u2518\n")

# codeup 10번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num=input()
# print(num)

# codeup 11번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# char=input()
# print(char)

# codeup 12번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num=float(input())
# print('%f' %num)

# codeup 13번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num1,num2=(input().split())
# print(num1,num2)

# codeup 14번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num1,num2=(input().split())
# print(num2,num1)

# codeup 15번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num=float(input())
# print("%.2f" %num)

# codeup 17번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num=int(input())
# for i in range(0,3):
#     print("%d " %num,end='')

# codeup 18번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# hour,minute=(input( ).split(':'))
# print(hour+':'+minute)

# codeup 19번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# year,month,day=map(int,input( ).split('.'))
# print('%04d.%02d.%02d' %(year,month ,day))

#codeup 20번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# front,back=map(str,input( ).split('-'))
# print('%s%s'%(front,back))

#codeup 21번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# data = input()
# if(len(data)<51):
#    print(data)

#codeup 22번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# sentence=input()
# if(len(sentence)<2001):
#     print(sentence)

#codeup 23번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# integar,floatnum = map(int, input().split('.'))
# if((integar>0)&len(str(floatnum))<7):
#     print(integar)
#     print(floatnum)

#codeup 24번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# word = input()
# if(len(str(word))<21):
#     for i in range(len(word)):
#         print('\'%s\'' %word[i])

#codeup 25번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=input()
# number=list(map(int,a))
# size=len(number)
# if(size<6):
#     temp=size-1
#     for i in range(0,size):
#         print('[%d]' %(number[i]*(pow(10,temp-i))))

#codeup 26번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# hour,minute,second=map(int,input( ).split(':'))
# print('%d' %minute)

#codeup 27번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# year,month,day=map(int,input( ).split('.'))
# print('%02d-%02d-%d' %(day, month ,year))

#codeup 28번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=int(input())
# print(a)

#codeup 29번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=float(input())
# print('%0.11f' %a)

#codeup 30번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=int(input())
# print(a)

#codeup 31번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=int(input())
# s="{0:o}".format(a)
# print(s)

#codeup 32번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=int(input())
# s="{0:x}".format(a)
# print(s)

#codeup 33번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=int(input())
# s="{0:x}".format(a)
# hex=s.upper()
# print(hex)

#codeup 34번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=input()
# x_in_int=(int(x,8))
# print(x_in_int)

#codeup 35번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=input()
# x=int(x,16)
# x_to_oct=oct(x)
# result=x_to_oct.lstrip('0o')
# print(result)

#codeup 36번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=input()
# print(ord(x))

#codeup 37번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# print(chr(x))

#codeup 38번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# print(x+y)

#codeup 39번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# print(x+y)

#codeup 40번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# print(-x)

#codeup 41번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=input()
# x=ord(x)+1
# print(chr(x))

#codeup 42번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# print(x//y)

#codeup 43번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# print(x%y)

#codeup 44번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# print(x+1)

#codeup 45번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# print(x+y) #합
# if(x<y): #차
#     print(y-x)
# else:
#     print(x-y)
# print(x*y)#곱
# if(x<y):#몫
#     print(y//x)
# else:
#     print(x//y)
# if(x<y):
#     print(y%x)
# else:
#     print(x%y)
#
# if(x<y):
#     result=round(y/x,3)
#     print("%0.2f" %result)
#
#
# else:
#     result=round(x/y, 3)
#     print("%0.2f" %result)

#codeup 46번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y,z=map(int,input().split())
# result=x+y+z
# print(result)
# print("%0.1f" %(result/3))

#codeup 47번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# print(x*2)

#codeup 48번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# print(x*pow(2,y))

#codeup 49번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# if(x>y):
#     print(1)
# else:print(0)

#codeup 50번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a,b=map(int,input().split())
# if(a==b):
#     print(1)
# else:
#     print(0)

#codeup 51번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a,b=map(int,input().split())
# if(b>=a):
#     print(1)
# else:
#     print(0)

#codeup 52번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a,b=map(int,input().split())
# if(a!=b):
#     print(1)
# else:
#     print(0)

#codeup 53번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# while(x==0 or x==1):
#     if (x == 0):
#         print(1)
#         break
#     else:
#         print(0)
#         break

#codeup 54번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# while(x,y==0 or x,y==1):
#     if(x==1 and y==1):
#         print(1)
#         break
#     else:
#         print(0)
#         break

#codeup 55번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# while(x,y==0 or x,y==1):
#     if(x==1 or y==1):
#         print(1)
#         break
#     else:
#         print(0)
#         break

#codeup 56번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# while(x,y==1 or x,y==0):
#     if(x!=y):
#         print(1)
#         break
#     else:
#         print(0)
#         break

#codeup 57번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# while(x,y==1 or x,y==0):
#     if(x==y):
#         print(1)
#         break
#     else:
#         print(0)
#         break

#codeup 58번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# while(x,y==1 or x,y==0):
#     if(x==0 and y==0):
#         print(1)
#         break
#     else:
#         print(0)
#         break

#codeup 59번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# x=bin(~x)
# result=int(x,2)
# print(result)

#codeup 60번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# result=bin(x&y)
# result=int(result,2)
# print(result)

#codeup 61번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# result=bin(x|y)
# result=int(result,2)
# print(result)

#codeup 62번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# result=bin(x^y)
# result=int(result,2)
# print(result)

#codeup 63번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y=map(int,input().split())
# print(x if x>y else y)

#codeup 64번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y,z=map(int,input().split())
# if (x<y)&(x<z):
#     print(x)
# elif (y<x)&(y<z):
#     print(y)
# else :
#     print(z)

#codeup 65번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y,z=map(int,input().split())
# if(x%2==0):
#     print(x)
# if(y%2==0):
#     print(y)
# if(z%2==0):
#     print(z)

#codeup 66번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x,y,z=map(int,input().split())
# if(x%2==0):
#     print('even')
# else:
#     print('odd')
#
# if(y%2==0):
#     print('even')
# else:
#     print('odd')
#
# if(z%2==0):
#     print('even')
# else:
#     print('odd')

#codeup 67번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# if(x<0):
#     print('minus')
# else:
#     print('plus')
#
# if(x%2==0):
#     print('even')
# else:
#     print('odd')

#codeup 68번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# if (x>=90 and x<=100):
#     print('A')
# if (x >= 70 and x <= 89):
#      print('B')
# if (x >= 40 and x <= 69):
#      print('C')
# if (x>=0 and x<=39):
#     print('D')

#codeup 69번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=input()
# def evaluate(x):
#     return {'A':'best!!!','B':'good!!','C':'run!','D':'slowly~'}.get(x,'what?')
# print(evaluate(x))

#codeup 70번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# def season(y):
#     return{
#     12:'winter',1:'winter',2: 'winter',
#     3:'spring', 4:'spring', 5:'spring',
#     6:'summer', 7:'summer',8:'summer',
#     9:'fall',10:'fall',11:'fall'
# }.get(x)
# print(season(x))

#codeup 71번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# user=list(map(int,input().split()))
# stop=user.index(0)
# for i in range(0,stop):
#     print(user[i])

#codeup 72번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num=int(input())
# for i in range(num):
#     number=list(map(int,input().split()))
#     break
#
# for j in range(0,num):
#     print(number[j])

#codeup 73번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# number=list(map(int,input().split()))
# if 0 in number:
#     for i in range(0,number.index(0)):
#         print(number[i])

#codeup 74번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# for i in range(x,0,-1):
#     print(i)

#codeup 75번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=int(input())
# for i in range(x-1,-1,-1):
#     print(i)

#codeup 76번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# x=input()
# for i in range(97,ord(x)+1,1):
#     print(chr(i), end=' ')

#codeup 77번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# user=int(input())
# for i in range(0,user+1,1):
#     print(i)

# #codeup 78번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# num=int(input())
# sum=0
# for i in range(1,num+1):
#     if i%2==0:
#         sum+=i
# print(sum)

# #codeup 79번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# user=list(map(str,input().split()))
# num=user.index('q')
# for i in range(0,num+1):
#     print(user[i])

# #codeup 80번
# 다시 풀어봐야함
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# user=int(input())
# sum=0
#
# for i in range(0,user):
#     sum=sum+i
#     if(sum>=user):
#         break
# print(i)

# #codeup 81번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# m,n=map(int,input().split())
# if((m<=10) &(n<=10)):
#     for i in range(1,m+1,1):
#         for j in range(1,n+1,1):
#             print(i,j)

# #codeup 82번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a = str(input())
# b =int(a,16)
# for i in range(1,16) :
#     print("%s*%X=%X"%(a,i,b*i))

#codeup 83번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# user=int(input())
# if((user>=1) &(user<=9)):
#     for i in range(1,user+1):
#         if(i==3 or i==6 or i==9):
#            print('X',end=' ')
#         else:
#             print(i,end=' ')

#codeup 84번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# r,g,b=map(int,input().split())
# for i in range(0,r):
#     for j in range(0,g):
#         for k in range(0,b):
#             print(i,j,k)
#
# print(r*g*b)

#codeup 85번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# h,b,c,s=map(int,input().split())
# if(h<=48000 and b<=32 and b%8==0 and c<=5 and s<=6000):
#     bit_to_byte=h*b*c*s/8
#     byte_to_mega=bit_to_byte/pow(2,20)
#     result=round(byte_to_mega,1)
#     print(result,'MB')

#codeup 86번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# w,h,b=map(int,input().split())
# if((w>=1 and w<=1024) and (h>=1 and h<=1024) and (b<=40 and b%4==0)):
#     bit_to_byte=w*h*b/8
#     byte_to_mega=bit_to_byte/pow(2,20)
#     result=format(byte_to_mega,".2f")
#     print(result,'MB')

#codeup 87번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# user=int(input())
# sum=0
# for i in range(1,user+1):
#     sum=sum+i
#     if(sum>=user):
#         break
# print(sum)

#codeup 88번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# user=int(input())
# for i in range(1,user+1):
#     if(i%3==0):
#         continue
#     print(i,end=' ')

#codeup 89번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a,d,n=map(int,input().split())
# for i in range(1,n):
#     a=a+d
# print(a)

#codeup 90번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a,r,n=map(int,input().split())
# for i in range(1,n):
#     a=a*r
# print(a)

#codeup 91번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a,m,d,n=map(int,input().split())
# for i in range(1,n):
#     a=a*m+d
# print(a)

#codeup 92번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a,b,c=map(int,input().split())
# day=1
# while(day%a!=0 or day%b!=0 or day%c!=0):
#     day=day+1
# print(day)

#codeup 93번
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a=int(input())
# b=input().split()
# arr=list()
#
# for i in range(24):
#     arr.append(0)
#
# for i in range(a):
#     arr[int(b[i])]+=1
#
# for i in range(1,24):
#     print(arr[i],end=' ')

#codeup 94번
# n=int(input())
# k=list(map(int,input().split()))
#
# for i in range(n-1,-1,-1):
#     print(k[i],end=' ')

#codeup 95번
# n=int(input())
# b=list(map(int,input().split()))
#
# print(min(b))

#codeup 93번 다시

# n=int(input())
# num=input().split()
# numList=list()
#
# for i in range(24):
#     numList.append(0)
#
# for i in range(n):
#     numList[int(num[i])]+=1
#
# for i in range(1,24):
#     print(numList[i], end=' ')

#codeup 94번
# n=int(input())
# k=input().split()
#
# for i in range(n-1,-1,-1):
#     print(k[i], end=' ')

#codeup 96번

# gomoku=[[0 for ga in range(20)] for sae in range(20)]
# n=int(input())
# for i in range(n):
#     x,y=map(int,input().split())
#     gomoku[x][y] = 1
#
# for i in range(1,20):
#     for j in range(1,20):
#         print(gomoku[i][j], end=' ')
#
#     print()

#codeup 97번
# gomoku=[[int(i) for i in input().split()] for j in range(19)]
# num=int(input())
# arr=[]
#
# for i in range(20):
#     arr.append([])
#     for j in range(20):
#         arr[i].append(0)
#
# for i in range(19):
#     for j in range(19):
#         arr[i+1][j+1]=int(gomoku[i][j])
#
# for i in range(num):
#     x,y=map(int,input().split())
#
#     for j in range(1,20):
#         if arr[x][j] == 0:
#             arr[x][j] = 1
#         else:
#             arr[x][j] = 0
#
#     for j in range(1,20):
#         if arr[j][y] == 0:
#             arr[j][y] = 1
#         else:
#             arr[j][y] = 0
#
#
# for i in range(1,20):
#     for j in range(1,20):
#         print(arr[i][j],end=' ')
#     print()

#codeup 98번
# h,w=map(int,input().split())
# arr=[]
# for i in range(100):
#     arr.append([])
#     for j in range(100):
#         arr[i].append(0)
#
# n=int(input())
#
# for i in range(1,n+1):
#     l,d,x,y = map(int, input().split())
#     for i in range(1,l+1):
#         if(d==1):
#             arr[x+(i-1)][y]=1
#         else:
#             arr[x][y+(i-1)]=1
#
# for i in range(1,h+1):
#     for j in range(1,w+1):
#         print(arr[i][j], end=' ')
#     print()

#codeup 99번
gomoku=[[int(i)for i in input().split() ] for j in range (10)]
arr=[]

for i in range(11):
    arr.append([])
    for j in range(11):
        arr[i].append(0)

for i in range(10):
    for j in range(10):
        arr[i+1][j+1]=int(gomoku[i][j])

for i in range(2,11):
    for j in range(2,11):
        if (arr[i][j] == 0):
            arr[i][j]=9
            if (arr[i][j+1] == 0):
                arr[i][j+1] = 9
                j+=1
            elif((arr[i+1][j]!=1) and (arr[i][j+1]==1)):
                i+=1
                arr[i+1][j]=9

        elif (arr[i][j] == 2):
                arr[i][j]=9
                break
        else:
            break

for i in range(1,11):
    for j in range(1,11):
        print(arr[i][j],end=' ')
    print()
