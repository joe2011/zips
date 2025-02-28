import os
import shutil
import requests
from zipfile import ZipFile
from io import BytesIO

def download_github_dir(url, dest):
    """Scarica file e directory da GitHub"""
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Se è un archivio ZIP, estrai
        if url.endswith('.zip'):
            zip_file = ZipFile(BytesIO(response.content))
            zip_file.extractall(dest)
        else:
            with open(dest, 'wb') as f:
                f.write(response.content)

        return True
    except Exception as e:
        print(f"Errore durante il download da GitHub: {e}")
        return False

def backup_and_copy(src, dest, backup_dir):
    """Backup e copia dei file"""
    if os.path.exists(dest):
        backup_path = os.path.join(backup_dir, os.path.basename(dest))
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        shutil.move(dest, backup_path)
        print(f"File esistente spostato in backup: {backup_path}")

    shutil.copytree(src, dest, dirs_exist_ok=True)
    print(f"File copiati da {src} a {dest}")