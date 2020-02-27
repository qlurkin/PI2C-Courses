import json
from functools import reduce, partial

with open('animals.json') as file:
    #animals = json.loads(file.read())['animals']
    animals = json.load(file)['animals']

animalNames = []
for animal in animals:
    animalNames.append(animal['name'])

getName = lambda animal: animal['name']

animalNames = map(getName, animals)

isDog = lambda animal: animal['species'] == 'dog'

keepDog = partial(filter, isDog)

dogs = keepDog(animals)

print(list(dogs))

def getWeight(animal):
    return animal['weight']

totalWeight = reduce(lambda acc, animal: acc + animal['weight'], animals, 0)

totalWeight = sum([getWeight(animal) for animal in animals])

data = [4, 5, 5, 7]

print(all([x > 0 for x in data]))
print(all(
    map(
        lambda x : x>0,
        data
    )
))

# Closure

def makeadder(n):
    def adder(x):
        return n+x
    return adder

f= makeadder(7)

#print(f(3))

def makecount(): 
    c = 0
    def count():
        nonlocal c
        c += 1
        return c
    return count

count = makecount()

print(count())
print(count())
print(count())
print(count())

def make_averager():
    values = []
    def avg(n):
        values.append(n)
        return sum(values)/len(values)
    return avg

avg = make_averager()

print(avg(10))
print(avg(20))