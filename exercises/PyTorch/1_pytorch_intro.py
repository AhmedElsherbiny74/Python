import torch
import torch.nn as nn

###
# This mean:
#   - Input: 3 numbers
#   - Output: 1 number 
model = nn.Linear(3, 1)

input_tensor = torch.tensor([[1.0, 2.0, 3.0]])
output = model(input_tensor)

print(output)
