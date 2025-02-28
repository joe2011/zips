import xbmcaddon
import xbmcgui
import os
from utils import download_github_dir, backup_and_copy

addon = xbmcaddon.Addon()
dialog = xbmcgui.Dialog()

def main():
    github_paths = [addon.getSetting(f"github_path_{i}") for i in range(1, 6)]
    dest_paths = [addon.getSetting(f"destination_path_{i}") for i in range(1, 6)]
    backup_path = addon.getSetting("backup_path")

    if not backup_path:
        dialog.ok("Errore", "Specifica un percorso di backup nei settings")
        return

    for i in range(5):
        if github_paths[i] and dest_paths[i]:
            temp_download_path = os.path.join(xbmc.translatePath('special://temp'), f"temp_folder_{i}")

            if download_github_dir(github_paths[i], temp_download_path):
                backup_and_copy(temp_download_path, dest_paths[i], backup_path)
                dialog.notification("Sincronizzazione completata", f"Files copiati in: {dest_paths[i]}", xbmcgui.NOTIFICATION_INFO)

    dialog.ok("Operazione completata", "Tutte le sincronizzazioni sono state eseguite")

if __name__ == "__main__":
    main()