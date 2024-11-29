import shutil
import os

def validate_file_path(file_path, expected_extension):
    if not os.path.isfile(file_path):
        return False, f"File '{file_path}' does not exist."
    if not file_path.lower().endswith(expected_extension.lower()):
        return False, f"File '{file_path}' is not a {expected_extension.upper()} file."
    return True, None

def exe_to_dll(exe_path, dll_path):
    try:
        valid, error = validate_file_path(exe_path, ".exe")
        if not valid:
            return False, error
        if os.path.isfile(dll_path):
            return False, f"Destination DLL file '{dll_path}' already exists. Please choose a different path."
        shutil.copy(exe_path, dll_path)
        return True, f"EXE successfully converted to DLL: {dll_path}"
    except Exception as e:
        return False, f"Error during conversion: {str(e)}"

def dll_to_exe(dll_path, exe_path):
    try:
        valid, error = validate_file_path(dll_path, ".dll")
        if not valid:
            return False, error
        if os.path.isfile(exe_path):
            return False, f"Destination EXE file '{exe_path}' already exists. Please choose a different path."
        shutil.copy(dll_path, exe_path)
        return True, f"DLL successfully converted to EXE: {exe_path}"
    except Exception as e:
        return False, f"Error during conversion: {str(e)}"
