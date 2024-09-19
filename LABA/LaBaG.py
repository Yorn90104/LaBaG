import sys
sys.stdout.reconfigure(encoding='utf-8')

import tkinter as tk
from PIL import Image, ImageTk
import pygame
from random import randint  # 隨機數字

# 初始化音訊
pygame.mixer.init()

def Ding():
    """播放叮音效"""
    pygame.mixer.music.load('.\\Asset\\Ding.mp3')  # 加載音效文件
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()  # 播放音效

#region 視窗區
def IMAGE(file, w, h):
    """處理成TK可識別的圖 (路徑, 長, 寬)"""
    pc = Image.open(file)
    pc = pc.resize((w , h) , Image.LANCZOS)  # 調整圖片大小
    pc = ImageTk.PhotoImage(pc)
    return pc

def CanvaPIC(pc, x, y):
    """加載新的圖片並放在CANVA上 (照片, 水平座標, 垂直座標)"""
    canvas.create_image(x, y, image = pc, anchor = "nw")

win = tk.Tk()  # 建立視窗
win.title("啦八機")  # 視窗標題
win.iconbitmap('.\\Asset\\Superhhh.ico')  # 視窗小圖
win.geometry("450x800")  # 視窗長寬
win.resizable(False , False)  # 禁用水平和垂直方向的調整

# 圖片
BG = IMAGE('.\\Asset\\BG.png' , 450 , 800)
Title = IMAGE('.\\Asset\\Title.png' , 450 , 253)
QST = IMAGE('.\\Asset\\QST.jpg' , 150 , 200)  # ?
Gss = IMAGE('.\\Asset\\Gss.jpg' , 150 , 200)  # A
Hhh = IMAGE('.\\Asset\\Hhh.jpg' , 150 , 200)  # B
Hentai = IMAGE('.\\Asset\\Hentai.jpg' , 150 , 200)  # C
Handsun = IMAGE('.\\Asset\\Handsun.jpg' , 150 , 200)  # D
Kachu = IMAGE('.\\Asset\\Kachu.jpg' , 150 , 200)  # E
Rrr = IMAGE('.\\Asset\\RRR.jpg' , 150 , 200)  # F
BeginPIC = IMAGE('.\\Asset\\Start.jpg' , 150 , 50)

# 創建 Canvas 並設置背景圖片
canvas = tk.Canvas(win, width=450, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=BG, anchor="nw")
#endregion

#region 遊戲邏輯變數區
ram1, ram2, ram3 = 0 , 0 , 0
p1, p2, p3 = '', '', ''
score, add, times, ed = 0 , 0 , 30 , 0

# 分數清單
same3 = [200 , 600 , 1600 , 1800 , 10000 , 20000]
same2 = [100 , 170 , 780 , 870 , 5000 , 10000]
same1 = [30 , 50 , 250 , 290 , 1200 , 2500]
picture = [Gss , Hhh , Hentai , Handsun , Kachu , Rrr]

# 初始圖片
L_PIC = CanvaPIC(QST, 0, 250)
M_PIC = CanvaPIC(QST, 150, 250)
R_PIC = CanvaPIC(QST, 300, 250)
#endregion

#region 遊戲邏輯函數區
def INIT():
    """初始化顯示"""
    global L_PIC, M_PIC, R_PIC, text_ADD
    canvas.delete(L_PIC)
    canvas.delete(M_PIC)
    canvas.delete(R_PIC)
    canvas.delete(text_ADD)

    text_ADD = canvas.create_text(225, 475, text="", font=("Arial", 16, "bold"))
    L_PIC = CanvaPIC(QST, 0, 250)
    M_PIC = CanvaPIC(QST, 150, 250)
    R_PIC = CanvaPIC(QST, 300, 250)

def PIC(p):
    """根據歸屬選擇圖 (歸屬)"""
    if p == "A":
        return picture[0]
    elif p == "B":
        return picture[1]
    elif p == "C":
        return picture[2]
    elif p == "D":
        return picture[3]
    elif p == "E":
        return picture[4]
    elif p == "F":
        return picture[5]

