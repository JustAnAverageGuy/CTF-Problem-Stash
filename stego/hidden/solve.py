#! /bin/python3

import os

for i in range(2, 100):
    os.system(f"unzip {i}.zip")
    os.system(f"rm {i}.zip")
