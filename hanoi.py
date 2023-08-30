# Tower of Hanoi game in Python

def hanoi(n, source, dest, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return
    hanoi(n-1, source, aux, dest)
    print(f"Move disk {n} from {source} to {dest}") 
    hanoi(n-1, aux, dest, source)

n = 3
hanoi(n, 'A', 'C', 'B')