import math

def binrep(n):
	while n > 0:
		bit = n % 2
		n //= 2
		yield bit

g = binrep(12)

for i in g:
	print(i)

g = binrep(12)

while True:
	try:
		print(next(g))
	except StopIteration:
		break

class NaturalIterator:
	def __init__(self, n):
		self.__generator = binrep(n)

	def __next__(self):
		return next(self.__generator)

	def __iter__(self):
		return self

class Natural:
	def __init__(self, n):
		self.__n = n

	def __iter__(self):
		return NaturalIterator(self.__n)

	def __getitem__(self, i):
		if 2**i > self.__n:
			raise IndexError()
		return self.__n//(2**i)%2

	def __len__(self):
		return math.ceil(math.log2(self.__n))

N = Natural(12)
print("len:", len(N))

i = 0
while i < len(N):
	print("bit {}: {}".format(i, N[i]))
	i += 1
try:
	N[len(N)]
	print("This should not be shown")
except IndexError:
	print("N[{}] raise an IndexError".format(len(N)))

for i in N:
	for j in N:
		print(i, j)