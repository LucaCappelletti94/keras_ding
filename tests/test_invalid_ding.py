from keras_ding import Ding
import pytest

def test_ding():
    d = Ding()
    with pytest.raises(ValueError):
        Ding("kebab")
    with pytest.raises(ValueError):
        Ding("tests/test_invalid_ding.py")
    Ding(d._path)