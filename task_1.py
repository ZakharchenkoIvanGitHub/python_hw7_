"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""
import os


def sort_file(path):
    sort_dic = {
        "video": ["avi", "mov", "mp4"],
        "audio": ["mp3", "wma"],
        "text": ["doc", "txt"],
        "picture": ["jpg", "jpeg", "gif"]
    }

    list_dir = os.listdir(path)

    for obj in list_dir:
        if os.path.isfile(os.path.join(path, obj)):
            for k, v in sort_dic.items():
                if os.path.splitext(obj)[-1][1:] in v:
                    if not os.path.isdir(os.path.join(path, k)):
                        os.mkdir(os.path.join(path, k))
                    os.replace(os.path.join(path, obj), os.path.join(path, k, obj))
                    break


sort_file("sort_dir")
