# What is Pytorch Really
- it's a python library used for building and running machine learning models
- It's tool working with numbers in bulk (tensors)
-> "Numpy + GPU + Deep learning support"

# Understanding Tensors
- Tensors = container of numbers

# Types of tensors
1. 1D (Vector)
    - x = torch.tensor([1, 2, 3])
2. 2D (matrix)
    - x = torch.tensor([[1, 2]
                        [3, 4]])
3. (like images)
    - x = torch.randn(3, 224, 224)

# CPU vs GPU
- pytorch can run on GPU (Faster)
device = "cuda" if torch.cuda.is_available() else "cpu"
x = x.to(device)
- “I can move tensors between CPU and GPU using .to(device) depending on availability.”










# Questions
- Differance between * and matmul?
- “I can move tensors between CPU and GPU using .to(device) depending on availability.”