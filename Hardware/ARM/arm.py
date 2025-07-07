# Given values
total_persons = 25
play_hockey = 15
play_football = 17
play_both = 10

# Calculate the number of persons playing at least one sport (hockey OR football)
# Using the principle of inclusion-exclusion:
# |A U B| = |A| + |B| - |A intersection B|
play_at_least_one = play_hockey + play_football - play_both

# Calculate the number of persons playing neither sport
# Neither = Total - (Persons playing at least one)
play_neither = total_persons - play_at_least_one

print(f"Total persons in the room: {total_persons}")
print(f"Persons playing hockey: {play_hockey}")
print(f"Persons playing football: {play_football}")
print(f"Persons playing both hockey and football: {play_both}")
print("\n")
print(f"Persons playing at least one sport (Hockey OR Football): {play_at_least_one}")
print(f"Persons playing neither hockey nor football: {play_neither}")


