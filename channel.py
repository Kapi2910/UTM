from collections import deque

# Create a class called channel that has a queue of all the message objects
# Class object will be a queue of message objects

class Channel:
    def __init__(self):
        self.queue = deque()
        