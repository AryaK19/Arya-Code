import cv2 as cv
#_____________________________________________recognizing_________________________________________
def persons_input(hand_cordinates):
    def distance(x1,y1,x2,y2):
        distance=int((((x1-x2)**2)+((y1-y2)**2))**(1/2))
        return distance
    persons_input=""
    # Fingering up
    index_up=False
    middel_up=False
    ring_up=False
    littel_up=False
    if distance(hand_cordinates[5][1],hand_cordinates[5][2],hand_cordinates[6][1],hand_cordinates[6][2])<distance(hand_cordinates[5][1],hand_cordinates[5][2],hand_cordinates[7][1],hand_cordinates[7][2]):
        index_up=True
    if distance(hand_cordinates[9][1],hand_cordinates[9][2],hand_cordinates[10][1],hand_cordinates[10][2])<distance(hand_cordinates[9][1],hand_cordinates[9][2],hand_cordinates[11][1],hand_cordinates[11][2]):
        middel_up=True
    if distance(hand_cordinates[13][1],hand_cordinates[13][2],hand_cordinates[14][1],hand_cordinates[14][2])<distance(hand_cordinates[13][1],hand_cordinates[13][2],hand_cordinates[15][1],hand_cordinates[15][2]):
        ring_up=True
    if distance(hand_cordinates[17][1],hand_cordinates[17][2],hand_cordinates[18][1],hand_cordinates[18][2])<distance(hand_cordinates[17][1],hand_cordinates[17][2],hand_cordinates[19][1],hand_cordinates[19][2]):
        littel_up=True
    # Stone,Paper,Scissor
    if index_up==False and middel_up==False and ring_up==False and littel_up==False:
        persons_input="STONE"
    elif index_up==True and middel_up==True and ring_up==True and littel_up==True:
        persons_input="PAPER"
    elif index_up==True and middel_up==True and ring_up==False and littel_up==False:
        persons_input="SCISSORS"
    elif index_up==False and middel_up==True and ring_up==False and littel_up==False:
        persons_input="FUCK U"
    elif index_up==True and middel_up==True and ring_up==False and littel_up==True:
        persons_input="KAUSHIK"
        
    return persons_input

#_________________________________________________geting_frame_______________________________________
def get_fram(image,hand_cordinate,string):
   def x_max(hand_cordinate):
      max_val=0
      for cordinate_list in hand_cordinate:
         if max_val<cordinate_list[1]:    # 1 is x-cord value
            max_val=cordinate_list[1]
      return max_val
   def y_max(hand_cordinate):
      max_val=0
      for cordinate_list in hand_cordinate:
         if max_val<cordinate_list[2]:    # 2 is y-cord value
            max_val=cordinate_list[2]
      return max_val
   def x_min(hand_cordinate):
      min_val=hand_cordinate[0][1]
      for cordinate_list in hand_cordinate:
         if min_val>cordinate_list[1]:
            min_val=cordinate_list[1]
      return min_val
   def y_min(hand_cordinate):
      min_val=hand_cordinate[0][2]
      for cordinate_list in hand_cordinate:
         if min_val>cordinate_list[2]:
            min_val=cordinate_list[2]
      return min_val
   
   def show_holy_rect(image,start_point,end_point,string):
      maxX=image.shape[1]
      image = cv.rectangle(image, start_point, end_point, (0,0,255), 1)
      image = cv.rectangle(image,(start_point[0],start_point[1]+20),(end_point[0],start_point[1]+3),(0,0,255),-1)
      image = cv.putText(cv.flip(image,1),string, (maxX-end_point[0],start_point[1]+20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv.LINE_AA)
      return cv.flip(image,1)

   image=show_holy_rect(image,(x_min(hand_cordinate)-7,y_max(hand_cordinate)+7),(x_max(hand_cordinate)+7,y_min(hand_cordinate)-7),string)

   return image
