import torch
import numpy as np
from torchvision import transforms
from dataset import AsciiConvNetDataset
from learner import model

dataset = AsciiConvNetDataset('dataset/extract/', train=True, train_test_split_ratio=1,
    transforms=transforms.ToTensor())
loader = torch.utils.data.DataLoader(dataset=dataset, batch_size=1, shuffle=False)
model.load_state_dict(torch.load('models/model.ckpt'))

count = 0
total = 0
correct = 0
for images, labels in loader:
    predicted = torch.max(model.forward(images), 1)[1].item()
    actual = labels.item()

    # print(predicted, actual, predicted == actual)

    total += 1
    correct += int(predicted == actual)

    count += 1
    if count == 1:
        break

print('Accuracy: ', correct, total, correct / total * 100)

torch.onnx.export(model, torch.autograd.Variable(torch.randn(1,3,30,30)), 'models/model.proto', verbose=False)
print('saved onnx model')
