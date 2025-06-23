import keyword

print("Demo Python Program")

print (8+8)

print('Exiting program')

print(keyword.kwlist)


###############Guess my favorite Food#############

'''
print("Let's play!")
answer = input("Guess what's my favourite fruit?")
favourite_food="mulberry"

if favourite_food == answer:
    print("Yay, you Won!!")
else:
    print("Oops, Gotta try again!")
'''


def favourite_city(cityname):
    print("one of my favourite cities is ", cityname)

favourite_city("Bangalore")
favourite_city('Chandigarh')


#############Collections###############

#list
fruits = [
    'apple',
    'banana',
    'mango'
]
print(fruits)
print(fruits[2])

#dictonary
age=""
my_information = {
    'name': 'devanshi',
    age: 23,
    'birthday': '23Jan'
}

print(my_information)
for fruit in fruits:
    print(fruit)
print(my_information['birthday'])


i=5
endpoint=100
while i<=endpoint:
    print(i)
    i+=5