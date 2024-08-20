
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

def findChords(notes: Set[int]):
    major = []
    minor = []
    for root in notes:
        if (root+7)%12 in notes:
            if (root+4)%12 in notes:
                major.append(root)
            if (root+3)%12 in notes:
                minor.append(root)
    return [major, minor]
    

def solve(tuning: List[int], changes: List[List[int]], numbers:bool):
    strings = tuning
    for change in changes:
        strings = apply(strings, change)


    notes = sorted(set(strings))
    chords = findChords(notes)

    space = 20

    # Print formatted output
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
                    f"{col4} {' ' * (space - len('third final field:'))} major: {chords[0]}, minor: {chords[1]}")        
    else:
        formatted_string = (
                f"{col1}{' ' * (space - len(col1))}{toNames(tuning)}\n"
                f"{col2}{' ' * (space - len(col2))}{toNames(strings)}\n"
                f"{col3} {' ' * (space - len(col3))}{toNames(notes)}\n"
                f"{col4}{' ' * (space - len(col4))} major: {[Names(x).name for x in chords[0]]}, minor: {[Names(x).name for x in chords[1]]}")
        
    print(formatted_string)

tuning = [7, 10,0, 2, 4, 7, 0, 4, 11,2]
a =      [2, 0, 0, 0, 0, 2, 0, 0, 0, 0]
b =      [0, 0, 0, 0, 1, 0, 0, 1, 0, 0]
c =      [0, 0, 0, 0, 0, 2, 2, 0, 0, 0]
etuning = (transpose(tuning, 4))

solve(tuning, [c,b], False)