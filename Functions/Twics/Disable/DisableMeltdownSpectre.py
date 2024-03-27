import winreg as reg


def MeltdownSpectre_Disable():
    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_WRITE)

        # Удаление значения feature_settings_override_mask
        try:
            reg.DeleteValue(registry_key, "FeatureSettingsOverrideMask")
            print("Значение 'FeatureSettingsOverrideMask' удалено.")
        except FileNotFoundError:
            print("Значение 'FeatureSettingsOverrideMask' не найдено.")

        # Изменение значения feature_settings_override на 0
        reg.SetValueEx(registry_key, "FeatureSettingsOverride", 0, reg.REG_DWORD, 0)
        print("Значение 'FeatureSettingsOverride' изменено на 0.")

        reg.CloseKey(registry_key)
    except WindowsError as e:
        print(f"Ошибка при доступе к реестру: {e}")


