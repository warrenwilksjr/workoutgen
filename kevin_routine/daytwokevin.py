import random
from categories.back_movements import vert_pull_movements
from categories.back_movements import horzaontal_row_movements_axel
from categories.back_movements import horzontal_row_movements
from categories.back_movements import trap_movements
from categories.shoulders_movements import rear_delt_movements
from categories.shoulders_movements import side_delt_movements
from categories.shoulders_movements import front_delt_movements
from setsreps import main_rep_range
from setsreps import secondary_rep_range
from setsreps import fail_rep_range
from setsreps import all_ranges
from intensity import intensity_techniques
from intensity import superset

def kevindaytwo():
    #make random selections
    vert_pull_movement_rand = random.choice(vert_pull_movements)
    horzontal_row_movement_rand = random.choice(horzontal_row_movements)
    horzontal_row_movement_axel_rand = random.choice(horzaontal_row_movements_axel)
    trap_movement_rand = random.choice(trap_movements)
    side_movement_rand = random.choice(side_delt_movements)
    front_movement_rand = random.choice(front_delt_movements)
    rear_movement_rand = random.choice(rear_delt_movements)
    main_rep_range_rand = random.choice(main_rep_range)
    secondary_rep_range_rand = random.choice(secondary_rep_range)
    all_ranges_rand = random.choice(all_ranges)
    intensity_techiques_rand_day_1 = random.choice(intensity_techniques)
    intensity_techiques_rand_day_2 = random.choice(intensity_techniques)
    superset_rand = random.choice(superset)


    side_or_rear_delt_focus = input("Do you want to focus side or rear delts? \n 1. Side \n 2. Rear \n\n")
    axel_or_not = input("Do you want to a axel movement? \n 1. Yes \n 2. No \n\n")

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

    if axel_or_not == "1":
           print("5. ",horzontal_row_movement_axel_rand,main_rep_range_rand)
    else:
           print("5. ",horzontal_row_movement_rand,all_ranges_rand, intensity_techiques_rand_day_1)
    #if hamsting_variation == "1" and horzontal_row_movement_rand == "Chest Supported Dumbbell Row" or horzontal_row_movement_rand == "Dumbbell Row" or  horzontal_row_movement_rand == "Low Cable Row":
     #       print("5. ",horzontal_row_movement_rand,secondary_rep_range_rand,intensity_techiques_rand_day_2)
    #elif hamsting_variation == "2":
     #       print("5. ",horzontal_row_movement_axel_rand,main_rep_range_rand)
    #else: print("5. ",horzontal_row_movement_rand,main_rep_range_rand,intensity_techiques_rand_day_2)

    print("\n")