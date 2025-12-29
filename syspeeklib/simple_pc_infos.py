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

def get_simple_gpu_info():
    
    import platform
    info = {"Name": "Unknown"}
    system = platform.system()

    # NVIDIA GPU detection using GPUtil
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            info["Name"] = gpus[0].name
            return info
    except:
        pass
    
    if system == "Windows":
        # Try WMI method first
        try:
            import wmi
            c = wmi.WMI()
            gpu_info = c.Win32_VideoController()[0]
            info["Name"] = gpu_info.Name
            return info
        except:
            pass
        # Windows Management Instrumentation Command-line (WMIC) method
        try:
            import subprocess

            result = subprocess.run(
                ["wmic", "path", "win32_videocontroller", "get", "name"],
                capture_output=True,
                text=True
            )

            lines = [l.strip() for l in result.stdout.split("\n") if l.strip()]
            if len(lines) > 1:
                info["Name"] = lines[1]
                return info
        except:
            pass

        # PowerShell method
        try:
            import subprocess

            result = subprocess.run(
                [
                    "powershell",
                    "-Command",
                    "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"
                ],
                capture_output=True,
                text=True
            )

            name = result.stdout.strip()
            if name:
                info["Name"] = name
        except:
            pass
        
    elif system == "Linux":
        
        # Try lspci command
        try:
            import subprocess
            result = subprocess.run(
                ["lspci"],
                capture_output=True,
                text=True
            )
            for line in result.stdout.split("\n"):
                if "VGA" in line or "3D controller" in line:
                    info["Name"] = line.split(":")[-1].strip()
                    return info
        except:
            pass

    return info
