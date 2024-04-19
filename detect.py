import cv2
from gtts import gTTS
model = cv2.dnn.readNetFromTensorflow('idk')
image = cv2.imread('fish.jpg')
blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(300, 300), mean=(104.0, 177.0, 123.0), swapRB=True, crop=False)
model.setInput(blob)
output = model.forward()
highest_confidence = 0
best_label = ""
for detection in output[0, 0]:
    confidence = detection[2]
    if confidence > highest_confidence:
        highest_confidence = confidence
        best_label = detection[1]
tts = gTTS(best_label)
tts.save('voice.mp3')