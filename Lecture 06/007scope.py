# a var defined w/i the body of a fn 
# is visible only w/i the fn not outside it

def f():
	x = 10
	print("inside f() x = ", x)

print("outside f() x = ", x) # NameError: x is not defined
f()