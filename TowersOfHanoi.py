from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks
stacks = []

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.extend([left_stack, middle_stack, right_stack])


# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_optimal_moves = 2**num_disks - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")


# Get User Input
def get_input():
    choices = {i.get_name()[0]: i for i in stacks}
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = list(choices.keys())[i]
            print(f"Enter {letter} for {name}")
        user_input = input().upper()
        if user_input in choices:
            return choices[user_input]


# Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for i in range(len(stacks)):
        print(stacks[i].print_items())

    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        if from_stack.is_empty():
            print(
                f"\n\nInvalid Move. {from_stack.get_name()} stack is empty. Try Again"
            )
            continue

        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        if to_stack.peek() and from_stack.peek() > to_stack.peek():
            print("\n\nInvalid Move. Try Again")
            continue

        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves += 1
        break

print("\n\n\n...Current Stacks...")
for i in range(len(stacks)):
    print(stacks[i].print_items())

print(
    f"You finished with {num_user_moves} moves\nOptimal number of moves is {num_optimal_moves}"
)

if num_user_moves == num_optimal_moves:
    print("Congradulations you finished with optimal number of moves")
