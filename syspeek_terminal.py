# NOTE: This entire code is temporary and will be completely rewritten later.

def main():
    
    from rich import console
    from syspeeklib import simple_pc_infos

    console = console.Console()
    
    # Retrieve simple operating system information
    computer_infos = {'OS': simple_pc_infos.get_simple_os_info(), 
                      'CPU': simple_pc_infos.get_simple_cpu_info()}

    # Display name and release of the operating system
    os_infos = computer_infos['OS']
    os_name = f"{os_infos['System']} {os_infos['Release']}"
    
    # Display CPU brand
    cpu_brand = computer_infos['CPU']['Brand']
    
    console.print(f'Operating System:', style=f'bold white on blue', end=''); console.print('', os_name, style='yellow')
    console.print(f'Processor:', style=f'bold white on blue', end=''); console.print('', cpu_brand, style='yellow')
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
