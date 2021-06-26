#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import json
import traceback
from .tblfmt import SimpleTable

def prepare_table(xjson,xheader=None) :
    header=list()
    if xheader :
        header = [ h for h in xheader.split(",") if h]
    data = list()
    try:
        if type(xjson) is str :
            js = json.loads(xjson)
        else :
            js = xjson
        if type(js) is list and all([type(i) is list for i in js]) :
            for row in js :
                r=list()
                for col in row :
                    r.append(str(col))
                data.append(r)
        elif type(js) is list and all([type(i) is dict for i in js]) :
            # now each row is a dict
            if not header :
                loaded=set()
                for row in js :
                    for k in row.keys() :
                        if k not in loaded :
                            header.append(k)
                            loaded.add(k)
            for row in js :
                r=list()
                for h in header :
                    r.append(row.get(h,""))
                data.append(r)
        else :
            print("# not supported format.")
            print(json.dumps(js,indent=2))
            return (None,None)
    except:
        traceback.print_exc()
        if args.debug:
            print(INPUT)
        return (None,None)
    if header :
        return (data,header)
    else :
        return (data[1:],data[0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument("-H", "--header", dest="header", help="optional header")
    parser.add_argument("-m", "--maxrows", dest="maxrows", type=int, default=2**30, help="max rows per table")
    parser.add_argument("-X", "--debug", dest="debug", action="store_true", default=False, help="debug mode",)
    args = parser.parse_args()

    if args.infile:
        if not os.path.isfile(args.infile):
            print("# {} not exists.".format(args.infile))
        with open(args.infile, "r") as f:
            INPUT = f.read()
    else:
        INPUT = sys.stdin.read()

    data,header = prepare_table(INPUT,args.header)

    if args.debug :
        print("header = ",header)
        print("data = ",data)
    #data=None, header=None, cols=None, maxwidth=-1, noheader=False,tree=False
    print(SimpleTable(data=data,header=header,maxrows=args.maxrows,noheader=True if not header else False))

if __name__ == "__main__":
    main()
