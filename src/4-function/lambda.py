def polynomial(x):
    return x ** 2 + 5


print(polynomial(2))    # 9

print((lambda x: x ** 2 + 5)(2))    # 9

mult = lambda x: x * x
print(mult(3))
