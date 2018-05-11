import tkinter as tk
import os
import tkinter.filedialog as tfild
import tkinter.messagebox as tmsg
import tkinter.ttk as ttk
import re

data=[]


def Select():
    # ファイル選択ダイアログの表示
    root = tk.Tk()
    root.withdraw()
    fTyp = [("","*.txt;*.dat")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tfild.askopenfilename(filetypes = fTyp,initialdir = iDir)
    return file

def ファイル選択():
    global df
    try:
    # 全データ
        df = Select()
    except FileNotFoundError:
        tmsg.showinfo("エラー",'ファイルが読み込めませんでした。')
        return
    m1.entryconfigure("処理実行",state=tk.NORMAL)
    Text.configure(state=tk.NORMAL)
    Text.insert(tk.END,"ファイルを選択しました\n")
    Text.configure(state=tk.DISABLED)
    

def 処理実行():
    ld = open(df)
    lines = ld.readlines()
    ld.close()

    Text.configure(state=tk.NORMAL)

    for line in lines:
        if line.find("GS_X") >= 0:
                Text.insert(tk.END,line[:-1])
                Text.insert(tk.END,"\n")
                data.insert=int(re.sub(r'\D', '', line[:-1]))

    Text.configure(state=tk.DISABLED)

def Clear():
    Text.configure(state=tk.NORMAL)
    Text.delete(1.0,tk.END)
    Text.configure(state=tk.DISABLED)

def on_closing():
    quit()

#ここからウィンドウ設定

root=tk.Tk()
root.geometry("800x600")
root.title("データ解析_GUI")

f2=tk.Frame(root)
f0 = tk.Frame(f2)
f1 = tk.Frame(f2)

Text=tk.Text(root,font=("メイリオ",12),state=tk.DISABLED)
Text.place(x=0,y=100)

# メニューの設定
m0 =tk. Menu(root)
root.configure(menu = m0)

m1 = tk.Menu(m0, tearoff = False)
m0.add_cascade(label = 'メニュー', under = 0, menu = m1)
m1.add_command(label = 'ファイルを選択', command = ファイル選択)
m1.add_command(label = '処理実行', command = 処理実行,state=tk.DISABLED)
m1.add_command(label = 'クリア', command = Clear)

v=[]
Cbutton=[]
j=0

for i in ["X加速度","Y加速度","Z加速度","速度","GPS",]:#未実装
    v.append(tk.StringVar())
    Cbutton.append(tk.Checkbutton(f1,text=i,font=("メイリオ",12),onvalue=i,offvalue="",variable=v[j]))
    Cbutton[j].pack(side = 'left')
    j=j+1

Cbox=ttk.Combobox(f2,state="readonly")
Cbox["values"]=("グラフなし","折れ線グラフ")
Cbox.current(0)

f0.pack(anchor=tk.W)
f1.pack(anchor=tk.W)
Cbox.pack(anchor=tk.W)
f2.place(x=0,y=0)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()