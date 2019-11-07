from keras_ding import Ding
from keras_ding.utils import InvisibleAudio


def test_invisible_audio():
    InvisibleAudio(Ding()._path).play()
