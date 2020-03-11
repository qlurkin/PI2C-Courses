import re

pattern = re.compile(r'\w+')

class Sentence:
    def __init__(self, sentence):
        self.__sentence = sentence
        self.__words = pattern.findall(sentence)

    def __iter__(self):
        return SentenceIterator(self.__words)

class SentenceIterator:
    def __init__(self, words):
        self.__words = words
        self.__next = 0

    def __next__(self):
        try:
            elem = self.__words[self.__next]
            self.__next += 1
        except IndexError:
            raise StopIteration()
        return elem

phrase = Sentence("Je suis super")

# for w in phrase:
#     print(w)

data = [1, 2, 3]

for i in phrase:
    for j in phrase:
        print(i, j)

print(dir(Sentence))


# for i in range(100000000000):
#     print(i)

# i = 0
# while i<100000000000:
#     print(i)
#     i+=1

#print(list(range(1000)))

def data():
    i = 0
    while True:
        yield i
        i += 1

g = data()

truc = (x ** 2 for x in g)

print(truc)

print(next(truc))
print(next(truc))
print(next(truc))
print(next(truc))
print(next(truc))
print(next(truc))
