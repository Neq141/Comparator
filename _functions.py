import fileinput
import hashlib
import os
import subprocess
from time import time as _time


def get_file_hash_sha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_file_hash_sha512(filename):
    sha512_hash = hashlib.sha512()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha512_hash.update(byte_block)
    return sha512_hash.hexdigest()


def get_file_hash_md5(filename):
    md5_hash = hashlib.md5()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()


# runs the program and puts all the stdout and stderr in a log file
# returns the time it took to run the program :)
def _execute(file: str, Os: str) -> float:
    dt = lambda _t1, _t2: _t2 - _t1

    compiler: str

    if Os == 'windows':
        try:
            if file.endswith(".py"):
                compiler = "python"  # only 2 are supported for windows you can help by adding more
            elif file.endswith(".exe"):
                compiler = "./"
            else:
                assert NotImplementedError, f"Only 2 are supported for windows you can help by adding more\nYou cannot run {file}"
        except Exception as e:
            assert NotImplementedError, f"{e}\nThere was an error running the program, if the files are not ending " \
                                        f"with .py or .exe then they may not be a compiler which this program could use"
        try:
            cmd = [compiler, file]

            t1 = _time()
            # redirect output to null device
            with open('LOG.txt', 'w') as devnull:
                subprocess.run(cmd, stdout=devnull, stderr=devnull, shell=True)

            t2 = _time()
        except subprocess.CalledProcessError as e:
            assert e, f"Compiler error\nThe compiler {compiler} cannot be called, {compiler} may not be on your system"

    if Os == 'linux':
        if file.endswith(".py"):
            compiler = "python3"
        elif file.endswith(".out") or file.endswith(".bin"):
            compiler = "./"
        else:
            assert NotImplementedError, f"Only 2 are supported for linux you can help by adding more\nYou cannot run {file}"

        try:
            cmd = [compiler, file]

            t1 = _time()
            # redirect output to null device
            with open('/dev/null', 'w') as devnull:
                subprocess.run(cmd, stdout=devnull, stderr=devnull, shell=True)

            t2 = _time()
        except subprocess.CalledProcessError as e:
            assert e, f"Compiler error\nThe compiler {compiler} cannot be called, {compiler} may not be on your system"

    return dt(t1, t2)


def compare(files: list):
    raise NotImplementedError
    pass


def size(files: list) -> list:  # done

    size_list: list = []

    for file in files:
        size_list.append(os.path.getsize(file))

    return size_list


def time(files: list, Os: str) -> list:
    # only works with python for now

    time_list: list = []
    for i, file in enumerate(files):
        time_list.append(_execute(file, Os))

    return time_list


def lines_of_code(files: list) -> list:
    def get_file_line_length(filename):
        line_count = 0
        with fileinput.input(files=filename) as f:
            for _ in f:
                line_count += 1
        return line_count

    lines_of_code_list: list = []
    for file in files:
        lines_of_code_list.append(get_file_line_length(file))

    return lines_of_code_list


def sha256(files: list) -> list:
    # works
    hash_list: list = []
    for file in files:
        hash_list.append(get_file_hash_sha256(file))

    return hash_list


def sha512(files: list) -> list:
    # works
    hash_list: list = []
    for file in files:
        hash_list.append(get_file_hash_sha512(file))

    return hash_list


def md5(files: list) -> list:
    hash_list: list = []
    for file in files:
        hash_list.append(get_file_hash_md5(file))

    return hash_list
