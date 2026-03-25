import time
from time import sleep
print('AKMENS')
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

time.sleep(0.3)

print('ŠĶĒRES')
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

time.sleep(0.3)

print('PAPĪRS')
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def akmens():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    sleep(1)

def skeres():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    sleep(1)

def papirs():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    sleep(1)
speletajs1 = input("Spēlētājs 1 akmens, šķēres, papīrs:").lower()
speletajs2 = input("Spēlētājs 2 akmens, šķēres, papīrs:").lower()

if speletajs1 == speletajs2:
    print('Neizšķirts!')
elif (speletajs1 == "akmens" and speletajs2 == "šķēres") or (speletajs1 == "šķēres" and speletajs2 == "papīrs") or (speletajs1 == "papīrs" and speletajs2 == "akmens"):
    print('Spēlētājs 1 uzvar!')
else:
    print('Spēlētājs 2 uzvar!')