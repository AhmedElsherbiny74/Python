import torch
import torchvision.models as models
import numpy as np
import onnxruntime as ort

# ─────────────────────────────────────────
# PART 1: PYTORCH — Load and run the model
# ─────────────────────────────────────────

# Load a trained model
model = models.resnet18(pretrained = True)
model.eval()    # switch to inferance mode

#prepare input as a pytorch tensor
# shape: [1 image, 3 color channels, 224x224 pixels]
input_tensor = torch.rand(1, 3, 244, 244)

with torch.no_grad():
    pytorch_output = model(input_tensor)

print("PyTorch output shape:", pytorch_output.shape)  # [1, 1000]
print("PyTorch predicted class:", pytorch_output.argmax().item())


# ─────────────────────────────────────────
# PART 2: Export Pytorch model -> ONNX
# ─────────────────────────────────────────

torch.onnx.export(
    model,                      # model to export
    input_tensor,               # example input
    "resnet18.onnx",            # output file name  
    input_names = ["input"],    # name the input
    output_names = ["output"],  # name the output
    opset_version = 11          # ONNX version 
)   

print("✅ Model exported to resnet18.onnx")

# ─────────────────────────────────────────
# PART 3: ONNX RUNTIME — Load and run
# ─────────────────────────────────────────

# Load the ONNX model
session = ort.InferenceSession("resnet18.onnx")

# 6. Convert input to NumPy
input_numpy = input_tensor.numpy()

# 7. Run ONNX inferance
# Compare:
#   - PyTorch:
#     - output = model(input_tensor)
#   - ONNX:
#     - outputs = session.run(None, {"input": input_numpy})
# Same idea with different syntax
onnx_output = session.run(None, {"input": input_numpy})