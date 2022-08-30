# def add(number):
#     num_1 = number**3
#     return num_1
# print(add(10))

### farmers animal

# def farmer(anm_1 , anm_2 , anm_3):
#     total_anm = anm_1*2 + anm_2*4 + anm_3*4
#     return total_anm
# print(f" the total animal's are : {farmer(2,3,5)}")

##ascii  value

# def ctoa(value):
#     value_0 = ord(value)
#     return value_0
# print(ctoa("3"))


##count d in expression

# def d_count(expression):
#     count_d = expression.count("d")
#     return count_d
# print(d_count("dddddddddddddddddddd"))


# def allvalues(value):
#     allvalues_0 = ord(value)
#     return allvalues_0
# print(allvalues("s"))


## radian calculation
# import math
# import math
#
#
# def radtodeg(radian):
#     radian_1 = radian
#     radian_2 = math.pi
#     rad_math = "{:.1f}".format(radian_1*180/radian_2)
#     return rad_math
# print(radtodeg(50))

##resistance calculation

# def tot_res(r_1,r_2, r_3):
#     rn_1 =sum([r_1,r_2,r_3])
#     return rn_1
# print(tot_res(1,1,0))

## hackerrank01

# def num_def(number):
#     num_1 = number
#     if num_1 >=20 :
#         if num_1%2==0 :
#          print("wweird")
#     elif 2<= num_1<=5 :
#         if num_1 % 2 == 0 or num_1 % 2 !=0:
#          print("nooot weird")
#     elif 6<=num_1 <= 20:
#         if num_1%2 == 0 :
#          print("ofc weird")
#     else:
#          print("noot weird")
# (num_def(18))

# fix bug( identical value)

# def check_equals(lst_1,lst_2):
#     a= list(lst_1)
#     b = list(lst_2)
#     if lst_1 == lst_2 :
#         return True
#     return False
#
# print(check_equals([1,3],[1,3]))

##date(leap year)

# def leap_year(year):
#     year_1 = year
#     if year_1 % 400==0 or year_1 % 4==0 :
#             if year_1!=0:
#                return True
#     return False
# print(leap_year(2028))


## check if obj 1 is = obj 2del

# def twodict(dict_1 , dict_2):
#     dict_1 = {
#         "name": "asif",
#         "father's name": "altaf hussain",
#         "roll no" : 1155606
#         }
#     dict_2 = {
#         "name": "asif",
#         "father's name": "altaf hussain",
#         "roll no": 1155606
#     }
#     one_dict = dict_1
#     two__dict = dict_2
#     if one_dict == two__dict :
#         return True
#     return False
# print(twodict("name","name"))

## stuttering using def funtion

# def stutt(stutt_1):
#     final_stutt = stutt_1
#     print(final_stutt[0],final_stutt[1],"...",final_stutt[0],final_stutt[1],final_stutt)
# stutt("incredible")

# basic calculator
# def calculation(input_1 , sign_1 , input_2):
#     num_1 = input_1
#     num_2 = input_2
#     sign_final = sign_1
#     if sign_final == "+":
#         return num_1 + num_2
#     elif sign_final == "-" :
#         return  num_1 - num_2
#     elif sign_final == "*":
#         return num_1*num_2
#     elif sign_final == "/":
#         if input_2 == 0:
#             return "can't divide it by zero"
#     return num_1/num_2
# print(calculation(2,"/",3))
#
#
#

## find factorial
# import  math
# def factorial(n):
#     if n >0 :
#         print(math.factorial(6))
#     else:
#         print("error")
# factorial(12)

#price and discount

# def dis(price,discount):
#     if price and discount > 00 :
#         print("Rs.",round(discount/100*price))
#     else:
#         print(("error"))
# dis(200,15)

# def min_max(number):
#     m_num = list(number)
#     max_num = max(m_num)
#     r_max = m_num.remove(max_num)
#     print(r_max)
# min_max([1,2,3,4,5])


# mm_num = [1,3,4,5,6]
# mm_num.remove(max(mm_num))
# mm_num.remove(min(mm_num))
# avg_num  = sum(mm_num)/len(mm_num)
# print

# square of every entered num

# a = input("enter the number: ")
# final_rr = 0 0r " "
# for num in a:
#     a = input("enter the number: ")
# # final_rr = " "
# # for num in a:
# #     result_num = str(int(num)**2)
# #     final_rr = final_rr + result_num
# #     final_rrr = int(final_rr)
# # print((final_rrr))

# i = 0
# int_1 = 10
# while i<int_1:
#     i+=1
#     print(i,i**2)


# i = 0
# int_1 = 300
# while i<300:
#     i+=10
#     print(i)

# comp = 105
# int_1 = 7
# while comp > 6:
#     comp-= 1
#     print(comp)

# def fcatoril(num):
#     num_0 = 1
#     num_1 = num
#     while num_0 < num_1:
#         num_1 += 2
#         print(num_1)
# fcatoril(12

