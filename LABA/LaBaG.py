import sys
sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk
from PIL import Image , ImageTk
from random import randint #隨機數字

#region 視窗區
def IMAGE(file , w , h) :
    "處理成TK可識別的圖"
    "(路徑,長,寬)"
    pc = Image.open(file)  
    pc = pc.resize((w, h), Image.LANCZOS)  # 调整图片大小
    pc = ImageTk.PhotoImage(pc)
    return pc

def resize_BG(event) :
    #獲取當前長寬
    New_width = event.width
    New_height = event.height

    #調整大小&更新圖片
    New_BG = IMAGE(r'.\Asset\BG.png' , New_width , New_height)
    canvas.delete("bg") #刪除標記為"bg"的圖片
    canvas.create_image(0, 0, image=New_BG, anchor="nw", tags="bg") #新圖片

    #保存圖像引用 防止被回收(New_BG為非全域變數)
    canvas.image = New_BG
    
    # 更新 Canvas 的大小以匹配新的視窗大小
    canvas.config(width=New_width, height=New_height)

    canvas.coords(button_Begin, New_width // 2, New_height // 2)

win = tk.Tk() #建立視窗
win.title("啦八機") #視窗標題
win.iconbitmap(r'.\Asset\Superhhh.ico') #視窗小圖
win.geometry("640x360") #視窗長寬

BG = IMAGE(r'.\Asset\BG.png' , 640 , 360)

# 创建 Canvas & 设置背景图片
canvas = tk.Canvas(win, width=640, height=360)
canvas.pack(fill="both", expand=True) #在視窗中水平和垂直方向上擴展，以填充其父容器的空間
canvas.create_image(0, 0, image=BG, anchor="nw" , tags = "bg") #初次加載圖片 & "nw" = north west & 標記圖片為"bg"

#綁定視窗大小變化事件
win.bind('<Configure>', resize_BG)

#endregion

#region 定義區
ram1 , ram2 , ram3 = 0 , 0 , 0

p1 , p2 , p3 = '' , '' , ''

score = 0
add = 0
times = 30
ed = 0

#分數清單
same3 = [200 , 600 , 1600 , 1800 , 10000 , 20000]
same2 = [100 , 170 , 780 , 870 , 5000 , 10000]
same1 = [30 , 50 , 250 , 290 , 1200 , 2500]

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

def ADD(x,y,lst) :
      '(歸屬,增加分,分數清單)'
      if x == 'A':
            y = y + lst[0]
      elif x == 'B' :
            y = y + lst[1]
      elif x == 'C' :
            y = y + lst[2]
      elif x == 'D' :
            y = y + lst[3]
      elif x == 'E' :
            y = y + lst[4]
      elif x == 'F' :
            y = y + lst[5]
      return y

def result() :
    global score , add , ed
    ed += 1
    score += add
    print(f"第{ed}次")
    print(f"+{add}")
    print(f"目前分數：{score}")
    add = 0

def Begin() :
      global ram1 , ram2 , ram3 , p1 , p2 , p3 , score , add , ed

      print(u"按鈕被點擊了！")
      
      if ed >= times :
            #判斷結束
            print(U"遊戲已結束")
            print(u"最終分數為：",score)
            return

      #未結束
      #隨機數
      ram1 = randint(1,100)
      ram2 = randint(1,100)
      ram3 = randint(1,100)

      #歸屬
      p1 = change(p1,ram1)
      p2 = change(p2,ram2)
      p3 = change(p3,ram3)


      print(f' | {p1} | {p2} | {p3} |')

      #增加分數
      #3個相同
      if p1 == p2 == p3 :
            add = ADD(p1 , add , same3)

      #2個相同=(2個相同的+1個不同的)/1.3
      # 1 & 2
      elif p1 == p2 :
            add = ADD(p1 , add , same2)
            #不同的
            add = ADD(p3 , add , same1)

            add = round( add / 1.3 )

      # 2 & 3
      elif p2 == p3 :
            #2個同
            add = ADD(p2 , add , same2)
            #不同的
            add = ADD(p1 , add , same1)

            add = round( add / 1.3 )

      # 1 & 3
      elif p1 == p3 :
            #2個同
            add = ADD(p3 , add , same2)
            #不同的
            add = ADD(p2 , add , same1)

            add = round( add / 1.3 )

      #3個都不同 加總/3
      elif p1 != p2 != p3 :
            #1
            add = ADD(p1 , add , same1)
            
            #2
            add = ADD(p2 , add , same1)
            
            #3
            add = ADD(p3 , add , same1)
      
            add = round( add / 3 )

      result()
                  
#endregion

print(u"共 {} 次".format(times))

start = tk.Button(win, text="開始", command=Begin)
button_Begin = canvas.create_window(320, 180, window=start)#將按鈕放置Canva上 320 180 為居中初始位置

win.mainloop() #視窗常駐

