def logical_and(a, b):
    return a and b

def logical_or(a, b):
    return a or b

def logical_not(a):
    return not a

def implication(a, b):
    return not a or b

def biconditional(a, b):
    return a == b

def get_user_input():
    try:
        a = int(input("Enter value for A (0 or 1): "))
        b = int(input("Enter value for B (0 or 1): "))
        if a not in [0, 1] or b not in [0, 1]:
            raise ValueError
        return bool(a), bool(b)
    except ValueError:
        print("Invalid input! Please enter 0 or 1.")
        return get_user_input()

def display_results(a, b):
    print(f"\nResults for A = {a}, B = {b}")
    print(f"A AND B: {logical_and(a, b)}")
    print(f"A OR B: {logical_or(a, b)}")
    print(f"NOT A: {logical_not(a)}")
    print(f"A => B: {implication(a, b)}")
    print(f"A <=> B: {biconditional(a, b)}")
    print()

def generate_truth_table():
    print("Truth Table")
    print("A B | AND OR NOT_A A=>B A<=>B")
    print("-------------------------------")
    for a in [True, False]:
        for b in [True, False]:
            print(f"{int(a)} {int(b)} |  {int(logical_and(a, b))}   {int(logical_or(a, b))}    {int(logical_not(a))}     {int(implication(a, b))}     {int(biconditional(a, b))}")
    print()

def main():
    while True:
        mode = input("Choose mode: (1) User Input, (2) Truth Table, (q) Quit: ").strip()
        if mode == '1':
            a, b = get_user_input()
            display_results(a, b)
        elif mode == '2':
            generate_truth_table()
        elif mode.lower() == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
