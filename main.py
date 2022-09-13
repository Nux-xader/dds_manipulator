import traceback, sys, os
from wand.image import Image
from wand.display import display


log_file = "logs.txt"
clr = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def write_log():
    ex_type, ex_value, ex_traceback = sys.exc_info()
    err = "\n".join(tuple(f"File {trace[0]}, Line {trace[1]}, in {trace[2]}\n{trace[3]}" for trace in traceback.extract_tb(ex_traceback)))+f"\n{ex_type.__name__}: {ex_value}\n"
    open(log_file, "a").write(f"\n[{datetime.now()}] {err} {30*'_'}")

def progress(progs, total):
    print("")
    percent = 100*(progs/float(total))
    bar = '█'*int(percent)+'-'*(100-int(percent))
    print(f"\r [{bar}] {percent:.2f}%", end="\r")

def banner():
    print(f"""
 █▀▄ █▀▄ █▀
 █▄▀ █▄▀ ▄█  V1.0.0
 
 █▀▄▀█ ▄▀█ █▄░█ █ █▀█ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█
 █░▀░█ █▀█ █░▀█ █ █▀▀ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄

 Coder by : https://github.com/Nux-xader
 Contact  : https://wa.me/6281251389915
 _______________________________________________
""")


def manipulate(path, saveto):
    img = Image(filename=path).clone()
    img.flop()
    img.rotate(180)
    img.save(filename=saveto)
    hexdata = open(saveto, 'rb').read().replace(b"\x0a", b"\x02", 1)
    open(saveto, 'wb').write(hexdata)


def main():
    clr()
    banner()
    while True:
        dds_directory = str(input(" [*] Enter dds dir : "))
        try:
            dds_files = [f"{dds_directory}/{i}" for i in os.listdir(dds_directory) if i.split(".")[-1].lower() == "dds"]
            if len(dds_files) == 0:
                print(f" [!] Directory {dds_directory} not contain dds file")
                continue
            print(f" [+] {len(dds_files)} dds file detected")
            break
        except:
            print(f" [!] Directory {dds_directory} not found")


    while True:
        saveto = str(input(" [*] Enter directory for result : "))
        try:
            if ("/" in saveto) or ("\\" in saveto):
                print(" [!] Can't use / or \\ in result directory")
                continue
            os.mkdir(saveto)
            break
        except:
            print(f" [!] Directory {saveto} already exists")

    clr()
    banner()
    for n, dds_file in enumerate(dds_files):
        manipulate(dds_file, f"{saveto}/{dds_file.split('/')[-1]}")
        progress(n+1, len(dds_files))
    print("\n\n [+] Program finished")


if __name__ == "__main__":
    main()