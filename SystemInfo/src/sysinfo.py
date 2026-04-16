"""
sysinfo.py - System Information Module for SysInfo Pro
=======================================================
Module: Part A - System Information Report
Developer: Princeton
SRS Reference: Section 3.1 (SYSINFO-OS-01 to SYSINFO-DISK-03)
Project: Operating Systems Semester Project
Institution: Tubman University, Dept. of Computer Science
Academic Year: 2025-2026

This module retrieves and displays comprehensive system information
including OS details, CPU statistics, memory usage, page file info,
and disk drive information using the psutil library.
"""

import platform
import psutil
import os
from datetime import datetime, timedelta


def get_os_info() -> dict:
    """
    Retrieve operating system information.
    
    Returns:
        dict: Contains OS name, version, hostname, username, and uptime.
    
    SRS Requirements:
        - SYSINFO-OS-01: Full OS name and version
        - SYSINFO-OS-02: Computer hostname and username
        - SYSINFO-OS-03: System uptime in hours and minutes
    """
    # Get system boot time and calculate uptime
    boot_time = psutil.boot_time()
    uptime_seconds = datetime.now() - datetime.fromtimestamp(boot_time)
    
    # Convert uptime to hours and minutes
    total_seconds = int(uptime_seconds.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    return {
        "os": platform.platform(),
        "hostname": platform.node(),
        "username": os.getlogin(),
        "uptime": f"{hours} hours, {minutes} minutes"
    }


def get_cpu_info() -> dict:
    """
    Retrieve CPU information and statistics.
    
    Returns:
        dict: Contains CPU model, physical/logical cores, clock speed, and usage.
    
    SRS Requirements:
        - SYSINFO-CPU-01: CPU brand name and model
        - SYSINFO-CPU-02: Number of physical cores and logical processors
        - SYSINFO-CPU-03: Current CPU usage percentage (live reading)
        - SYSINFO-CPU-04: Current CPU clock speed in GHz
    """
    # Get CPU frequency (may be None on some systems/VMs)
    cpu_freq = psutil.cpu_freq()
    speed_ghz = f"{cpu_freq.current / 1000:.2f} GHz" if cpu_freq else "N/A"
    
    # Get live CPU usage with 1-second interval for accurate reading
    usage_percent = psutil.cpu_percent(interval=1)
    
    return {
        "model": platform.processor(),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "speed_ghz": speed_ghz,
        "usage_percent": usage_percent
    }


def get_ram_info() -> dict:
    """
    Retrieve RAM (Random Access Memory) statistics.
    
    Returns:
        dict: Contains total, used, and available RAM in GB with percentage.
    
    SRS Requirements:
        - SYSINFO-RAM-01: Total installed RAM in GB
        - SYSINFO-RAM-02: Currently used RAM in GB and as percentage
        - SYSINFO-RAM-03: Currently available RAM in GB
    """
    mem = psutil.virtual_memory()
    gb = 1024 ** 3  # Convert bytes to GB
    
    return {
        "total_gb": f"{mem.total / gb:.2f} GB",
        "used_gb": f"{mem.used / gb:.2f} GB",
        "used_percent": mem.percent,
        "available_gb": f"{mem.available / gb:.2f} GB"
    }


def get_pagefile_info() -> dict:
    """
    Retrieve page file (virtual memory) information.
    
    Returns:
        dict: Contains total and used page file size in GB with educational note.
    
    SRS Requirements:
        - SYSINFO-PF-01: Total page file size in GB
        - SYSINFO-PF-02: Currently used page file in GB
        - SYSINFO-PF-03: Simple explanation of what a page file is
    
    OS Concept:
        The page file (also called swap file or virtual memory) is disk space
        that the operating system uses as an extension of physical RAM when
        memory is full. This prevents system crashes but is slower than RAM.
    """
    swap = psutil.swap_memory()
    gb = 1024 ** 3
    
    return {
        "total_gb": f"{swap.total / gb:.2f} GB",
        "used_gb": f"{swap.used / gb:.2f} GB",
        "note": "A page file is disk space the OS uses as extra memory when RAM is full. "
                "It prevents system crashes when physical memory is exhausted."
    }


def get_disk_info() -> tuple:
    """
    Retrieve information about all disk drives.
    
    Returns:
        tuple: (list of drive info dicts, NTFS vs FAT32 explanation string)
    
    SRS Requirements:
        - SYSINFO-DISK-01: For each drive: letter, total/used/free space, usage %
        - SYSINFO-DISK-02: File system type for each drive (NTFS, FAT32, etc.)
        - SYSINFO-DISK-03: Explanation of NTFS vs FAT32 differences
    
    OS Concept:
        NTFS (New Technology File System) is the modern Windows filesystem with
        journaling (crash recovery), file permissions, encryption, and support
        for files larger than 4GB. FAT32 is older, less feature-rich, but offers
        better cross-platform compatibility (works on Mac, Linux, game consoles).
    """
    drives = []
    gb = 1024 ** 3
    
    # Iterate through all disk partitions
    for partition in psutil.disk_partitions():
        # Skip CD-ROM drives on Windows
        if os.name == 'nt' and 'cdrom' in partition.opts.lower():
            continue
        
        try:
            # Get disk usage statistics for this partition
            usage = psutil.disk_usage(partition.mountpoint)
            
            drives.append({
                "letter": partition.device,
                "fstype": partition.fstype if partition.fstype else "Unknown",
                "total_gb": f"{usage.total / gb:.2f} GB",
                "used_gb": f"{usage.used / gb:.2f} GB",
                "free_gb": f"{usage.free / gb:.2f} GB",
                "usage_percent": usage.percent
            })
        except PermissionError:
            # Skip drives we don't have permission to access
            continue
    
    ntfs_explanation = (
        "NTFS (New Technology File System) supports journaling, file permissions, "
        "encryption, and files larger than 4GB. FAT32 is older and limited to 4GB "
        "max file size but offers better cross-platform compatibility."
    )
    
    return drives, ntfs_explanation


def display_report():
    """
    Main function to display formatted system information report.
    
    This function calls all info-gathering functions and prints a
    well-formatted, human-readable report to the console.
    
    SRS Compliance:
        - Formats output exactly as specified in SRS sample
        - Includes all required sections (OS, CPU, RAM, Page File, Disk)
        - Uses clear section headers and aligned columns
        - Includes educational notes for Page File and NTFS
    
    Usage:
        Called by main.py when user selects Option 1 from menu.
        Can also be run standalone: python sysinfo.py
    """
    # Gather all system information
    os_info = get_os_info()
    cpu_info = get_cpu_info()
    ram_info = get_ram_info()
    pf_info = get_pagefile_info()
    disks, ntfs_note = get_disk_info()
    
    # Print formatted report header
    print("=" * 50)
    print("SYSINFO PRO - SYSTEM REPORT".center(50))
    print("=" * 50)
    
    # Section 1: Operating System Information
    print("\n[ OPERATING SYSTEM ]")
    print(f"OS       : {os_info['os']}")
    print(f"Hostname : {os_info['hostname']}")
    print(f"Username : {os_info['username']}")
    print(f"Uptime   : {os_info['uptime']}")
    
    # Section 2: CPU Information
    print("\n[ CPU ]")
    print(f"Model         : {cpu_info['model']}")
    print(f"Cores         : {cpu_info['physical_cores']} physical / {cpu_info['logical_cores']} logical")
    print(f"Current Speed : {cpu_info['speed_ghz']}")
    print(f"Usage         : {cpu_info['usage_percent']}%")
    
    # Section 3: Memory (RAM) Information
    print("\n[ MEMORY (RAM) ]")
    print(f"Total     : {ram_info['total_gb']}")
    print(f"Used      : {ram_info['used_gb']} ({ram_info['used_percent']}%)")
    print(f"Available : {ram_info['available_gb']}")
    
    # Section 4: Page File / Virtual Memory
    print("\n[ PAGE FILE ]")
    print(f"Total : {pf_info['total_gb']}")
    print(f"Used  : {pf_info['used_gb']}")
    print(f"Note  : {pf_info['note']}")
    
    # Section 5: Disk Drives Information
    print("\n[ DISK DRIVES ]")
    for drive in disks:
        print(f"Drive {drive['letter']} ({drive['fstype']})")
        print(f"  Total: {drive['total_gb']}")
        print(f"  Used : {drive['used_gb']} ({drive['usage_percent']}%)")
        print(f"  Free : {drive['free_gb']}")
    
    # Print NTFS explanation
    print(f"\nNote: {ntfs_note}")
    print("=" * 50)


# ============================================================================
# MAIN ENTRY POINT (for standalone testing)
# ============================================================================
if __name__ == "__main__":
    """
    When run directly (python sysinfo.py), display the system report.
    This allows testing the module independently before integration.
    """
    try:
        display_report()
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        print("Please ensure you have psutil installed: pip install psutil")