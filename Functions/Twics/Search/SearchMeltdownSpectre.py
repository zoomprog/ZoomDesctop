import winreg as reg


def MeltdownSpectre_Search():
    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management"
        registry_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_READ)

        # Попытка получить значения из реестра
        try:
            feature_settings, _ = reg.QueryValueEx(registry_key, "FeatureSettings")
        except FileNotFoundError:
            feature_settings = None

        try:
            feature_settings_override, _ = reg.QueryValueEx(registry_key, "FeatureSettingsOverride")
        except FileNotFoundError:
            feature_settings_override = None

        try:
            feature_settings_override_mask, _ = reg.QueryValueEx(registry_key, "FeatureSettingsOverrideMask")
        except FileNotFoundError:
            feature_settings_override_mask = None

        # Проверка значений и возврат соответствующего результата
        if feature_settings == 1 and feature_settings_override == 3 and feature_settings_override_mask == 3:
            return 'Enable'
        else:
            return 'Disable'
    except WindowsError as e:
        print(f"Ошибка при доступе к реестру: {e}")
        return 'Disable'  # Возвращаем 'Disable' в случае любой ошибки доступа к реестру
