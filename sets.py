# sets & set methods
# mutable
# cannot have duplicates
# sorted automatically by python
# for most set methods, order matters

set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}

# .union() and | operand return  combination of sets
# sets not altered, dulpicates disgarded
print(set1.union(set2))

print(set1 | set2)

# .difference(*args) returns new set with elements not in *args
# - operand achieves the same result
print(set1.difference(set2))

print(set2.difference(set1))

print(set1 - set2)

# .symmetric_difference() or ^ operand returns new set of elements unique to each set

print(set1.symmetric_difference(set2))
print(set1 ^ set2)

# .intersection() or & operand returns new set of common elements between sets

print(set1.intersection(set2))
print(set2 & set1)
