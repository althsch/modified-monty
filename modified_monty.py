import random
from tqdm import tqdm

contains = 0
outside = 0
for i in tqdm(range(10000000)):
    containers = [False for i in range(4)]
    # is inside
    if random.random() < .2:
        outside+=1
        continue

    containers[random.randrange(len(containers))] = True

    # randomly open 3
    for i in range(3):
        containers.pop(random.randrange(len(containers)))

    # if final container contains
    if containers[0]:
        contains+=1
        continue

total = outside+contains
print(f"outside: {outside}")
print(f"contains: {contains}")
print(f"percentage inside: {contains/total}")
