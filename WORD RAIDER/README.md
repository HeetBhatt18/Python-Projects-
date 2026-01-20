# 🛍️ Shopping Complex Shortest Path Game (Python)

A simple **console-based Python game** that helps a player find the **shortest path** to reach a shop inside a shopping complex using **Dijkstra’s Algorithm**.

This project is beginner-friendly and demonstrates how **graph algorithms** are used in real-world scenarios like navigation and pathfinding.

---

## 📌 Project Overview

In this game:
- Each **shop** is represented as a **node**
- Each **path between shops** has a **distance (cost)**
- The player selects:
  - A **starting shop**
  - A **target shop** (where the item is available)
- The program calculates the **shortest path** and **minimum distance** to reach the item

---

## 🧠 Algorithm Used

**Dijkstra’s Algorithm**
- Finds the shortest path in a weighted graph
- Uses a **priority queue (heap)** for efficiency
- Ensures optimal distance calculation

---

## 🛠️ Technologies Used

- **Python 3**
- Built-in libraries:
  - `heapq` (priority queue)

No external libraries required.

---

## ▶️ How to Run the Game

### Step 1: Clone or Download
Download the Python file or clone the repository.

### Step 2: Open in VS Code
Open the project folder in **VS Code**.

### Step 3: Run the Program
Open terminal and run:

```bash
python shopping_complex_game.py
🛍️ WELCOME TO THE SHOPPING COMPLEX GAME 🛍️

Available Shops:
• Shop A
• Shop B
• Shop C
• Shop D
• Shop E
• Shop F

Enter your starting shop: A
Enter the shop where item is available: F

🔍 Finding shortest path...

✅ ITEM FOUND!
🛣️ Path Taken:
A → D → E → F
📏 Total Distance: 3

🎮 GAME OVER




