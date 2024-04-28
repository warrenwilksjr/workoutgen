import random


#Chest Movements Definition
main_chest_movements = ["Bench Press", "Smith Press", "Incline Bench Press", "Incline Smith Press", "Dumbbell Press", "Incline Dumbbell Press", 
                        "Slight Incline Smith Press","Slight Incline Dumbbell Press","Plate Loaded Machine Press", "Plate Loaded Decline Press", 
                       "Plate Loaded Incline Press" ]
fly_movements = ["Pec Deck", "Dumbbell Fly","Incline Dumbbell Fly","Cable Fly","High to Low Cable Fly","Low to High Cable Fly"]
chest_movement_rand = random.choice(main_chest_movements)
fly_movement_rand = random.choice(fly_movements)

#Arm Movements Definition
bicep_movements = ["Ez Bar Curl","Preacher EZ bar curl","Db Curl","Seated Db Curl", "Machine Curl","Cable Curl","Single arm cable curl"]
tricep_movements = ["Pushdowns","Bar Pushdowns", "Dips","Weighted Dips","Skullcrusher","DB Skullcrushers","Cable Extensions","Close Grip Bench",
                    "Smith Close Grip Bench", "Push-up"]
bicep_movement_rand = random.choice(bicep_movements)
tricep_movement_rand = random.choice(tricep_movements)

#Shoulders Movements Definition
side_delt_movements = ["Dumbbell Laterals", "Seated Dumbbell Laterals", "Cable Laterals", "One arm Cable Laterals", "Behind the Neck Laterals",
                       "Chest Supported Y Raise", "Lying Y Raise", "Barbell Upright Row", "Dumbbell Upright Row","Cable Upright Row" ]
front_delt_movements = ["High Incline Smith Press", "High Incline Barbell Press", "High Incline Dumbbell Press", "Plate Loaded Shoulder Press",
                        "Machine Shoulder Press", "Barbell Press", "Dumbbell Press", "Arnold Press", "Seated Arnold Press"]
rear_delt_movements = ["Bent Dumbbell Rear Delt Fly", "Reverse Pec Deck", "Chest Supported Dumbbell Rear Delt Fly","Cable Rear Fly", "Facepull", "Barbell Facepull",
                       "Seated Facepull"]
side_movement_rand = random.choice(side_delt_movements)
front_movement_rand = random.choice(front_delt_movements)
rear_movement_rand = random.choice(rear_delt_movements)



#Rep Range Definition
main_rep_range = ["3 x 5-8","3 x 6-10","3 x 8-12"]
secondary_rep_range = ["3 x 8-12", "3 x 10-15","3 x 15-20"]
main_rep_range_rand = random.choice(main_rep_range)
secondary_rep_range_rand = random.choice(secondary_rep_range)


#Your weekly workout
print("Here is your day one routine: \n")

print("Day 2 routine: \n")
print(side_movement_rand,secondary_rep_range_rand)
print(front_movement_rand,main_rep_range_rand)
print(rear_movement_rand,secondary_rep_range_rand)
print("\n")

print("Day 3 routine: \n")
print(chest_movement_rand,main_rep_range_rand)
print(fly_movement_rand,secondary_rep_range_rand)
print(bicep_movement_rand,secondary_rep_range_rand)
print(tricep_movement_rand,secondary_rep_range_rand)

