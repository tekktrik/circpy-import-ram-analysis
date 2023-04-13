# SPDX-FileCopyrightText: 2023 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# type: ignore

from time import sleep
from gc import mem_alloc

sleep(5)

print("[RP2040JS:START]")

pre_import = mem_alloc()

import test_module

post_import = mem_alloc()

print(post_import - pre_import)

print("[RP2040JS:END]")

while True:
    pass
