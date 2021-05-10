
#import libraries

import pandas as pd
import cv2

#load the image and dataset

img_path = 'C:\IoT and Computer vision\color detection\Color detection\pic1.jpg'
csv_path = 'C:\IoT and Computer vision\color detection\Color detection\colors.csv'
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
dataframe = pd.read_csv(csv_path, names=index, header=None)

#Read the image
img = cv2.imread(img_path)

#resize the image
img = cv2.resize(img,(1200,800))
clicked = False
xpos = ypos = b = g = r = 0

#to obtain color name from the csv dataset

def get_color_name(R,G,B):
    min = 2000
    for i in range(len(dataframe)):
        p = abs(R-int(dataframe.loc[i,'R']))+abs(G-int(dataframe.loc[i,'G']))+abs(B-int(dataframe.loc[i,'B']))
        if p <= min:
            min = p
            cname = dataframe.loc[i,'color_name']
    return cname

#to mark the x and y coordinates 

def draw_function(event, x, y, flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked, xpos, ypos, b, g, r
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

#to show the color name  on the image

while True:
    cv2.imshow('image',img)
    if clicked :
        cv2.rectangle(img,(20,20),(600,60),(b,g,r), -1)
        text = get_color_name(r,g,b) + 'R=' + str(r) + 'G=' + str(g) + 'B=' + str(b)
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
