# x = 23.45678
# print(type(x))
# print(f"{x:.2f}")
#
# x = 2 + 3j
# print(x.real)
# print(x.imag)
#
# name = str(input("Enter your name:"))
# age = int(input("Enter your age:"))
# address = str(input("Enter your address:"))
# print('My name is', name)
# print('I am', age, 'years old')
# print('I live in', address)

# course='python for beginners'
# dir: returns all the methods and attributes of the object

# print(course)
# print(course.upper())
# print(course.capitalize())
# print(course.title())
# print(course.lower())
# space gapping left minimize
# print(course.lstrip())
#
# user_name=''
# function name snake case
# UserName=''
#  class name pascal case
# userName=''
#  variable name camel case
# single or double court mainly single court
# boolean
# True,False,None
# array    list,tuple,set,dictionary set of collection

# list: ordered,mutable,allows duplicate elements
# allows duplicate members

# data=[11, 13, 'Ram','Sita','Kathmandu', 14 , 15, 16, '@', 'djf']
# print(data[6],data[7])

# data =[
#     [1,2,3],
#     [3,4,5],
#     [7,8,9]
# ]
# print(data[0][0])
# print(data[2][2])

# data =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [10,11,12,
#     [13,45,[67,89]]]
# ]
# print (data[3][3])
# print(data[3][3][1])
# print(data[3][3][2][1])

# data = ['ram', 'sita', 'Hari', 'gita']
# data.append('shyam')
# # data.insert(2, 'Riya')
# print(data)
# print(dir(data))(contains all existed item)


# data = ['ram', 'sita', 'Hari', 'gita']
# print(len(data))[returns number of items]
# print(data.pop())[delete the last item]
# print(data.pop(2))#delete the data item acc to position

# data.clear() (delete all items only remaining box)
# data.remove('sita')(we have to given item, it doesn't work on position)

# data.sort() (only one data type for sorting otherwise conflict occurs)
# data.append(['riya','purnima']) (print according to given form)
# data.extend(['riya','purnima']) (removes the bracket by extend)
# print(data.count()) (returns the value count of each item)
# print(data.index('sita')) (returns the index of given data)
# print(data)

# users=[
#     ['sita','gita','laxmi'],
#     ['ram','hari'],
# ]
# users.pop([0][2])
# users.append('shyam')
# users.insert()
# users[0].pop()
# users[0].remove('laxmi')
# users[1].append('shyam')
# print(users)

# data=['sita','gita','laxmi','ram','hari']
# data.sort(reverse=False) (by default false, ascending order)
# data.sort(reverse=True)
# print(data)

# data=['a','A','b','B']
# data.sort() ( According to ascii value)
# print (data)

# a = 'a'
# print(ord(a))
# print(chr(97))

# users=[
#     ['sita','gita','laxmi'],
#     ['ram','hari'],
# ]
# a=users[0]
# b=[]
# b.extend(a)
# b.extend(users[1])
# print(b)


#tuple
data = ('ram', 'sita','hari','gita')
data[0]='hari'
#TypeError: 'tuple' object doesn't support item ordered and unchangeable position
print(dir(data))
print (data[2])