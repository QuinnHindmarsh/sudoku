from solve import Solve
from random import randomint

# Place a certain amount of random numbers in grid
# Solve
# Remove 4 at a time from the start, then closer to the end only 2 at a time. check for more then one solution after each set of removal
# If ever more then one solution, undo move
# Before checking the solution count check if it conforms to certain rules. at least 8 unique nums. + distabuition rules

# If it gets to 27 with these rules being correct, return this
