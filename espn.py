import sys
from calcy import *

#test match
england1,india1,england2 = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
england_total=add(england1, england2)
score_diff=sub(england_total, india1)
runs_required=add(score_diff, 1)
print("runs required to win is:",runs_required)

