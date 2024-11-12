print ("HELLO, MY NAME IS FERNANDO")
print ("KaCHumba 2")
print ("Welcome to KaCHumba 2")  
print ("The monsters of the underworld are attaking the village of KaCHumba, you have to hurry up, take some provisions and go with your partner, to the magician palace to ask for help")
choice = input("choose your character name")
money= 700 

import random
from random import randint

health= 100
food= 20
water= 20
clothes= 10
bullets= 15
miles=0
rest=2
game= True
print ("you have chosen", choice)
print ("you have been saveing money for 1year and you saved 700 dollars")
print("buy to anteto some provisions")


print ("A.Food,water,clothes= 400dollars") 
print ("B.Water,Bullets,books=dollars=550 dollars")
print ("C.Food,Bullets, clothes= 300 dollars")
print (choice, "you have to choose one of the three options")
option= input ("choose your option")
if option == "A":
  print ("you have 300 dollars left")
  money= money-400
if option == "B":
  print ("you have 150 dollars left")
  money= money-550
if option == "C":
  print ("you have 400 dollars left")
  money= money-300

print ("you are in the village of KaCHumba, you have to choose between two paths")
print ("choose carefully the correct path will take you to the magician palace")
print ("1.The path of the antilopes")
print ("2.The path of the parrots")
path= input ("choose your path")
if path == "1":
  print (path, "you have chosen the path of the antilopes")
  print("GOOD LUCK")
  health = health-3
if path == "2":
  print (path, "you have chosen the path of the parrots")
  print ("GOOD LUCK")
  health = health-10
print ("you have", money, "dollars")
print ("you have", health, "health")
print ("you have", food, "food")
print ("you have", miles, "miles")
while game:
  print ("10. Eat food")
  print ("11. Drink water")
  print ("12. Use clothes")
  print ("13. Shoot bullets")
  print ("14. Fast pace")
  print ("15. Slow pace")
  print ("16. Rest")
  choice= input ("What is your choice?")
  if choice == "10":
    print ("if you choose 10 your health is going to be increased by 10, but you will lose 1.5 food")
    health= health+10
    food= food-1.5
    print ("your health is now", health)
    print ("your food is now", food)
  elif choice == "11":
    print ("if you choose 11 your health is going to be increased by 5, but you will lose 1 water")
    health= health+5
    water= water-1
    print ("your health is now", health)
    print ("your water is now", water)
  elif choice == "12":
    print ("if you choose 12 your health is going to be increased by 3, but you will lose 1 clothes")
    health= health+3
    clothes= clothes-1
    print ("your health is now", health)
    print ("your clothes is now", clothes)
  elif choice == "13":
    print ("if you choose 13 your food is going to be increased by 2, but you will lose 3 bullets")
    food= food+2
    bullets= bullets-3
    print ("your food is now", food)
    print ("your bullets is now", bullets)
  elif choice == "14":
    
    miles= miles+ randint (5, 7)
    health= health-10
    print ("your miles is now", miles)
    print ("your health is now", health)
  elif choice == "15":
   
    miles= miles+ randint (2,4)
    health= health-5
    print ("your miles is now", miles)
    print ("your health is now", health)
  elif choice == "16":
    print ("if you choose 16 your health is going to be increased by 5, but you will lose 2 food       and 2 water")
    print ("your food is now", food)
    print ("your water is now", water)


  if miles>100:
    print ("you have reached the magician palace")
    print ("you have to choose between two doors")
    print ("1.The door of the fire")
    print ("2.The dooor of the water")
    door= input ("choose your door")
    if door == "1":
      print ("you win")
      game= False
    if door == "2":
      print ("you lose")
      game= False

  if health<0:
    print ("you have died")
    game= False
    
    0