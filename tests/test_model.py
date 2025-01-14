import torch
from src.dtu_cnn_classifier.model import MyAwesomeModel
import pytest

def test_basic_model():
    model = MyAwesomeModel()
    x = torch.randn(1, 1, 28, 28)
    y = model(x)
    assert y.shape == (1, 10)

def test_error_on_wrong_shape():
    model = MyAwesomeModel()
    with pytest.raises(ValueError, match='Expected input to a 4D tensor'):
        model(torch.randn(1,2,3))
    with pytest.raises(ValueError, match='Expected each sample to have shape \\[1, 28, 28\\]'):
        model(torch.randn(1,1,28,29))

@pytest.mark.parametrize("batch_size", [32, 64])
def test_batch_sizes(batch_size: int) -> None:
    model = MyAwesomeModel()
    x = torch.randn(batch_size, 1, 28, 28)
    y = model(x)
    assert y.shape == (batch_size, 10)