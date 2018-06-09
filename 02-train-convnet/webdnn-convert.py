from webdnn.frontend.onnx import ONNXConverter
import onnx

graph = onnx.load('models/model.proto')
print(graph)
print('=' * 80)
graph = ONNXConverter().convert(graph)
print(graph)
