# 🔢 The Core Problem
Computers can't store every possible number perfectly. They have limited memory per number. So they have to make a choice:

"How do I store 3.14159265358979... in just 32 bits?"

---

# 🧠 BIG IDEA FIRST

So far you did:

```id="flowA"
input → model → output (numbers)
```

👉 These “numbers” are stored in the computer

Now the question is:

❓ **How does the computer store these numbers?**

---

# 🔢 1. FLOATING-POINT (what you already used)

This is the **default in PyTorch and ONNX**

🧠 What is it?
Floating-point means the decimal point can float — it moves around to represent very large or very small numbers.
---

## 🧠 Simple idea:

👉 Numbers with decimals

Examples:

```id="floatEx"
3.14
0.001
-2.75
```

---

## 🟢 In your code:

```python id="f1k2j9"
input_tensor = torch.rand(1, 3, 224, 224)
```

👉 These are **floating-point numbers**

---

## ❓ Why we use it

* Very accurate
* Good for training models

---

# 🔢 2. FIXED-POINT (simplified idea)

👉 Store numbers as **integers (no decimals)**

---

## 🧠 Trick:

Instead of:

```id="float2"
3.14
```

We store:

```id="fixed2"
314   (and remember scale = 100)
```

---

## 🟡 Meaning:

```id="fixedMeaning"
314 → 3.14
```

---

## ❓ Why use this?

* Faster
* Uses less memory
* Works better on small devices (mobile, embedded)

---

# ⚖️ 3. MAIN DIFFERENCE (VERY IMPORTANT)

| Feature  | Floating | Fixed  |
| -------- | -------- | ------ |
| Accuracy | High     | Lower  |
| Speed    | Slower   | Faster |
| Memory   | More     | Less   |

---

- Floating-point:  can represent  0.0000001  or  9999999.5
- Fixed-point: can only represent  -128, -127, ... 0, 1, 2 ... 127
---

# 🔥 CONNECT THIS TO YOUR WORK (IMPORTANT)

You did:

👉 PyTorch → ONNX → inference

Now imagine:

👉 We want to run model on:

* mobile phone
* small chip

---

## Problem:

Floating-point is:
❌ heavy
❌ slow

---

## Solution:

👉 Convert model to **fixed-point (or lower precision)**

This is called:

👉 **Quantization**
- This process of converting from float32 → INT8 is called Quantization — a word you'll definitely hear in the interview.
---

# 🧪 4. WHAT PROBLEM HAPPENS?

When we change numbers:

```id="prob"
3.141592 → 3.14
```

👉 we lose precision

---

## Result:

👉 Output may change a little

---

# 🔍 5. NUMERICAL ACCURACY (VERY IMPORTANT)

This means:

👉 “How close is the result to the original?”

---

## Example:

```id="acc1"
PyTorch output = 0.923456
ONNX output   = 0.923450
```

👉 Very close ✅

---

## But:

```id="acc2"
0.92 vs 0.80
```

👉 Problem ❌

---

# 🧪 HOW WE CHECK

You already saw:

```python id="check1"
np.allclose(a, b, atol=1e-5)
```

---

## 🧠 Meaning:

👉 “Are numbers almost equal?”

---

# 🔥 CONNECT EVERYTHING TOGETHER

---

## Full real-world pipeline:

```id="fullReal"
PyTorch (float)
   ↓
ONNX (float)
   ↓
Quantized model (fixed / int)
   ↓
Run on device
```

---

## And we must:

👉 ALWAYS check accuracy after each step

---

# 🎯 WHAT INTERVIEWER WANTS

You don’t need deep math — just this understanding:

---

## 💬 Perfect answer:

“I understand that models typically use floating-point numbers for accuracy, but for deployment we may convert to lower precision like fixed-point to improve performance. I also understand the importance of validating numerical accuracy after conversion.”

---

# 🧪 Questions

Answer in simple words:

1. What is floating-point?
2. What is fixed-point?
3. Why do we use fixed-point sometimes?
4. What is numerical accuracy?
5. Why do we compare outputs (PyTorch vs ONNX)?

