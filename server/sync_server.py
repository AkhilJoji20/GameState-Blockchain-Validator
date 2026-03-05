import json
from common.blockchain import Blockchain
from server.validator import validate_block

def sync():
    client_chain = Blockchain("data/client_chain.json")
    server_chain = Blockchain("data/server_chain.json")

    if len(server_chain.chain) == 0:
        with open("data/server_chain.json", "w") as f:
            json.dump([{
                "index": b.index,
                "timestamp": b.timestamp,
                "game_state": b.game_state,
                "previous_hash": b.previous_hash,
                "hash": b.hash
            } for b in client_chain.chain], f, indent=4)

        print("Server baseline established")
        return

    last_server_block = server_chain.chain[-1]

    for block in client_chain.chain:
        if block.index <= last_server_block.index:
            continue

        valid, msg = validate_block(
            last_server_block.game_state,
            block.game_state
        )

        if not valid:
            print("Tampering detected:", msg)
            print("Rolling back to last trusted state")

            with open("data/game_state.json", "w") as f:
                json.dump(last_server_block.game_state, f, indent=4)

            valid_blocks = [
                b for b in client_chain.chain
                if b.index <= last_server_block.index
            ]

            with open("data/client_chain.json", "w") as f:
                json.dump([{
                    "index": b.index,
                    "timestamp": b.timestamp,
                    "game_state": b.game_state,
                    "previous_hash": b.previous_hash,
                    "hash": b.hash
                } for b in valid_blocks], f, indent=4)

            print("Client blockchain rolled back")
            return
        server_chain.add_block(block.game_state)
        last_server_block = block

    print("Sync successful")

if __name__ == "__main__":
    sync()
