#!/bin/python3

defstats = {
    "inp": 30.,
    "nip": .1,
    "dir": 0.
    }

class bot:
    def __init__(self, name, stats = None, affinities = None):
        self.name = name
        if stats is None: stats = dict(defstats)
        if affinites is None: affinities = dict()
