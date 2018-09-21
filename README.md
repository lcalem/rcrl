
---

## Cube representation

The representation we use here is a (1, 54) vector, each value representing the color of a sticker.\
The 6 are listed in this order: Front Top Back Bottom Right Left\
Each face contains 9 values (6 * 9 = 54)\
Each value is an integer between 0 and 5 representing the color of the sticker:\
COLORS = {\
    0: 'Green',\
    1: 'White',\
    2: 'Blue',\
    3: 'Yellow',\
    4: 'Red',\
    5: 'Orange'\
}\
\
The 'standard' position of the solved cube will be represented with the white face on top\

---

## Cube actions

Actions are represented with (54, 54) permutation matrices.\
state * action -> new_state\
(1, 54) * (54, 54) -> (1, 54)\

The permutation matrices for all actions are obtained from the 3 basic permutation matrices representing the actions [r], [u], and R.\
[Notation of actions](https://ruwix.com/the-rubiks-cube/notation/advanced/)


---

## Useful links

[online solver](https://ruwix.com/online-rubiks-cube-solver-program/)\
[original subject](http://www.lifl.fr/~lepallec/StagesM2/afficherSujet.php?sujet=1516195925)

---

## Credits

[WydD](https://github.com/WydD) for his Cube knowledge\
[dennybritz](https://github.com/dennybritz) for examples that helped me build my [estimators](https://github.com/dennybritz/reinforcement-learning/blob/dfef331a54b54885d0b4b8600055ea5aedd346d4/DQN/Deep%20Q%20Learning.ipynb)