from tkinter import *
from pyautogui import size
from gtts import gTTS
import os
from PIL import ImageTk, Image
def new():
    global w2
    px2 = PhotoImage(width=1, height=1)
    w1.destroy()
    w2 = Toplevel()
    w2.geometry(str(swidth)+"x"+str(sheight))
    w2.resizable(0, 0)
    w2.attributes('-fullscreen', True)
    try:
        os.remove('runs/detect/predict/fish.jpg')
        os.remove("runs/detect/predict/labels/fish.txt")
        os.rmdir("runs/detect/predict/labels/")
        os.rmdir("runs/detect/predict/")
        #os.remove("fish.jpg")
        os.remove('fish.mp3')
        os.remove('fishzh.mp3')
    except:
        pass
    names = ['areolate grouper', 'big eye', 'blackhead sea bream', 'fourfinger threadfin', 'golden threadfin bream', 'grey mullet', 'grouper', 'headgrunt', 'leopard coral trout', 'moontail grouper', 'pampano', 'panther grouper', 'plectropomusmaculatus', 'pomfret', 'queensland grouper', 'red emperor', 'red grouper', 'redtilpma', 'rogaa', 'sabah giant grouper', 'sardin', 'sebae', 'silver grunt', 'squaretail coral grouper', 'tuna', 'yellow fin seabream']    
    nameszh = ['芝麻斑', '大眼鯽', '黑鱲', '馬友', '紅衫魚', '烏頭', '石斑', '頭鱸', '東星斑', '燕尾斑', '黃立倉', '老鼠斑', '泰星斑', '倉魚', '花尾龍躉', '紅魚', '紅瓜子斑', '珍珠鱲', '黑瓜子斑', '沙巴龍躉', '沙甸魚', '三刀魚', '銀鯽魚', '西星斑', '吞拿魚', '黃脚鱲']
    #os.system("libcamera-still -o fish.jpg")
    #os.system("yolo detect predict model=/home/paco/Desktop/fishai/detect/best.pt source=fish.jpg save_txt=True")
    #os.remove("fish.jpg")
    try:
        txt = open('runs/detect/predict/labels/fish.txt', 'r')
    except:                                 
        print("No fish detected")
        tts = gTTS("No fish detected")
        ttszh = gTTS('未檢測到魚', lang='zh-tw')
        tts.save('fish.mp3')
        ttszh.save('fishzh.mp3')
        theimg = Image.open('fish.jpg')
        theimg = theimg.resize((int(swidth*0.8), int(sheight*0.45)))
        pimg = ImageTk.PhotoImage(theimg)
        Label(w2, image=pimg).grid(row=0, column=0)
        Label(w2, text='未檢測到魚').grid(row=1, column=0)
        Label(w2, text='No fish detected').grid(row=2, column=0)
        Button(w2, image=px2, text="Return to Menu", command=lambda: [w2.destroy(), start()], width=bwidth, height=bheight, compound='c').grid(column=0, row=2)
        #os.system('mpg123 fishzh.mp3')
        #os.system('mpg123 fish.mp3')
        #w2.mainloop()
    line = txt.readline()
    #while line is not None and list != '':
    classno = int(line[0])
    label = names[classno]
    labelzh = nameszh[classno]
    tts = gTTS(str(label))
    tts.save('fish.mp3')
    ttszh = gTTS(str(labelzh), lang='zh-tw')
    ttszh.save('fishzh.mp3')
    print(label)
    theimg = Image.open('runs/detect/predict/fish.jpg')
    theimg = theimg.resize((int(swidth*0.8), int(sheight*0.45)))
    pimg = ImageTk.PhotoImage(theimg)
    Label(w2, image=pimg).grid(row=0, column=0,)
    Label(w2, text=labelzh).grid(row=1, column=0)
    Label(w2, text=label).grid(row=2, column=0)
    Button(w1, image=px2, text="Return to Menu", command=new, width=bwidth, height=bheight, compound='c').grid(column=0, row=2)
    os.system('mpg123 fishzh.mp3')
    os.system('mpg123 fish.mp3')
    #img = cv2.imread("runs/detect/predict/fish.jpg")
    #cv2.imshow("result", img)
    #cv2.destroyAllWindows()
    #w2.mainloop()
def start():
    global swidth, sheight, bwidth, bheight, w1
    w1 = Toplevel()
    screensize = size()
    swidth = screensize.width
    sheight = screensize.height
    w1.geometry(str(swidth)+"x"+str(sheight))
    w1.resizable(0, 0)
    w1.attributes('-fullscreen', True)
    bwidth = int(swidth*0.2)
    bheight = int(sheight*0.15)
    px = PhotoImage(width=1, height=1)
    Button(w1, image=px, text="Start", command=new, width=bwidth, height=bheight, compound='c').place(relx=0.5, rely=0.5, anchor=CENTER)
    w1.mainloop()
start()