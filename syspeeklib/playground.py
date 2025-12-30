import interpreter

while True:
    command = input()
    command = interpreter.user_command_in_commands_list(command)

    print(command)
