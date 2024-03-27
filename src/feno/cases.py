import subprocess
import os
import glob

class Cases:

    @staticmethod
    def run(cases_file, source_readme, source_dir):
        # find all files in the directory terminatig with .tio or .vpl
        files = list(glob.iglob(source_dir + '/**', recursive=True))
        files = [f for f in files if os.path.isfile(f)]
        files = [f for f in files if f.endswith(".tio") or f.endswith(".vpl")]
        cmd = " ".join(["tko", "build", cases_file, source_readme] + files)
        output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)

