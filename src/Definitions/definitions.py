import os
from pathlib import Path

BOT_PATH = Path(os.path.dirname(os.path.abspath(__file__))).parents[1]
CONFING_FILES = os.path.join(BOT_PATH, "config_files")
ANNOUNCEMENTS_PATH = os.path.join(CONFING_FILES, "announcements_files")
