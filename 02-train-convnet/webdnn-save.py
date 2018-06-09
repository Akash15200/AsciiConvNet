import torch, torchvision
from learner import model

print(model)

from webdnn.frontend.
from webdnn.backend import generate_descriptor
import sys

sys.settrace(True)

dummy_input = torch.autograd.Variable(torch.randn(1, 3, 30, 30))
print(dummy_input)
graph = PyTorchConverter().convert(model, dummy_input)

# print(graph)
exec_info = generate_descriptor("fallback", graph)  # also "webgpu", "webassembly", "webgl", "fallback" are available.
exec_info.save("./output")
