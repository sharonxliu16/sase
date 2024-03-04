# working 6 games since one is homecoming; each person must work at least 3 games, so 3*12 = 36, which means that 6 people from eboard will be at each game (36/6 = 6) which means each number is repeated 6 times

import random

games=[1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]

eboard=["sharon: ", "jimmy: ", "ethan: ", "justina: ", "alma: ", "yasmine: ", "andrew: ", "joey: ", "bayu: ", "britney: ", "jude: ", "janel: "]

i=len(games)-1
j=len(eboard)-1
count=0
temp=[] #games for each person
while i!=0: #continue assigning games to people until the list is empty
  while count!=3: #3 random games for each person
    game=random.choice(games)
    if game not in temp: #checks if random game drawn is already one of the games assigned in temp list
      temp.append(game)
      games.remove(game)
    count+=1
  print(eboard[j], temp, "\n")
  i-=3
  temp=[]
  count=0
  j-=1
