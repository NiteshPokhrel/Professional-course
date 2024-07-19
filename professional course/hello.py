#print("hello world")

#if 5>2:
 #   print("Five is greater than two!")



#x=5
#y="john"
#print(x)
#print(y)


#x = 5
#x = "john"
#print(x)


# x = y = z = "orange"
# print(x)
# print(y)
# print(z)


# x , y , z = "orange" , "banana" , "cherry"
# print(x)
# print(y)
# print(z)



# fruits = ["apple" , "banana" , "cherry"]
# x,y,z = fruits
# print(x)
# print('y')
# print("z")



#inp=input("statement")

# a=33
# b=200
# if b>a:
#     print('b is greater than a')
# else:
#     print("b is not greater than a")



# inp=input("what is your name?  --------")
# print(inp) 




#if 5>2:
#print("Five is greater than two!")

#if 5>2:
   # print("Five is greater than two")
#if 5>2:
    #   print("five is greater than two")

#if 5>2:
  #print("five is greater than two")
 # print("five is greater than two")
 



# age = 18

# if age < 18:
#     print("You can't vote")

# elif 18 == 18:
#     print("You can vote")
# elif 18 <= age :
    
#     print("You can vote")
# else:
#     print("You can't vote")




# s='Texas'
# for i in s :
#     print(i)




# for i in range(0,10,2):
#     print(i)




# x = [1,2]
# y = [4,5]
# for i in x:
#     for j in y:
#         print(i,j)




# mylist = ['texas', 'international', 'collage', 'mitrapark', 'ktm']
# print(mylist)
#print(mylist[1])
# del mylist[2]
# print(mylist)

# popped = mylist.pop(1)
# print(popped)
# print(mylist)

# index = mylist.index('ktm')
# count = mylist.count('ktm')
# print(count)

# length = len(mylist)
# print(length)


# if 'collage' in mylist:
#     print("Yes,it is in the database")

# else:
#     print("It is not in the database")



# mylist = [ ]
# size = int(input("enter the size of the list   "))
# for i in range(size):
#     el = int(input("enter the element"))
#     mylist.append(el)
#     print(mylist)




# mytuple = (5,4,1,2,3,4,5,7,8)
# print(mytuple)

# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[0:3])




# tuple1 = (1,2,3)
# tuple2 = (3,4,6)
# concatenate = tuple1 + tuple2
# print(concatenate)


# mytuple = (1,2,3,4,5)
# print(mytuple)
# print(mytuple[3])



# mytuple=(1,2,2,4,6,3,4,5)
# count2  = mytuple.count(5)
# print(count2)

# r= mytuple.index(4)
# print(r)


# length = len(mytuple)
# print(length)


# a = max(mytuple)
# print(a)


# a = min(mytuple)
# print(a)



# mydict = {
#     "name":"Texas",
#     "location":"Mitrapark",
#     "country":"Nepal"
# }
# print(mydict)


# print(mydict["name"])
# print(mydict["location"])


# mydict["name"] = "Dursikshya"
# print(mydict)


# mydict["Email"] = "pokhrelnitesh69@gmail.com"
# print(mydict)


# del mydict["Email"]
# print(mydict)




# a = mydict.pop("country")
# print(a)



# for key in mydict:
#     print(key,mydict[key])



# for value in mydict.values():
#     print(value)

# for key,value in mydict.items():
#     print(key,value)




# nested_dict={
#         "person1":{"name":"Alice", "age":25},
#         "person2":{"name":"Bob", "age":30}
#     }
# for person,info in nested_dict.items():
#         name=info["name"]
#         age=info["age"]
#         print(f"{person}:Name={name},Age={age}")
  





# greeting = "hello"
# name = "baby"
# message = greeting + "," + name + "😘"
# print(message)



# slice = greeting[1:4]
# print(slice)



# s = "hello"
# sliced = s[:-1]
# print(sliced)


# length = len(greeting)
# print(length)



# name = "nitesh"
# age = 22
# intro = f"My name is {name} and iam {age} years old"
# print(intro)



# intro = "My name is {} and Iam {} years old.".format(name,age)
# print(intro)



# intro = "My name is %s and Iam %d years old." %(name,age)
# print(intro)




# multi_line =""" 
# this is a string that spans
# multiple lines. It's useful for 
# long text
# """

# print(multi_line)



# newline= "hello\n world"
# tabbed="hello\tword"
# quoted="she said,\"hello!\""
# print(newline)
# print(tabbed)
# print(quoted)





# def add(a,b):
#     return(a+b)
# result= add(3,4)
# print(result)


# def greet():
#     print("hello world!")
# greet()



# def evenodd(a):
#     if a%2 ==0:
#         print("even")
#     else:
#         print("odd")

# evenodd(6)
# evenodd(7)



# def greet(name,message):
#     print(f"{message},{name}!")
# greet(name="Texas",message="Good morning")



# def greet(name,message="Hello"):
#   print(f"{message},{name}!")
# greet("Texas")
# greet("Intl","Good morning")




# def greet(*names):
#    for name in names:
#       print(f"Hello,{name}!")
# greet("Alice","Bob","charlie")
      




# def greet(**kwargs):
#    for key, value in kwargs.items():
#       print(f"{key} is {value}")
# greet(name="alice",age=25,city="newyork")
# greet(name="bob",profession="developer")




# def factorial(n):
#    if n==1:
#       return 1
#    else:
#       return n* factorial(n-1)
# result = factorial(5)
# print(result)





# import numpy as np
# data1 = [6,7.5,8,0,1]
# arr1 = np.array(data1)
# print(arr1)
# print(arr1.dtype)
# print(arr1.shape)
# print(arr1.ndim)




# array = np.array([[0,1,2],[2,3,4]])
# print(array)
                

# array = np.eye(3)
# print(array)



# array = np.random.randint(10,20,(5,5))
# print(array)



# arr=np.arange(10)
# print(arr)
# arr_slice=arr[5:8]
# arr_slice[1]=12345
# print(arr)
# arr_slice[:]=64
# print(arr)



