"""
Skript, um die Webcam zu aktivieren und Live Aufnahmen zu nehmen

frame[120:120+250, 200:200+250, :] <-- modifiziere das Frame, um optimal auf das Bauteil zu sehen
"""
import cv2
import uuid
import os

POS_PATH = os.path.join('data', 'positive')
NEG_PATH = os.path.join('data', 'negative')
ANC_PATH = os.path.join('data', 'anchor')

os.makedirs(POS_PATH)
os.makedirs(NEG_PATH)
os.makedirs(ANC_PATH)

id = uuid.uuid1

cap = cv2.VideoCapture(4) # choose the right device here
while cap.isOpened():
    ret, frame = cap.read()
    # begrenze das Frame auf 250x250px
    frame = frame[120:120+250, 200:200+250, :]

    # erfasse Bilder (anchor = a, positive = p) und speichere sie durch Tastenbefehle 
    if cv2.waitKey(1) & 0XFF == ord('a'):
        # create unique file path
        imgname = os.path.join(ANC_PATH, '{}.jpg'.format(id))
        # write out anchor image 
        cv2.imwrite(imgname, frame)


    if cv2.waitKey(1) & 0XFF == ord('p'):
        # create unique file path
        imgname = os.path.join(POS_PATH, '{}.jpg'.format(id))
        # write out positive image 
        cv2.imwrite(imgname, frame)


    # show image on window
    cv2.imshow('image recognition', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# release webcam
cap.release()
#close image frame
cv2.destroyAllWindows()
