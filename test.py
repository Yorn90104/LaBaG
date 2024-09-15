#i = 1
#while i <= 9 :
#    j = 1
#    while j <= 9 :#and j <= i :
#       print(i,'x',j,'=',i * j,end='   ')
#       j = j + 1
#    print()
#    i = i + 1


import random

ram2 = random.randint(1,100)
add = 0
p2 = "x"

def change(x,y) :
      
      if y <= 36 :
            x = 'a'
      elif 36 < y <= 60 :
            x = 'b'
      elif 60 < y <= 77 :
            x = 'c'
      elif 77 < y <= 89 :
            x = 'd'
      elif 89 < y <= 97 :
            x = 'e'
      else :
            x = 'f'
      return x

#if ram2 <= 36 :
#   p2 = 'a'
#elif 36 < ram2 <= 60 :
#   p2 = 'b'
# elif 60 < ram2 <= 77 :
#    p2 = 'c'
# elif 77 < ram2 <= 89 :
#    p2 = 'd'
# elif 89 < ram2 <= 97 :
#    p2 = 'e'
# else :
#    p2 = 'f'

p2 = change(p2 , ram2)
print(p2)
print(ram2)

def only(x,y) :
      if x == 'a':
            y = y + 100
      elif x == 'b' :
            y = y + 170
      elif x == 'c' :
            y = y + 780
      elif x == 'd' :
            y = y + 870
      elif x == 'e' :
            y = y + 5000
      elif x == 'f' :
            y = y + 10000
      return y

add = only(p2,add)
      
print(add)