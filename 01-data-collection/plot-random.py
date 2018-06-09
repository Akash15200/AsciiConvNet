import numpy as np
import matplotlib.pyplot as plt
import random

def load_csv(filename):
    with open(filename, 'r') as f:
        rows = []
        for line in f.readlines():
            row = line.split(',')
            row = list(map(int, row))
            rows.append(row)
        return np.asarray(rows, dtype=np.float)


x = load_csv('dataset/extract/x.csv')
y = load_csv('dataset/extract/y.csv')

print(x, y)
rand = random.randint(0, x.shape[0])
plt.imshow(x[rand,:].reshape(30, 30).T, cmap='gray')
plt.show()
