#START Question num 1
positive_count = 0
negative_count = 0
zero_count = 0
div_by_7_count = 0
last_positive = None
last_negative = None

for i in range(10):
    number: int = int(input("Enter a number: "))

    if number == -9999:
        break

    if number > 1000 or number < -1000:
        continue

    if number > 0:
        positive_count += 1
        last_positive = number
    elif number < 0:
        negative_count += 1
        last_negative = number
    elif number == 0:
        zero_count += 1

    if number % 7 == 0 and number != 0:
        div_by_7_count += 1
else:
    print(f"Positive numbers:{positive_count}")
    print(f"Negative numbers: {negative_count}")
    print(f"Zero numbers: {zero_count}")
    print(f"Numbers divisible by 7: {div_by_7_count}")
    print(f"Last positive number: {last_positive}")
    print(f"Last negative number: {last_negative}")
#END

#START Question num 2
world_record = 6.23
good_jumps_count = 0
total_good_jumps = 0
highest_jump = 0
world_record_holder = None
world_record_jump = None

for i in range(7):
    try:
        jump_result: float = float(input(f"Enter the result of the jump for country number {i + 1}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if jump_result < 5.80:
        continue

    good_jumps_count += 1
    total_good_jumps += jump_result

    if jump_result > highest_jump:
        highest_jump = jump_result

    if jump_result > world_record:
        world_record_holder = input("The world record is broken! Enter the name of the athlete: ")
        world_record_jump = jump_result

average_good_jumps = total_good_jumps / good_jumps_count if good_jumps_count > 0 else 0

print(f"Number of good jumps: {good_jumps_count}")
print(f"Average of good jumps: {average_good_jumps}")
print(f"Highest jump: {highest_jump}")

if world_record_holder:
    print(f"A new world record was set! {world_record_holder} jumped {world_record_jump} meters.")
else:
    print("No new world record was set.")
#END

#START Question num 3
while True:
    try:
        num: int = int(input("Enter an odd number: "))
        if num % 2 == 1:
            break
        else:
            print("Please enter an odd number.")
    except ValueError:
        print("Please enter a valid number.")

for i in range(1, num + 1, 2):
    spaces = (num - i) // 2
    print(" " * spaces, end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

for i in range(num - 2, 0, -2):
    spaces = (num - i) // 2
    print(" " * spaces, end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()
#END