# num_0 = 0
# num_1 = 13
# facto = 1
# while num_0 < num_1:
#     num_0 += 1
#     facto = facto + num_0
# print(facto)


## using for loop
# num_0 = 7
# result = 1
# for x in range (1,num_0+1):
#     result = result * x
# print(result)

## first ten reverse natural number

# a = 11
# b = 1
# while b < a :
#     a-=1
#     print(a)


## SUM OF 10 NAT. NUM

# num = 5
# i = 1
# sum = 1
# while i< num:
#     i += 1
#     sum = sum +i
# print(sum)

## table using while loop  and for loop by taking input from user

# i_u = int(input("enter the number: "))

# i_wl = 1
# while i_wl < 10:
#     i_wl = i_wl +1
#     print(i_u,"*",i_wl,"=" ,i_u * i_wl)

# num_1 = 12
# num_range = 10
# for x in range(1,num_range +1):
#     print(num_1 ,"*", x ,"=" ,num_1*x)

## sum of all even  numbers

# num_1 =0
# num_2 = 20
# while num_1<=num_2:
#     num_1+=2
#     print(num_1)

## prime number using while loop

# a =int(input("enter the number: "))
# i = 0
# while i<=a:
#     i+=1
#     if i%2 != 0 :
#         print(i,"is  prime number")

## sum of all even numbers that falls between two numbers

# f_1 = int(input("enter the first number: "))
# f_2 = int(input("enter the second number: "))
# while f_1 +1 < f_2 :
#     f_1 += 1
#     if f_1%2==0:
#         print(f_1)

## total resistance in  circuit without while loop

# def tot_res (resistance):
#     val_resistance = list(resistance)
#     tot_resistance = sum(val_resistance)
#     if tot_resistance >= 10:
#         print(tot_resistance,"ohms")
#     else:
#         print(tot_resistance,"ohm")
# tot_res([1,1,1,1,1,1,1,1,1,1])

# number base to binary

# def vowel(word):

# # vow_1 =len("aeiou")
# # num_enter = input("enter the word: ")
# a_1= "asif"
# result = 0
# for x in a_1:
#     print(x)
#     result = '' + x
#     print(result)


## find vowel in the given function

# def maxmin(maxmi):
#     maxmin_1 = list(maxmi)
#     maxmin_2 =  max(maxmin_1) - min(maxmin_1)
#     print(maxmin_2)
# maxmin([2,3,4,5,6,7,8,9,10])
#

### vowel without if else and loop

# e_value = input("enter the word: ")
# final_count =  e_value.count("a")+ e_value.count("e") + e_value.count("i") + e_value.count("o") + e_value.count("u")
# print(final_count)

## getting special characters

#
# a = 3
# i = "10"
#
# while a>=0:
#     print(i*a+"1")
#     a-=1

## decimal to binary by using while and for loop

# def DecimalToBinary(num):
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end='')DecimalToBinary(512)

### list find any odd repeating
import math

# def new_1(num_1):
#     if num_1==0:
#         return
#     else:
#         new_1(int(num_1/2))
#         print(num_1%2,end='')
# new_1(15)


# a = 2
# result = ""
# while a>0:
#     b = a%2
#     result += str(b)
#     f_result = result
#     a //= 2
# print(f_result[::-1])

# repeating odd value:

# a = [1,2,3,-1,-2,-2,1,2,3]
# b = sorted(a)
# i = 0
# while len(b)> i:
#     print(b[i])
#     i+=1
#     if b.count(i)>=0:
#         if b%2!=0:
#             print("the odd value is",b)
#     else:
#         print("error")
#
####
# def unpack(first,*middle):
#     l_list = list(first)
#     f_list = list(*middle)
#     return(l_list,f_list)
# print(unpack([1,2,3,4,5,6,7,8]))

# def numf(num,num_1 ):
#     return num + len([num_1])
# print(numf(1,(2,3,7,8)))

# age = input("entre yours age: ")
# ticket_price = 20 if int(age) >= 18 else 5
# print(ticket_price)

import time

# rows = 4
# columns = 4
#
# for x in range(rows):
#     for y in range(columns):
#         if( x==rows -1  or y== columns-1):
#             print("*", end ="  ")
#         else:
#             print(" ",end="  ")
#     print()

# def oddnum(num_odd):
#     odd_num =(list(num_odd))
#     for i in odd_num:
#         print(i)
# oddnum([1,2,3,4,5,6])
#
# def num_index(num_list , num_in):
#     num_ind_1 = list(num_list)
#     ind_num = int(num_in)
#     final_index = num_ind_1[ind_num]
#     return final_index
# print(num_index([1,2,3,4,5,8,7],3.444444/2))

# a = int(input("enter the number: "))
# i = 0
# result = 0
# while a>i:
#     if i%2 != 0:
#       print(i)
#     i+=1

a = [1,2,3,4]
b = 0
for x in a:
    if x%2 == 0:
        print(x)
    else:
        print("")


























