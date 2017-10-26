import Tkinter
import tkFileDialog
import os
from bisect import bisect_right

offset = 25


def find_gt(a, x):
    """Find leftmost value greater than x"""
    x = bisect_right(a, x)
    if x != len(a):
        return a[x]
    raise ValueError

left_extruder = 'T0'
right_extruder = 'T1'

left_locations = []
right_locations = []


root = Tkinter.Tk()
root.withdraw()  # use to hide tkinter window

currdir = os.getcwd()
file_path = tkFileDialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
# g_file = open(file_path, 'r')
with open(file_path, "r") as f:
    data = [l.strip() for l in f.readlines()]
# print data[217]

for i in range(0, len(data)):
    if str(data[i]) == left_extruder:
        left_locations.append(i)
    elif data[i] == right_extruder:
        right_locations.append(i)

ranges_to_change = []

for i in left_locations:
    ranges_to_change.append([i, find_gt(right_locations, i)])

for i in ranges_to_change:
    print('a')
    pos = i[0]
    for line in data[i[0]: i[1]]:

        if 'X' in line:
            start = line.find('X') + 1
            print start
            end = line.find(' ', start)
            val = float(line[start:end])
            val -= 25
            data[pos] = line[0:start] + str(val) + line[end:]
            print(line)
            print(data[pos])
        pos += 1

with open('output.gcode', "w") as f:
    for line in data:
        f.write(line + '\n')
# print(left_locations)
# print(right_locations)
