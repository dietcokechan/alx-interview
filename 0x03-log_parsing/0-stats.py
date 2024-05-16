#!/usr/bin/python3
""" Log parsing """
import sys


if __name__ == '__main__':
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    statusc = {i: 0 for i in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for i, j in sorted(stats.items()):
            if j:
                print("{}: {}".format(i, j))

    try:
        for line in sys.stdin:
            count += 1
            ls = line.split()
            try:
                c = ls[-2]
                if c in statusc:
                    statusc[c] += 1
            except BaseException:
                pass
            try:
                filesize += int(ls[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(statusc, filesize)
        print_stats(statusc, filesize)
    except KeyboardInterrupt:
        print_stats(statusc, filesize)
        raise
