# ABRSM Grade 5 Trumpet Scales Generator

import random

scales = [
    "B major scale, range: a 12th (up to F sharp)",
    "C major scale, range: a 12th (up to G)",    
    "D flat major scale, range: a 12th (up to A flat)",
    "G major scale, range: 2 octaves",
    "B flat harmonic minor scale, range: a 12th (up to F)",
    "C sharp harmonic minor scale, range: a 12th (up to G sharp)",       
    "F harmonic minor scale, range: one octave and down to the dominant",
    "G harmonic minor scale, range: 2 octaves",
    
    "Chromatic scale starting on G, 2 octaves",
    "Whole-tone scale starting on G, 2 octaves",
    
    "B major arpeggio, range: a 12th (up to F sharp)",
    "C major arpeggio, range: a 12th (up to G)",    
    "D flat major arpeggio, range: a 12th (up to A flat)",
    "G major arpeggio, range: 2 octaves",
    "B flat minor arpeggio, range: a 12th (up to F)",
    "C sharp minor arpeggio, range: a 12th (up to G sharp)",       
    "F minor arpeggio, range: one octave and down to the dominant",
    "G minor arpeggio, range: 2 octaves",
    
    "Dominant seventh of C, 2 octaves",
    "Dominant seventh of D flat, 2 octaves",
    "Diminished seventh starting on G, 2 octaves",
]

random.shuffle(scales)

print("Welcome to the random scale generator for grade 5 trumpet.\n")

for i, scale in enumerate(scales):
    scale += ', ' + random.choice(['tongued', 'slurred'])

    # Replace commas with line breaks
    scale = scale.replace(', ', '\n')

    input("\nPress Enter to generate the next scale: ")
    
    print(scale)
    print(f"\nYou have played {i+1} scale(s).\nYou have {len(scales)-(i+1)} scale(s) still to play.\n")

print("\nWell done! You have finished your trumpet scales for today!")
