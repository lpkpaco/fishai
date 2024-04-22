import os
import cv2
from gtts import gTTS
#from playsound import playsound
while True:
    try:
        os.remove('runs/detect/predict/fish.jpg')
        os.remove("runs/detect/predict/labels/fish.txt")
        os.rmdir("runs/detect/predict/labels/")
        os.rmdir("runs/detect/predict/")
        os.remove("fish.jpg")
        os.remove('fish.mp3')
    except:
        pass
    names = ['areolate grouper', 'big eye', 'blackhead sea bream', 'fourfinger threadfin', 'golden threadfin bream', 'grey mullet', 'grouper', 'headgrunt', 'leopard coral trout', 'moontail grouper', 'pampano', 'panther grouper', 'plectropomusmaculatus', 'pomfret', 'queensland grouper', 'red emperor', 'red grouper', 'redtilpma', 'rogaa', 'sabah giant grouper', 'sardin', 'sebae', 'silver grunt', 'squaretail coral grouper', 'tuna', 'yellow fin seabream']    
    os.system("libcamera-still -o fish.jpg")
    os.system("yolo detect predict model=/home/paco/Desktop/fishai/detect/best.pt source=fish.jpg save_txt=True")
    #os.remove("fish.jpg")
    try:
        txt = open('runs/detect/predict/labels/fish.txt', 'r')
    except:                                 
        print("No fish detected")
        tts = gTTS("No fish detected")
        tts.save('fish.mp3')
        os.system('mpg123 fish.mp3')
        continue
    line = txt.readline()
    #while line is not None and list != '':
    classno = int(line[0])
    label = names[classno]
    tts = gTTS(str(label))
    tts.save('fish.mp3')
    print(label)
    os.system('mpg123 fish.mp3')
    img = cv2.imread("runs/detect/predict/fish.jpg")
    cv2.imshow("result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
