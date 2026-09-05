#started 14 june 2026 15:53 SUN

import torch
import torch.nn as nn
import random

class MinimalNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(2,1)  #builds network, A=in B=out
    
    def forward(self,x):
        return self.layer(x)    #runs network
    
model=MinimalNet()
optimizer = torch.optim.SGD(model.parameters(), lr=0.002)


weights=0
def find_state():
    global weights
    
    weights_new = model.layer.weight.flatten().tolist()
    
    weight_dif=[]
    for i in range(len(weights_new)):
        if weights!=0: weight_dif.append(weights_new[i] - weights[i])
    
    weights = weights_new
    bias = model.layer.bias.item()
    
    return {"weights":weights,"bias":bias,"weight_dif":weight_dif}
    
    
pred_old=0
def main_loop(num1,num2):
    global pred_old
    
    input_data = torch.tensor([[num1, num2]], dtype=torch.float32)  #converts to format
    pred = model(input_data)                                        # calls class to run network
    
    correct=num1+num2
    loss=torch.abs((pred - correct)) ** 2                      #Does the reward based on difference 
    print(loss,torch.abs((pred - correct)) ** 2  )
    optimizer.zero_grad()                                           
    loss.backward()                                               # Step 1: Calculate the back blame for improve
    optimizer.step()                                                 # Step 2: Turn the dials (weights)
    
    
    return {"pred":pred.item(),"correct":correct}      
    
for i in range(100):
    num1 = float(random.randint(1,2000))
    num2 = float(random.randint(1,2000))
    main_loop(num1,num2)


out = main_loop(3,8)
print(out)
print(find_state())














