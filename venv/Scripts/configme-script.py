#!C:\Users\drofa\PycharmProjects\untitled2\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'configme==0.0.4','console_scripts','configme'
__requires__ = 'configme==0.0.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('configme==0.0.4', 'console_scripts', 'configme')()
    )
