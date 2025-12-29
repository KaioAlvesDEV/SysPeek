def main():
    
    from rich import print
    from syspeeklib import simple_pc_infos

    # Retrieve simple operating system information
    computer_infos = {'OS': simple_pc_infos.get_simple_os_info(), 
                      'CPU': simple_pc_infos.get_simple_cpu_info()}

    # Display name and release of the operating system
    os_infos = computer_infos['OS']
    os_name = f"{os_infos['System']} {os_infos['Release']}"
    
    # Display CPU brand
    cpu_brand = computer_infos['CPU']['Brand']
    
    print(f'[bold blue]Operating System:[/bold blue][yellow] {os_name}[/yellow]')
    print(f'[bold blue]Processor:[/bold blue][yellow] {cpu_brand}[/yellow]')
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
