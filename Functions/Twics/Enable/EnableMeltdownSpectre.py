import winreg as reg


def MeltdownSpectre_Enable():
    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)
        # Установка или создание значения для FeatureSettingsOverride и FeatureSettingsOverrideMask
        # Если значения не существуют, они будут созданы с указанными значениями
        reg.SetValueEx(registry_key, "FeatureSettingsOverride", 0, reg.REG_DWORD, 3)
        reg.SetValueEx(registry_key, "FeatureSettingsOverrideMask", 0, reg.REG_DWORD, 3)
        print('True')
        reg.CloseKey(registry_key)

    except WindowsError as e:
        print(f"Ошибка при доступе к реестру: {e}")


