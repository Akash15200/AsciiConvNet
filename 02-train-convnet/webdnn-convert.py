from webdnn.frontend.onnx import ONNXConverter
import onnx
from webdnn.backend import generate_descriptor


graph = onnx.load('models/model.proto')
print(graph)
print('=' * 80)
graph = ONNXConverter().convert(graph)
print(graph)

exec_info = generate_descriptor("webassembly", graph)  # also "webgpu", "webassembly", "webgl", "fallback" are available.
exec_info.save("./output")
