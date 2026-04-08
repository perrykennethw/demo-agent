import os

def get_files_info(working_dir, directory="."):
    working_dir_abs = os.path.abspath(working_dir)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    files = os.listdir(target_dir)

    result = []
    for file in files:
        filepath = os.path.join(target_dir, file)
        result.append(f"- {file}: file_size={os.path.getsize(filepath)}, is_dir={os.path.isdir(filepath)}")

    return "\n".join(result)
