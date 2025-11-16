def Main():
    running = True

    while running:
        print("Hello\n"
              "Please Select an Operation:\n"
              "1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Divide\n"
              )

        choice = int(input("Choice 1-4: "))

        if choice == 1:
            op = "Add"
        elif choice == 2:
            op = "Subtract"
        elif choice == 3:
            op = "Multiply"
        elif choice == 4:
            op = "Divide"
        else:
            print("Invalid choice!")
            continue

        n1 = int(input(f"Enter the first number to {op}: "))
        n2 = int(input(f"Enter the second number to {op}: "))

        if choice == 1:
            final = n1 + n2
        elif choice == 2:
            final = n1 - n2
        elif choice == 3:
            final = n1 * n2
        elif choice == 4:
            final = n1 / n2

        print(f"It Equals: {final}")

        done = input("Are you done? YES/NO: ").strip().lower()

        if done == "yes":
            running = False
        else:
            running = True


Main()
