def is_safe_state(processes, available, max_demand, allocation):
    n = len(processes)
    m = len(available)

    # Calculate Need matrix
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_sequence = []
    work = available.copy()
    while len(safe_sequence) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]
                safe_sequence.append(f'P{i}')
                finish[i] = True
                allocated = True
                break
        if not allocated:
            break
    if len(safe_sequence) == n:
        print("\n System is in a safe state.")
        print("Safe sequence:", " -> ".join(safe_sequence))
    else:
        print("\n System is NOT in a safe state.")

# Input from User
n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"Process P{i}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Demand Matrix:")
max_demand = []
for i in range(n):
    row = list(map(int, input(f"Process P{i}: ").split()))
    max_demand.append(row)
available = list(map(int, input("\nEnter Available Resources: ").split()))
processes = [f'P{i}' for i in range(n)]

# Run Banker's Algorithm
is_safe_state(processes, available, max_demand, allocation)
