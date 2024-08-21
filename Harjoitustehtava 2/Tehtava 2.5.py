import math
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))
massa = ((((((leiviska*20)+naula)*32)+luoti)*13.3))
massakg = massa/1000
massag = massa%1000
print(f"Massa on nykymittojen mukaan: {massa:} \n{massakg:.0f} kilogrammaa ja {massag:3.2f} grammaa")