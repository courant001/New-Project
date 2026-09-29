import os
import shutil


def copy_content(source, destination):
    if not os.path.exists(source):
        raise Exception("Source path does not exist")
    if os.path.exists(destination):
            shutil.rmtree(destination)
    os.mkdir(destination)
    content = os.listdir(source)

    print(content)
    for item in content:
        item_path = os.path.join(source, item)
        print(item_path)
        if os.path.isfile(item_path):
            shutil.copy(item_path, destination)
        else:
            new_dir = os.path.join(destination, item)
            os.mkdir(new_dir)
            copy_content(item_path, new_dir)