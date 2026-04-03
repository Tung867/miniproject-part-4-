
def f(a, b):
    return a + b

def g(a, b):
    return a - b
x = int(input())
y = int(input())
print(f(x,y))
print(g(x,y))

if x > y:
    print("x is bigger")
else:
    print("y is bigger")

if x > y:
    print("difference:", x - y)
else:
    print("difference:", y - x)