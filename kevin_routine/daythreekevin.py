from categories.chest_movements import main_chest_movements
from categories.fly_movements import fly_movements
from categories.arm_movements import bicep_movements
from categories.arm_movements import tricep_movements
from setsreps import main_rep_range
from setsreps import secondary_rep_range
from setsreps import all_ranges
from intensity import intensity_techniques
import random

def kevindaythree():
    # Make random selections
    chest_rand = random.choice(main_chest_movements)
    fly_rand = random.choice(fly_movements)
    bicep_rand = random.choice(bicep_movements)
    tricep_rand = random.choice(tricep_movements)
    main_rep_range_rand = random.choice(main_rep_range)
    secondary_rep_range_rand = random.choice(secondary_rep_range)
    all_ranges_rand = random.choice(all_ranges)
    intensity_techniques_rand = random.choice(intensity_techniques)

    # Chest and Arms Print
    print("Day 3 routine: \n")
    print("1. ", chest_rand, main_rep_range_rand, intensity_techniques_rand)
    print("2: ", fly_rand, secondary_rep_range_rand, intensity_techniques_rand)
    print("3. ", bicep_rand, all_ranges_rand, intensity_techniques_rand)
    print("4. ", tricep_rand, all_ranges_rand, intensity_techniques_rand)
    print("\n")
    

