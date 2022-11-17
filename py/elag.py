"""""
valasz = input(str("Jó napod van? "))
if valasz  == "igen" :
    print("akkor jo")    
if valasz == 'nem':
    print("akkor old meg magad")
elif valasz != "nem" and valasz != "igen":
    print("bazdmeg")

szam = int(input("adj egy szamot "))
if szam % 2 == 0:
    print("paros")
else:
    print("paratlan")
"""




import random
gondolt_szam = random.randint(1,6)
print('Súgok:', gondolt_szam)
tipp = int(input("tippelj egy számot"))
if gondolt_szam == tipp:
    print("jól tippeltél")
else: 
    print("nemjól tippeltél")
