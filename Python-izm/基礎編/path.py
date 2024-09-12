# python path.py
import os


PROJECT_DIR = 'C:¥python-izm'
SETTINGS_FILE = 'settings.ini'

print(os.path.join(PROJECT_DIR, SETTINGS_FILE)) # /でパスが構築される
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))
