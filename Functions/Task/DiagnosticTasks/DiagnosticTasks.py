import re
import subprocess


def SearchProactiveScan():
    command = 'schtasks /Query /TN "Microsoft\Windows\Chkdsk\ProactiveScan"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'ProactiveScan\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False


def ProactiveScanOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Chkdsk\ProactiveScan', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")


def ProactiveScanOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Chkdsk\ProactiveScan', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")


def SearchRecommendedTroubleshootingScanner():
    command = 'schtasks /Query /TN "Microsoft\Windows\Diagnosis\RecommendedTroubleshootingScanner"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'RecommendedTroubleshootingScanner\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False


def RecommendedTroubleshootingScannerOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Diagnosis\RecommendedTroubleshootingScanner', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")


def RecommendedTroubleshootingScannerOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Diagnosis\RecommendedTroubleshootingScanner', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")





def SearchMicrosoftWindowsDiskDiagnosticDataCollector():
    command = 'schtasks /Query /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Microsoft-Windows-DiskDiagnosticDataColl\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False





def MicrosoftWindowsDiskDiagnosticDataCollectorOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector: {e}")

def MicrosoftWindowsDiskDiagnosticDataCollectorOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticDataCollector', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchScheduled():
    command = 'schtasks /Query /TN "Microsoft\Windows\Diagnosis\Scheduled"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Scheduled\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False


def ScheduledOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Diagnosis\Scheduled', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem: {e}")


def ScheduledOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Diagnosis\Scheduled', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchMicrosoftWindowsDiskDiagnosticResolver():
    command = 'schtasks /Query /TN "\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Microsoft-Windows-DiskDiagnosticResolver\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def MicrosoftWindowsDiskDiagnosticResolverOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def MicrosoftWindowsDiskDiagnosticResolverOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchDiagnostics():
    command = 'schtasks /Query /TN "\Microsoft\Windows\DiskFootprint\Diagnostics"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Diagnostics\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def DiagnosticsOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskFootprint\Diagnostics', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def DiagnosticsOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskFootprint\Diagnostics', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchStorageSense():
    command = 'schtasks /Query /TN "\Microsoft\Windows\DiskFootprint\StorageSense"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'StorageSense\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def StorageSenseOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskFootprint\StorageSense', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def StorageSenseOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\DiskFootprint\StorageSense', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchRunFullMemoryDiagnostic():
    command = 'schtasks /Query /TN "\Microsoft\Windows\MemoryDiagnostic\RunFullMemoryDiagnostic"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'RunFullMemoryDiagnostic\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def RunFullMemoryDiagnosticOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\MemoryDiagnostic\RunFullMemoryDiagnostic', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def RunFullMemoryDiagnosticOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\MemoryDiagnostic\RunFullMemoryDiagnostic', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchProcessMemoryDiagnosticEvents():
    command = 'schtasks /Query /TN "\Microsoft\Windows\MemoryDiagnostic\ProcessMemoryDiagnosticEvents"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'ProcessMemoryDiagnosticEvents\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def ProcessMemoryDiagnosticEventsOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\MemoryDiagnostic\ProcessMemoryDiagnosticEvents', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def ProcessMemoryDiagnosticEventsOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\MemoryDiagnostic\ProcessMemoryDiagnosticEvents', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchAnalyzeSystemTask():
    command = 'schtasks /Query /TN "\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'AnalyzeSystem\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def AnalyzeSystemTaskOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def AnalyzeSystemTaskOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\Microsoft\Windows\Power Efficiency Diagnostics\AnalyzeSystem'': {e}")

def SearchBgTaskRegistrationMaintenanceTask():
    command = 'schtasks /Query /TN "\Microsoft\Windows\BrokerInfrastructure\BgTaskRegistrationMaintenanceTask"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'BgTaskRegistrationMaintenanceTask\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def BgTaskRegistrationMaintenanceTaskOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\BrokerInfrastructure\BgTaskRegistrationMaintenanceTask', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def BgTaskRegistrationMaintenanceTaskOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\BrokerInfrastructure\BgTaskRegistrationMaintenanceTask', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\M")


def Searchappuriverifierdaily():
    command = "schtasks /Query /TN \"Microsoft\\Windows\\ApplicationData\\appuriverifierdaily\""

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return 'Not Found'

    # Using a regular expression to find the line with the task and its status
    match = re.search(r'appuriverifierdaily\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Getting the task status from the matched line
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        return 'Not Found'


def appuriverifierdailyOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\ApplicationData\appuriverifierdaily', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\ApplicationData\appuriverifierdaily: {e}")

def appuriverifierdailyOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\ApplicationData\appuriverifierdaily', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\M")

def SearchUsageDataReporting():
    command = 'schtasks /Query /TN \"Microsoft\\Windows\\Flighting\\FeatureConfig\\UsageDataReporting"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'UsageDataReporting\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def UsageDataReportingOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Flighting\FeatureConfig\UsageDataReporting', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def UsageDataReportingOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\Flighting\FeatureConfig\UsageDataReporting', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\M")

def SearchCalibrationLoader():
    command = 'schtasks /Query /TN "\Microsoft\Windows\WindowsColorSystem\Calibration Loader"'

    try:
        output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return False

    # Использование регулярного выражения для поиска строки с задачей и её статусом
    match = re.search(r'Calibration Loader\s+.*\s+(Ready|Running|Disabled)', output)
    if match:
        # Получение статуса задачи из найденной строки
        status = match.group(1)
        if status == "Disabled":
            return 'Disabled'
        else:
            return 'Enabled'
    else:
        print("Задача не найдена.")
        return False

def CalibrationLoaderOn():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\WindowsColorSystem\Calibration Loader', '/ENABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке включить задачу \Microsoft\Windows\DiskDiagnostic\Microsoft-Windows-DiskDiagnosticResolver: {e}")

def CalibrationLoaderOff():
    try:
        subprocess.run(['schtasks', '/Change', '/TN', r'\Microsoft\Windows\WindowsColorSystem\Calibration Loader', '/DISABLE'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при попытке выключить задачу 'r'\M")

