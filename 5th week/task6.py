import sys
import shutil
import os
if len(sys.argv) < 2:
    print("Usage: python task6.py <filename>")
    sys.exit(1)
filename = sys.argv[1]
if not os.path.isfile(filename):
    print(f"The file '{filename}' does not exist.")
    sys.exit(1)
backup_filename = filename + ".bak"
try:
    shutil.copy(filename, backup_filename)
    print(f"Backup created: {backup_filename}")
except Exception as e:
    print(f"Failed to create backup. Error: {e}")
