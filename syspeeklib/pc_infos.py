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
        'Release': platform.release(),
        'Version': platform.version(),
        'Node': platform.node(),
        'Machine': platform.machine()
    }
    return os_info


def get_cpu_info() -> dict:
    """Retrieve CPU information combining cpuinfo and psutil.

    Returns:
        dict: A dictionary containing detailed CPU info.
    """

    import cpuinfo
    import psutil

    info = cpuinfo.get_cpu_info()

    def parse_cache_size(cache_value):
        try:
            return int(cache_value)
        except (ValueError, TypeError):
            return None

    l1cache_bytes = parse_cache_size(info.get('l1_cache_size', None))
    l2cache_bytes = parse_cache_size(info.get('l2_cache_size', None))
    l3cache_bytes = parse_cache_size(info.get('l3_cache_size', None))

    def bytes_to_mb_str(num_bytes):
        if num_bytes is None:
            return "Unknown"
        return f"{num_bytes / (1024 ** 2):.2f} MB"

    l1cache_size_mb_str = bytes_to_mb_str(l1cache_bytes)
    l2cache_size_mb_str = bytes_to_mb_str(l2cache_bytes)
    l3cache_size_mb_str = bytes_to_mb_str(l3cache_bytes)

    # Use psutil to get more reliable core counts
    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    
    flags_str = ''
    flags_list = info.get('flags', [])
    for i, flag in enumerate(flags_list):
        if i == 0:
            flags_str += f'{flag}'
        else:
            flags_str += f', {flag}'

    cpu_info = {
        "Brand": info.get("brand_raw", "Unknown"),
        "Vendor": info.get("vendor_id_raw", "Unknown"),
        "Architecture": info.get("arch", "Unknown"),
        "Bits": info.get("bits", "Unknown"),

        "Physical Cores": physical_cores if physical_cores is not None else "Unknown",
        "Logical Cores": logical_cores if logical_cores is not None else "Unknown",

        "Advertised Frequency": info.get("hz_advertised_friendly", "Unknown"),

        "L1 Data Cache": info.get("l1_data_cache_size", "Unknown"),
        "L1 Instruction Cache": l1cache_size_mb_str,
        "L2 Cache": l2cache_size_mb_str,
        "L3 Cache": l3cache_size_mb_str,

        "Flags": flags_str
    }
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
