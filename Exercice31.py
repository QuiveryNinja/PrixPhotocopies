"""
LASSUS Augustin
1ere 1
Exercice 31 Page 60
30 septembre 2020
"""

def Prix():
    n = int(input("Combien de photocopies souhaitez vous: "))
    if n <= 20:
        res = n * 0.50
        res = str(res)
        print("Le prix total sera de: "+ res + " euros") 
        return 
    elif 20 < n <= 50:
        res = n * 0.25
        res = str(res)
        print("Le prix total sera de: "+ res + "euros") 
        return 
    elif 50 < n <= 100:
        res = n * 0.10
        res = str(res)
        print("Le prix total sera de: " + res + "euros") 
        return 
    else:
        res = n * 0.05
        res = str(res)
        print("Le prix total sera de: "+ res + "euros") 
        return 

Prix()