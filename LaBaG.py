import random

ram1 = 0
ram2 = 0
ram3 = 0
p1 = 'x'
p2 = 'x'
p3 = 'x'
score = 0
add = 0
times = 30
ed = 0

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

print("共 {} 次".format(times))

while ed < times :
    add = 0
    #暫時代替按鈕
    button=input("按下 ENTER 開始")
    if button == "" :
        #隨機數
        ram1 = random.randint(1,100)
        ram2 = random.randint(1,100)
        ram3 = random.randint(1,100)

        #1
        p1 = change(p1,ram1)

        #2
        p2 = change(p2,ram2)

        #3
        p3 = change(p3,ram3)


        print(p1,' ',p2,' ',p3)

        #增加分數
        #3個相同
        if p1 == p2 == p3 :
            if p1 == 'a':
                add = add + 200
            elif p1 == 'b' :
                add = add + 600
            elif p1 == 'c' :
                add = add + 1600
            elif p1 == 'd' :
                add = add + 1800
            elif p1 == 'e' :
                add = add + 10000
            elif p1 == 'f' :
                add = add + 20000

        #2個相同=(2個相同的+1個不同的)/1.3
        #1 & 2
        elif p1 == p2 :
            #2個同
            if p2 == 'a':
                add = add + 100
            elif p2 == 'b' :
                add = add + 170
            elif p2 == 'c' :
                add = add + 780
            elif p2 == 'd' :
                add = add + 870
            elif p2 == 'e' :
                add = add + 5000
            elif p2 == 'f' :
                add = add + 10000
            #不同的
            if p3 == 'a':
                add = add + 30
            elif p3 == 'b' :
                add = add + 50
            elif p3 == 'c' :
                add = add + 250
            elif p3 == 'd' :
                add = add + 290
            elif p3 == 'e' :
                add = add + 1200
            elif p3 == 'f' :
                add = add + 2500
            add = round( add / 1.3 )

        #2 & 3
        elif p2 == p3 :
            #2個同
            if p2 == 'a':
                add = add + 100
            elif p2 == 'b' :
                add = add + 170
            elif p2 == 'c' :
                add = add + 780
            elif p2 == 'd' :
                add = add + 870
            elif p2 == 'e' :
                add = add + 5000
            elif p2 == 'f' :
                add = add + 10000
            #不同的
            if p1 == 'a':
                add = add + 30
            elif p1 == 'b' :
                add = add + 50
            elif p1 == 'c' :
                add = add + 250
            elif p1 == 'd' :
                add = add + 290
            elif p1 == 'e' :
                add = add + 1200
            elif p1 == 'f' :
                add = add + 2500
            add = round( add / 1.3 )

        #1 & 3
        elif p1 == p3 :
            #2個同
            if p3 == 'a':
                add = add + 100
            elif p3 == 'b' :
                add = add + 170
            elif p3 == 'c' :
                add = add + 780
            elif p3 == 'd' :
                add = add + 870
            elif p3 == 'e' :
                add = add + 5000
            elif p3 == 'f' :
                add = add + 10000
            #不同的
            if p2 == 'a':
                add = add + 30
            elif p2 == 'b' :
                add = add + 50
            elif p2 == 'c' :
                add = add + 250
            elif p2 == 'd' :
                add = add + 290
            elif p2 == 'e' :
                add = add + 1200
            elif p2 == 'f' :
                add = add + 2500
            add = round( add / 1.3 )

        #3個都不同 加總/3
        elif p1 != p2 != p3 :
            #1
            add = only(p1,add)
            
            #2
            add = only(p2,add)
            
            #3
            add = only(p3,add)
           
            add = round( add / 3 )

        score = score + add
        ed = ed + 1

        print("第{}次".format(ed))
        print("+" ,add)
        print("目前分數：",score)
    else:
        print("請勿做多餘的動作")

print("END")
print("最終分數為：",score)