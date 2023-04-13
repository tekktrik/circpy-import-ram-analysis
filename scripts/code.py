# type: ignore

from time import sleep
from gc import mem_alloc

sleep(5)

print("[RP2040JS:START]")

pre_import = mem_alloc()

import {{ import_name }}

post_import = mem_alloc()

print(post_import - pre_import)

print("[RP2040JS:END]")

while True:
    pass
