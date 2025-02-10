import tkinter as tk
from tkinter import ttk

# Tower costs dictionary
tower_costs = {
    "Dart Monkey": {
        "base_cost": 200,
        "upgrades": {
            (2, 0, 3): 2500,
            (0, 3, 2): 3200,
            (5, 0, 0): 20000,
        }
    },
    "Boomerang Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
}

# GUI setup
root = tk.Tk()  # Corrected this line
root.title("BTD6 Tower Cost Calculator")
root.geometry("400x300")

# Dropdown for tower selection
tower_label = tk.Label(root, text="Select Tower:")
tower_label.pack()

selected_tower = tk.StringVar()
tower_dropdown = ttk.Combobox(root, textvariable=selected_tower, values=list(tower_costs.keys()))
tower_dropdown.pack()

# Dropdown for upgrade paths
upgrade_label = tk.Label(root, text="Select Crosspath:")
upgrade_label.pack()

selected_upgrade = tk.StringVar()
upgrade_dropdown = ttk.Combobox(root, textvariable=selected_upgrade)
upgrade_dropdown.pack()

# Result label
result_label = tk.Label(root, text="Total Cost: ", font=("Arial", 14))
result_label.pack(pady=10)

# Update upgrades when tower is selected
def update_upgrades(event):
    tower = selected_tower.get()
    if tower in tower_costs:
        upgrade_dropdown["values"] = [str(k) for k in tower_costs[tower]["upgrades"].keys()]
        upgrade_dropdown.current(0)  # Default to first upgrade

tower_dropdown.bind("<<ComboboxSelected>>", update_upgrades)

# Function to show cost
def show_cost():
    tower = selected_tower.get()
    try:
        upgrade = eval(selected_upgrade.get())  # Convert string back to tuple
        if tower in tower_costs and upgrade in tower_costs[tower]["upgrades"]:
            base_cost = tower_costs[tower]["base_cost"]
            upgrade_cost = tower_costs[tower]["upgrades"][upgrade]
            total_cost = base_cost + upgrade_cost
            result_label.config(text=f"Total Cost: ${total_cost}")
        else:
            result_label.config(text="Invalid Selection")
    except:
        result_label.config(text="Select a valid crosspath")

# Button to calculate cost
calculate_button = tk.Button(root, text="Calculate Cost", command=show_cost)
calculate_button.pack()

root.mainloop()
