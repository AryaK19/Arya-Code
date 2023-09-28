import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os


class Liner_QNet(nn.Module):
    def __init__(self,input_size,hidden_size,output_size):
        super().__init__()
        self.liner1 = nn.Linear(input_size,hidden_size)
        self.liner2 = nn.Linear(hidden_size,output_size)

    def  forward(self,x):
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x

    def save(self,  file_name="model.pth"):
        model_folder_path = "./model"
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)

        file_name = os.path.join(model_folder_path,file_name)
        torch.save(self.state_dict(),file_name)


class QTrainer:
    def __init__(self,model,lr,gamma):
        self.lr = lr
        self.gamma = gamma
        self.model = model
        self.model = model
        self.optimizer = optim.Adam(model.parameters,lr=float(self.lr))
        self.criterion = nn.MSELoss()

    def trian_step(self,state,action,reward,next_new,done):
        state = torch.tensor(state,dtype=torch.float)
        next_state = torch.tensor(next_state,dtype=torch.float)
        action = torch.tensor(action , dtype= torch.long)
        reward = torch.tensor(reward,dtype=torch.float)
        # (n,x)

        if len(state.shape) == 1:
            # (1,x)
            state = torch.unsqueeze(state,0)
            next_state = torch.tensor(next_state,dtype=torch.float)
            action = torch.tensor(action , dtype= torch.long)
            reward = torch.tensor(reward,dtype=torch.float)
            done = (done, )
            
            #1:predict the Q value with the current value
            pred = self.model(state)

            target = prd.clone()
            for idx in range(len(done)):
                Q_new = reward[idx]
                if not done[idx]:
                    Q_new = reward[idx] + self.gamma + torch.max(self.model(next_state[idx]))

                target[idx][torch.argmax(action).item()] = Q_new

            #2: Q_new = r + y * max(next perdicted Q value)
            # pred.clone()
            # preds[argmax(action)] = Q_new

            self.optimizer.zero_grad()
            loss = self.criterion(target,pred)
            loss.backward()

            self.optimizer.step()