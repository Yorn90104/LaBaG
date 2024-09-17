import tkinter as tk
from PIL import Image, ImageTk
from random import randint

def IMAGE(file, w, h):
    """處理成Tkinter可識別的圖像"""
    pc = Image.open(file)
    pc = pc.resize((w, h), Image.LANCZOS)
    pc = ImageTk.PhotoImage(pc)
    return pc

def change(y):
    """根據隨機數字轉換為類別"""
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

def ADD(x, y, lst):
    """根據類別更新分數"""
    index = ord(x) - ord('A')
    if 0 <= index < len(lst):
        return y + lst[index]
    return y

def result():
    global score, add, ed, p1, p2, p3
    ed += 1
    score += add
    print(f"第{ed}次")
    print(f' | {p1} | {p2} | {p3} |')
    print(f"+{add}")
    print(f"目前分數：{score}")
    add = 0

def Begin():
    global ram1, ram2, ram3, p1, p2, p3, score, add, ed

    if ed < times:
        # 隨機數
        ram1, ram2, ram3 = randint(1, 100), randint(1, 100), randint(1, 100)

        # 類別轉換
        p1 = change(ram1)
        p2 = change(ram2)
        p3 = change(ram3)

        # 增加分數
        if p1 == p2 == p3:
            add = ADD(p1, add, same3)
        elif p1 == p2 or p2 == p3 or p1 == p3:
            add = ADD(p1, add, same2) if p1 == p2 else ADD(p2, add, same2) if p2 == p3 else ADD(p3, add, same2)
            add = ADD(p1 if p1 != p2 else p3, add, same1)
            add = round(add / 1.3)
        else:
            add = ADD(p1, add, same1) + ADD(p2, add, same1) + ADD(p3, add, same1)
            add = round(add / 3)

        result()

        if ed >= times:
            print("遊戲已結束")
            print(f"最終分數為：{score}")
            return

# 遊戲參數
same3 = [200, 600, 1600, 1800, 10000, 20000]
same2 = [100, 170, 780, 870, 5000, 10000]
same1 = [30, 50, 250, 290, 1200, 2500]

score = 0
add = 0
times = 30
ed = 0

# 設置Tkinter視窗
win = tk.Tk()
win.title("遊戲")
win.iconbitmap(r'.\Asset\Superhhh.ico')
win.geometry("360x640")
win.resizable(False, False)

BG = IMAGE(r'.\Asset\BG.png', 360, 640)

canvas = tk.Canvas(win, width=360, height=640)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=BG, anchor="nw")

start = tk.Button(win, text="開始", command=Begin)
button_Begin = canvas.create_window(180, 320, window=start)

win.mainloop()
