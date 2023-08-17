"""Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""

import os


def group_rename(num_dig_serial,
                 source_extension,
                 end_extension,
                 range_original_name: list,
                 file_name=None,
                 path=None):

    seq_number = 0

    def get_seq_number():
        nonlocal seq_number
        str_number = str(seq_number)
        seq_number += 1

        if len(str_number) > num_dig_serial:
            str_number = str_number[len(str_number) - num_dig_serial:]
        elif len(str_number) < num_dig_serial:
            str_number = "0" * (num_dig_serial - len(str_number)) + str_number

        return str_number

    path = os.getcwd() if path is None else path

    list_dir = os.listdir(path)
    for obj in list_dir:
        if os.path.isfile(os.path.join(path, obj)):
            if source_extension == os.path.splitext(obj)[-1][1:]:
                old_name = os.path.splitext(obj)[0][range_original_name[0] - 1: range_original_name[1]]
                file_name = "" if file_name is None else file_name
                new_name = f"{old_name}_{file_name}_{get_seq_number()}.{end_extension}"

                while os.path.isfile(os.path.join(path, new_name)):
                    new_name = f"{old_name}_{file_name}_{get_seq_number()}.{end_extension}"

                os.rename(os.path.join(path, obj), os.path.join(path, new_name))


group_rename(4, "mp4", "avi", [1, 3], "new_file", "rename_dir")
