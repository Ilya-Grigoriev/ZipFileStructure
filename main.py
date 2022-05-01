import os
from zipfile import ZipFile


def search_paths(paths, cur):
    return [i for i in paths if cur in i and cur != i]


def made_path(path):
    path = path.rstrip('/')
    return (path.count('/') * 2 * ' ') + path.rstrip('/').split('/')[-1]


def human_read_format(size):
    bite_list = ['Б', 'КБ', 'МБ', 'ГБ']
    count = 0
    while size >= 1023:
        size /= 1024
        count += 1
    return f'{round(size)}{bite_list[count]}'


with ZipFile('test.zip') as myzip:
    list_zip = [(i.filename, i.file_size, i) for i in myzip.filelist]
    cur = list_zip[0]
    while True:
        if len(list_zip) == 0:
            break
        cur = list_zip[0]
        print(made_path(cur[0]))
        list_1 = [i for i in list_zip if cur[0] in i[0] and cur[0] != i[0]]
        list_zip.remove(cur)
        if len(list_1) > 1:
            for i in list_1:
                if i in list_zip:
                    if not i[2].is_dir():
                        print(f'{made_path(i[0])} {human_read_format(i[1])}')
                    else:
                        print(made_path(i[0]))
                for j in search_paths(list_1, i):
                    if not j[2].is_dir():
                        print(f'{made_path(j[0])} {human_read_format(j[1])}')
                    elif j in list_zip:
                        print(made_path(j))
                    if j in list_zip:
                        list_zip.remove(j)
                if i in list_zip:
                    list_zip.remove(i)
