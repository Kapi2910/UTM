from collections import deque

class Trigger:
    def __init__(self):
        self._attached = deque()
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Trigger, cls).__new__(cls)
        return cls._instance

    def attach(self, drones: deque):
        self._attached = drones

    def intersection(self):
        for a in self._attached:
            print(f"Drone {a.name} is at intersection? f{d.at_intersection}")