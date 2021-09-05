from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import History

def add_layer(model, layer_type, dropout=None, neurons=None, activation=None):
  if layer_type == 0:
    layer = Dropout(dropout)
  elif layer_type == 1:
    layer = Dense(neurons, activation=activation)
  return model.add(layer)

def compile_model(model, loss, activation):
  return model.compile(loss=loss, metrics=["accuracy"])

def train_model(model, X, y, batch_size, epochs, callbacks=None, validation_data=None):
  return model.fit(X, y, batch_size=batch_size, callbacks=callbacks, validation_data=validation_data)
