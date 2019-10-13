from keras.models import Sequential
from keras.layers import Dense
from keras_ding import Ding
import silence_tensorflow
import numpy as np

def test_ding():
    x, y = np.random.randint(0, 2, size=(2, 100, 1))
    model = Sequential([Dense(units=1)])
    model.compile(loss="MSE", optimizer="nadam")
    model.fit(
        x=x,
        y=y,
        epochs=10,
        callbacks=[Ding()]
    )
