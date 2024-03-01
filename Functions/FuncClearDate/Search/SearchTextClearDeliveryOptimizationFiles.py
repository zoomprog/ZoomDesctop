import os

def get_delivery_optimization_size():
    delivery_optimization_path = r'C:\Windows\SoftwareDistribution\DeliveryOptimization'

    try:
        total_size = sum(
            os.path.getsize(os.path.join(dirpath, filename))
            for dirpath, _, filenames in os.walk(delivery_optimization_path)
            for filename in filenames
        )

        # Конвертируем байты в гигабайты
        total_size_gb = total_size / (1024**3)
        return total_size_gb

    except Exception as e:
        print(f"Произошла ошибка: {e}")

