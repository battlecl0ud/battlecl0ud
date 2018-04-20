# -*- coding: utf-8 -*-
import ui
import docker

def main():
    # coloring:
    ui.info("This is", ui.red, "red",
            ui.reset, "and this is", ui.bold, "bold")
    ui.info(ui.check)

    # enumerating:
    list_of_things = ["foo", "bar", "baz"]
    for i, thing in enumerate(list_of_things):
        ui.info_count(i, len(list_of_things), thing)

for i in range(10):
    ui.info_progress("PROGRESSS", i, 10)
if __name__ == '__main__':
    # coloring:
    ui.info("This is", ui.red, "red",
            ui.reset, "and this is", ui.bold, "bold")
    main()






"""Main module."""
