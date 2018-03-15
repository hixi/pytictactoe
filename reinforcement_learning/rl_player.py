import numpy as np

from pytictactoe.player.base_player import BasePlayer

from reinforcement_learning.input_handler import get_input_state, index_to_field


class RlPlayer(BasePlayer):
    def __init__(self, model):
        super().__init__()
        self.memories = []
        self.model = model
        self.gamma = 0.95  # discount rate
        self.epsilon = 1.0  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.current_state = None
        self.current_action = None
        self.loss = []

    def act(self, input_state):
        act_values = self.model.predict(np.expand_dims(input_state, axis=0))
        return np.argsort(act_values[0])[::-1]

    def remember(self, state, action, reward, next_state, done):
        self.memories.append((state, action, reward, next_state, done))

    def replay(self):
        for state, action, reward, next_state, done in self.memories:
            state = np.expand_dims(state, axis=0)
            next_state = np.expand_dims(next_state, axis=0)
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            history = self.model.fit(state, target_f, epochs=1, verbose=0)
            self.loss += history.history['loss']
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
        self.memories = []

    def choose_field(self, grid):
        allowed = False
        index = 0
        self.current_state = get_input_state(grid=grid)
        while not allowed:
            predictions = self.act(input_state=self.current_state)
            self.current_action = predictions[index]
            field = index_to_field(predictions[index])
            allowed = yield field
            if allowed:
                yield None
            else:
                index += 1

    def after_decision(self, grid, won):
        done = True if won is not None else False
        reward = calculate_reward(won)
        next_state = get_input_state(grid=grid)
        self.remember(state=self.current_state, action=self.current_action, reward=reward, next_state=next_state,
                      done=done)


def calculate_reward(won):
    if won:
        return 1
    if won is None:
        return 0.
    if not won:
        return -1.
