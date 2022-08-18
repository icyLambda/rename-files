""" This script rename files """

__author__ = "Dmitrii V (nickname: icyLambda)"
__copyright__ = "Copyright 2022, The Dmitrii V Project"
__credits__ = ["Dmitrii V"]
__license__ = "GNU General Public License (GPLv3)"
__version__ = "1.0.0"
__maintainer__ = "Dmitrii V"
__email__ = "icyLambda@gmail.com"
__status__ = "Production"

import os
import re


def exit_start_restart():
    data_output: dict = {}

    print("Q - Exit/Quit.")
    print("ADD - Adding text.")
    print("RENAME or NEW - Renaming a file.")

    status: bool = True
    while status:
        print()
        print("Enter your answer:", end=" ")

        try:
            action = input().lower()
        except KeyboardInterrupt:
            print("\nProgram completed...")
            exit()
        else:
            if action == "add":
                action = input("START - to the begining. END - In the end: ").lower()
                action = f"add_{action}"
            elif action == "new":
                action = "rename"

            if action == "add_start" or action == "add_end" or action == "rename":
                status = False
            elif action == "q":
                exit()
            else:
                print("\nWrong answer...\n".upper())
                print("To exit the program, enter - \"Q\".".title())
                print("To continue - \"ADD\", \"ADD-START\", \"ADD-END\", \"NEW\" or \"RENAME\"".title())
                continue

            path_folder = input("Specify the path to the folder: ").lower()
            path_folder_start = path_folder[0:3]
            result = re.search(r"(^\w:\\)", path_folder)

            if result is None:
                continue

            if f"{path_folder_start}" == f"{result.group(0)}":
                text = input("Insert any text: ").lower()

                data_output["path_folder"] = path_folder
                data_output["action"] = action
                data_output["text"] = text

    return data_output


def rename_files_in_directory(path_to_dirs: str, action: str, text: str):
    dirs: list[str] = []
    files: list[str] = []
    count: int = 0

    if os.path.isdir(path_to_dirs):
        dir_files = os.listdir(path_to_dirs)

        print()

        for count, file in enumerate(dir_files):
            full_path = os.path.join(path_to_dirs, file)
            f_name, f_ext = os.path.splitext(file)

            # Commented out code will be useful for debugging if uncommented.
            # print()
            # print("----------")
            # print(full_path)
            # print(path_to_dirs)
            # print(file)
            # print("----------")

            count += 1
            index_str = f"0{count}" if count < 10 else str(count)

            if os.path.isfile(full_path):
                if action == "add_start":
                    new_path = f"{path_to_dirs}\\{text}-{f_name}{f_ext}"
                    os.rename(full_path, new_path)
                    files.append(new_path)
                elif action == "rename":
                    new_path = f"{path_to_dirs}\\{text}-{index_str}{f_ext}"
                    os.rename(full_path, new_path)
                    files.append(new_path)
                elif action == "add_end":
                    new_path = f"{path_to_dirs}\\{f_name}-{text}{f_ext}"
                    os.rename(full_path, new_path)
                    files.append(new_path)
                else:
                    print("No such action...")
            elif os.path.isdir(full_path):
                dirs.append(full_path)

    return dirs, files, count


def main():
    status = True
    while status:
        data_output = exit_start_restart()

        try:
            dirs, files, number_edit_cycles = rename_files_in_directory(
                path_to_dirs=data_output["path_folder"],
                action=data_output["action"],
                text=data_output["text"]
            )
        except Exception:
            continue

        print("Files List:")
        index_file = 0
        for file in files:
            index_file += 1
            print(f"{index_file}: {file}")

        index_dir = 0
        if index_dir:
            print("\nDirectory List:")
            for file in dirs:
                index_dir += 1
                print(f"{index_dir}: {file}")

        print("\nNumber of renamed files:", number_edit_cycles)
        print()


if __name__ == '__main__':
    print()
    main()
    print()
    input("Please Enter for Exit program")
