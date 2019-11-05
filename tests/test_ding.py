from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from keras_ding import Ding
import silence_tensorflow
import numpy as np

def test_ding():
    x, y = np.random.randint(0, 2, size=(2, 100, 1))
    model = Sequential([
        Dense(units=1, activation="relu")
    ])
    model.compile(loss="MSE", optimizer="nadam")
    model.fit(
        x=x,
        y=y,
        verbose=0,
        callbacks=[Ding()]
    )
