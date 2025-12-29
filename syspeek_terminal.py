def main():
    from rich import print
    from syspeeklib import simple_pc_infos

    # Retrieve simple operating system information
    computer_infos = {'OS': simple_pc_infos.get_simple_os_info()}

    # Display name and release of the operating system
    os_infos = computer_infos['OS']
    os_name = f"{os_infos['System']} {os_infos['Release']}"

    # Print the operating system information using rich formatting
    print(f'[bold yellow]Operating System:[/bold yellow][green] {os_name}[/green]')
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
