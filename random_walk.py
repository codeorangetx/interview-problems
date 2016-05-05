"""
This question was asked by OpenDoor. 

Using the Markov chain below, write a function to simulate a variable length random walk.

Example: 'a' -> 'a' -> 'a' -> 'b' -> 'b' -> 'b'
"""


# Markov Chain

trans_probs = [
('a','a',0.9),
('a','b',0.075),
('a','c',0.025),
('b','a',0.15),
('b','b',0.8),
('b','c',0.05),
('c','a',0.25),
('c','b',0.25),
('c','c',0.5)
]


from random import random

def random_walk (steps) :

    prob_dict = {}
    for trans in trans_probs :
        current, next_state, prob = trans
        if current not in prob_dict :
            prob_dict[current] = {next_state: (0, prob)}
        else :
            c = max(v[1] for v in prob_dict[current].values())
            prob_dict[current][next_state] =  (c, c + prob)

    current_state = steps[0][0]
    steps_taken = []

    for step in xrange(steps):
        r = random()

        for next_state in prob_dict[current_state] :
            next_prob = prob_dict[current_state][next_state]
            if next_prob[0] < r < next_prob[1] :
                steps_taken += [next_state]
                current_state = next_state

    return steps_taken


print random_walk(10)


