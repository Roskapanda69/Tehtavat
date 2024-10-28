import numpy as np

# Tehtävä 1:

a = 2.493
b = 0.911

print(np.degrees(a))
print(np.degrees(b))

# Tehtävä 2

a2 = 137.7
b2 = 62.3

print(np.radians(a2))
print(np.radians(b2))

# Tehtävä 3

a3 = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in a3:
    print(f'{i} = {np.radians(i)}')

# Tehtävä 4

katetti1= 1.6
katetti2= 2.3
hypotenuusa= np.hypot(katetti1,katetti2)
print(hypotenuusa)
