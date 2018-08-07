# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tfild
import os
import cv2
import numpy as np

def Select(file_extension:str ="*.*") ->str :
    # ファイル選択ダイアログの表示
    #file_extensionはファイルの拡張子を指定(指定しなければすべて表示)
    root = tk.Tk()
    root.withdraw()
    fTyp = [("",file_extension)]
    mypicrure_path=os.getenv("HOMEDRIVE") + os.getenv("HOMEPATH") + "\\Pictures"
    iDir = os.path.abspath(mypicrure_path)
    file = tfild.askopenfilename(filetypes = fTyp,initialdir = iDir)
    return file

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None