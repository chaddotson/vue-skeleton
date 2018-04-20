
c = None

with open("dependency_tree.txt", "r") as f:
    c = f.readlines()

if c is None:
    exit()
from collections import Counter

def parse(lines, current_index, current_depth, tracker):

    
    line = lines[current_index]



    count = Counter(line)

    depth = count.get("|", 0) + count.get("├", 0) + count.get("└", 0)

    if(current_depth < depth):
        parse(lins, current_index)

    print(depth)


tracker = []

parse(c, 0, 0, tracker)