def ChangeA(x, y):
    """根據隨機數生成圖片的歸屬 (歸屬, 隨機數)"""
    if y <= 36:
        return 'A'
    elif 36 < y <= 60:
        return 'B'
    elif 60 < y <= 77:
        return 'C'
    elif 77 < y <= 89:
        return 'D'
    elif 89 < y <= 97:
        return 'E'
    else:
        return 'F'

def Local(L, p, x, y):
    """哪個位置變圖 (位置, 歸屬, 圖)"""
    canvas.delete(L)  # 刪除舊圖片
    L = CanvaPIC(PIC(p), x, y)  # 加載新圖片
    Ding()

def Display():
    """顯示結果"""
    global score, add, ed, times, text_Score, text_ADD, text_Times
    canvas.delete(text_ADD)
    canvas.delete(text_Score)
    canvas.delete(text_Times)

    text_ADD = canvas.create_text(225, 475, text=f"+{add}", font=("Arial", 16, "bold"), fill="yellow")
    text_Score = canvas.create_text(225, 500, text=f"目前分數：{score}", font=("Arial", 16, "bold"), fill="white")
    text_Times = canvas.create_text(225, 525, text=f"剩餘次數：{times - ed}", font=("Arial", 16, "bold"), fill="white")

def ADD(x, y, lst):
    """增加分數 (歸屬, 增加分數, 分數清單)"""
    if x == 'A':
        y += lst[0]
    elif x == 'B':
        y += lst[1]
    elif x == 'C':
        y += lst[2]
    elif x == 'D':
        y += lst[3]
    elif x == 'E':
        y += lst[4]
    elif x == 'F':
        y += lst[5]
    return y

def result():
    """計算和顯示結果"""
    global score, add, ed, p1, p2, p3, text_Score
    ed += 1
    score += add
    print(f"第{ed}次")
    print(f' | {p1} | {p2} | {p3} |')
    print(f"+{add}")
    print(f"目前分數：{score}")
    Display()
    add = 0

def Able():
    """3.5秒後啟用開始按鈕 & ENTER"""
    win.after(3500, lambda: start_button.config(state="normal"))
    win.after(3500, lambda: win.bind('<Return>', ENTER))

def Unable():
    """停用按鈕和ENTER鍵"""
    start_button.config(state="disabled")
    win.unbind('<Return>')

def Begin() :
      global ram1 , ram2 , ram3 , p1 , p2 , p3 , score , add , ed , L_PIC , M_PIC , R_PIC

      print(u"按鈕被點擊了！")

      Unable()

      INIT()
      
      if ed < times :
      
            #隨機數
            ram1 , ram2 , ram3 = randint(1,100) , randint(1,100) , randint(1,100)

            #歸屬
            p1 = ChangeA(p1,ram1)
            p2 = ChangeA(p2,ram2)
            p3 = ChangeA(p3,ram3)

            #每隔0.5秒改圖片
            win.after(500 , lambda : Local(L_PIC , p1 , 0 , 250))
            win.after(1000 , lambda : Local(M_PIC , p2 , 150 , 250))
            win.after(1500 , lambda : Local(R_PIC , p3 , 300 , 250))

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

            win.after(3000 , result)
            
            if ed >= times :
                  #判斷結束
                  print(U"遊戲已結束")
                  print(u"最終分數為：",score)
                  
                  Unable()
                  return
            else :
                  Able()
                  
#endregion

print(u"共 {} 次".format(times))

def ENTER(event) :
      Begin()

start_button = tk.Button(win , image = BeginPIC , command=Begin)
win.bind('<Return>', ENTER)
button_Begin = canvas.create_window(225 , 575 , window = start_button) #將按鈕放置Canva上居中位置

text_ADD =  canvas.create_text(225, 475, text = "" , font = ("Arial", 16 , "bold"))
text_Score =  canvas.create_text(225, 500, text = f"目前分數：{score}", font = ("Arial", 16 , "bold") , fill = "white")
text_Times =  canvas.create_text(225, 525, text = f"剩餘次數：{times - ed}", font = ("Arial", 16 , "bold") , fill = "white")

pic_Title = CanvaPIC(Title , 0 , 25)

win.mainloop() #視窗常駐

