import os, sys
import argparse
import configparser
import _functions as functions

OS_TYPE: str = sys.platform
if OS_TYPE.startswith("win"):
    OS_TYPE = "windows"
if OS_TYPE.endswith("nix"):
    OS_TYPE = "linux"


def parse_args():
    config = configparser.ConfigParser()
    config.read("config.ini")

    return {
        "SIZE": config["DEFAULT"]["SIZE"],
        "TIME": config["DEFAULT"]["TIME"],
        "LINES_OF_CODE": config["DEFAULT"]["LINES_OF_CODE"],
        "SHA256": config["DEFAULT"]["SHA256"],
        "SHA512": config["DEFAULT"]["SHA512"],
        "MD5": config["DEFAULT"]["MD5"]
    }


def main(to_compare: dict):
    config = parse_args()

    for key, value in to_compare.items():
        if value is not None:
            if key == "compare":  # config mode
                if config["SIZE"]:

                    sizes: list = functions.size(to_compare["compare"])
                    print("Sizes are:")
                    for i, file_name in enumerate(sizes):
                        print(f"{i} : {compare[i]} = {sizes[i]} bytes")

                if config["TIME"]:
                    times: list = functions.time(to_compare["compare"], OS_TYPE)
                    print("Times are:")
                    for i, file_name in enumerate(times):
                        print(f"{i} : {compare[i]} = {float(times[i])}")

                if config["LINES_OF_CODE"]:
                    lines: list = functions.lines_of_code(to_compare["compare"])
                    print("Lines of code are:")
                    for i, file_name in enumerate(lines):
                        print(f"{i} : {compare[i]} = {lines[i]}")
                if config["SHA256"]:
                    hashes: list = functions.sha256(to_compare["compare"])
                    print("SHA256 Hashes are:")
                    for i, file_name in enumerate(hashes):
                        print(f"{i} : {compare[i]} = {hashes[i]}")

                if config["SHA512"]:
                    hashes: list = functions.sha512(to_compare["compare"])
                    print("SHA512 Hashes are:")
                    for i, file_name in enumerate(hashes):
                        print(f"{i} : {compare[i]} = {hashes[i]}")
                if config["MD5"]:
                    hashes: list = functions.md5(to_compare["compare"])
                    print("Hashes are:")
                    for i, file_name in enumerate(hashes):
                        print(f"{i} : {compare[i]} = {hashes[i]}")

            if key == "size":  # worked last time I checked

                sizes: list = functions.size(to_compare["size"])
                print("Sizes are:")
                for i, file_name in enumerate(sizes):
                    print(f"{i} : {size[i]} = {sizes[i]} bytes")

            if key == "time":
                times: list = functions.time(to_compare["time"], OS_TYPE)
                print("Times are:")
                for i, file_name in enumerate(times):
                    print(f"{i} : {time[i]} = {float(times[i])}")

            if key == "lines_of_code":
                lines: list = functions.lines_of_code(to_compare["lines_of_code"])
                print("Lines of code are:")
                for i, file_name in enumerate(lines):
                    print(f"{i} : {lines_of_code[i]} = {lines[i]}")

            if key == "sha256":
                hashes: list = functions.sha256(to_compare["sha256"])
                print("Hashes are:")
                for i, file_name in enumerate(hashes):
                    print(f"{i} : {sha256[i]} = {hashes[i]}")

            if key == "sha512":
                hashes: list = functions.sha512(to_compare["sha512"])
                print("Hashes are:")
                for i, file_name in enumerate(hashes):
                    print(f"{i} : {sha512[i]} = {hashes[i]}")

            if key == "md5":
                hashes: list = functions.md5(to_compare["md5"])
                print("Hashes are:")
                for i, file_name in enumerate(hashes):
                    print(f"{i} : {md5[i]} = {hashes[i]}")


if __name__ == '__main__':
    # gets the arguments from argv
    parser = argparse.ArgumentParser(
        prog='comparator.py',
        description='Compares any number of files in anyway that you can imagine',
        epilog="don't forget to star this repository on github #Link_to_come")

    parser.add_argument("-c", "--compare", nargs='*', help="compares files by the default config")
    parser.add_argument("-s", "--size", nargs='*', help="compares files by the size")
    parser.add_argument("-t", "--time", nargs='*', help="compares files by the time it takes to run")
    parser.add_argument("-len", "--lines-of-code", nargs='*', help="compares files by lines of code")
    parser.add_argument("--sha256", nargs='*', help="compares files sha256 hashes")
    parser.add_argument("--sha512", nargs='*', help="compares files sha512 hashes")
    parser.add_argument("--md5", nargs='*', help="compares files md5 hashes")
    args = parser.parse_args()

    # access and notify the user

    if compare := args.compare:
        print(f"Comparing files by the default config: {' '.join(args.compare)}")
    if size := args.size:
        print(f"Comparing files by size: {' '.join(size)}")
    if time := args.time:
        print(f"Comparing files by time: {' '.join(time)}")
    if lines_of_code := args.lines_of_code:
        print(f"Comparing files by lines of code: {' '.join(lines_of_code)}")
    if sha256 := args.sha256:
        print(f"Comparing files by sha256 hash: {' '.join(sha256)}")
    if sha512 := args.sha512:
        print(f"Comparing files by sha512 hash: {' '.join(sha512)}")
    if md5 := args.md5:
        print(f"Comparing files by md5 hash: {' '.join(md5)}")

    to_compare: dict = {
        "compare": compare,
        "size": size,
        "time": time,
        "lines_of_code": lines_of_code,
        "sha256": sha256,
        "sha512": sha512,
        "md5": md5
    }

    main(to_compare)

    # checks if there is any arguments passed
    if len(sys.argv) == 1:
        print(parser.format_help())
