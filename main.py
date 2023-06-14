from os import listdir
from os.path import isfile, join
import gh_md_to_html

def exceptions(name):
    if name[0] == ".":
        return True
    if name == "CNAME":
        return True
    if name == "index.md":
        return True
    if name == "github-markdown-css":
        return True
    return False

def rec(path):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    dirs = [f for f in listdir(path) if not isfile(join(path, f))]
    # print(files, dirs)

    with open(path + "/index.md", "w") as f:
        ww = ""
        for file in files:
            if exceptions(file):
                continue
            if file[-3:] == "pdf":
                ww += "[{file}](https://media.githubusercontent.com/media/MKutay/cdn/main/{path}/{file})  \n".format(path = path, file = file)
                continue
            ww += "[{file}](./{file})  \n".format(file = file)
        for dir in dirs:
            if exceptions(dir):
                continue
            ww += "[{dir}](./{dir}/)  \n".format(dir = dir)
            rec("{path}/{dir}".format(path = path, dir = dir))
        # f.write(ww)

    print(path)
    gh_md_to_html.main(path + "/index.md", math=True)

rec(".")
