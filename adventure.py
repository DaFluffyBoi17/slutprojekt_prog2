start_input = input(""" please choose an option
1. start
2. quit
3. secret, shh    """)

if start_input == "1":
    print("starting")

if start_input == "2":
    quit

if start_input == "3":
    secret_code = input("input secret code ")

else:
    print("incorrect input")