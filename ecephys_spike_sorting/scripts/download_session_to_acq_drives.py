from __future__ import annotations

import subprocess
import sys

import np_session


def download_session_to_acq_drives(session: str | int | np_session.Session, probe_letters: str = 'ABCDEF'):
    session = np_session.Session(session)
    for network_path in (session.npexp_path, ) + ((session.lims_path, ) if session.lims_path else ()):
        for drive, folder_suffix in (('A:', 'ABC'), ('B:', 'DEF')):
            if not any(probe_letter in folder_suffix for probe_letter in probe_letters):
                continue
            probe_folder_on_network = network_path / f'{session.folder}_probe{folder_suffix}'
            if not len(tuple(probe_folder_on_network.rglob('*continuous.dat'))) == 6:
                continue
            probe_folder_on_acq_drive = f'{drive}\\{session.folder}_probe{folder_suffix}'
            if probe_folder_on_network.exists():
                print(f'Copying {probe_folder_on_network} to {drive}')
                subprocess.run(['robocopy', str(probe_folder_on_network), str(probe_folder_on_acq_drive), '/S', '/J', '/R:0', '/W:0', '/MT:32'])


if __name__ == "__main__":
    download_session_to_acq_drives(sys.argv[1], (''.join(sys.argv[2:]) if len(sys.argv) > 2 else 'ABCDEF'))
