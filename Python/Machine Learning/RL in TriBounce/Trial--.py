from GameForML import Tribounce
import random as rn
import numpy as np


game = Tribounce(render=True)

done = False
while  not done:
    action = 1
    state,reward,done,info = game.run(action)


game.close()



print(state)

