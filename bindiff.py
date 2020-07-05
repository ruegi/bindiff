"""
bindiff.py
Vergleicht zwei Ordner binär

rg, ab 2020-07-03
WORKING VERSION auf CEBULON /archiv/video !!

"""

import os 
import sys
# import progressbar
# progressbar.streams.wrap_stderr()

from pathlib import Path

from typing import List

primPath = "/mnt/platte/schnitt"
secPath = "/archiv/video/_in4"

# test pfade
# primPath = "E:/Filme/schnitt.alt"
# secPath = "y:/video/_in4"


class Ergebnis():
    def __init__(self):
        self.gesamt : int = 0
        self.ok: int = 0
        self.fehler: int = 0
        self.binfehler: int = 0
        self.fList: List = [] 

    def __str__(self):        
        return f"{self.gesamt} geprüft: davon {self.ok} OK; {self.fehler} fehlerhaft\n Fehlrehafte Binärvergleiche:\n" + "\n".join(self.fList)
    
    def adderr(self, ftext):
        self.fList.append(ftext)
        self.binfehler += 1


def progress(count, total, status='', bar_len=40):
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    percents = 100.0 if percents > 100.0 else percents
    bar = '#' * filled_len + '-' * (bar_len - filled_len)

    fmt = '\r[%s] %s%s ...%s' % (bar, percents, '%', status)
    # print('\b' * len(fmt), end='', flush=True)  # clears the line     # funktioniert nicht!
    sys.stdout.write(fmt)
    sys.stdout.flush()


def bin_vgl(file1: str, file2: str, flen: int) -> bool:
    global result
    name = file1[file1.rfind("/")+1:]
    # führt einen binären Vergleich der beiden Dateien zurück;  
    # bei Übereinstimmung wird True zurückgegeben, sosnt false
    buflen = 32*1024*1024    # 32 MB
    isOK = True    
    with open(file1, "rb") as f1, open(file2, "rb") as f2: # progressbar.ProgressBar(max_value=100, redirect_stdout=True) as bar:
        # print(f">> {name} ... binärer Vergleich .. ", end="", flush=True)
        # print(f">> {name} ... binärer Vergleich .. ")
        lenleft = flen
        buflen = min(buflen, lenleft) 
        # pcent = 0
        pos = 0
        txt = f"binärer Vergleich: {name}"
        progress(pos, flen, status=txt)
        # progressbar.streams.flush()      
        while lenleft > 0:
            b1 = f1.read(buflen)
            b2 = f2.read(buflen)
            pos += buflen
            # print(".",end="")
            lenleft -= buflen
            # pcent = int((flen - lenleft)/flen)
            progress(pos, flen, status=txt)
            # bar.update(pcent)
            
            if b1 == b2:
                continue
            else:
                pos = flen - lenleft
                print(f"\nBinärer Fehler bei Position {pos} - {pos + buflen} ")
                result.adderr(f"{file1} bei Position {pos}")
                isOK = False
                break
    if isOK:
        print(" ... OK\n")

    return isOK

prim_path: Path = Path(primPath)
sec_path: Path = Path(secPath)

for p_root, p_dirs, p_files in os.walk(prim_path):
    prim_root = p_root
    prim_files = p_files
    break

# sec_root, sec_dirs, sec_files = os.walk(sec_path)
result = Ergebnis()

for name in prim_files:
    result.gesamt += 1
    prim_file = os.path.join(prim_root, name)
    sec_file = os.path.join(sec_path, name)
    if os.path.isfile(sec_file):
        prim_stats = os.stat(prim_file)
        sec_stats = os.stat(sec_file)
        if prim_stats.st_size == sec_stats.st_size:
            print(f"> {name} ... Existiert und längengleich .. OK\n")
            if bin_vgl(prim_file, sec_file, prim_stats.st_size):
                result.ok += 1
            else:
                result.fehler += 1
        else:
            print(f"> {name} ... {prim_stats.st_size()} <=ne=> {sec_stats.st_size()}")
            result.fehler += 1
    else:
        print(f">>> {sec_file} ... FEHLT")
        result.fehler += 1

print(result)
