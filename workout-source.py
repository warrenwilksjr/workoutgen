import random


#Chest Movements Definition
main_chest_movements = ["Bench Press", "Smith Press", "Incline Bench Press", "Incline Smith Press", "Dumbbell Press", 
                         "Incline Dumbbell Press", "Slight Incline Smith Press","Slight Incline Dumbbell Press",
                         "Plate Loaded Machine Press", "Plate Loaded Decline Press", "Plate Loaded Incline Press" ]
fly_movements = ["Pec Deck", "Dumbbell Fly","Incline Dumbbell Fly","Cable Fly","High to Low Cable Fly","Low to High Cable Fly"]
chest_movement_rand = random.choice(main_chest_movements)
fly_movement_rand = random.choice(fly_movements)

#Arm Movements Definition
bicep_movements = ["Ez Bar Curl","Preacher EZ bar curl","Db Curl","Seated Db Curl", "Machine Curl",
                   "Cable Curl","Single arm cable curl","Hammer Curl", "Pin Wheel Curl", "Preacher Hammer Curl"]
tricep_movements = ["Pushdowns","Bar Pushdowns", "Dips","Weighted Dips","Skullcrusher","DB Skullcrushers",
                    "Cable Extensions","Close Grip Bench","Smith Close Grip Bench", "Push-up"]
bicep_movement_rand = random.choice(bicep_movements)
tricep_movement_rand = random.choice(tricep_movements)

#Shoulders Movements Definition
side_delt_movements = ["Dumbbell Laterals", "Seated Dumbbell Laterals", "Cable Laterals", "One arm Cable Laterals", 
                       "Behind the Neck Laterals","Chest Supported Y Raise", "Lying Y Raise", 
                       "Barbell Upright Row", "Dumbbell Upright Row","Cable Upright Row" ]
front_delt_movements = ["High Incline Smith Press", "High Incline Barbell Press", "High Incline Dumbbell Press",
                         "Plate Loaded Shoulder Press","Machine Shoulder Press", "Barbell Press", "Dumbbell Press",
                           "Arnold Press", "Seated Arnold Press"]
rear_delt_movements = ["Bent Dumbbell Rear Delt Fly", "Reverse Pec Deck", "Chest Supported Dumbbell Rear Delt Fly",
                       "Cable Rear Fly", "Facepull", "Barbell Facepull", "Seated Facepull"]
side_movement_rand = random.choice(side_delt_movements)
front_movement_rand = random.choice(front_delt_movements)
rear_movement_rand = random.choice(rear_delt_movements)

#Back Movements Definition
vert_pull_movements = ["Neutral Lat Pulldown", "Pull ups","Assisted Pull-up", "Weighted Pull Ups", "Lat Pulldown",
                       "Single Arm Pulldown", "Single Arm Plate Loaded Pulldown","Close Grip Pulldown"]
horzontal_row_movements = [ "Chest Supported Row",   "Chest Supported T Bar Row", "Dumbbell Row",
                           "Chest Supported Dumbbell Row","Low Cable Row"]
horzaontal_row_movements_axel = ["Barbell row","Meadows Row", "T Bar Row","Smith Machine Row"]
trap_movements = ["Dumbbell Shrug", "Barbell Shrug", "Smith Machine Shrug"]
vert_pull_movement_rand = random.choice(vert_pull_movements)
horzontal_row_movement_rand = random.choice(horzontal_row_movements)
horzontal_row_movement_axel_rand = random.choice(horzaontal_row_movements_axel)
trap_movement_rand = random.choice(trap_movements)

#Quad Movements Definition
quad_movements = ["Leg Press", "Squat", "Smith Squat", "Hack Squat"]
secondary_quad_movements = ["Leg Extensions", "Dumbbell Lunges", "Split Squats", "Leg Press"]
quad_movements_rand = random.choice(quad_movements)
secondary_quad_movement_rand = random.choice(secondary_quad_movements)

#Hamstring Movements Definition
ham_curl_movements = ["Seated Ham Curl", "Lying Ham Curl", "Kneeling Ham Curl"]
hip_hinge_movements = ["RDL", "Stiff Leg Deadlift", "Dumbbell RDL", "Deadlift"]
ham_curl_movement_rand = random.choice(ham_curl_movements)
hip_hinge_movement_rand = random.choice(hip_hinge_movements)

#Calve Movements Definition
calf_movements = ["Standing Calves", "Seated Calves", "Leg Press Calves"]
calf_movement_rand = random.choice(calf_movements)

