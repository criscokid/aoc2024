#!/usr/bin/python3

import sys
import os
import shutil
from pathlib import Path

day_name = sys.argv[1]
print(day_name)

if not os.path.exists(day_name):
    os.makedirs(day_name)

shutil.copy("daily/dayna.py", f"{day_name}/{day_name}a.py")
Path(f"{day_name}/input1.txt").touch()
Path(f"{day_name}/sample1.txt").touch()
