# hanoi_tower_problem.py
def hanoi_tower(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi_tower(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi_tower(n-1, auxiliary, target, source)

if __name__ == "__main__":
    n = int(input("Enter number of disks: "))
    hanoi_tower(n, 'A', 'C', 'B')
