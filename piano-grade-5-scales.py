# ABRSM Grade 5 Piano Scales Generator

import random

scales = [
    "A major, similar motion scale, 2 octaves, hands together, legato",
    "E major, similar motion scale, 2 octaves, hands together, legato",
    "B major, similar motion scale, 2 octaves, hands together, legato",
    "F sharp major, similar motion scale, 2 octaves, hands together, legato",
    "D flat major, similar motion scale, 2 octaves, hands together, legato",
    "F sharp harmonic minor, similar motion scale, 2 octaves, hands together, legato",
    "C sharp harmonic minor, similar motion scale, 2 octaves, hands together, legato",
    "G sharp harmonic minor, similar motion scale, 2 octaves, hands together, legato",
    "E flat harmonic minor, similar motion scale, 2 octaves, hands together, legato",  
    "B flat harmonic minor, similar motion scale, 2 octaves, hands together, legato",  
    
    "A flat major, staccato scale, 2 octaves, right hand",
    "A flat major, staccato scale, 2 octaves, left hand",
    "F harmonic minor, staccato scale, 2 octaves, right hand",
    "F harmonic minor, staccato scale, 2 octaves, left hand",

    "D flat major, contrary motion scale, 2 octaves, hands together, legato",
    "C sharp harmonic minor, contrary motion scale, 2 octaves, hands together, legato",
    
    "Chromatic contrary motion scale, starting on F sharp in the LH and A sharp in RH, 2 octaves, hands together, legato"
    
    "A major arpeggio, 2 octaves, legato, hands together",
    "E major arpeggio, 2 octaves, legato, hands together",
    "B major arpeggio, 2 octaves, legato, hands together",
    "F sharp major arpeggio, 2 octaves, legato, hands together",
    "A flat major arpeggio, 2 octaves, legato, hands together",
    "D flat major arpeggio, 2 octaves, legato, hands together",
    "F sharp minor arpeggio, 2 octaves, legato, hands together",
    "C sharp minor arpeggio, 2 octaves, legato, hands together",
    "G sharp minor arpeggio, 2 octaves, legato, hands together",
    "E flat arpeggio, 2 octaves, legato, hands together",
    "F minor arpeggio, 2 octaves, legato, hands together",
    "B flat minor arpeggio, 2 octaves, legato, hands together",
    
    "Diminished seventh starting on B, 2 octaves, legato, right hand",
    "Diminished seventh starting on B, 2 octaves, legato, left hand",
]

random.shuffle(scales)

print("Welcome to the random scale generator for grade 5 piano.\n")

for i, scale in enumerate(scales):

    # Replace commas with line breaks
    scale = scale.replace(', ', '\n')

    input("\nPress Enter to generate the next scale: ")
    
    print(scale)
    print(f"\nYou have played {i+1} scale(s).\nYou have {len(scales)-(i+1)} scale(s) still to play.\n")

print("\nWell done! You have finished your piano scales for today!")
