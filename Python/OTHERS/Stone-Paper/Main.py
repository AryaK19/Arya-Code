from Voice import *

import time
import random
#_______________________________________________wining____________________________________________
def Check_Who_Win(person,computer):
   result=""
   if person=="STONE" and computer=="STONE":
      result="Tie"
   elif person=="STONE" and computer=="PAPER":
      result="I win"
   elif person=="STONE" and computer=="SCISSORS":
      result="You win"
   elif person=="PAPER" and computer=="STONE":
      result="You win"
   elif person=="PAPER" and computer=="PAPER":
      result="Tie"
   elif person=="PAPER" and computer=="SCISSORS":
      result="I win"
   elif person=="SCISSORS" and computer=="STONE":
      result="I win"
   elif person=="SCISSORS" and computer=="PAPER":
      result="You win"
   elif person=="SCISSORS" and computer=="SCISSORS":
      result="Tie"
   return result

values=['STONE','PAPER','SCISSORS']
while True:
   com_val=random.choice(values)
   per_val=input('STONE PAPER SCISSORS \n')
   if not per_val:
      continue
   print(com_val)
   speak(com_val)
   
   time.sleep(1)
   speak(Check_Who_Win(per_val,com_val))
   
   time.sleep(1)
