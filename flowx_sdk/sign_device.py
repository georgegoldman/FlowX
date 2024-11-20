import hashlib
import platform
import uuid
import os

def get_system_info():
    # Gather system details
    system_info = {
        "platform": platform.system(),
        "platform_version": platform.version(),
        "platform_release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "mac_address": get_mac_address(),
        "uuid": str(uuid.getnode())
    }
    return system_info

def get_mac_address():
    # Get the MAC address
    return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for  elements in range(0, 2 * 6, 8)])

def generate_hardware_fingerprint():
    # Get system details
    system_info = get_system_info()


    # Convert the details to a sorted string
    info_string = ''.join(f"{key}={value};" for key, value in sorted(system_info.items()))

    # Generate a SHA-256 hash
    fingerprint = hashlib.sha256(info_string.encode()).hexdigest()
    return fingerprint
