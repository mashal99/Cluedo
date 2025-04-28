from solution.solution import random_solution

def main():
    print("Welcome to Cluedo! (Part 1 setup)")
    solution = random_solution()
    # In a real game you'd hide this; here it just demonstrates that setup works.
    print("DEBUG ➞ murder solution:", solution)

if __name__ == "__main__":
    main()
