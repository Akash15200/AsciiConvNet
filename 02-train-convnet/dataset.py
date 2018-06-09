import torch
import numpy as np
from pathlib import Path
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


def load_csv(filename):
    with open(filename, 'r') as f:
        rows = []
        for line in f.readlines():
            rows.append(list(map(int, line.split(','))))
        return np.asarray(rows, dtype=np.float)


def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

class AsciiConvNetDataset(Dataset):
    def __init__(self, extract_dir, train=True, train_test_split_ratio=0.8, transforms=None):
        self.extract_dir = Path(extract_dir)
        assert self.extract_dir.exists()

        images = load_csv(self.extract_dir/'x.csv')
        labels = load_csv(self.extract_dir/'y.csv')

        images, labels = unison_shuffled_copies(images, labels)
        split_index = int(train_test_split_ratio * len(images))

        if train:
            images, labels = images[:split_index,:], labels[:split_index,:]
        else:
            images, labels = images[split_index:,:], labels[split_index:,:]

        self.images = images
        self.labels = labels
        self.transforms = transforms

    def __len__(self):
        return self.images.shape[0]

    def __getitem__(self, idx):
        """ Return (image, label) pair for a given index."""
        image, label = self.images[idx, :].reshape(30, 30).T, self.labels[idx, 0]
        image = np.asarray([image, image, image]).reshape(30, 30, 3)
        label = torch.tensor(label - 1)

        if self.transforms:
            image = self.transforms(image)
        return image.float(), label.long()

if __name__ == '__main__':
    dataset = AsciiConvNetDataset('dataset/extract/', train=True, transforms=transforms.ToTensor())
    loader = DataLoader(dataset=dataset, batch_size=10, shuffle=True)

    for images, labels in loader:
        print(images.size(), labels.size())

    print(len(dataset))
