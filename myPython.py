print('Om Saraswati Deviyai Namaha')

# n=input('Enter n: ')
# print(n)
# print(type(n))
# m=int(n)
# print(m)
# print(type(m))

str="Amma Nanna"
print(str[6:10])
print(str.upper())
import random
ran=random.randrange(1,10)
print(ran)
print(f"Hi i am {ran} ok na")

# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

list=[]
list.append(1)
list.insert(1,4)
list.reverse()
# list.remove(4)
print(list)
# list in python and arrays in python
my_list = ['apple', 'banana', 'orange','banana']
for _ in my_list:
    print(_)

del my_list[0] #used for deleting in list
print("\n")

[print(X) for X in my_list]

for x in range(2,10,2):
    print(x)

new_list=[x if x!="man" else "orange" for x in my_list]
print(new_list)

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for x in nested_list:
    for i in x:
        print(i)

#declaration of tuple
tupledecl=()
print(type(tupledecl))

mytuple=tuple(my_list)
print(type(mytuple))

mysets=set({})
print(type(mysets))
forUpdateset={6,5,4}
mysets.add("Hi")
mysets.add("I am ")
mysets.add("Amar")
mysets.add(5)
# mysets.clear() remove all elements
# mysets.discard(5) remove element
mysets.update(forUpdateset)
new=mysets.difference(forUpdateset)
print(new)
print(mysets)

# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates
mydict={}
print(type(mydict))
mydict['key1']=1
mydict['key2']=2
mydict['key3']=3
mydict['key4']="Amar"
mydict.update({"Name":"Krishna"})
mydict.setdefault("key5","Ram")
print(mydict)
#gives values and key in [(),(),()] -> 2D list of tuples
s=mydict.items()
print(s)

for key,value in mydict.items():
    print(f"{key}:{value}")


# Find most frequent element in a list

def mostfre(isList):
    maxcount=0
    count=0
    num=0

    for item in isList:
        count=isList.count(item)
        if count>maxcount:
            maxcount=count
            num=item
    return num

myList = [2, 1, 3, 3, 1, 3]
res=mostfre(myList)
print(f"The most repeated number in list is : {res}")

x=lambda a,b,c:a+b+c

print(x(1,2,3))

x=lambda name:"Hello"+name
print(x(" Ram"))

# map

number=[1, 2, 3, 4, 5]

toSquare=lambda numb : numb*numb

com=map(toSquare,number)

for i in com:
    print(i)

toUpp="hello"

convertoUpp=lambda char: char.upper()

sr=map(convertoUpp,toUpp)

for name in sr:
    print(name)

addten=lambda nu:nu+10

ch=map(addten,number)

for i in ch:
    print(i)

a=[1, 2, 3]
b=[4, 5, 6]

pro=map(lambda a,b:a*b,a,b)
for i in pro:
    print(i)

sen="This is a sentence"
spsens=sen.split()

re=map(lambda spsen: len(spsen),spsens)

for i in re:
    print(i)


