import os

from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential

from reinforcement_learning.input_handler import input_size, output_size


def build_model(model_path, learning_rate=0.001):
    model = Sequential()
    model.add(Dense(54, input_shape=(input_size,), activation='relu'))
    model.add(Dense(72, activation='relu'))
    model.add(Dense(35, activation='relu'))
    model.add(Dense(output_size, activation='linear'))
    model.compile(loss='mse', optimizer=Adam(lr=learning_rate))
    load_model(model, model_path)
    return model


def load_model(model, file_path='rl_model.h5'):
    if os.path.exists(file_path):
        model.load_weights(file_path)
