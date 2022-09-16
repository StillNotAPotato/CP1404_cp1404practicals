import os
import shutil

def main():
    os.chdir('FilesToSort')
    for directory_name, subdirectories, filenames in os.walk('.'):
        sort_files_into_directories(filenames)


def sort_files_into_directories(filenames):
    for filename in filenames:
        data = filename.split(".")
        extension = data[1]
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        shutil.move(filename, extension + '/' + filename)

if __name__ == '__main__':
    main()
