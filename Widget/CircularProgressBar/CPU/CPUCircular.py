import psutil

# Получение процента загрузки для каждого ядра CPU за последнюю секунду
def cpu_Bar():
    cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)
    CpuUsage = 0
    for i, usage in enumerate(cpu_usage_per_core, start=1):
        CpuUsage += usage
    return CpuUsage

