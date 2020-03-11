import time

def sleep(t=1):
	def decorator(f):
		def wrapper(*args, **kwargs):
			res = f(*args, **kwargs)
			time.sleep(t)
			return res
		return wrapper
	return decorator

@sleep(2)
def printnum(n):
	print(n)

i = 5
while i > 0:
	printnum(i)
	i -= 1
print("!!!! KABOOOOOM !!!!")