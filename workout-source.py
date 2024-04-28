import random


#Chest Movements Definition
main_chest_movements = ["Bench Press", "Smith Press", "Incline Bench Press", "Incline Smith Press", "Dumbbell Press", "Incline Dumbbell Press", 
                        "Slight Incline Smith Press","Slight Incline Dumbbell Press","Plate Loaded Machine Press", "Plate Loaded Decline Press", 
                       "Plate Loaded Incline Press" ]
fly_movements = ["Pec Deck", "Dumbbell Fly","Incline Dumbbell Fly","Cable Fly","High to Low Cable Fly","Low to High Cable Fly"]
day_1_chest_movement = random.choice(main_chest_movements)
day_1_fly_movement = random.choice(fly_movements)

#Arm Movements Definition
bicep_movements = ["Ez Bar Curl","Preacher EZ bar curl","Db Curl","Seated Db Curl", "Machine Curl","Cable Curl","Single arm cable curl"]
tricep_movements = ["Pushdowns","Bar Pushdowns", "Dips","Weighted Dips","Skullcrusher","DB Skullcrushers","Cable Extensions","Close Grip Bench",
                    "Smith Close Grip Bench", "Push-up"]
day_1_bicep_movement = random.choice(bicep_movements)
day_1_tricep_movement = random.choice(tricep_movements)


#Rep Range Definition
main_rep_range = ["3 x 5-8","3 x 6-10","3 x 8-12"]
secondary_rep_range = ["3 x 8-12", "3 x 10-15","3 x 15-20"]
main_rep_range_rand = random.choice(main_rep_range)
secondary_rep_range_rand = random.choice(secondary_rep_range)


#Your weekly workout
print("Here is your day one routine: \n")
print(day_1_chest_movement,main_rep_range_rand)
print(day_1_fly_movement,secondary_rep_range_rand)
print(day_1_bicep_movement,secondary_rep_range_rand)
print(day_1_tricep_movement,secondary_rep_range_rand)

