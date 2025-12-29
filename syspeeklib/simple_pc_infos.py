import platform

def get_simple_os_info():
    
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
        'Release': platform.release(),
    }
    
    return simple_os_info
