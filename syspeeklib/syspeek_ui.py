from rich.table import Table
from rich import print
from rich.console import Console
console = Console()

def clear():
    
    import os
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def initial_table(computer_infos) -> str:
    
    # Format the information for display
    os_str = str(f'{computer_infos['OS']['System']} {computer_infos['OS']['Release']}')
    cpu_str = str(computer_infos['CPU']['Brand'])
    ram_str = f"{computer_infos['RAM']['Rounded Total']:.2f} GB"
    disk_str = f"{computer_infos['DISK']['Rounded Total']:.2f} GB"
    gpu_str = str(computer_infos['GPU']['Name'])

    table = Table(title="SysPeek - System Information", style="bold blue on blue")
    
    table.add_column("Component", style="cyan on blue", no_wrap=True)
    table.add_column("Details", style="yellow on white")
    
    rows = [('Operating System', os_str), ('CPU', cpu_str), ('RAM', ram_str), ('Disk', disk_str), ('GPU', gpu_str)]
        
    for label, values in rows:
        table.add_row(label, values)

    return table


def os_table(computer_infos) -> str:
    
    # Format the information for display
    os_system = str(f'{computer_infos['OS']['System']}')
    os_release = str(f'{computer_infos['OS']['Release']}')
    os_version = str(f'{computer_infos['OS']['Version']}')
    os_node = str(f'{computer_infos['OS']['Node']}')
    os_machine = str(f'{computer_infos['OS']['Machine']}')

    table = Table(title="SysPeek - Operating System", style="bold blue on blue")
    
    table.add_column("Component", style="cyan on blue", no_wrap=True)
    table.add_column("Details", style="yellow on white")
    
    rows = [('System', os_system), ('Release', os_release), ('Version', os_version), ('Node', os_node), ('Machine', os_machine)]
        
    for label, values in rows:
        table.add_row(label, values)

    return table


def loading(segs_total=1, loading_atualizations=100, description='Loading...'):
    
    from rich.progress import track
    from rich.console import Console
    from time import sleep
    
    console = Console()
    
    segs_per_atualization = segs_total / loading_atualizations
    
    for i in track(range(loading_atualizations), description=description):
        sleep(segs_per_atualization)
    console.clear()


def command_line(computer_infos):
    
    from syspeeklib import interpreter
    from os import system
    
    global console
    screen = initial_table(computer_infos)
    
    while True:    
        console.print('\n>>>', style='bold white on blue', end='')
        command = input(' ').strip()
        available_command = interpreter.user_command_in_commands_list(command)
    
        if available_command:
            clear()
            if command == 'exit':
                quit()
            elif command == 'goto home':
                screen = initial_table(computer_infos)
                console.print(screen, justify='center')
            elif command == 'goto os':
                screen = os_table(computer_infos)
                console.print(screen, justify='center')
        else:
            clear()
            console.print(screen, justify='center')
            console.print('\n[bold red]Invalid command (type help for help)[/]')
