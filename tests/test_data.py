# tests/test_data.py
import torch
import pytest
from src.dtu_cnn_classifier.data import corrupt_mnist

def test_data():
    train, test = corrupt_mnist()

    assert len(train) == 30000
    assert len(test) == 5000
    
    for dataset in [train, test]:
        images, labels = dataset.tensors
        assert images.shape[1:] == (1, 28, 28)
        assert labels.min() >= 0 and labels.max() <= 9
        
    train_labels = train.tensors[1] 
    test_labels = test.tensors[1]
    assert torch.all(torch.unique(train_labels) == torch.arange(10))
    assert torch.all(torch.unique(test_labels) == torch.arange(10))