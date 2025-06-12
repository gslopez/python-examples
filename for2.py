# 4 different ways to iterate over a list of dictionaries

tasks = [
    {"title": "Task 1", "description": "Description of Task 1", "state": False},
    {"title": "Task 2", "description": "Description of Task 2", "state": True},
    {"title": "Task 3", "description": "Description of Task 3", "state": False},
]

idx = 0
# 1. Using a while loop
while idx < len(tasks):
    print(tasks[idx])
    idx += 1

# 2. Using a for loop with range
for i in range(len(tasks)):
    print(tasks[i])

# 3. Using a for loop directly on the list
for i in range(len(tasks)):
    task = tasks[i]
    print(task)

# 4. Using a for loop with unpacking
for task in tasks:
    print(task)

