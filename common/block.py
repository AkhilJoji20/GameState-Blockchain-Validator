import hashlib
import time
import json

class Block:
    def __init__(self, index, game_state, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.game_state = game_state
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = json.dumps(self.game_state, sort_keys=True)
        content = f"{self.index}{self.timestamp}{data}{self.previous_hash}"
        return hashlib.sha256(content.encode()).hexdigest()
