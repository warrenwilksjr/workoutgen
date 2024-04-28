import random

main_chest_movements = ["Bench Press", "Smith Press", "Incline Bench Press", "Incline Smith Press", "Dumbbell Press", "Incline Dumbbell Press", 
                        "Slight Incline Smith Press","Slight Incline Dumbbell Press","Plate Loaded Machine Press", "Plate Loaded Decline Press", 
                       "Plate Loaded Incline Press" ]
main_rep_range = ["3 x 6-10","3 x 8-12"]
day_1_1st_movement = random.choice(main_chest_movements)
main_rep_range_rand = random.choice(main_rep_range)

print(day_1_1st_movement,main_rep_range_rand)
print(main_rep_range_rand)