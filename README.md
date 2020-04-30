[![Build Status](https://travis-ci.org/Murthy10/pytictactoe.svg?branch=master)](https://travis-ci.org/Murthy10/pytictactoe)
<a href="url"><img src="/docs/images/jasskarten.gif" align="right" width="300" ></a>
# pytictactoe
Pytictactoe is an implementation of the well known Tic-Tac-Toe game.

As OpenAI Gym provides APIs for several popular games to learn your algorithms master these games.
Pytictactoe aims to offer an API in the same manner.



## Usage
To install pytictactoe, simply:
```bash
git clone https://github.com/Murthy10/pytictactoe.git
cd pytictactoe
pip install -r requirements.txt
python setup.py install
```
pytictactoe officially supports Python 3.4, 3.5, 3.6, 3.7, 3.5-dev, 3.6-dev, 3.7-dev, nightly and PyPy3.

### CLI :computer:
Beside of the API, pytictactoe provides a CLI client to play game.
Currently your opponent will be a bot choosing a random position.

After the pip installation you could run the ```pytictactoe``` command on the console to play a game:
```bash
$ pytictactoe

    0   1   2
  -------------
0 | X | O |   |
  -------------
1 | O |   |   |
  -------------
2 |   |   | X |
  -------------

Please chose x-coordinate from 0 to 2: 
1
Please chose y-coordinate from 0 to 2: 
1

Round 1 is over.
Points: Player 1: 1 , Player 2: 0, Remis: 0. 
```

## API :clipboard:
The idea of pytictactoe is to extend the game with your own implemented player.

## Build your own Player :runner:

Basically the Player has to provide the method choose_field(grid).
I recommend to inherit from the BasePlayer class.

To get more familiar with this concept let's have a look at the already mentioned Random Player.
```python
import random

from pytictactoe.field import Field
from pytictactoe.player.base_player import BasePlayer


class RandomPlayer(BasePlayer):
    def choose_field(self, grid):
        allowed = False
        while not allowed:
            field = Field(x=random.randint(0, 2), y=random.randint(0, 2))
            allowed = yield field
            if allowed:
                yield None
```
What's going on here?

The Random Player is pretty naive and he simply chooses randomly a position, if the turn is not allowed he randomly chooses a new one until the rules of Tic-Tac-Toe are satisfied.

Now you should be ready to get your hands dirty to implement your own player and beat the random player! :trophy: