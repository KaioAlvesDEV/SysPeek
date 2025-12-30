import platform
from syspeeklib import gets

def get_os_info() -> dict:
    
    """Retrieve basic operating system information.

    Returns:
        dict: A dictionary containing the system name and release version.
            Keys:
                - 'System': The name of the operating system (e.g., 'Windows', 'Linux', 'Darwin').
                - 'Release': The release version of the operating system.
    """
    # Get system and release information
    os_info = {
        'System': platform.system(),
        'Release': platform.release()
    }
    return os_info


def get_cpu_info() -> dict:
    
    """Retrieve CPU information.

    Returns:
        dict: A dictionary containing the CPU brand.
    """
    
    import cpuinfo 
    
    cpu_info = {
        'Brand': cpuinfo.get_cpu_info().get('brand_raw', 'Unknown'),}
    return cpu_info


def get_memory_info() -> dict:
    
    """Retrieve memory information.

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
    
    memory_info = {
        'Total': mem_gb,
        'Rounded Total': ceil(mem_gb),  # Rounded up total memory in GB
    }
    return memory_info
    
    
def get_disk_info() -> dict:
    
    """Retrieve disk information.

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
    
    disk_info = {
        'Total': disk_gb,
        'Rounded Total': ceil(disk_gb),  # Rounded up total disk space in GB
        'Used': disk.used,
    }
    return disk_info


def get_gpu_info() -> dict:
    
    """Retrieve basic GPU information.

    Returns:
        dict: A dictionary containing GPU infos.
    """
    gpu_info = {'Name': gets.gets_gpu_name()}
    return gpu_info
