from categories.quad_movements import quad_movements
from categories.quad_movements import secondary_quad_movements
from categories.hamstring_movements import ham_curl_movements
from categories.hip_hinge_movements import hip_hinge_movements
from categories.calf_movements import calf_movements
from setsreps import main_rep_range
from setsreps import secondary_rep_range
from setsreps import all_ranges
from intensity import intensity_techniques
import random

def kevindayone():
     # Make random selections
    quad_movements_rand = random.choice(quad_movements)
    secondary_quad_movement_rand = random.choice(secondary_quad_movements)
    ham_curl_movements_rand = random.choice(ham_curl_movements)
    hip_hinge_movements_rand = random.choice(hip_hinge_movements)
    calf_movements_rand = random.choice(calf_movements)
    main_rep_range_rand = random.choice(main_rep_range)
    secondary_rep_range_rand = random.choice(secondary_rep_range)
    all_ranges_rand = random.choice(all_ranges)
    intensity_techniques_rand = random.choice(intensity_techniques)

    # User input
    hamstring_variation = input("Do you want to hip hinge or Leg Curl: \n 1. Hip Hinge \n 2. Leg Curl \n\n")
    squat_variation = input("Can you barbell squat: \n 1. Yes \n 2. No \n\n")

    # Print Day 1 routine
    print("Day 1 routine: \n")

    if hamstring_variation == "2":
        print("1. ", ham_curl_movements_rand, secondary_rep_range_rand, intensity_techniques_rand)
    elif hamstring_variation == "1" and hip_hinge_movements_rand == "Dumbbell RDL":
        print("1. ", hip_hinge_movements_rand, secondary_rep_range_rand, intensity_techniques_rand)
    else:
        print("1. ", hip_hinge_movements_rand, main_rep_range_rand)

    if squat_variation == "1":
        print("2. ", quad_movements_rand, main_rep_range_rand)
    else:
        print("2. ", secondary_quad_movement_rand, secondary_rep_range_rand, intensity_techniques_rand)

    print("3. ", secondary_quad_movement_rand, secondary_rep_range_rand, intensity_techniques_rand)
    print("4. ", calf_movements_rand, all_ranges_rand, intensity_techniques_rand)

    print("\n")
    

