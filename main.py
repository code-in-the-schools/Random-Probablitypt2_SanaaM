import random

#create list 10
#create list 100
#create list 100000

randomListone = []
for i in range (10):
  n = random.randint (1,6)
  randomListone.append(n)
  

randomListtwo = []
for i in range(100): 
  r = random.randint (1,6) 
  randomListtwo.append(r)
  


randomlistthree = []
for i in range (100000):
  m = random.randint (1,6)
  randomlistthree.append(m)  


percentageN = input(1/10)*6 
percentageR = input(1/100)*6
percentageM = input (1/10000)*6

print(percentageN)
print(percentageR)
print(percentageM)


