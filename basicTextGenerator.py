A = """The operation is complete. The output is as shown above."""

while True:
    print("""
    What would you like to do?

    1) Gradual Text Display
    2) Display Text a Specific Number of Times
    3) Display Text (With Hearts at the Beginning and End)
    4) Exit
    """)

    choice = input("Please select an option: ")
    program_info = f"""

    WELCOME
    This program is designed to perform different tasks based on keyboard inputs.
    Please proceed with the tasks one by one.
    You selected option {choice}.

    """

    if choice == "1":
        print(program_info)
        target_text = input("Please enter a text: ")
        
        def gradual_writer(text):
            for i in range(1, len(text) + 1):
                print(text[:i])
            for i in range(len(text) - 1, 0, -1):
                print(text[:i])

        gradual_writer(target_text)

    elif choice == "2":
        import keyboard
        from time import sleep as wait
        print(program_info)
        repeat_count = int(input("How many times would you like to repeat the text? "))
        text = input("Please enter the text to repeat: ")
        delay = float(input("How many seconds should pass between repetitions? "))
        print("Preparing to run...")
        wait(2)
        
        for i in range(repeat_count):
            keyboard.write(text)
            keyboard.press_and_release('enter')
            wait(delay)
            if keyboard.is_pressed('space'):
                exit()
        print(A)

    elif choice == "3":
        print(program_info)
        target_text = input("Please enter a text: ")

        def vertical_hearts(text):
            heart = "\u2764"
            for char in text:
                print(f"{heart} {char} {heart}")

        vertical_hearts(target_text)

        input(A)

    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        print("Invalid selection. Please choose 1, 2, 3, or 4.")
