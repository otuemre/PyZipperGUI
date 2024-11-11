import zipfile
from pathlib import Path

def create_archive(file_paths, to_folder_path):
    path = Path(to_folder_path, "compress.zip")

    with zipfile.ZipFile(path, "w") as archive:
        for file_path in file_paths:
            file_path = Path(file_path)
            archive.write(file_path, arcname=file_path.name)


def unzipper(archive_path, to_folder_path):
    with zipfile.ZipFile(archive_path, "r") as archive:
        archive.extractall(to_folder_path)
