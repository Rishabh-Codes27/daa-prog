def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towers_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, source, destination)

# Main code to execute for different number of disks
if __name__ == "__main__":
    for disks in range(1, 5):  # Test for 1 to 4 disks
        print(f"\nSolving Towers of Hanoi for {disks} disk(s):")
        towers_of_hanoi(disks, 'A', 'B', 'C')