#Rep Range Definition
main_rep_range = ["3 x 5-8","3 x 6-10","3 x 8-12", "3 x 6-8, 8-10, 10-12", "3 x 10-12, 8-10, 6-8"]
secondary_rep_range = ["3 x 8-12", "3 x 10-15","3 x 15-20"]
all_ranges = ["3 x 5-8","3 x 6-10","3 x 8-12","3 x 10-15","3 x 15-20"]
fail_rep_range = "3 x fail"
main_rep_range_rand = random.choice(main_rep_range)
secondary_rep_range_rand = random.choice(secondary_rep_range)
all_ranges_rand = random.choice(all_ranges)

#Intensity techiques
intensity_techiques = [":Last Set - dropset", ":Last Set - double dropset", ":Last Set triple dropset", 
                       ":Every Set myo-rep match", ":Last Set: 3 rest pause sets"]
superset = ["y","n"]
intensity_techiques_rand_day_1 = random.choice(intensity_techiques)
intensity_techiques_rand_day_2 = random.choice(intensity_techiques)
superset_rand = random.choice(superset)

#Obtaining User Input
hamsting_variation = input("Do you want to hip hinge or Leg Curl: \n 1. Hip Hinge \n 2. Leg Curl \n\n")
squat_variation = input("Can you barbell squat: \n 1. Yes \n 2. No \n\n")
side_or_rear_delt_focus = input("Do you want to focus side or rear delts? \n 1. Side \n 2. Rear \n\n")


#Your weekly workout
print("\nHere is your weekly routine: \n")

#Leg Print Out: Need to remove a hamstring movement from day. Move Deads to hams. Combine ham movements. These are advance
print("Day 1 routine: \n")

if hamsting_variation == "2":
        print("1. ",ham_curl_movement_rand,secondary_rep_range_rand, intensity_techiques_rand_day_1)
elif hamsting_variation == "1" and hip_hinge_movement_rand == "Dumbbell RDL":
        print("1. ",hip_hinge_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_1)
else:
        print("1. ",hip_hinge_movement_rand,main_rep_range_rand)

if squat_variation == "1":
        print("2. ",quad_movements_rand,main_rep_range_rand)
else:
        print("2. ", secondary_quad_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_1)
print("3. ",secondary_quad_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_1)
print("4. ",calf_movement_rand,all_ranges_rand,intensity_techiques_rand_day_1)


print("\n")

#Back and Shoulder Print. Pick between a side or rear delt. add both once advance
print("Day 2 routine: \n")
if side_or_rear_delt_focus == "1":
        print("1. ",side_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)
else:
     print("1. ",rear_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)   
print("2. ",front_movement_rand,main_rep_range_rand)

if trap_movement_rand == "Dumbbell Shrug":
        print("3. ",trap_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)
else: print("3. ",trap_movement_rand,main_rep_range_rand,intensity_techiques_rand_day_2)

if vert_pull_movement_rand == "Pull ups" or vert_pull_movement_rand == "Assisted Pull-up":
        print("4. ",vert_pull_movement_rand,fail_rep_range,intensity_techiques_rand_day_2)
elif vert_pull_movement_rand == "Weighted Pull Ups" or vert_pull_movement_rand == "Single Arm Plate Loaded Pulldown":
        print("4. ",vert_pull_movement_rand,main_rep_range_rand,intensity_techiques_rand_day_2)
else: print("4. ",vert_pull_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)


if hamsting_variation == "1" and horzontal_row_movement_rand == "Chest Supported Dumbbell Row" or horzontal_row_movement_rand == "Dumbbell Row" or  horzontal_row_movement_rand == "Low Cable Row":
        print("5. ",horzontal_row_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)
elif hamsting_variation == "2":
        print("5. ",horzontal_row_movement_axel_rand,main_rep_range_rand)
else: print("5. ",horzontal_row_movement_rand,main_rep_range_rand,intensity_techiques_rand_day_2)

print("\n")

#Chest and Arms Print
print("Day 3 routine: \n")
if chest_movement_rand == "Bench Press" or chest_movement_rand == "Incline Bench Press":
        print("1. ",chest_movement_rand,main_rep_range_rand)
else:
      print("1. ",chest_movement_rand,main_rep_range_rand,intensity_techiques_rand_day_1)  
print("2. ",fly_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_1)
print("3. ",bicep_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)
print("4. ",tricep_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)

print("\n")

