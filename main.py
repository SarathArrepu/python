import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
u = int(input("Enter Choice "))
map = [scissors,paper,rock]
c = map[random.randint(0,2)]
print(c)

if u == "scissors":
  if c == "paper":
   print("u wins")
  elif c == "rock":
   print("c wins")
  else:
   print("try again")

