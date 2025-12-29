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
