import platform

def get_simple_os_info() -> dict:
    
    """Retrieve basic operating system information.

    Returns:
        dict: A dictionary containing the system name and release version.
            Keys:
                - 'System': The name of the operating system (e.g., 'Windows', 'Linux', 'Darwin').
                - 'Release': The release version of the operating system.
    """
    # Get system and release information
    simple_os_info = {
        'System': platform.system(),
        'Release': platform.release()
    }
    
    return simple_os_info

def get_simple_cpu_info() -> dict:
    
    """Retrieve basic CPU information.

    Returns:
        dict: A dictionary containing the CPU brand.
    """
    
    import cpuinfo 
    
    simple_cpu_info = {
        'Brand': cpuinfo.get_cpu_info().get('brand_raw', 'Unknown'),}
    
    return simple_cpu_info

def get_simple_memory_info() -> dict:
    
    """Retrieve basic memory information.

    Returns:
        dict: A dictionary containing total and available memory in bytes.
            Keys:
                - 'Total': Total physical memory in bytes.
                - 'Available': Available physical memory in bytes.
    """
    
    import psutil
    from math import ceil
    
    mem = psutil.virtual_memory()
    mem_gb = mem.total / (1024 ** 3)  # Convert bytes to GB
    
    simple_memory_info = {
        'Total': mem_gb,
        'Rounded Total': ceil(mem_gb),  # Rounded up total memory in GB
    }
    
    return simple_memory_info
    
def get_simple_disk_info() -> dict:
    
    """Retrieve basic disk information.

    Returns:
        dict: A dictionary containing total and used disk space in bytes.
            Keys:
                - 'Total': Total disk space in bytes.
                - 'Used': Used disk space in bytes.
    """
    
    import psutil
    from math import ceil
    
    disk = psutil.disk_usage('/')
    
    disk_gb = disk.total / (1024 ** 3)  # Convert bytes to GB
    
    simple_disk_info = {
        'Total': disk_gb,
        'Rounded Total': ceil(disk_gb),  # Rounded up total disk space in GB
        'Used': disk.used,
    }
    
    return simple_disk_info
