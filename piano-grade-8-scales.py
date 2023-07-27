# ABRSM Grade 8 Piano Scales Generator

import random

scales = [
    "C major, similar motion scale, 4 octaves",
    "E flat major, similar motion scale, 4 octaves",
    "F sharp major, similar motion scale, 4 octaves",
    "A major, similar motion scale, 4 octaves",
    "C harmonic minor, similar motion scale, 4 octaves",
    "E flat harmonic minor, similar motion scale, 4 octaves",
    "F sharp harmonic minor, similar motion scale, 4 octaves",
    "A major harmonic minor, similar motion scale, 4 octaves",
    "C melodic minor, similar motion scale, 4 octaves",
    "E flat melodic minor, similar motion scale, 4 octaves",
    "F sharp melodic minor, similar motion scale, 4 octaves",
    "A major melodic minor, similar motion scale, 4 octaves",
    "C major, scale a sixth apart, 4 octaves",
    "E flat major, scale a sixth apart, 4 octaves",
    "F sharp major, scale a sixth apart, 4 octaves",
    "A major, scale a sixth apart, 4 octaves",
    "C harmonic minor, scale a sixth apart, 4 octaves",
    "E flat harmonic minor, scale a sixth apart, 4 octaves",
    "F sharp harmonic minor, scale a sixth apart, 4 octaves",
    "A major harmonic minor, scale a sixth apart, 4 octaves",
    "C major, contrary motion scale, 2 octaves",
    "E flat major, contrary motion scale, 2 octaves",
    "F sharp major, contrary motion scale, 2 octaves",
    "A major, contrary motion scale, 2 octaves",
    "C harmonic minor, contrary motion scale, 2 octaves",
    "E flat harmonic minor, contrary motion scale, 2 octaves",
    "F sharp harmonic minor, contrary motion scale, 2 octaves",
    "A major harmonic minor, contrary motion scale, 2 octaves",
    "E flat major, legato scale in thirds, 2 octaves, legato, right hand",
    "E flat major, legato scale in thirds, 2 octaves, legato, left hand",
    "C major, staccato scale in sixths, 2 octaves, right hand",
    "C major, staccato scale in sixths, 2 octaves, left hand",
    "Chromatic scale a major sixth apart, starting on E flat in the LH and C in the RH, 4 octaves, hands together",
    "Whole-tone scale starting on E flat, 4 octaves, hands together",
    "Whole-tone scale starting on C, 4 octaves, hands together",
    "C major arpeggio, 4 octaves, legato, hands together, second inversion",
    "E flat major arpeggio, 4 octaves, legato, hands together, second inversion",
    "F sharp major arpeggio, 4 octaves, legato, hands together, second inversion",
    "A major arpeggio, 4 octaves, legato, hands together, second inversion",
    "C minor arpeggio, 4 octaves, legato, hands together, second inversion",
    "E flat minor arpeggio, 4 octaves, legato, hands together, second inversion",
    "F sharp minor arpeggio, 4 octaves, legato, hands together, second inversion",
    "A minor arpeggio, 4 octaves, legato, hands together, second inversion",
    "Dominant seventh of C, 4 octaves, legato, hands together",
    "Dominant seventh of E flat, 4 octaves, legato, hands together",
    "Dominant seventh of F sharp, 4 octaves, legato, hands together",
    "Dominant seventh of A, 4 octaves, legato, hands together",
    "Diminished seventh starting on E flat, 4 octaves, legato, hands together",
    "Diminished seventh starting on C, 4 octaves, legato, hands together",
]

random.shuffle(scales)

print("Welcome to the random scale generator for grade 8 piano.\n")

for i, scale in enumerate(scales):
    if 'staccato' not in scale and 'legato' not in scale:
        scale += ', ' + random.choice(['staccato', 'legato'])

    # Replace commas with line breaks
    scale = scale.replace(', ', '\n')

    input("\nPress Enter to generate the next scale: ")
    
    print(scale)
    print(f"\nYou have played {i+1} scale(s).\nYou have {len(scales)-(i+1)} scale(s) still to play.\n")

print("\nWell done! You have finished your piano scales for today!")
