print("==================================================")
print("                   ~ Creature Lab ~               ")
print("==================================================")

print("Choose your creature's body:-")
print("1. Wolf")
print("2. Reptile")
print("3. Bird")
print("4. Bear")

body_choice=input("Enter your choice here:")
if body_choice == "1":
    body = "Wolf"

elif body_choice == "2":
    body = "Reptile"

elif body_choice == "3":
    body = "Bird"

elif body_choice == "4":
    body = "Bear"

print("Choose your creature's ability:-")
print("1. Strength")
print("2. Speed")
print("3. Flight")
print("4. Regeneration")

ability_choice=input("Enter your choice here:")
if ability_choice == "1":
    ability = "Strength"

elif ability_choice == "2":
    ability = "Speed"

elif ability_choice == "3":
    ability = "Flight"

elif ability_choice == "4":
    ability = "Regeneration"

print("Choose your creature's defence:-")
print("1. Spikes")
print("2. Armor")
print("3. Shell")
print("4. Camouflage")

defence_choice=input("Enter your choice here:")
if defence_choice == "1":
    defence = "Spikes"

elif defence_choice == "2":
    defence = "Armor"

elif defence_choice == "3":
    defence = "Shell"

elif defence_choice == "4":
    defence = "Camouflage"

name=input("enter your creature's name here:")

