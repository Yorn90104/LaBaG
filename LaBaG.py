
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

print("共 {} 次".format(times))

while ed < times :
    add = 0
    #暫時代替按鈕
    button=input("按下 ENTER 開始")
    if button == "" :
        #隨機數
        import random
        ram1 = random.randint(1,100)
        ram2 = random.randint(1,100)
        ram3 = random.randint(1,100)

        #1
        if ram1 <= 36 :
            p1 = 'a'
        elif 36 < ram1 <= 60 :
            p1 = 'b'
        elif 60 < ram1 <= 77 :
            p1 = 'c'
        elif 77 < ram1 <= 89 :
            p1 = 'd'
        elif 89 < ram1 <= 97 :
            p1 = 'e'
        else :
            p1 = 'f'
        #2
        if ram2 <= 36 :
            p2 = 'a'
        elif 36 < ram2 <= 60 :
            p2 = 'b'
        elif 60 < ram2 <= 77 :
            p2 = 'c'
        elif 77 < ram2 <= 89 :
            p2 = 'd'
        elif 89 < ram2 <= 97 :
            p2 = 'e'
        else :
            p2 = 'f'
        #3
        if ram3 <= 36 :
            p3 = 'a'
        elif 36 < ram3 <= 60 :
            p3 = 'b'
        elif 60 < ram3 <= 77 :
            p3 = 'c'
        elif 77 < ram3 <= 89 :
            p3 = 'd'
        elif 89 < ram3 <= 97 :
            p3 = 'e'
        else :
            p3 = 'f'

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
            #2
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
            #3
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