def gets_platform() -> str:
    
    import platform
    system = platform.system()
    return system


def gets_gpu_name() -> str:
    
    system = gets_platform()
    gpu_name = "Unknown"

    # NVIDIA GPU detection using GPUtil
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if gpus:
            gpu_name = gpus[0].name
            return gpu_name
    except:
        pass
    
    if system == "Windows":
        # Try WMI method first
        try:
            import wmi
            c = wmi.WMI()
            gpu_name = c.Win32_VideoController()[0]
            gpu_name = gpu_name.Name
            return gpu_name
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
                gpu_name = lines[1]
                return gpu_name
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
                gpu_name = name
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
                    gpu_name = line.split(":")[-1].strip()
                    return gpu_name
        except:
            pass
        
    return gpu_name
        

def gets_safe_dict(data, *keys):
    for key in keys:
        if not isinstance(data, dict):
            return 'N/A'
        data = str(data.get(key))
    return data
    