import tkinter as tk
import subprocess
import threading
import json

DATA_FILE = "data/game_state.json"

def run_command_async(command):
    def task():
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, result.stdout if result.stdout else result.stderr)

    threading.Thread(target=task).start()

def start_session():
    run_command_async("python -m server.sync_server")

def normal_play():
    run_command_async("python -c \"from client.offline_play import normal_play; normal_play()\"")

def create_block_from_current():
    run_command_async("python -c \"from client.offline_play import create_block_from_current_state; create_block_from_current_state()\"")

def tamper_state():
    tampered = {
        "level": 100,
        "money": 999999,
        "items": ["rare_car"]
    }
    with open(DATA_FILE, "w") as f:
        json.dump(tampered, f, indent=4)

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Game state tampered.\n")

def view_game_state():
    with open(DATA_FILE, "r") as f:
        state = json.load(f)

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, json.dumps(state, indent=4))

def view_blockchain_visual():
    try:
        with open("data/client_chain.json", "r") as f:
            chain = json.load(f)
    except:
        return

    window = tk.Toplevel()
    window.title("Client Blockchain View")
    window.geometry("600x600")

    canvas = tk.Canvas(window)
    scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for block in chain:
        frame = tk.Frame(scrollable_frame, bd=2, relief="solid", padx=10, pady=10)
        frame.pack(pady=10, padx=20, fill="x")

        tk.Label(frame, text=f"Block {block['index']}", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(frame, text=f"Level: {block['game_state']['level']}").pack(anchor="w")
        tk.Label(frame, text=f"Money: {block['game_state']['money']}").pack(anchor="w")
        tk.Label(frame, text=f"Previous Hash: {block['previous_hash'][:20]}...").pack(anchor="w")
        tk.Label(frame, text=f"Hash: {block['hash'][:20]}...").pack(anchor="w")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

root = tk.Tk()
root.title("Blockchain Game Integrity Dashboard")
root.geometry("600x600")

tk.Label(root, text="Blockchain Rollback & Recovery Demo", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(root, text="Start Session (Sync)", width=30, command=start_session).pack(pady=5)
tk.Button(root, text="Normal Offline Play", width=30, command=normal_play).pack(pady=5)
tk.Button(root, text="Tamper Game State", width=30, command=tamper_state).pack(pady=5)
tk.Button(root, text="Create Block from Current State", width=30, command=create_block_from_current).pack(pady=5)
tk.Button(root, text="Sync with Server", width=30, command=start_session).pack(pady=5)
tk.Button(root, text="View Game State", width=30, command=view_game_state).pack(pady=5)
tk.Button(root, text="View Client Blockchain (Visual)", width=30, command=view_blockchain_visual).pack(pady=5)

output_box = tk.Text(root, height=10, width=70)
output_box.pack(pady=10)

root.mainloop()
