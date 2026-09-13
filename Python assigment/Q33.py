# Write a program to check if two sets are disjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}

if set1.isdisjoint(set2):
    print("Sets are disjoint (no common elements).")
else:
    print("Sets are not disjoint (they share elements).")
