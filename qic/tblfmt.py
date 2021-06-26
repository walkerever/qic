#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import re
import csv
import copy
from wcwidth import wcswidth
from collections import defaultdict
from itertools import zip_longest
from .commandline import commandline


class SimpleTable:
    def __init__(self, data=None, header=None, cols=None, maxwidth=-1, noheader=False,tree=False,maxrows=2**30):
        self.__maxwidth = int(maxwidth)
        self.__noheader = noheader
        self.__maxrows = maxrows
        self.__tree = tree 
        if cols and re.search(",", cols):
            ncols = len(header)
            xmap = [int(i) for i in re.split(r",", cols) if int(i) < ncols]
            self.__header = [header[i] for i in xmap]
            self.__data = list()
            for d in data:
                self.__data.append([d[i] for i in xmap])
        else:
            self.__header = header or list()
            self.__data = data or list()
            if self.__noheader and len(self.__data) > 0 :
                self.__header = self.__data[0]
        self.__data = self.__data[:self.__maxrows]
        self.__num_of_cols = len(self.__header)

    def import_csv(self, csvfile, header=True):
        pass

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, pos):
        return self.__data[pos]

    def __add__(self, other):
        if self.__num_of_cols != other.__num_of_cols:
            return None
        return SimpleTable(self.__data + other.__data, self.__header)

    def __iadd__(self, other):
        if self.__num_of_cols != other.__num_of_cols:
            return None
        self.__data += other.__data

    def get_json(self):
        import json
        tbl = list()
        for r in self.__data:
            row = dict()
            for ix, val in enumerate(r):
                row[self.__header[ix]] = val
            tbl.append(row)
        return json.dumps(tbl, indent=2)

    def get_yaml(self):
        import yaml
        tbl = list()
        for r in self.__data:
            row = dict()
            for ix, val in enumerate(r):
                row[self.__header[ix]] = val
            tbl.append(row)
        return yaml.safe_dump(tbl, default_flow_style=False)

    def get_csv(self):
        import io
        si = io.StringIO()
        w = csv.writer(si)
        if self.__header:
            w.writerow(self.__header)
        for r in self.__data:
            w.writerow(r)
        return si.getvalue()

    def get_html(self):
        res = '<table border=1 style="border-collapse:collapse;">\n'
        res += "<tr>\n"
        for h in self.__header:
            res += "<td><b>" + str(h) + "</b></td>\n"
        res += "</tr>\n"
        for row in self.__data:
            res += "<tr>\n"
            for c in row:
                if not c :
                    if c == 0 :
                        c = "0"
                    else :
                        c = ""
                res += "<td>" + str(str(c).replace("\n", "<br>")) + "</td>\n"
            res += "</tr>\n"
        return res

    def repr_pivot(self):
        maxwidth = max([wcswidth(h) for h in self.__header])
        fmtstr = "{:" + str(maxwidth) + "} : {}"
        res = ""
        for r, row in enumerate(self.__data):
            if r > 0:
                res += "--\n"
            for i, c in enumerate(row):
                res += fmtstr.format(self.__header[i], c) + "\n"
        return res

    def __wcswidth_x(self, s):
        res = 0
        for ln in s.splitlines():
            wclen = wcswidth(ln)
            if wclen > res:
                res = wclen
        return res

    def __splitstring(self, s, maxwidth):
        result = list()
        for ln in s.splitlines():
            if wcswidth(ln) <= maxwidth:
                result.append(ln)
            else:
                left = ln
                while left:
                    start = 0
                    end = min(maxwidth, len(left))
                    while wcswidth(left[start:end]) > maxwidth:
                        end -= 1
                    result.append(left[start:end])
                    left = left[end:]
        return result

    def __splitrow(self, row):
        if self.__maxwidth < 20:
            return zip_longest(*[c.splitlines() for c in row], fillvalue="")
        else:
            return zip_longest(
                *[self.__splitstring(str(c), self.__maxwidth) for c in row],
                fillvalue=""
            )

    def __repr__(self):
        width = [0 for _ in range(len(self.__header))]
        for row in self.__data + [self.__header]:
            for ix, col in enumerate(row):
                if not col :
                    if col == 0 :
                        col = "0"
                    else :
                        col = ""
                if ix > len(width) - 1:
                    break
                wclen = self.__wcswidth_x(str(col))
                if wclen > width[ix]:
                    width[ix] = wclen
        if self.__maxwidth >= 20:
            width = [min(w, self.__maxwidth) for w in width]
        twidth = copy.copy(width)
        for ix, w in enumerate(twidth):
            twidth[ix] = (
                w - wcswidth(str(self.__header[ix])) + len(str(self.__header[ix]))
            )
        def supports_color():
            plat = sys.platform
            supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
            is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
            m = re.search(r"^xterm",os.environ.get("TERM","n/a"),re.IGNORECASE)
            ret,out,err = commandline.qx("uname -s")
            iscygwin = re.search(r"cygwin",out,re.IGNORECASE)
            return (is_a_tty or iscygwin) and (m or supported_platform)
        class bcolors:
            HEADER = '\033[95m'
            OKBLUE = '\033[94m'
            OKCYAN = '\033[96m'
            OKGREEN = '\033[92m'
            WARNING = '\033[93m'
            FAIL = '\033[91m'
            ENDC = '\033[0m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
        fmtstr = "".join(["{:" + str(l + 1) + "}" for l in twidth])
        res = ""
        if not self.__noheader:
            if supports_color() :
                res += bcolors.BOLD + fmtstr.format(*self.__header).rstrip() + bcolors.ENDC + "\n"
                res += ("-" * (sum(width) + len(width) - 1)) + "\n"
            else :
                res += fmtstr.format(*self.__header).rstrip() + "\n"
                res += ("-" * (sum(width) + len(width) - 1)) + "\n"
        oldrow = None
        for ix,r in enumerate(self.__data):
            if ix == 0 :
                row = [str(c) if c or c==0 else "" for c in r]
                oldrow = r
            else :
                if not self.__tree :
                    row = [str(c) if c or c==0 else "" for c in r]
                else :
                    nr = [ c for c in r ]
                    for ix, c in enumerate(r) :
                        if (oldrow[ix] is None and c is None) or c == oldrow[ix] :
                            nr[ix] = ""
                        else :
                            break
                    row = [str(c) if c or c==0 else "" for c in nr]
                    oldrow = r
            if len(row) < len(width):
                row.extend([""] * (len(width) - len(row)))
            for t in self.__splitrow(row):
                twidth = copy.copy(width)
                for ix, w in enumerate(twidth):
                    twidth[ix] = w - wcswidth(str(t[ix])) + len(str(t[ix]))
                fmtstr = "".join(["{:" + str(l + 1) + "}" for l in twidth])
                res += fmtstr.format(*t).rstrip() + "\n"
        return res


