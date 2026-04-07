import torch

# --- Creating tensors ---

a = torch.tensor([1, 2, 3])         # 1D tensor
b = torch.tensor([[1, 2], [3, 4]])  # 2D tensor a matrix

print(a)
print(b.shape)                      # torch.size -> 2 rows , 2 columns

# --- Basic Operations ---

x = torch.tensor([10.0, 20.0, 30.0])
y = torch.tensor([1.0, 2.0, 3.0])

print(x + y)
print(x * y)
print(x.mean())                     # Avarege of numbers

# --- Tensors Creators ---

zeros = torch.zeros(3, 3)           # create matrix 3 x 3 all zeros
ones = torch.ones(2, 4)             # matrix 2 x 4 all ones
rand = torch.rand(2, 2)             # rondom values between o and 1

print(zeros)
print(ones)
print(rand)
print(rand.shape)                   # size torch.size([2, 2])