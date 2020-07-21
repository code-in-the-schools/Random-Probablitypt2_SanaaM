import random

#create list 10
#create list 100
#create list 100000

randomList = [1,6]
for i in range (1,9):
  n = random.randint (1,6)
  randomList.append(n)
  print(randomList)

randomList2 = [1,6]
for i in range (1,99): 
  r = random.randint (1,6) 
  randomList2.append(r)
  print(randomList2)


randomlist3 = [1,6]
for i in range (1,99999):
  m = random.randint (1,6)
  randomlist3.append(m)
print(randomlist3)
