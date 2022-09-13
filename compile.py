import py_compile, shutil, os


dir_name = "."
files = ["main.py"]

try:shutil.rmtree("__pycache__")
except: pass
try: os.mkdir(dir_name)
except: pass

for file in files:
	py_compile.compile(file)
	open(f"{dir_name}/{file.split('.')[0]}.pyc", "wb").write(open("__pycache__/"+[i for i in os.listdir("__pycache__") if i.split(".")[0] == file.split(".")[0]][0], "rb").read())