# importing the module 
import cv2 

coordinates = []
file = r"F:\Hackathon\Vithack\Final\Certificate-Generator\templates\template10.jpeg"
# function to display the coordinates of 
# of the points clicked on the image 
def click_event(event, x, y, flags, params):
            
	# checking for left mouse clicks 
	if event == cv2.EVENT_LBUTTONDOWN: 

		# displaying the coordinates 
		# on the Shell 
		print(x, ' ', y) 

		# displaying the coordinates 
		# on the image window 
		font = cv2.FONT_HERSHEY_SIMPLEX 
		cv2.putText(img, str(x) + ',' +
					str(y), (x,y), font, 
					1, (255, 0, 0), 2) 
		cv2.imshow('image', img)
		coordinates.append([x,y])

	# checking for right mouse clicks	 
	if event==cv2.EVENT_RBUTTONDOWN: 

		# displaying the coordinates 
		# on the Shell 
		print(x, ' ', y) 

		# displaying the coordinates 
		# on the image window 
		font = cv2.FONT_HERSHEY_SIMPLEX 
		b = img[y, x, 0] 
		g = img[y, x, 1] 
		r = img[y, x, 2] 
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r), 
					(x,y), font, 1, 
					(255, 255, 0), 2) 
		cv2.imshow('image', img)

    
# driver function 
if __name__=="__main__": 

	# reading the image 
	img = cv2.imread(file , 1) 

	# displaying the image 
	cv2.imshow('image', img) 

	# setting mouse hadler for the image 
	# and calling the click_event() function 
	cv2.setMouseCallback('image', click_event) 

	# wait for a key to be pressed to exit 
	cv2.waitKey(0) 

	# close the window 
	cv2.destroyAllWindows()

	print('list ',coordinates)

#Create Sample files
	
from pandas import read_csv
from PIL import Image, ImageDraw, ImageFont
import random


coordinate = coordinates

data = read_csv("test1.csv").values.tolist()
template = Image.open(file)
font = ImageFont.truetype("SFPro.ttf",30)
eventfont = ImageFont.truetype("SFPro.ttf",24)

#color = (61,181,148)


number_values = input("Provide a sequence of numbers separated by commas: ")
 
list_number_values = number_values.split(",")
for i in range(0, len(list_number_values)): 
    list_number_values[i] = int(list_number_values[i]) 
      
color = tuple(list_number_values)

def makeCertificate(student):
    cert = template.copy()
    draw = ImageDraw.Draw(cert)
    
    '''#name
    w, h = draw.textsize(student[0],font)
    draw.text(xy = (965-w/2,535),text=student[0],fill=color,font=font)
    #rank
    if student[3] == "None":
        #llosr
        draw.rectangle([(652,670),(733,672)], fill ="white") 
        draw.rectangle([(815,660),(935,661)], fill =color) 
    else:
        #rank holder
        draw.rectangle([(525,670),(640,672)], fill ="white") 
        w,h = draw.textsize(student[3],font)
        draw.text(xy = (875-w/2,640),text=student[3],fill=color,font=font)
    #event
    w,h = draw.textsize(student[2],font)
    if w > 170:
        w,h = draw.textsize(student[2],eventfont)
        draw.text(xy = (1208-w/2,645),text=student[2],fill=color,font=eventfont)
    else:
        draw.text(xy = (1208-w/2,640),text=student[2],fill=color,font=font)'''
    for i in range(3):
        if(i == 0):
            w, h = draw.textsize(student[0],font)
            x,y = coordinate[0][0],coordinate[0][1]
            draw.text(xy = (x-w/2,y),text=student[0],fill=color,font=font)
        if(i == 1):
            x,y = coordinate[1][0],coordinate[1][1]
            if student[3] == "None":
                #llosr
                x1, y1 = x-175-50, y+15
                x2, y2 = x-50, y+15
                draw.rectangle([(x1,y1),(x1+80,y1+2)], fill ="white") 
                draw.rectangle([(x2,y2),(x2+80,y2+2)], fill =color) 
            else:
                #rank holder
                x1, y1 = x-75-275, y+10
                draw.rectangle([(x1,y1),(x1+80,y1+2)], fill ="white") 
                w,h = draw.textsize(student[3],font)
                draw.text(xy = (x-w/2,y),text=student[3],fill=color,font=font)
        if(i == 2):
            x,y = coordinate[2][0],coordinate[2][1]
            w,h = draw.textsize(student[2],font)
            if w > 170:
                w,h = draw.textsize(student[2],eventfont)
                draw.text(xy = (x-w/2,y),text=student[2],fill=color,font=eventfont)
            else:
                draw.text(xy = (x-w/2,y),text=student[2],fill=color,font=font)
        
        

        
    print(student[0])
    cert.save(str("img/"+student[0])+str(random.randint(1000,9999))+".png")
    
for i in data:
    makeCertificate(i)



