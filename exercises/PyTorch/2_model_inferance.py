import torch
import torchvision.models as models

# --- Step 1 — Load the Model ---

# option A : Load a full saved model
#model_1 = torch.load('model.pth')

# option B : load from torchvision 
# we are using model called Resnet18 this is already trained on 1000 categories (cats, dogs, cars, etc.)
#       - models.resnet18() → call function to create model
#       - pretrained=True → load trained weights
#       - model = ... → store it in variable
model_2 = models.resnet18(pretrained= True) 


# --- Step 2 — Set to Evaluation Mode ---
# it mean -> “Switch model to inference mode”
# why use it ? 
#   Because during training:
#        -model behaves differently (dropout, batchnorm)
# During inference:
#        -we want stable, fixed behavior
model_2.eval()


# --- Step 3 — Prepare Your Input ---
# Creating a fake image data
# Simulating an input one image: 1 image, 3 color channels, 224x224 pixels
# The "1" means we're sending 1 image at a time (batch size = 1)
input_tensor = torch.rand(1, 3, 224, 224)  # shape: [batch, channels, height, width]

# --- Step 4 — Run Inference ---
# Run the model without tracking gradients”
# torch.no_grad()     -> turn OFF training calculations
# model(input_tensor) -> give input → get output
# Why? Because: We are NOT training,We want faster execution and Save memory
with torch.no_grad():
        output = model_2(input_tensor)

print(output.shape)

# Get the predicted class (highest score)
# It mean Get the index of highest value
# Get the index of highest value
# dim=1 = search across columns
# Why? Because: model gives scores and we want the best class
predicted_class = output.argmax(dim=1)
print(predicted_class)  # e.g. tensor([422])