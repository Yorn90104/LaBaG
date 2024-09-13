#region 定義區
from random import randint

ram1 = 0
ram2 = 0
ram3 = 0

p1 = ''
p2 = ''
p3 = ''

score = 0
add = 0
times = 30
ed = 0

def change(x,y) :
      '(歸屬,隨機數)'
      if y <= 36 :
            x = 'A'
      elif 36 < y <= 60 :
            x = 'B'
      elif 60 < y <= 77 :
            x = 'C'
      elif 77 < y <= 89 :
            x = 'D'
      elif 89 < y <= 97 :
            x = 'E'
      else :
            x = 'F'
      return x

def only(x,y) :
      '(歸屬,增加分)'
      if x == 'A':
            y = y + 100
      elif x == 'B' :
            y = y + 170
      elif x == 'C' :
            y = y + 780
      elif x == 'D' :
            y = y + 870
      elif x == 'E' :
            y = y + 5000
      elif x == 'F' :
            y = y + 10000
      return y

def result(s , a , e) :
    "(總分,增加分,已遊玩次數)"
    s = s + a
    print(f"第{e}次")
    print("+" ,a)
    print("目前分數：",s)

#endregion

#region 執行區
print("共 {} 次".format(times))
print("按下 ENTER 開始")
while ed < times :
    add = 0
    
    #暫時代替按鈕
    press=input()
    
    if press == "" :
        #隨機數
        ram1 = randint(1,100)
        ram2 = randint(1,100)
        ram3 = randint(1,100)

        #歸屬
        p1 = change(p1,ram1)
        p2 = change(p2,ram2)
        p3 = change(p3,ram3)


        print(' | ', p1 ,' | ', p2 ,' | ', p3 ,' | ')

        #增加分數
        #3個相同
        if p1 == p2 == p3 :
            if p1 == 'A':
                add = add + 200
            elif p1 == 'B' :
                add = add + 600
            elif p1 == 'C' :
                add = add + 1600
            elif p1 == 'D' :
                add = add + 1800
            elif p1 == 'E' :
                add = add + 10000
            elif p1 == 'F' :
                add = add + 20000

        #2個相同=(2個相同的+1個不同的)/1.3
        # 1 & 2
        elif p1 == p2 :
            #2個同
            if p2 == 'A':
                add = add + 100
            elif p2 == 'B' :
                add = add + 170
            elif p2 == 'C' :
                add = add + 780
            elif p2 == 'D' :
                add = add + 870
            elif p2 == 'E' :
                add = add + 5000
            elif p2 == 'F' :
                add = add + 10000
            #不同的
            if p3 == 'A':
                add = add + 30
            elif p3 == 'B' :
                add = add + 50
            elif p3 == 'C' :
                add = add + 250
            elif p3 == 'D' :
                add = add + 290
            elif p3 == 'E' :
                add = add + 1200
            elif p3 == 'F' :
                add = add + 2500
            add = round( add / 1.3 )

        # 2 & 3
        elif p2 == p3 :
            #2個同
            if p2 == 'A':
                add = add + 100
            elif p2 == 'B' :
                add = add + 170
            elif p2 == 'C' :
                add = add + 780
            elif p2 == 'D' :
                add = add + 870
            elif p2 == 'E' :
                add = add + 5000
            elif p2 == 'F' :
                add = add + 10000
            #不同的
            if p1 == 'A':
                add = add + 30
            elif p1 == 'B' :
                add = add + 50
            elif p1 == 'C' :
                add = add + 250
            elif p1 == 'D' :
                add = add + 290
            elif p1 == 'E' :
                add = add + 1200
            elif p1 == 'F' :
                add = add + 2500
            add = round( add / 1.3 )

        # 1 & 3
        elif p1 == p3 :
            #2個同
            if p3 == 'A':
                add = add + 100
            elif p3 == 'B' :
                add = add + 170
            elif p3 == 'C' :
                add = add + 780
            elif p3 == 'D' :
                add = add + 870
            elif p3 == 'E' :
                add = add + 5000
            elif p3 == 'F' :
                add = add + 10000
            #不同的
            if p2 == 'A':
                add = add + 30
            elif p2 == 'B' :
                add = add + 50
            elif p2 == 'C' :
                add = add + 250
            elif p2 == 'D' :
                add = add + 290
            elif p2 == 'E' :
                add = add + 1200
            elif p2 == 'F' :
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

        
        ed += 1

        result(score , add , ed)
        
    else:
        print("請勿做多餘的動作")
#endregion

#region 結尾
print("END")
print("最終分數為：",score)
#endregion
