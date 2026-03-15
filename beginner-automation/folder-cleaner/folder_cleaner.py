import os

folder_path = "D:\\"

for root, dirs, files in os.walk(folder_path, topdown=False):
    for d in dirs:
        dir_path = os.path.join(root, d)
        try:
            is_empty = not os.listdir(dir_path)
        except (PermissionError, FileNotFoundError, OSError) as exc:
            # Skip directories we can't access (e.g., System Volume Information) or that disappear mid-walk.
            print(f"Skipping '{dir_path}' ({exc.__class__.__name__}): {exc}")
            continue

        if is_empty:
            os.rmdir(dir_path)
            print(f"Deleted empty folder: {dir_path}")
