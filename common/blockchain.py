import json
import os
from common.block import Block

class Blockchain:
    def __init__(self, path):
        self.path = path
        self.chain = []
        self.load_chain()

    def create_genesis(self):
        genesis = Block(0, {"level": 1, "money": 0}, "0")
        self.chain = [genesis]
        self.save_chain()

    def load_chain(self):
        if not os.path.exists(self.path):
            self.chain = []
            return

        with open(self.path, "r") as f:
            try:
                data = json.load(f)
            except:
                self.chain = []
                return

        if not data:
            self.chain = []
            return

        self.chain = []
        for b in data:
            block = Block(b["index"], b["game_state"], b["previous_hash"])
            block.timestamp = b["timestamp"]
            block.hash = b["hash"]
            self.chain.append(block)

        with open(self.path, "r") as f:
            data = json.load(f)
            if not data:
                self.chain = []
                return
            self.chain = []
            for b in data:
                block = Block(b["index"], b["game_state"], b["previous_hash"])
                block.timestamp = b["timestamp"]
                block.hash = b["hash"]
                self.chain.append(block)

    def add_block(self, game_state):

        # If chain is empty → create genesis block first
        if len(self.chain) == 0:
            genesis = Block(0, game_state, "0")
            self.chain.append(genesis)
            self.save_chain()
            return

        last = self.chain[-1]
        new_block = Block(len(self.chain), game_state, last.hash)
        self.chain.append(new_block)
        self.save_chain()

    def save_chain(self):
        with open(self.path, "w") as f:
            json.dump([{
                "index": b.index,
                "timestamp": b.timestamp,
                "game_state": b.game_state,
                "previous_hash": b.previous_hash,
                "hash": b.hash
            } for b in self.chain], f, indent=4)