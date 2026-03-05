# GameState-Blockchain-Validator 🔗

**GameState Blockchain Validator** is a prototype system that uses blockchain principles to detect tampering in offline game progress. Each gameplay session is stored as a hash-linked block, allowing the server to validate game state transitions and automatically restore the last trusted state if manipulation is detected.

---

## 🧩 Problem Statement

Many games allow offline gameplay where progress is stored locally and later synchronized with an online server. Since save files are stored on the client device, players may modify them to gain unfair advantages such as higher levels, increased currency, or rare items.

This project demonstrates how blockchain concepts can create a **tamper-evident ledger of game progress**, allowing servers to detect manipulated states during synchronization.

---

## 🚀 Features

- 🔗 Blockchain-based game progress tracking
- 📦 Hash-linked block structure
- 🎮 Client-side offline gameplay recording
- 🛡 Server-side validation of state transitions
- 🚨 Tampering detection for manipulated game states
- 🔄 Automatic rollback to the last trusted state
- 🖥 GUI dashboard for demonstration
- 📊 Visual representation of blockchain blocks

---

## 🏗 System Architecture

The project simulates a hybrid **client-server architecture**.

### Client
- Plays offline game sessions
- Stores local game state
- Records each session into blockchain blocks

### Server
- Maintains trusted blockchain ledger
- Validates incoming blocks
- Detects tampering
- Restores trusted state if manipulation is detected

---

## 📂 Project Structure

```
GameState-Blockchain-Validator
│
├── client
│   ├── game_state.py
│   └── offline_play.py
│
├── common
│   ├── block.py
│   └── blockchain.py
│
├── server
│   ├── sync_server.py
│   └── validator.py
│
├── gui
│   └── dashboard.py
│
├── data
│   ├── client_chain.json
│   ├── server_chain.json
│   └── game_state.json
│
└── README.md
```

---

## 🔗 How the Blockchain Works

Each block contains:

- **Index** – Position of the block in the chain  
- **Timestamp** – Time the block was created  
- **Game State** – Snapshot of level, money, and items  
- **Previous Hash** – Hash of the previous block  
- **Hash** – SHA256 hash of the current block  

Because each block contains the previous block's hash, all blocks are linked together forming a blockchain. If a block is modified, the chain becomes invalid, allowing the system to detect tampering.

---

## 🚨 Tampering Detection

During synchronization, the server validates the new blocks by checking:

- Valid level progression
- Logical currency increase
- Consistency with the previous trusted state

If manipulation is detected:

1. The tampered block is rejected  
2. The game state is restored to the last trusted block  
3. Invalid blocks are removed from the client chain  

---

## 🧪 How to Run

### Prerequisites

- Python 3.10+

### Run the GUI Dashboard

```bash
python gui/dashboard.py
```

---

## 🎮 Demonstration Flow

### Normal Gameplay

1. Start Session  
2. Play Offline  
3. Sync with Server  

The server validates the new block and updates the trusted blockchain ledger.

### Tampering Detection

1. Modify the game state file
2. Create a block from the tampered state
3. Sync with server

The system detects the invalid transition and automatically restores the last trusted state.

---

## ⚠ Limitations

This project is a **prototype for educational purposes** and does not include:

- Distributed blockchain nodes
- Consensus mechanisms
- Cryptographic signatures
- Real network communication

The server acts as a centralized validator in this demonstration.

---

## 🔮 Future Improvements

- Multi-node blockchain simulation
- Peer-to-peer validation
- Cryptographic block signing
- Real client-server network communication
- Advanced anti-cheat detection algorithms
