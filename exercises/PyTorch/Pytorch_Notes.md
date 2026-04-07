# What is Pytorch Really
- it's a python library used for building and running machine learning models
- It's tool working with numbers in bulk (tensors)
-> "Numpy + GPU + Deep learning support"

# Understanding Tensors
- Tensors = container of numbers
- Temsor is array but smarter and faster and used for AI

# Types of tensors
- A single number → 0D tensor (called a scalar): 7
- A list of numbers → 1D tensor: [1, 2, 3]
- A table of numbers → 2D tensor: [[1,2],[3,4]]
- A cube of numbers → 3D tensor: (think of a color image — width × height × 3 colors)

# CPU vs GPU
- pytorch can run on GPU (Faster)
device = "cuda" if torch.cuda.is_available() else "cpu"
x = x.to(device)
- “I can move tensors between CPU and GPU using .to(device) depending on availability.”





Got it — that’s fair, and thanks for saying it directly. Let’s reset and do this **the right way from zero**, no assumptions, no jumping.

I’ll teach you like you’ve **never touched this before**, and we’ll build understanding step by step.

---

# 🧠 STEP 0: What are we even trying to do?

In machine learning:

👉 We don’t deal with single numbers
👉 We deal with **a lot of numbers at once**

Example:

* Image = thousands of numbers
* Sound = thousands of numbers
* Data = tables of numbers

So we need:

> A way to store and manipulate MANY numbers easily

---

# STEP 1: Simple Python First (NO PyTorch yet)

### Normal variables:

```python
a = 5
b = 10
print(a + b)
```

👉 Easy, right?

---

### Now multiple numbers:

```python
numbers = [1, 2, 3, 4]
```

👉 This is a **list**

---

### Problem with lists ❌

Lists are:

* Slow for math
* Not designed for heavy calculations

---

# ⚡ STEP 2: Better way → Arrays

We use something like:

👉 **NumPy arrays** (foundation of everything)

Example:

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
```

👉 Output:

```
[5 7 9]
```

---

## 🔥 Key Idea

Instead of looping:

```python
for i in range(3):
    print(a[i] + b[i])
```

👉 We do it in ONE line:

```python
a + b
```

---

# 🧠 NOW YOU ARE READY FOR PYTORCH

---

# 🔥 STEP 3: What is PyTorch?

PyTorch is:

👉 “NumPy… but smarter and faster, and used for AI”

---

## 🧩 The ONLY new word: TENSOR

👉 Tensor = array (same idea as NumPy)

---

## 🟢 Example (same as before)

```python
import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print(a + b)
```

👉 SAME result:

```
tensor([5, 7, 9])
```

---

## 🎯 Important:

Don’t overthink “tensor”

👉 Just remember:

> Tensor = list of numbers (but powerful)

---

# Key Properties Every Tensor Has
1. .shape: Dimensions of tensor size
2. .dtype: Type of numbers stored on tensor 
3. .device: where it lives CPU or GPU -> Cpu or Cude

# 🧱 1: Shapes (VERY IMPORTANT)

---
## For get the size of tensor 
## torch.size([2, 2]) means 2 rows , 2 columns 

## Example:

```python
t = torch.rand(3, 4)
print(t.shape)   # torch.Size([3, 4])
print(t.dtype)   # torch.float32
print(t.device)  # cpu
```

👉 This looks like:

```
1 2
3 4
```

---

## Shape:

```python
x.shape
```

👉 Output:

```
(2, 2)
```

---

## 🧠 Meaning:

* 2 rows
* 2 columns

---

# 🧪 STEP 5: Operations (Now it will make sense)

---

## ➕ Add:

```python
a + b
```

---

## ✖️ Multiply (element by element):

```python
a * b
```

---

## 🔥 Matrix multiplication:

```python
torch.matmul(a, b)
```

---

## ⚠️ Difference (IMPORTANT)

### Element-wise:

```
[1,2,3]
*
[4,5,6]
=
[4,10,18]
```

---

### Matrix multiply:

Different rule (used in AI models)

---

# 🧠 STEP 6: WHY ARE WE DOING THIS?

Because:

👉 Machine learning model = just math on tensors

---

# 🧱 STEP 7: Simplest Model Idea EVER

A model is just:

```
input → math → output
```

---

## Example:

```python
import torch.nn as nn

model = nn.Linear(2, 1)
```

👉 Meaning:

* Input = 2 numbers
* Output = 1 number

---

## Try it:

```python
x = torch.tensor([[1.0, 2.0]])
y = model(x)

print(y)
```

---

# 🔥 STEP 8: Inference (VERY IMPORTANT)

🧠 Big Picture First
What is a Model?
A machine learning model is a program that was trained on data to make predictions. For example:

- Input: a photo → Output: "this is a cat"
- Input: a sentence → Output: "this is positive sentiment"

👉 Inference = “use model to get answer”

## What is Inference?
- Inference means using a already-trained model to make predictions. You're NOT training it — someone else already did that hard work. You just load it and run it.
---

## 🔑 The 4 Steps of Model Inference in PyTorch
1. Load the model
2. Set it to evaluation mode
3. Prepare your input as a tensor
4. Run it and get output

- HINT: Show example 2_model_inferance.py
----

## Correct way:

```python
model.eval()

with torch.no_grad():
    output = model(x)
```

---

## 🧠 Why?

* `eval()` → stop training mode
* `no_grad()` → faster, no memory waste

---

# 🎯 REAL UNDERSTANDING CHECK

Tell me honestly:

Can you now answer:

1. What is a tensor?
2. Why not just use Python lists?
3. What does this mean:
4. What is inference?

---




# Questions
- Differance between * and matmul?
- “I can move tensors between CPU and GPU using .to(device) depending on availability.”
- what happen if we don'y use eval?
- Differance between tensor and array , list