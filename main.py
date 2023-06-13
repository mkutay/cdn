from os import listdir
from os.path import isfile, join

def exceptions(name):
    if name[0] == ".":
        return True
    if name == "CNAME":
        return True
    if name == "index.md":
        return True
    return False

def rec(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    dirs = [f for f in listdir(path) if not isfile(join(path, f))]
    print(files, dirs)

    with open(path + "/index.md", "w") as f:
        ww = ""
        for file in files:
            if exceptions(file):
                continue
            ww += "[{file}]({path}/{file})\n".format(file = file, path = path)
        for dir in dirs:
            if exceptions(dir):
                continue
            ww += "[{dir}]({path}/{dir}/index.md)\n".format(dir = dir, path = path)
            rec("{path}/{dir}".format(path = path, dir = dir))
        f.write(ww)

rec(".")
