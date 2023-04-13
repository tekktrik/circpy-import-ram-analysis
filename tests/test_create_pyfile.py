# SPDX-FileCopyrightText: 2023 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import subprocess


def test_created_code_py():

    import_name = "test_module"
    save_path = "./test_results/test_package/code.py"

    # create_pyfile.main("test_module", save_path)
    proc = subprocess.Popen(
        ["python", "scripts/create_pyfile.py", import_name, save_path]
    )
    res = proc.communicate()

    assert proc.returncode == 0

    with open(save_path, mode="r", encoding="utf-8") as genfile:
        gen_contents = genfile.read()

    with open("./tests/results/code.py", mode="r", encoding="utf-8") as resfile:
        res_contents = resfile.read()

    assert gen_contents.strip() == res_contents.strip()
