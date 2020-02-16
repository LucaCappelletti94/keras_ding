from keras_ding import Ding
import pytest

def test_ding():
    d = Ding()
    with pytest.raises(ValueError):
        Ding(sample="kebab")
    with pytest.raises(ValueError):
        Ding(path="kebab")
    with pytest.raises(ValueError):
        Ding(path="tests/test_invalid_ding.py")
    Ding(path=d._path)