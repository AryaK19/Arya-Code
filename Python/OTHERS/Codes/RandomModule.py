import random
value = random.random
print(value)

value1 = random.uniform(1,10)
print(value1)

value2 = random.randint(1,10)
print(value2)
print()
names = ["Ashish", "Tejas", "Nikita", "Saroj", "Kaushik", "Adolf", "Arnold"]
value3 = random.choice(names)
print(value3, 'is the name')

result = random.choices(names)
print(result)

result2 = random.choices(names, k=10)
print(result2)

color = ['R', 'G', 'B']
result3 = random.choices(color, weights=[18,18,2], k = 10)
print(result3)
print("'Weight' assigns probability of assignment to the data")
print()
# Weight assigns probability of assignment to the data

deck = list(range(1,53))
print(deck)
random.shuffle(deck)
print(deck)
print()

hand = random.sample(deck, k=5)
print(hand)
# For getting Unique values every time

print("\nCREATING RANDOM FAKE EMAILS : \n")
# I already have the names list
cities = ['Aurangabad', 'Pune', 'Chandigarh', 'Mumbai', 'Bangalore', 'Chennai', 'Delhi']

firstname = random.choice(names)
fromhere = random.choice(cities)
phone_number = f'{random.randint(70,90)}{random.randint(10000000, 99999999)}'

print(f"Randomly Generated Email Address : {firstname}.{fromhere}.{phone_number}@notmail.com")
