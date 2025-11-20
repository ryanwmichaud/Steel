
from enum import Enum
from typing import List, Set


class Names(Enum): 
    C = 0
    CD = 1
    D = 2
    DE = 3
    E = 4
    F = 5
    FG = 6
    G = 7
    GA = 8
    A = 9
    AB = 10
    B = 11




def apply(tuning, change):
    return [(x+y)%12 for (x,y) in zip(tuning, change)]

def transpose(notes, interval):
    return [(x+interval)%12 for x in notes]

def toNames(notes):
    return [Names(x).name for x in notes]

def findChords(notes: Set[int], qualities):
    if not isinstance(notes, set):
        raise TypeError("expected notes to be a set")
    
    results= {
        'major' : [],
        'minor' : [],
        'dim' : [],
        'maj6' : [],
        'min6' : [],
        'min7' : [],
        'hdim' : [],
        'fdim' : [],
        '7' : []
    }

    for root in notes:
        if (root+7)%12 in notes:
            if (root+4)%12 in notes:
                results['major'].append(root)
                if (root+9)%12 in notes:
                    results['maj6'].append(root)
                    results['min7'].append((root+9)%12)
                if (root+10)%12 in notes:
                    results['7'].append(root)
            if (root+3)%12 in notes:
                results['minor'].append(root)
                if (root+9)%12 in notes:
                    results['min6'].append((root))
                    results['hdim'].append((root+9)%12)
        if (root+6)%12 in notes and (root+3)%12 in notes:
            results['dim'].append(root)
            if (root+9)%12 in notes:
                results['fdim'].append(root)

    output = []
    for quality in qualities:
        output.append((quality, results[quality]))
    return output
    

def solve(tuning: list[int], changes: list[list[int]],  qualities:list[str], numbers:bool=False):
    strings = tuning
    for change in changes:
        strings = apply(strings, change)


    notes = set(strings)
    chords = findChords(notes, qualities)

    space = 20

    # print formatted output
    formatted_string =""
    col1 = "old tuning"
    col2 = "new tuning"
    col3 = "notes present"
    col4 = "possible chords"

    if numbers:
        formatted_string = (
                f"{col1} {' ' * (space - len(col1))} {tuning}\n"
                f"{col2} {' ' * (space - len(col2))} {strings}\n"
                f"{col3} {' ' * (space - len(col3))} {notes}\n"
                f"{col4} {' ' * (space - len(col4))} major: {chords[0]}, minor: {chords[1]}, major6: {chords[2]}")        
    else:
        formatted_string = (
                f"{col1}{' ' * (space - len(col1))} {toNames(tuning)}\n"
                f"{col2}{' ' * (space - len(col2))} {toNames(strings)}\n"
                f"{col3} {' ' * (space - len(col3))} {toNames(notes)}"
                )
        
    print(formatted_string)
    for quality in chords:
        if(len(quality[1])!=0):
            print(quality[0], toNames(quality[1]))
    print()

tuning =  [7, 10,0, 2, 4, 7, 0, 4, 11,2]

open =    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

a  =      [2, 0, 0, 0, 0, 2, 0, 0, 0, 0]
b  =      [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
c  =      [0, 0, 0, 0, 0, 2, 2, 0, 0, 0]
ab =      [2, 0, 0, 0, 1, 2, 0, 1, 0, 0]
bc =      [0, 0, 0, 0, 1, 2, 2, 1, 0, 0]

d =       [0, 0,-1, 0, 0, 0,-1, 0, 0, 0]
f =       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0]

g =       [0, 0, 0, 0, 0, -1, 0, 0, 0, 0]
h =       [0, 0, 0, 0, 0, 0, 0, 0,-1, 0]

pedals = [open, a, b, ab, bc]
left_kick  = [open, d, f]
right_kick  = [open, g, h]
etuning = (transpose(tuning, 4))

def brute_force():
    for p in pedals:
        for l in left_kick:
            for r in right_kick:
                print(p, l, r)
                solve(etuning, [p, l, r], ['maj6'])

brute_force()