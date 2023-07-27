# ABRSM Grade 5 Flute Scales Generator

import random

scales = [
    "C major scale, 2 octaves",
    "D major scale, 2 octaves",
    "E major scale, 2 octaves",
    "A flat major scale, 2 octaves",
    "A major scale, 2 octaves",
    
    "C minor scale, 2 octaves",
    "E minor scale, 2 octaves",
    "F minor scale, 2 octaves",
    "F sharp minor scale, 2 octaves",
    "A minor scale, 2 octaves",
    
    "Chromatic scale, starting on C sharp, 2 octaves",
    "Chromatic scale, starting on F, 2 octaves",
    
    "C major arpeggio, 2 octaves",
    "D major arpeggio, 2 octaves",
    "E major arpeggio, 2 octaves",
    "A flat major arpeggio, 2 octaves",
    "A major arpeggio, 2 octaves",
    
    "C minor arpeggio, 2 octaves",
    "E minor arpeggio, 2 octaves",
    "F minor arpeggio, 2 octaves",
    "F sharp minor arpeggio, 2 octaves",
    "A minor arpeggio, 2 octaves",
    
    "Dominant seventh of A, 2 octaves, resolving on the tonic",
    "Dominant seventh of B flat, 2 octaves, resolving on the tonic",
    
    "Diminished seventh starting on E flat, 2 octaves",
]

random.shuffle(scales)

print("Welcome to the random scale generator for grade 5 flute.\n")

for i, scale in enumerate(scales):
    scale += ', ' + random.choice(['tongued', 'slurred'])

    # Replace commas with line breaks
    scale = scale.replace(', ', '\n')

    input("\nPress Enter to generate the next scale: ")
    
    print(scale)
    print(f"\nYou have played {i+1} scale(s).\nYou have {len(scales)-(i+1)} scale(s) still to play.\n")

print("\nWell done! You have finished your flute scales for today!")
