tasks = (
    "Morning Run",
    "College Attendance",
    "College Subjects Revision",
    "Family Calls",
    "Coding"
)

completed_tasks = []
incomplete_tasks = []

for task in tasks:
    print("----------------")
    print(task)
    response = input("Did you complete this task? (yes/no): ").lower()

    if response == "yes":
        completed_tasks.append(task)
        print("Task completed")
    else:
        incomplete_tasks.append(task)
        print("Task not completed")

print("\n------- SUMMARY -------")
print("Completed tasks:")

for task in completed_tasks:
    print("-", task)

print()

print("Incomplete tasks")
for taskss in incomplete_tasks:
    print("-", taskss)

print(f"\nTotal completed: {len(completed_tasks)} / {len(tasks)}")
print((len(completed_tasks)/len(tasks))*100, "% tasks completed")
        


    