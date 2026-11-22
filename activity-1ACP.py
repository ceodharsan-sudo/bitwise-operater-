a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print("Swap:", a, b)
n = 5
print("Double:", n << 1)
a = -5
b = 10
if (a ^ b) < 0:
    print("Different signs")
else:
    print("Same signs")
a = 20
b = 4
count = 0
while a >= b:
    a = a - b
    count += 1
print("Division:", count)
