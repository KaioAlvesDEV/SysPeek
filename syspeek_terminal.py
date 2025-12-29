def main():
    
    from syspeeklib import simple_pc_infos, syspeek_ui
    from rich import print
    
    # Retrieve simple operating system information
    computer_infos = {'OS': simple_pc_infos.get_simple_os_info(), 
                      'CPU': simple_pc_infos.get_simple_cpu_info(),
                      'RAM': simple_pc_infos.get_simple_memory_info(),
                      'DISK': simple_pc_infos.get_simple_disk_info(),
                      'GPU': simple_pc_infos.get_simple_gpu_info()}
    
    
    syspeek_ui.loading(1.2, 25)
    
    print(syspeek_ui.initial_table(computer_infos))
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
