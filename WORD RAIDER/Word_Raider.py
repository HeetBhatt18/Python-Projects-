import heapq

# -------------------------------
# SHOPPING COMPLEX MAP
# -------------------------------
# Each shop is a node
# Each path has a distance (cost)

shopping_complex = {
    "A": {"B": 2, "D": 1},
    "B": {"A": 2, "C": 3, "E": 2},
    "C": {"B": 3, "F": 5},
    "D": {"A": 1, "E": 1},
    "E": {"D": 1, "B": 2, "F": 1},
    "F": {}  # Target shop (item available here)
}

# -------------------------------
# DIJKSTRA ALGORITHM
# -------------------------------
def shortest_path(graph, start, target):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        distance, current_shop, path = heapq.heappop(priority_queue)

        if current_shop in visited:
            continue

        visited.add(current_shop)
        path = path + [current_shop]

        if current_shop == target:
            return distance, path

        for neighbor, cost in graph[current_shop].items():
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (distance + cost, neighbor, path)
                )

    return float("inf"), []


# -------------------------------
# GAME START
# -------------------------------
def start_game():
    print("\n🛍️ WELCOME TO THE SHOPPING COMPLEX GAME 🛍️")
    print("-" * 45)

    print("\nAvailable Shops:")
    for shop in shopping_complex:
        print(f"• Shop {shop}")

    start_shop = input("\nEnter your starting shop: ").upper()
    target_shop = input("Enter the shop where item is available: ").upper()

    if start_shop not in shopping_complex or target_shop not in shopping_complex:
        print("\n❌ Invalid shop entered!")
        return

    print("\n🔍 Finding shortest path...\n")

    distance, path = shortest_path(shopping_complex, start_shop, target_shop)

    if path:
        print("✅ ITEM FOUND!")
        print("🛣️ Path Taken:")
        print(" → ".join(path))
        print(f"📏 Total Distance: {distance}")
    else:
        print("❌ No path found to the target shop.")

    print("\n🎮 GAME OVER")
    print("-" * 45)


# -------------------------------
# RUN GAME
# -------------------------------
if __name__ == "__main__":
    start_game()
    