def tokenize(s):
    offset = 0
    tokens = list()
    while True:
        m = re.search(r"\S+\s*", s[offset:])
        if m:
            tokens.append([offset + m.start(), offset + m.end(), m.group().rstrip()])
            offset += m.end()
        else:
            break
    tokens[-1][1] = -1
    return tokens


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--lineno",
        dest="lineno",
        default=False,
        action="store_true",
        help="show line no.",
    )
    parser.add_argument("-H", "--header", dest="header", help="header columns")
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument(
        "-c",
        "--column",
        action="append",
        dest="column",
        help="column names. used when there" "re spaces within.",
    )
    parser.add_argument(
        "-C",
        "--dump-column",
        dest="dumpcols",
        help="only print columns indentified by index numbers.",
    )
    parser.add_argument(
        "-s", "--sortby", dest="sortby", help="column id starts with 0."
    )
    parser.add_argument(
        "-b",
        "--sep-char",
        dest="sepchar",
        default="\s+",
        help="char to seperate columns",
    )
    parser.add_argument(
        "-w",
        "--maxwidth",
        dest="maxwidth",
        type=int,
        default=-1,
        help="max col width when print in console, min==20",
    )
    parser.add_argument(
        "-t",
        "--table",
        dest="table",
        action="store_true",
        default=False,
        help="input preformatted by spaces. header should not include spaces.",
    )
    parser.add_argument(
        "-v",
        "--pivot",
        dest="pivot",
        action="store_true",
        default=False,
        help="pivot wide tables.",
    )
    parser.add_argument(
        "-T",
        "--tree",
        dest="tree",
        action="store_true",
        default=False,
        help="indicate the table is of tree struture",
    )
    parser.add_argument("-F", "--format", dest="format", help="json,yaml,csv,html")
    parser.add_argument(
        "-d",
        "--dataonly",
        dest="dataonly",
        action="store_true",
        default=False,
        help="indicate there's no header",
    )
    parser.add_argument(
        "-X",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="debug mode",
    )
    args = parser.parse_args()

    colsdict = defaultdict()
    colsdict_revert = defaultdict()
    if args.column:
        for c in args.column:
            oc = c
            mc = re.sub("\s", "_", oc)
            colsdict[oc] = mc
            colsdict_revert[mc] = oc
    if args.header and colsdict:
        for c, nc in colsdict.items():
            args.header = re.sub(c, nc, args.header)
    xheader = None
    header = list()
    if args.lineno:
        header.append("#")
    if args.header:
        mhdr = args.header
        if not args.table:
            header.extend(re.split(r"{}".format(args.sepchar), mhdr))
        else:
            xheader = tokenize(mhdr)
            header = [v.rstrip() for (s, t, v) in xheader]
    data = list()
    lno = 0
    INPUT = sys.stdin
    if args.infile:
        with open(args.infile, "r") as f:
            INPUT = f.readlines()
    for ln in INPUT:
        if not ln or not re.search(r"\S+", ln):
            continue
        if not header:
            for c, nc in colsdict.items():
                ln = re.sub(c, nc, ln)
        if not args.table:
            arr = re.split(r"{}".format(args.sepchar), ln.rstrip())
        else:
            if xheader:
                arr = [ln[s:t].rstrip() for (s, t, v) in xheader]
            else:
                for c, nc in colsdict.items():
                    ln = re.sub(c, nc, ln)
                xheader = tokenize(ln)
                if args.lineno:
                    header = ["#"] + [v.rstrip() for (s, t, v) in xheader]
                else:
                    header = [v.rstrip() for (s, t, v) in xheader]
                continue
        if len(header) == 0 or (args.lineno and len(header) == 1):
            if not args.table:
                header.extend(arr)
        else:
            lno += 1
            if args.lineno:
                data.append([str(lno)] + arr)
            else:
                data.append(arr)
    oheader = list()
    for h in header:
        nh = colsdict_revert.get(h, h)
        oheader.append(nh)
    if args.dataonly:
        data = [oheader] + data
    if args.sortby:

        def fsort(x):
            v = list()
            for i in re.split(r",", args.sortby):
                v0 = x[int(i)] or ""
                if re.match(r"^\d+(\.\d*)*$", v0):
                    v.append(float(v0))
                else:
                    v.append(0)
                v.append(v0)
            return v

        data = sorted(data, key=fsort)
    if args.pivot:
        print(SimpleTable(header=oheader, data=data, cols=args.dumpcols).repr_pivot())
    else:
        t = SimpleTable(
            header=oheader,
            data=data,
            cols=args.dumpcols,
            maxwidth=args.maxwidth,
            noheader=args.dataonly,
            tree=args.tree,
        )
        if args.format == "json":
            print(t.get_json(), end="")
        elif args.format == "yaml":
            print(t.get_yaml(), end="")
        elif args.format == "csv":
            print(t.get_csv(), end="")
        elif args.format == "html":
            print(t.get_html(), end="")
        else:
            print(t, end="")


if __name__ == "__main__":
    main()
