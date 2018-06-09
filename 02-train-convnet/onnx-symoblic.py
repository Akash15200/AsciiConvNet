

def reshape(g, self, shape):
    if not _is_value(shape):
        if self.isTensor():
            self_sizes = self.type().sizes()
            if self_sizes and len(size) == 2 and self_sizes[0] == size[0]:
                return g.op("Flatten", self, axis_i=1)
        shape = g.op("Constant", value_t=torch.LongTensor(size))
    return g.op("Reshape", self, shape)


def reshape(g, self, shape):
    size = shape
    self_sizes = self.type().sizes()
    if self_sizes and len(size) == 2 and self_sizes[0] == size[0]:
        return g.op("Flatten", self, axis_i=1)
    shape = g.op("Constant", value_t=torch.LongTensor(size))
    return g.op("Reshape", self, shape)
