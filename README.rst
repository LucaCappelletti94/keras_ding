Keras Ding
=========================================================================================
|pip| |downloads|

Keras callback for playing a sound when training is complete. The callbacks additionally works also within jupyter notebook,
so that if you are working on a notebook on a remote machine it plays the audio within your browser and not in the server.

How do I install this package?
----------------------------------------------
You will need a couple packages that you might not already have installed:

.. code:: shell

    sudo apt install python3-dev
    sudo apt install libasound2-dev

Finally as usual, just download it using pip:

.. code:: shell

    pip install keras_ding


Usage examples
-----------------------------------------------
So suppose you have your Keras model `my_keras_model` and you want to hear a sound when it is done training.
Here you go:

.. code:: python

    from keras_ding import KerasDing

    my_keras_model.fit(
        x, y,
        callbacks=[
            KerasDing()
        ]
    )

What abount a custom sound? Just pass it as an argument.

.. code:: python

    from keras_ding import KerasDing

    my_keras_model.fit(
        x, y,
        callbacks=[
            KerasDing(path="my_custom_sound.mp3")
        ]
    )


.. |pip| image:: https://badge.fury.io/py/keras-ding.svg
    :target: https://badge.fury.io/py/keras-ding
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/keras-ding
    :target: https://pepy.tech/badge/keras-ding
    :alt: Pypi total project downloads 
