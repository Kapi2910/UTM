# Create a message object that holds information about the current cell number and drone's id

class Message:
    def __init__(self, drone_id, curr_pos):
        self.id = drone_id
        self.cell_num = curr_pos