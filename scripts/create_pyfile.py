# SPDX-FileCopyrightText: 2023 Alec Delaney, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import click
import pathlib
from typing import Any
from jinja2 import Environment, FileSystemLoader, select_autoescape

import os

print(os.getcwd())
loader = FileSystemLoader("./scripts")
print(loader.list_templates())
env = Environment(
    loader=FileSystemLoader("./scripts"),
    autoescape=select_autoescape(),
)


@click.command()
@click.argument("import_name")
@click.argument(
    "save_path", type=click.Path(exists=False, writable=True, resolve_path=True)
)
def main(import_name: Any, save_path: str):
    template = env.get_template("code.py")
    rendered = template.render(import_name=str(import_name))
    save_path_obj = pathlib.Path(save_path)
    save_path_obj.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, mode="w", encoding="utf-8") as file:
        file.write(rendered)


if __name__ == "__main__":
    main()
