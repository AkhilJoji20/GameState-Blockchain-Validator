from common.blockchain import Blockchain
from client.game_state import play_session, load_state

def normal_play():
    state = play_session()
    chain = Blockchain("data/client_chain.json")
    chain.add_block(state)
    print("Offline progress recorded:", state)

def create_block_from_current_state():
    state = load_state()
    chain = Blockchain("data/client_chain.json")
    chain.add_block(state)
    print("Block created from CURRENT state:", state)

if __name__ == "__main__":
    print("1 = Normal Play")
    print("2 = Create Block From Current State (Tamper Test)")
    choice = input("Select: ")

    if choice == "1":
        normal_play()
    else:
        create_block_from_current_state()
