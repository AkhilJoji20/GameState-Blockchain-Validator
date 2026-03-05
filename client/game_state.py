import json

FILE = "data/game_state.json"

def load_state():
    with open(FILE, "r") as f:
        return json.load(f)

def save_state(state):
    with open(FILE, "w") as f:
        json.dump(state, f, indent=4)

def play_session():
    state = load_state()
    state["level"] += 1
    state["money"] += 1000
    save_state(state)
    return state        
