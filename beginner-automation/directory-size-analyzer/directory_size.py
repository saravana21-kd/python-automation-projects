import os

folder_path = input("Enter folder path: ")

for dirpath, dirnames, filenames in os.walk(folder_path):
    size = 0

    for file in filenames:
        filepath = os.path.join(dirpath, file)

        if os.path.exists(filepath):
            size += os.path.getsize(filepath)

    print(f"{dirpath} → {round(size/(1024*1024),2)} MB")