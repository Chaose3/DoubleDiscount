import PySimpleGUI as sg

# Difficulty multipliers
difficulty_multipliers = {
    "Easy": 0.85,
    "Medium": 1.0,
    "Hard": 1.15,
    "Impoppable": 1.20
}

# Tower costs, storing individual upgrade costs
tower_costs = {
    "Dart Monkey": {
        "base_cost": 200,
        "upgrades": {
            "top": [0, 250, 500, 1200, 5000, 18855],
            "middle": [0, 200, 450, 1000, 4300, 57975],
            "bottom": [0, 175, 400, 900, 3800, 26365],
        }
    },
    "Boomerang Monkey": {
        "base_cost": 325,
        "upgrades": {
            "top": [0, 300, 600, 1400, 6000, 36800],
            "middle": [0, 275, 550, 1250, 5200, 44360],
            "bottom": [0, 250, 500, 1100, 4800, 58430],
        }
    }
}

# GUI Layout
layout = [
    [sg.Text("Select Tower:"), sg.Combo(list(tower_costs.keys()), key="TOWER")],
    [sg.Text("Select Difficulty:"), sg.Combo(list(difficulty_multipliers.keys()), key="DIFFICULTY")],
    [sg.Text("Number of Discount Villages (0-3):"), sg.Combo([0, 1, 2, 3], key="VILLAGES")],
    [sg.Text("Top Path Upgrade:"), sg.Combo(["None", "1", "2", "3", "4", "5"], key="TOP")],
    [sg.Text("Middle Path Upgrade:"), sg.Combo(["None", "1", "2", "3", "4", "5"], key="MIDDLE")],
    [sg.Text("Bottom Path Upgrade:"), sg.Combo(["None", "1", "2", "3", "4", "5"], key="BOTTOM")],
    [sg.Button("Calculate"), sg.Text("", key="RESULT")],
]

# Create window
window = sg.Window("BTD6 Tower Cost Calculator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "Calculate":
        tower = values["TOWER"]
        difficulty = values["DIFFICULTY"]
        villages = int(values["VILLAGES"]) if values["VILLAGES"] else 0

        # Get upgrade choices for top, middle, and bottom paths
        top_upgrade = int(values["TOP"]) if values["TOP"] != "None" else 0
        middle_upgrade = int(values["MIDDLE"]) if values["MIDDLE"] != "None" else 0
        bottom_upgrade = int(values["BOTTOM"]) if values["BOTTOM"] != "None" else 0

        # Check that no more than two paths are upgraded
        upgrade_paths = sum(1 for x in [top_upgrade, middle_upgrade, bottom_upgrade] if x > 0)
        if upgrade_paths > 2:
            window["RESULT"].update("Error: You can only upgrade two paths!")
            continue

        # Check that no upgrade exceeds 2 in the third path
        upgrade_levels = sorted([top_upgrade, middle_upgrade, bottom_upgrade], reverse=True)
        if upgrade_levels[2] >= 3:
            window["RESULT"].update("Error: Only two paths can be upgraded beyond tier 2!")
            continue

        if tower and difficulty:
            base_cost = tower_costs[tower]["base_cost"]
            difficulty_multiplier = difficulty_multipliers[difficulty]
            discount_multiplier = max(0, 1 - (0.15 + (villages - 1) * 0.05)) if villages > 0 else 1

            # Calculate total upgrade cost
            upgrade_costs = sum(
                tower_costs[tower]["upgrades"]["top"][top_upgrade] +
                tower_costs[tower]["upgrades"]["middle"][middle_upgrade] +
                tower_costs[tower]["upgrades"]["bottom"][bottom_upgrade]
            )

            # Final price calculation
            final_cost = (base_cost + upgrade_costs) * difficulty_multiplier * discount_multiplier
            window["RESULT"].update(f"Total Cost: ${final_cost:.2f}")
        else:
            window["RESULT"].update("Please fill all fields.")

window.close()