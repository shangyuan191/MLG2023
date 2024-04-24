import torch

if torch.cuda.is_available():
    print("CUDA is available.")
else:
    print("CUDA is not available.")

if torch.cuda.is_available():
    print("CUDA is available. CUDA version:", torch.version.cuda)
else:
    print("CUDA is not available.")