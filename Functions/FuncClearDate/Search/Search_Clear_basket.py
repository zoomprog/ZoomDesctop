import ctypes

def get_frame_Clear_basket():
    try:
        # Define the structure for SHQUERYRBINFO
        class SHQUERYRBINFO(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_uint),
                        ("i64Size", ctypes.c_ulonglong),
                        ("i64NumItems", ctypes.c_ulonglong)]

        # Call SHQueryRecycleBin to get information about the Recycle Bin
        shqueryrbinfo = SHQUERYRBINFO()
        shqueryrbinfo.cbSize = ctypes.sizeof(SHQUERYRBINFO)
        result = ctypes.windll.shell32.SHQueryRecycleBinW(None, ctypes.byref(shqueryrbinfo))

        if result == 0:
            # Successfully retrieved the Recycle Bin information
            size_mb = shqueryrbinfo.i64Size / (1024 * 1024)
            return size_mb
        else:
            # Failed to retrieve the Recycle Bin information
            raise RuntimeError(f"Failed to retrieve Recycle Bin information. Error code: {result}")
    except Exception as e:
        # Handle exceptions
        print(f"Произошла ошибка: {e}")

