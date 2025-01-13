#import matplotlib.pyplot as plt
#import numpy as np
import torch

tensor = torch.tensor([[1,2],
                       [4,5],
                       [6,7],
                       [8,9]])


vector = torch.tensor([1,
                       2,
                       3,
                       4])

print(tensor*vector)