creature_database = {

    # ==================== WOLF ====================

    ("Wolf", "Strength", "Spikes"): {
        "rarity": "Epic",
        "power": 92,
        "intelligence": 58,
        "threat": 89,
        "humanity": 32
    },

    ("Wolf", "Strength", "Armor"): {
        "rarity": "Epic",
        "power": 94,
        "intelligence": 55,
        "threat": 91,
        "humanity": 28
    },

    ("Wolf", "Strength", "Shell"): {
        "rarity": "Rare",
        "power": 87,
        "intelligence": 54,
        "threat": 78,
        "humanity": 35
    },

    ("Wolf", "Strength", "Camouflage"): {
        "rarity": "Rare",
        "power": 82,
        "intelligence": 67,
        "threat": 73,
        "humanity": 52
    },

    ("Wolf", "Speed", "Spikes"): {
        "rarity": "Rare",
        "power": 72,
        "intelligence": 63,
        "threat": 82,
        "humanity": 38
    },

    ("Wolf", "Speed", "Armor"): {
        "rarity": "Rare",
        "power": 76,
        "intelligence": 60,
        "threat": 84,
        "humanity": 35
    },

    ("Wolf", "Speed", "Shell"): {
        "rarity": "Common",
        "power": 68,
        "intelligence": 58,
        "threat": 65,
        "humanity": 42
    },

    ("Wolf", "Speed", "Camouflage"): {
        "rarity": "Rare",
        "power": 65,
        "intelligence": 78,
        "threat": 70,
        "humanity": 68
    },

    ("Wolf", "Flight", "Spikes"): {
        "rarity": "Rare",
        "power": 70,
        "intelligence": 65,
        "threat": 78,
        "humanity": 40
    },

    ("Wolf", "Flight", "Armor"): {
        "rarity": "Rare",
        "power": 73,
        "intelligence": 62,
        "threat": 81,
        "humanity": 35
    },

    ("Wolf", "Flight", "Shell"): {
        "rarity": "Common",
        "power": 62,
        "intelligence": 58,
        "threat": 62,
        "humanity": 44
    },

    ("Wolf", "Flight", "Camouflage"): {
        "rarity": "Rare",
        "power": 64,
        "intelligence": 80,
        "threat": 72,
        "humanity": 65
    },

    ("Wolf", "Regeneration", "Spikes"): {
        "rarity": "Epic",
        "power": 84,
        "intelligence": 62,
        "threat": 91,
        "humanity": 25
    },

    ("Wolf", "Regeneration", "Armor"): {
        "rarity": "Epic",
        "power": 88,
        "intelligence": 59,
        "threat": 94,
        "humanity": 21
    },

    ("Wolf", "Regeneration", "Shell"): {
        "rarity": "Rare",
        "power": 80,
        "intelligence": 57,
        "threat": 82,
        "humanity": 29
    },

    ("Wolf", "Regeneration", "Camouflage"): {
        "rarity": "Epic",
        "power": 75,
        "intelligence": 82,
        "threat": 79,
        "humanity": 58
    },


    # ==================== REPTILE ====================

    ("Reptile", "Strength", "Spikes"): {
        "rarity": "Epic",
        "power": 90,
        "intelligence": 50,
        "threat": 87,
        "humanity": 25
    },

    ("Reptile", "Strength", "Armor"): {
        "rarity": "Epic",
        "power": 93,
        "intelligence": 48,
        "threat": 92,
        "humanity": 20
    },

    ("Reptile", "Strength", "Shell"): {
        "rarity": "Epic",
        "power": 91,
        "intelligence": 45,
        "threat": 88,
        "humanity": 18
    },

    ("Reptile", "Strength", "Camouflage"): {
        "rarity": "Rare",
        "power": 82,
        "intelligence": 64,
        "threat": 76,
        "humanity": 48
    },

    ("Reptile", "Speed", "Spikes"): {
        "rarity": "Rare",
        "power": 69,
        "intelligence": 55,
        "threat": 78,
        "humanity": 30
    },

    ("Reptile", "Speed", "Armor"): {
        "rarity": "Rare",
        "power": 73,
        "intelligence": 52,
        "threat": 82,
        "humanity": 25
    },

    ("Reptile", "Speed", "Shell"): {
        "rarity": "Rare",
        "power": 67,
        "intelligence": 49,
        "threat": 70,
        "humanity": 27
    },

    ("Reptile", "Speed", "Camouflage"): {
        "rarity": "Rare",
        "power": 62,
        "intelligence": 73,
        "threat": 67,
        "humanity": 55
    },

    ("Reptile", "Flight", "Spikes"): {
        "rarity": "Rare",
        "power": 66,
        "intelligence": 57,
        "threat": 75,
        "humanity": 34
    },

    ("Reptile", "Flight", "Armor"): {
        "rarity": "Rare",
        "power": 70,
        "intelligence": 54,
        "threat": 80,
        "humanity": 29
    },

    ("Reptile", "Flight", "Shell"): {
        "rarity": "Rare",
        "power": 64,
        "intelligence": 51,
        "threat": 69,
        "humanity": 31
    },

    ("Reptile", "Flight", "Camouflage"): {
        "rarity": "Rare",
        "power": 61,
        "intelligence": 76,
        "threat": 71,
        "humanity": 60
    },

    ("Reptile", "Regeneration", "Spikes"): {
        "rarity": "Epic",
        "power": 85,
        "intelligence": 58,
        "threat": 92,
        "humanity": 22
    },

    ("Reptile", "Regeneration", "Armor"): {
        "rarity": "Epic",
        "power": 89,
        "intelligence": 55,
        "threat": 96,
        "humanity": 17
    },

    ("Reptile", "Regeneration", "Shell"): {
        "rarity": "Epic",
        "power": 87,
        "intelligence": 52,
        "threat": 94,
        "humanity": 15
    },

    ("Reptile", "Regeneration", "Camouflage"): {
        "rarity": "Epic",
        "power": 76,
        "intelligence": 79,
        "threat": 83,
        "humanity": 50
    },


    # ==================== BIRD ====================

    ("Bird", "Strength", "Spikes"): {
        "rarity": "Rare",
        "power": 65,
        "intelligence": 68,
        "threat": 70,
        "humanity": 48
    },

    ("Bird", "Strength", "Armor"): {
        "rarity": "Rare",
        "power": 69,
        "intelligence": 65,
        "threat": 75,
        "humanity": 43
    },

    ("Bird", "Strength", "Shell"): {
        "rarity": "Common",
        "power": 58,
        "intelligence": 61,
        "threat": 57,
        "humanity": 50
    },

    ("Bird", "Strength", "Camouflage"): {
        "rarity": "Rare",
        "power": 61,
        "intelligence": 78,
        "threat": 63,
        "humanity": 72
    },

    ("Bird", "Speed", "Spikes"): {
        "rarity": "Rare",
        "power": 57,
        "intelligence": 72,
        "threat": 68,
        "humanity": 52
    },

    ("Bird", "Speed", "Armor"): {
        "rarity": "Rare",
        "power": 61,
        "intelligence": 69,
        "threat": 73,
        "humanity": 47
    },

    ("Bird", "Speed", "Shell"): {
        "rarity": "Common",
        "power": 51,
        "intelligence": 65,
        "threat": 55,
        "humanity": 53
    },

    ("Bird", "Speed", "Camouflage"): {
        "rarity": "Rare",
        "power": 54,
        "intelligence": 84,
        "threat": 62,
        "humanity": 78
    },

    ("Bird", "Flight", "Spikes"): {
        "rarity": "Epic",
        "power": 67,
        "intelligence": 76,
        "threat": 81,
        "humanity": 55
    },

    ("Bird", "Flight", "Armor"): {
        "rarity": "Epic",
        "power": 72,
        "intelligence": 73,
        "threat": 86,
        "humanity": 48
    },

    ("Bird", "Flight", "Shell"): {
        "rarity": "Rare",
        "power": 59,
        "intelligence": 69,
        "threat": 67,
        "humanity": 56
    },

    ("Bird", "Flight", "Camouflage"): {
        "rarity": "Epic",
        "power": 62,
        "intelligence": 91,
        "threat": 76,
        "humanity": 84
    },

    ("Bird", "Regeneration", "Spikes"): {
        "rarity": "Epic",
        "power": 74,
        "intelligence": 73,
        "threat": 86,
        "humanity": 46
    },

    ("Bird", "Regeneration", "Armor"): {
        "rarity": "Epic",
        "power": 79,
        "intelligence": 70,
        "threat": 91,
        "humanity": 40
    },

    ("Bird", "Regeneration", "Shell"): {
        "rarity": "Rare",
        "power": 68,
        "intelligence": 66,
        "threat": 75,
        "humanity": 45
    },

    ("Bird", "Regeneration", "Camouflage"): {
        "rarity": "Epic",
        "power": 67,
        "intelligence": 88,
        "threat": 78,
        "humanity": 76
    },


    # ==================== BEAR ====================

    ("Bear", "Strength", "Spikes"): {
        "rarity": "Epic",
        "power": 96,
        "intelligence": 58,
        "threat": 93,
        "humanity": 24
    },

    ("Bear", "Strength", "Armor"): {
        "rarity": "Legendary",
        "power": 100,
        "intelligence": 55,
        "threat": 99,
        "humanity": 15
    },

    ("Bear", "Strength", "Shell"): {
        "rarity": "Epic",
        "power": 98,
        "intelligence": 51,
        "threat": 95,
        "humanity": 18
    },

    ("Bear", "Strength", "Camouflage"): {
        "rarity": "Epic",
        "power": 91,
        "intelligence": 72,
        "threat": 88,
        "humanity": 42
    },

    ("Bear", "Speed", "Spikes"): {
        "rarity": "Rare",
        "power": 76,
        "intelligence": 62,
        "threat": 82,
        "humanity": 30
    },

    ("Bear", "Speed", "Armor"): {
        "rarity": "Epic",
        "power": 82,
        "intelligence": 59,
        "threat": 88,
        "humanity": 25
    },

    ("Bear", "Speed", "Shell"): {
        "rarity": "Rare",
        "power": 73,
        "intelligence": 55,
        "threat": 75,
        "humanity": 28
    },

    ("Bear", "Speed", "Camouflage"): {
        "rarity": "Rare",
        "power": 70,
        "intelligence": 76,
        "threat": 72,
        "humanity": 55
    },

    ("Bear", "Flight", "Spikes"): {
        "rarity": "Rare",
        "power": 78,
        "intelligence": 64,
        "threat": 80,
        "humanity": 32
    },

    ("Bear", "Flight", "Armor"): {
        "rarity": "Epic",
        "power": 84,
        "intelligence": 61,
        "threat": 87,
        "humanity": 27
    },

    ("Bear", "Flight", "Shell"): {
        "rarity": "Rare",
        "power": 75,
        "intelligence": 57,
        "threat": 73,
        "humanity": 30
    },

    ("Bear", "Flight", "Camouflage"): {
        "rarity": "Rare",
        "power": 72,
        "intelligence": 79,
        "threat": 75,
        "humanity": 58
    },

    ("Bear", "Regeneration", "Spikes"): {
        "rarity": "Legendary",
        "power": 93,
        "intelligence": 67,
        "threat": 100,
        "humanity": 12
    },

    ("Bear", "Regeneration", "Armor"): {
        "rarity": "Legendary",
        "power": 97,
        "intelligence": 63,
        "threat": 100,
        "humanity": 8
    },

    ("Bear", "Regeneration", "Shell"): {
        "rarity": "Epic",
        "power": 95,
        "intelligence": 59,
        "threat": 98,
        "humanity": 10
    },

    ("Bear", "Regeneration", "Camouflage"): {
        "rarity": "Legendary",
        "power": 88,
        "intelligence": 82,
        "threat": 94,
        "humanity": 35
    }
}

creature = creature_database[(body, ability, defence)]

rarity = creature["rarity"]
power = creature["power"]
intelligence = creature["intelligence"]
threat = creature["threat"]
humanity = creature["humanity"]

if humanity >= 81:
    status = "HIGHLY COMPATIBLE"
elif humanity >= 51:
    status = "COMPATIBLE"
elif humanity >= 21:
    status = "UNSTABLE"
else:
    status = "CRITICAL"

print("=====================================================")
print("                   ~ Experiment done ~               ")
print("=====================================================")

print("Creature Name:", name)
print("Body type:", body)
print("Ability:", ability)
print("Defence:", defence)
print("Rarity:", rarity)
print("Power:", power)
print("Intelligence:", intelligence)
print("Threat Level:", threat)
print("Humanity Compatibility:", humanity, "%")
print("Status:", status)

print=input("\n Press enter to exit...")
