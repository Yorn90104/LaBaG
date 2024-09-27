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

def GamePIC(pc, x, y):
    """加載新的圖片並放在Game的CANVA上 (照片, 水平座標, 垂直座標)"""
    canvas_Game.create_image(x, y, image = pc, anchor = "nw")

def EndPIC(pc, x, y):
    """加載新的圖片並放在End的CANVA上 (照片, 水平座標, 垂直座標)"""
    canvas_End.create_image(x, y, image = pc, anchor = "nw")

win = tk.Tk()  # 建立視窗
win.title("啦八機")  # 視窗標題
win.iconbitmap('.\\Asset\\Superhhh.ico')  # 視窗小圖
win.geometry("450x800")  # 視窗長寬
win.resizable(False , False)  # 禁用水平和垂直方向的調整

# 創建兩個 Frame，分別代表不同的畫面
frame_Game = tk.Frame(win, width=450, height=800, bg='lightblue')
frame_End = tk.Frame(win, width=450, height=800, bg='lightgreen')

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
SB = IMAGE('.\\Asset\\SB.png' , 450 , 169) #記分板

# 創建 Canvas 並設置背景圖片
#Game畫面
canvas_Game = tk.Canvas(frame_Game, width=450, height=800)
canvas_Game.pack(fill="both", expand=True)
canvas_Game.create_image(0, 0, image=BG, anchor="nw")
#End畫面
canvas_End = tk.Canvas(frame_End, width=450, height=800)
canvas_End.pack(fill="both", expand=True)
canvas_End.create_image(0, 0, image=BG, anchor="nw")
#endregion

#region 遊戲邏輯變數區
ram1, ram2, ram3 = 0 , 0 , 0
p1, p2, p3 = '', '', ''
score, add, times, ed = 0 , 0 , 5 , 0

# 分數清單
same3 = [200 , 600 , 1600 , 1800 , 10000 , 20000]
same2 = [100 , 170 , 780 , 870 , 5000 , 10000]
same1 = [30 , 50 , 250 , 290 , 1200 , 2500]
picture = [Gss , Hhh , Hentai , Handsun , Kachu , Rrr]

# 初始圖片
L_PIC = GamePIC(QST, 0, 250)
M_PIC = GamePIC(QST, 150, 250)
R_PIC = GamePIC(QST, 300, 250)
#endregion

#region 遊戲邏輯函數區
def INIT():
    """初始化顯示"""
    global L_PIC, M_PIC, R_PIC, text_ADD
    canvas_Game.delete(L_PIC)
    canvas_Game.delete(M_PIC)
    canvas_Game.delete(R_PIC)

    canvas_Game.itemconfig(text_ADD , text = "" )
    L_PIC = GamePIC(QST, 0, 250)
    M_PIC = GamePIC(QST, 150, 250)
    R_PIC = GamePIC(QST, 300, 250)

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
    canvas_Game.delete(L)  # 刪除舊圖片
    L = GamePIC(PIC(p), x, y)  # 加載新圖片
    Ding()

def Display():
    """顯示結果"""
    global score, add, ed, times, text_Score, text_ADD, text_Times

    canvas_Game.itemconfig(text_ADD , text = f"+{add}" )
    canvas_Game.itemconfig(text_Score , text = f"目前分數：{score}" )
    canvas_Game.itemconfig(text_Times , text = f"剩餘次數：{times - ed}" )

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

    return 

def Able():
    """3.5秒後啟用開始按鈕 & ENTER"""
    start_button.config(state="normal")
    win.bind('<Return>', ENTER)

def Unable():
    """停用按鈕和ENTER鍵"""
    start_button.config(state="disabled")
    win.unbind('<Return>')

def game_over():
    """遊戲結束，切換到結果頁面"""
    frame_Game.pack_forget()  # 隱藏遊戲畫面
    print("切換End畫面")
    frame_End.pack(fill='both', expand=True)  # 顯示遊戲結束畫面
    canvas_End.itemconfig(text_Over, text="遊戲結束！") 
    canvas_End.itemconfig(text_ANS, text=f"最終分數：{score}")  # 更新分數顯示

def Begin() :
      global ram1 , ram2 , ram3 , p1 , p2 , p3 , score , add , ed , L_PIC , M_PIC , R_PIC

      print(u"按鈕被點擊了！")

      Unable()

      INIT()
      
      if ed  < times :
      
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
            
            if ed + 1 >= times:
                # 判斷遊戲結束
                print("遊戲已結束")
                print(f"最終分數為：{score}")
                
                # 停用按鈕和鍵盤事件
                win.after(3500, Unable)

                # 切換到結束畫面
                win.after(3500, game_over)
                
            else:
                # 遊戲繼續
                win.after(3500 , lambda : Able())
                        
#endregion

print(u"共 {} 次".format(times))

def ENTER(event) :
      Begin()

#Game畫面
start_button = tk.Button(win , image = BeginPIC , command=Begin)
win.bind('<Return>', ENTER)
button_Begin = canvas_Game.create_window(225 , 575 , window = start_button) #將按鈕放置Game的Canva上

text_ADD =  canvas_Game.create_text(225, 475, text = "" , font = ("Arial", 16 , "bold") , fill = "yellow")
text_Score =  canvas_Game.create_text(225, 500, text = f"目前分數：{score}", font = ("Arial", 16 , "bold") , fill = "white")
text_Times =  canvas_Game.create_text(225, 525, text = f"剩餘次數：{times - ed}", font = ("Arial", 16 , "bold") , fill = "white")

pic_Title = GamePIC(Title , 0 , 25)

#End畫面
def Again():
    "再一次"
    global ram1 , ram2 , ram3 , p1 , p2 , p3 , score , add , ed  , times, text_Score, text_ADD, text_Times
    ram1, ram2, ram3 = 0 , 0 , 0
    p1, p2, p3 = '', '', ''
    score, add, ed = 0 , 0 , 0

    INIT()
    Able()
    canvas_Game.itemconfig(text_ADD , text = "" )
    canvas_Game.itemconfig(text_Score , text = f"目前分數：{score}" )
    canvas_Game.itemconfig(text_Times , text = f"剩餘次數：{times - ed}" )
    
    frame_End.pack_forget()
    frame_Game.pack(fill='both', expand=True)

again_button = tk.Button(win , text = "再玩一次" , command = Again , width = 10, height = 1 , font = ("Arial", 20, "bold"))
button_again = canvas_End.create_window(225 , 425 , window = again_button) #將按鈕放置END的Canva上

text_Over =  canvas_End.create_text(225, 280 , text = f"", font = ("Arial", 42 , "bold") , fill = "white")
text_ANS =  canvas_End.create_text(225, 345 , text = f"", font = ("Arial", 32 , "bold") , fill = "Gold")

pic_SB = EndPIC(SB , 0 , 500)

frame_Game.pack(fill='both', expand=True)
win.mainloop() #視窗常駐

