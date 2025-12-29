from rich.table import Table

def initial_table(computer_infos):
    
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

def loading(segs_total=1, loading_atualizations=100, description='Loading...'):
    
    from rich.progress import track
    from rich.console import Console
    from time import sleep
    
    console = Console()
    
    segs_per_atualization = segs_total / loading_atualizations
    
    for i in track(range(loading_atualizations), description=description):
        sleep(segs_per_atualization)
    console.clear()
