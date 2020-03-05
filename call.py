def hello():
	print('hello')

def call(f, *args, **kwargs):
	return f(*args, **kwargs)

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def compute(a, b, op=add):
	return op(a, b)

call(hello)
print(call(add, 3, 2))
print(call(compute, 2, 9))
print(call(compute, 2, 9, op=sub))