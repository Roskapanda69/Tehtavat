import random
print(f"Kolmi numeroinen koodi:")
for i  in range(0,3):
    print (random.randint(0, 9), end="")
print(f"\nNelinumeroinen koodi:")
for i in range(0,4):
    print (random.randint(1, 6),end="")
