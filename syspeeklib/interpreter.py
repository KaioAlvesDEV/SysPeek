def cut_string_in_two(string):
    
    string = string.strip().split()
    if len(string) > 2 or len(string) < 1:
        return -1
    return string

def commands_list() -> dict:
    return {
        'goto': ('os', 'cpu', 'ram', 'disk', 'gpu'),
        'exit': ()
    }

def user_command_in_commands_list(user_command) -> bool:
    
    user_command = cut_string_in_two(user_command) 
    available_commands = commands_list()
    
    if user_command == -1:
        return False
    
    user_command_is_in_available_commands = False
    user_command_is_in_available_subcommands = False
    
    for key in available_commands:
        if user_command[0] == key:
            user_command_is_in_available_commands = True
            break
    
    if not user_command_is_in_available_commands:
        return False
    
    if not available_commands[user_command[0]]:
        if len(user_command) == 1:
            return True
        else:
            return False

    for value in available_commands[user_command[0]]:
        try:
            if user_command[1] == value:
                user_command_is_in_available_subcommands = True
                break
        except IndexError:
            return False
    
    return user_command_is_in_available_subcommands
