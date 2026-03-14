import os
import shutil

folder_path = r"C:\Users\saras\Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):

        file_extension = os.path.splitext(filename)[1].lower()

        for folder_name, extensions in file_types.items():

            if file_extension in extensions:

                target_folder = os.path.join(folder_path, folder_name)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))

                break