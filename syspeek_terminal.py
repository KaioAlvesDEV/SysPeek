from syspeeklib import pc_infos

def main():
    
    from syspeeklib import syspeek_ui
    from rich import print
    from rich.console import Console
    console = Console()
    
    # Retrieve simple operating system information
    computer_infos = {
                      'OS':   pc_infos.get_os_info(), 
                      'CPU':  pc_infos.get_cpu_info(),
                      'RAM':  pc_infos.get_memory_info(),
                      'DISK': pc_infos.get_disk_info(),
                      'GPU':  pc_infos.get_gpu_info()
                      }
     
    
    syspeek_ui.loading(1.2, 25)
    
    console.print(syspeek_ui.initial_table(computer_infos), justify='center')
    syspeek_ui.command_line(computer_infos)

if __name__ == "__main__":
    main()
