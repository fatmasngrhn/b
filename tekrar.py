#1 den 30a kadar olan sayıları while döngüsü ile ekrana yazdırınız.
"""
for 5 in range (1,10):
print(s)
"""
    
"""
bas-1
while(bas<10):
    print(bas)
    bas=bas+1
"""

"""
for in range (2,30,2):
    print(1):
"""

"""
bas-2
while(bas<30):
      print(bas)
      bas=bas+2
"""
"""
while True:
    girdi = int(input("sayı giriniz"))
    if girdi==-1:
        break
    else:
            print(girdi)
""" 
  
# program 10 hak verir
# 45
# 23 -> sayı 23 den büyük
# 9 hak 40 -> sayı 40 dan büyük
# 8 hak 50 -> sayı 50 den küçük
# 7 hak 46 -> sayı 46 dan küçük
# 6 hak 44 -> sayı 44 den küçük
# 5 hak 45 -> tebrikler kazandın


import random 
tutulan=int(random.uniform(0,100))
hak = 10 
while hak>0:
    girdi=int(input("sayı giriniz"))
    if girdi>tutulan:
       print("daha küçük bir sayı giriniz")
    elif girdi>tutulan:
        print("daha büyük bir sayı giriniz")
    else:
        print("tebrikler", hak, "turda kazandınız")
    hak=hak-1

        



          

    