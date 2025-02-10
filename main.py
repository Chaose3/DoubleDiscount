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
    "Bomb Shooter": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Tack Shooter": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Ice Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },

    "Glue Gunner": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Submarine Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Buccaneer Shooter": { #Possibly wrong
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Monkey Ace": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Helicopter Monkey": { #Definatly wrong
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Mortar Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Dartling Gunner": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Sniper Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Wizard Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Super Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Ninja Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Alchemist Village": {
		"base_cost": 1200,
		"upgrades": {
			(2, 0, 0): 2500,
			(3, 0, 0): 4000,
		}
	},
    "Druid Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Mermonkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },

    "Banana Farm": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Engineer Monkey": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Spike Factory": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Monkey Village": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
    "Beast Handler": {
        "base_cost": 325,
        "upgrades": {
            (2, 3, 0): 4200,
            (0, 2, 3): 5000,
            (0, 5, 0): 18000,
        }
    },
}

difficulty_multipliers = {
    "Easy": 0.85,
    "Medium": 1.0,
    "Hard": 1.15,
    "Impoppable": 1.20
}

# GUI setup
root = tk.Tk()
root.title("BTD6 Tower Cost Calculator")
root.geometry("400x400")

# Tower selection dropdown
tower_label = tk.Label(root, text="Select Tower:")
tower_label.pack()

selected_tower = tk.StringVar()
tower_dropdown = ttk.Combobox(root, textvariable=selected_tower, values=list(tower_costs.keys()))
tower_dropdown.pack()

# Upgrade path selection
upgrade_label = tk.Label(root, text="Select Crosspath:")
upgrade_label.pack()
# Difficulty selection dropdown
tk.Label(root, text="Select Difficulty:").pack()
selected_difficulty = tk.StringVar(value="Medium")
difficulty_dropdown = ttk.Combobox(root, textvariable=selected_difficulty, values=["Easy", "Medium", "Hard", "Impoppable"])
difficulty_dropdown.pack()

# Upgrade path selection
upgrade_label = tk.Label(root, text="Select Crosspath:")
upgrade_label.pack()

selected_upgrade = tk.StringVar()
upgrade_dropdown = ttk.Combobox(root, textvariable=selected_upgrade)
upgrade_dropdown.pack()

# Discount village selection
village_label = tk.Label(root, text="Number of Discount Villages (0-3):")
village_label.pack()

selected_villages = tk.IntVar(value=0)
village_dropdown = ttk.Combobox(root, textvariable=selected_villages, values=[0, 1, 2, 3])
village_dropdown.pack()

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


# Function to calculate discount
def calculate_discount(village_count):
	if village_count == 0:
		return 1  # No discount
	base_discount = 0.15  # First village gives 15%
	extra_discount = 0.05 * (village_count - 1)  # Additional villages give 5% each
	total_discount = base_discount + extra_discount
	return max(0, 1 - total_discount)  # Convert discount to multiplier (e.g., 0.85 for 15%)


# Function to show final cost
def show_cost():
	tower = selected_tower.get()
	try:
		upgrade = eval(selected_upgrade.get())  # Convert string back to tuple
		village_count = selected_villages.get()  # Get selected village count
		difficulty = selected_difficulty.get()  # Get selected difficulty

		if tower in tower_costs and upgrade in tower_costs[tower]["upgrades"]:
			base_cost = tower_costs[tower]["base_cost"]
			upgrade_cost = tower_costs[tower]["upgrades"][upgrade]
			total_cost = base_cost + upgrade_cost

			# Apply difficulty multiplier
			difficulty_multiplier = difficulty_multipliers.get(difficulty, 1.0)
			total_cost *= difficulty_multiplier

			# Apply discount from villages
			discount_multiplier = calculate_discount(village_count)
			total_cost *= discount_multiplier

			# Round and display cost
			result_label.config(text=f"Total Cost: ${total_cost:.2f}")
		else:
			result_label.config(text="Invalid Selection")
	except:
		result_label.config(text="Select a valid crosspath")


# Button to calculate cost
calculate_button = tk.Button(root, text="Calculate Cost", command=show_cost)
calculate_button.pack()

root.mainloop()
