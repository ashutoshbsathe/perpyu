import torchvision.datasets as datasets 
import torchvision.transforms as transforms 
from torch.utils.data.sampler import SubsetRandomSampler as SRS 
import torch.utils.data as data_utils 
import numpy as np 
import sys 

MNIST_DATA_ROOT = './mnist_data/'
CIFAR10_DATA_ROOT = './cifar10_data/'
FMNIST_DATA_ROOT = './fmnist_data/'

SEED = 161803398874929 # Golden Ratio

def get_cifar10_data_loaders(batch_size=64, n_train=40000, \
    n_val=10000, n_test=10000, train_transform=None, \
    val_transform=None, test_transform=None):

    assert n_train + n_val == 50000
    if train_transform is None:
        train_transform = transforms.Compose([
            transforms.RandomCrop(size=32, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize((0.,0.,0.), (1.,1.,1.))
        ])
    if val_transform is None:
        val_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.,0.,0.), (1.,1.,1.))
        ])
    if test_transform is None:
        test_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.,0.,0.), (1.,1.,1.))
        ])
    
    train_set = datasets.CIFAR10(root=CIFAR10_DATA_ROOT, download=True, \
        train=True, transform=train_transform)
    val_set = datasets.CIFAR10(root=CIFAR10_DATA_ROOT, download=True, \
        train=True, transform=val_transform)
    test_set = datasets.CIFAR10(root=CIFAR10_DATA_ROOT, download=True, \
        train=False, transform=test_transform)

    indices = np.arange(0, 50000)
    np.random.seed(SEED)
    np.random.shuffle(indices)

    train_sampler = SRS(indices[:n_train])
    val_sampler = SRS(indices[n_train:])
    test_sampler = SRS(np.arange(0, 10000))

    train_loader = data_utils.DataLoader(train_set, batch_size=batch_size, \
        sampler=train_sampler)
    val_loader = data_utils.DataLoader(val_set, batch_size=batch_size, \
        sampler=val_sampler)
    test_loader = data_utils.DataLoader(test_set, batch_size=batch_size, \
        sampler=test_sampler)
    
    return train_loader, val_loader, test_loader 