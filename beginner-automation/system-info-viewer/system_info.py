import platform
import psutil

def get_size(bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

print("="*40)
print("   SYSTEM INFORMATION VIEWER")
print("="*40)

print(f"OS: {platform.system()} {platform.release()}")
print(f"Processor: {platform.processor()}")

print("\nCPU Cores:", psutil.cpu_count(logical=True))
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

memory = psutil.virtual_memory()
print("\nMemory Total:", get_size(memory.total))
print("Memory Used:", get_size(memory.used))
print("Memory Usage:", memory.percent, "%")

disk = psutil.disk_usage('/')
print("\nDisk Total:", get_size(disk.total))
print("Disk Used:", get_size(disk.used))
print("Disk Usage:", disk.percent, "%")

print("="*40)