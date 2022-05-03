import sys
import argparse
import os
import json
import yaml
import xmltodict
import re
import traceback
import time
import random
import string
from functools import partial
from .tblfmt import SimpleTable
from .commandline import commandline
from .json2table import prepare_table
from json2html import JsonConverter
from collections import (deque,defaultdict)
from types import FunctionType
from pygments import highlight
from pygments.lexers import (JsonLexer,YamlLexer,XmlLexer,IniLexer,HtmlLexer,guess_lexer)
from pygments.lexers.python import PythonLexer
from pygments.formatters import Terminal256Formatter
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer

sys.path.append(os.getcwd())

print = partial(print,flush=True)

DSQ_DOT="_yx_dsq_dot_yx_"

def _json(ds) :
    return json.dumps(ds,indent=2,sort_keys=True)
def _xml(ds) :
    import xml.dom.minidom as dom
    import dicttoxml
    xmlstr = dicttoxml.dicttoxml(ds).decode()
    xml = dom.parseString(xmlstr)
    return xml.toprettyxml()
def _yaml(ds) :
    return yaml.dump(ds,default_flow_style=False,explicit_start=True, explicit_end=False)
def _l(ds,brk="\n") :
    return brk.join([str(i) for i in ds])
def _h(ds) :
    return JsonConverter(ds).json2html()
def _zh(ds) :
    return JsonConverter(ds,recursive=True,collapseandexpand=True).json2html()
def _l2t(xjson,header=None,maxcolwidth=100) :
    data,header=prepare_table(xjson,header)
    return SimpleTable(data=data,header=header,maxwidth=maxcolwidth)
def _l2pt(xjson,header=None) :
    data,header=prepare_table(xjson,header)
    return SimpleTable(data=data,header=header).repr_pivot()
def _t(data=list(),header=None,dataonly=False,maxcolwidth=100) :
    return SimpleTable(data=data,header=header,noheader=dataonly,maxwidth=maxcolwidth)
def _pt(data=list(),header=None,dataonly=False) :
    return SimpleTable(data=data,header=header,noheader=dataonly).repr_pivot()
def _flatlist(ds,ret=None) :
    if ret is None :
        ret = list()
    if type(ds) is list :
        for i in ds :
            _flatlist(i,ret)
    else :
        ret.append(ds)
    return ret
def _qx(cmd) :
    try :
        ret,out,err = commandline.qx(cmd)
        print(out)
        if err :
            print(err)
    except :
        traceback.print_exc()
def _rawstr(ds,last="_"):
    res = ""
    if type(ds) is dict :
        for k,v in ds.items() :
            if type(v) in [dict,list] :
                res += _rawstr(v,last+"."+k) 
            else :
                if type(v) is str :
                    vstr = '"{}"'.format(v.replace('"','\\"'))
                else :
                    vstr = str(v)
                res += last + "." + k +"="+ vstr  + "\n"
    if type(ds) is list :
        for i,v in enumerate(ds) :
            if type(v) in [dict,list] :
                res += _rawstr(v,last+"["+str(i)+"]") 
            else :
                if type(v) is str :
                    vstr = '"{}"'.format(v.replace('"','\"'))
                else :
                    vstr = str(v)
                res += last+"["+str(i)+"]=" + str(v) + "\n"
    return res

_fl=_flatlist
_j=_json
_x=_xml
_y=_yaml

def dsq_main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="code", nargs='?', default="_", help="code to compile. may be a file.")
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument("-t", "--srctype", dest="srctype", default="JSON", help="JSON,YAML or XML")
    parser.add_argument("-i", "--indent", dest="indent", default=4, help="how many spaces for indent. default 4.")
    parser.add_argument("-l", "--rows", dest="rows",type=int, default=2**30, help="use this to shrink each list included. useful for DS including too many records.")
    parser.add_argument("-o", "--output", dest="outfile",default=None,help="write as well as console. ansi color kept.")
    parser.add_argument("-m", "--modules", dest="modules", help="import modules.")
    parser.add_argument("-K", "--keys", dest="keys_included", help="only keep these keys.")
    parser.add_argument("-E", "--nokeys", dest="keys_excluded", help="these keys should be excluded.")
    parser.add_argument("-F", "--functionize", dest="func", action="store_true", default=False, help="wrap code into an internal function",)
    parser.add_argument("-s", "--rawstr", dest="rawstr", action="store_true", default=False, help="output raw stings for easy grep",)
    parser.add_argument("-n", "--origin", dest="origin", action="store_true", default=False, help="no change to the input stream and take it as is. no expanding.")
    parser.add_argument("-I", "--interactive", dest="interactive", action="store_true", default=False, help="interactive mode",)
    parser.add_argument("-p", "--plain", dest="plain", action="store_true", default=False, help="force no color code",)
    parser.add_argument("-c", "--compact", dest="compact", action="store_true", default=False, help="dump data structure in compact mode",)
    parser.add_argument("-C", "--keepcolor", dest="keepcolor", action="store_true", default=False, help="do not remove ANSI color code from input stream.",)
    parser.add_argument("-X", "--debug", dest="debug", action="count", default=False, help="debug mode",)
    _x_args = parser.parse_args()

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

    def warn(s) :
        return bcolors.WARNING + s + bcolors.ENDC
    def notify(s) :
        return bcolors.OKCYAN + s + bcolors.ENDC
    def critical(s) :
        return bcolors.FAIL + s + bcolors.ENDC
    def print_err(s,lvl=0) :
        if lvl == 1 :
            print(notify(s),file=sys.stderr)
            return
        if lvl == 2 :
            print(warn(s),file=sys.stderr)
            return
        if lvl == 3 :
            print(critical(s),file=sys.stderr)
            return
        print(s,file=sys.stderr)

    if _x_args.debug >=2 :
        print_err("# args = ",lvl=1)
        strargs = "\n".join([str(v)+"="+str(getattr(_x_args,v)) for v in vars(_x_args)])
        print_err(strargs)

    def supports_color():
        plat = sys.platform
        supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
        is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        m = re.search(r"^xterm",os.environ.get("TERM","n/a"),re.IGNORECASE)
        try :
            ret,out,err = commandline.qx("uname -s")
        except :
            return False
        iscygwin = re.search(r"cygwin",out,re.IGNORECASE)
        return (is_a_tty or iscygwin) and (m or supported_platform)
    if not _x_args.plain :
        colored = True
        if not supports_color() :
            colored = False
        if os.environ.get("force_ansicolor","") in ["true","yes","y","1"] :
            colored = True
        _x_args.plain = colored
    if _x_args.keys_included :
        _xdt_keys_included = dict()
        for w in  _x_args.keys_included.split(",") :
            recursive = 0
            if re.search(r"(\*|\/|\+)+$",w) :
                recursive = 1
                w = re.sub(r"(\*|\/|\+)+$","",w)
            if w :
                _xdt_keys_included[w.lower()] = recursive
    else :
        _xdt_keys_included = None
    if _x_args.keys_excluded :
        _xset_keys_excluded = set([w.lower() for w in _x_args.keys_excluded.split(",") if w])
    else :
        _xset_keys_excluded = None

    def cutkeys_helper(ds,inkeys,outkeys) :
        if not inkeys and not outkeys :
            return ds
        if type(ds) is dict :
            ds = {k:v for k, v in ds.items() if (not inkeys or k.lower() in inkeys) and (not outkeys or k.lower() not in outkeys)}
            for k,v in ds.items() :
                if not inkeys or (inkeys and k.lower() in inkeys and inkeys[k.lower()] != 1) :
                    ds[k] = cutkeys_helper(v,inkeys,outkeys)
        if type(ds) is list :
            for i,v in enumerate(ds) :
                if type(v) in [dict,list] :
                    ds[i] = cutkeys_helper(v,inkeys,outkeys)
        return ds
    def cutkeys(ds,inkeys=_xdt_keys_included,outkeys=_xset_keys_excluded) :
        ds = cutkeys_helper(ds,inkeys,outkeys)
        if _xset_keys_excluded :
            ds = cutkeys_helper(ds,inkeys=dict(),outkeys=outkeys)
        return ds

    def shrink_list(ds,pos="_") :
        if type(ds) is dict :
            for k,v in ds.items() :
                if type(v) in [dict,list] :
                    ds[k] = shrink_list(v,pos+".{}".format(k))
        if type(ds) is list :
            oldlen = len(ds)
            if _x_args.rows < oldlen :
                print_err("# {}[] {} -> {}".format(pos,oldlen,_x_args.rows),lvl=1)
            ds = ds[:_x_args.rows]
            for i, v in enumerate(ds) :
                if type(v) in [dict,list] :
                    ds[i] = shrink_list(v,pos+"[{}]".format(i))
        return ds

    def collect_keys(ds, dt) :
        if type(ds) is dict :
            for k, v in ds.items() :
                dt[k.lower()].add(k)
                collect_keys(v,dt)
        elif type(ds) in [list,tuple] :
            for i in ds :
                collect_keys(i,dt)
        else :
            pass

    def show_result(res) :
        def print_tee(s) :
            if _x_args.outfile :
                with open(_x_args.outfile,"a") as fw :
                    fw.write(s)
            print(s)
        if _x_args.outfile :
            with open(_x_args.outfile,"w") as fw :
                pass
            xprint = print_tee
        else :
            xprint = print

        if not res :
           return
        if type(res) is str :
            if _x_args.plain :
                xprint(res) 
                return
            try :
                if _x_args.rawstr :
                    xprint(highlight(res,IniLexer(),Terminal256Formatter()))
                    return
            except :
                pass
            try :
                xprint(highlight(res,HtmlLexer(),Terminal256Formatter()))
                return
            except :
                pass
            try :
                json.loads(res)
                if _x_args.rows != 2**30 :
                    res = json.loads(res)
                    res = shrink_list(res)
                    res = json.dumps(res,indent=2,sort_keys=True)
                xprint(highlight(res,JsonLexer(),Terminal256Formatter()))
                return
            except :
                pass
            try :
                yaml.safe_load(res)
                if _x_args.rows != 2**30 :
                    res = yaml.safe_load(res)
                    res = shrink_list(res)
                    res = yaml.dump(res,default_flow_style=False,explicit_start=True, explicit_end=False)
                xprint(highlight(res,YamlLexer(),Terminal256Formatter()))
                return
            except :
                pass
            try :
                xmltodict.parse(res)
                xprint(highlight(res,XmlLexer(),Terminal256Formatter()))
                return
            except :
                pass
            xprint(highlight(res,guess_lexer(res),Terminal256Formatter()))
        else :
            res = cutkeys(res)
            res = shrink_list(res)
            if _x_args.rawstr :
                if _x_args.plain :
                    xprint(_rawstr(res))
                else :
                    xprint(highlight(_rawstr(res),IniLexer(),Terminal256Formatter()))
            else :
                try :
                    if _x_args.plain :
                        if _x_args.compact :
                            xprint(json.dumps(res))
                        else :
                            xprint(json.dumps(res,indent=2))
                    else :
                        if _x_args.compact :
                            xprint(highlight(json.dumps(res),JsonLexer(),Terminal256Formatter()))
                        else :
                            xprint(highlight(json.dumps(res,indent=2),JsonLexer(),Terminal256Formatter()))
                except :
                    xprint(str(res))

    def removespaces(code) :
        if not code or "{" not in code or "}" not in code :
            return code
        xcode = code
        m = re.search(r"\{.*?\s+.*?\}",xcode) 
        while m :
            before = code[:m.start()]
            end = code[m.end():]
            chain = m.group(0)
            newchain = re.sub(r"\s+","",chain)
            xcode = before + newchain + end
            m = re.search(r"\{.*?\s+.*?\}",xcode) 
        return xcode
        
    def log_special(code) :
        ret = dict()
        if not code :
            return (code,ret)
        if not ("<" in code and ">" in code) :
            return (code,ret)
        m = re.search(r"\<\s*([^\<\>]+?)\s*\>",code) 
        while m :
            full = m.group(0)
            tokeep = m.group(1)
            special = "".join([random.choice(string.ascii_lowercase) for _ in range(10)])
            code = code.replace(full,special)
            ret[special] = tokeep
            if _x_args.debug > 2:
                print("# [passwd] {} -> {}".format(tokeep,special))
            m = re.search(r"\<\s*([^\<\>]+?)\s*\>",code) 
        return (code, ret)
            

    def choiceexpand(code) :
        if not code :
            return code
        m = re.search(r"((\w|\-|\d|\.|\[|\]|\(|\))+?)\.\{\s*(\S+?\s*(,\s*\S+?)*)\s*\}",code)
        if not m :
            return code
        if code.count("{") > 1 :
            print_err("# recusive choices are not supported.",lvl=2)
            return code
        before = code[:m.start()]
        end = code[m.end():]
        dt = m.group(1)
        keys = m.group(3)
        #print(keys)
        res = before + "{" + ",".join(["'{}'".format(k.replace(".",DSQ_DOT))  + ":" + "{}.{}".format(dt,k) for k in keys.split(",")]) + "}" + end
        if _x_args.debug > 2:
            print("# [choice] before = ",code)
            print("# [choice] after  = ",res)
        return res

    def insert_spaces(code) :
        return code.replace("(","( ").replace(")"," )")

    def listexpand(code) :
        def hasslice(code) :
            if re.search(r"\[(\d|\:|\-|\s)*\]",code) and not re.search(r"\[(\s|\d|\-)+\]",code) :
                return True
            return False
        if not code or not hasslice(code) :
            return code
        def listexpand_helper(code) :
            if not hasslice(code) :
                return code
            xcode = code
            tvar = "_" + "".join([random.choice(string.ascii_lowercase) for _ in range(3)])
            #l,x = xcode.split("[]",1)
            m = re.match(r"(.*?)(\[(\d|\:|\s|\-)*\])(.*)",code)
            b,i,a = m.group(1),m.group(2),m.group(4)
            if re.sub(r"\s+","",i) in [ "[]", "[:]" ] :
                i=""
            return "[ {} for {} in {} ]".format(listexpand_helper(tvar+a),tvar,b+i)
        res = ""
        xcode = insert_spaces(code)
        _x_m = re.search(r"\S*\[(\d|\:|\-|\s)*\]\S*",xcode,re.DOTALL)
        while _x_m :
            before = xcode[:_x_m.start()]
            end = xcode[_x_m.end():]
            chain = _x_m.group(0)
            res += before + listexpand_helper(chain)
            xcode = end
            _x_m = re.search(r"\S*\[(\d|\:|\-|\s)*\]\S*",xcode,re.DOTALL)
        res += xcode
        if _x_args.debug > 2:
            print("# [ list ] before = ",code)
            print("# [ list ] after  = ",res)
        return res

    def dotexpand(code,keydt=None) :
        chgsin = code
        _x_m = re.search(r"\{(\w|\.)+\}|(\w+|\]|\))(\.\w+|\.\+\w+)+",chgsin,re.DOTALL)
        res=""
        while _x_m :
            before = chgsin[:_x_m.start()]
            end = chgsin[_x_m.end():]
            chain = _x_m.group(0)
            newchain = ""
            words = chain.split(".") 
            for i,w in enumerate(words) :
                if w.startswith("+") or (i==len(words)-1 and end.startswith("(")) :
                    nw = w.lstrip("+")
                    newchain += "." + nw
                else :
                    try :
                        if newchain == "" :
                            stest = w
                        else :
                            stest = newchain + "." + w
                        eval(stest)
                        newchain = stest
                        continue
                    except :
                        pass
                    nw = w.lower()
                    if nw in keydt and len(keydt[nw]) == 1 :
                        nw = list(keydt[nw])[0]
                        if _x_args.debug and w != nw :
                            print_err("# keyword replcement : {} -> {}".format(w,nw),lvl=1)
                    if newchain :
                        newchain += "['"+ nw + "']"
                    else :
                        newchain += nw
            res += before + newchain 
            chgsin = end
            _x_m = re.search(r"\{(\w|\.)+\}|(\w+|\]|\))(\.\w+|\.\+\w+)+",chgsin,re.DOTALL)
        res = res+chgsin
        if _x_args.debug > 2:
            print("# [ dot  ] before = ",code)
            print("# [ dot  ] after  = ",res)
        return res

    def runcode(code,data=None) :
        _ = data
        if not code :
            return
        if not _x_args.origin :
            code = code.replace("\\n","\n")
            code = removespaces(code)
            code,passbook = log_special(code)
            code = listexpand(code)
            code = choiceexpand(code)
            code = dotexpand(code,_x_key_dict)
            code = code.replace(DSQ_DOT,".")
            if passbook :
                for k,v in passbook.items() :
                    code = code.replace(k,v)
        if _x_args.debug:
            print_err("# run : ",lvl=1)
            print_err(code)
        attempts=0 
        err=""
        while True :
            try :
                if attempts == 0 :
                    if re.search("^\w+\s*=\S+",code) or len(code.splitlines())>1 or re.search(r"^(for|while)\s+",code) :
                        attempts += 1
                        continue
                    if _x_args.debug >= 2:
                        print_err("# eval : ",lvl=1)
                        print_err(code)
                    res = eval(code)
                    show_result(res)
                    return
                elif attempts == 1 :
                    if _x_args.debug >= 2:
                        print_err("# exec :",lvl=1)
                        print_err(code)
                    exec(code)
                    return
                else :
                    print_err("# expanded code :",lvl=2)
                    print_err("{}".format(code),lvl=2)
                    print_err("# {}".format(err.splitlines()[-1]),lvl=2)
                    #if _x_args.debug :
                    #    print_err(err,lvl=2)
                    return
            except :
                err += traceback.format_exc()
                attempts += 1
                continue

    INPUT = None
    if _x_args.infile:
        if not os.path.isfile(_x_args.infile):
            print_err("# {} not exists.".format(_x_args.infile),lvl=2)
        with open(_x_args.infile, "r") as f:
            INPUT = f.read()
            INPUT = INPUT.strip()
    else : 
        if not _x_args.interactive :
            import signal
            TIMEOUT = 10
            def interrupted(signal, frame):
                print("# timeout/no input from STDIN detected.",
                      file=sys.stderr,
                      flush=True)
                parser.print_help()
                sys.exit(0)
        
            try :
                signal.signal(signal.SIGALRM, interrupted)
                signal.alarm(TIMEOUT)
            except :
                pass
            INPUT = sys.stdin.read()
            signal.alarm(0)
            INPUT = INPUT.strip()
    if not INPUT :
        INPUT = json.dumps({})

    if _x_args.debug >= 3 :
        print_err("# INPUT :",lvl=1)
        print_err(INPUT)

    if not _x_args.keepcolor :
        INPUT = re.sub(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]',"",INPUT)


    try :
       if _x_args.srctype.upper() == "JSON" :
            _ = json.loads(INPUT)
       elif _x_args.srctype.upper() == "YAML" :
            _ = yaml.safe_load(INPUT)
       elif _x_args.srctype.upper() == "XML" :
            _ = xmltodict.parse(INPUT)
       else :
        print_err("# unsupported file type.",lvl=2)
        return -1
    except :
        print_err("# invalid JSON/YAML/XML.",lvl=2)
        traceback.print_exc()
        return -1

    if _x_args.debug >= 2 :
        print_err("# data loaded :",lvl=1)
        print_err(json.dumps(_,indent=2))

    _x_key_dict = defaultdict(set)
    collect_keys(_,dt=_x_key_dict)
    if _x_args.debug >= 2 :
        print_err("# keys collected : {}".format(str(_x_key_dict)),lvl=1)
    keys_extra= "_,_t,_x,_y,_j,_l,_tbl,_l2t,_l2pt,_pt,_qx,_rawstr,_flatlist,_fl".split(",")
    _x_word_completer = WordCompleter(sorted(list(set([x for x in _x_key_dict.keys()]+keys_extra))))
        
    if _x_args.modules :
        _x_args.modules = os.path.expanduser(_x_args.modules)
        _x_args.modules = os.path.expandvars(_x_args.modules)
        for m in _x_args.modules.split(",")  :
            if m :
                m.strip()
                if m.startswith("from ") :
                    exec(m)
                elif os.path.isfile(m) :
                    mpath = os.path.abspath(os.path.dirname(m))
                    mfile = os.path.basename(m) 
                    sys.path.append(mpath)
                    mn = mfile.replace(".py","")
                    import importlib
                    globals()[mn] = importlib.import_module(mn)
                elif os.path.isdir(m) :
                    mpath = os.path.abspath(m) 
                    sys.path.append(m)
                else :
                    import importlib
                    globals()[m] = importlib.import_module(m)

    def run_as_func(code,_=_) :
        fname = "".join([random.choice(string.ascii_letters) for _ in range(20)])
        newcode = ""
        if _x_args.modules :
            for m in _x_args.modules.split(",")  :
                if m :
                    m.strip()
                    if m.startswith("from ") :
                        newcode += m + "\n"
                    else :
                        newcode += "import " + m + "\n"
        newcode += "def {}(_) :\n".format(fname)
        code = code.replace("\\n","\n")
        for ln in code.splitlines() :
            ln = ln.rstrip()
            newcode += " "*(int(_x_args.indent)) + ln + "\n"
        code = listexpand(newcode)
        code = choiceexpand(newcode)
        code = dotexpand(newcode,_x_key_dict)
        code = code.replace(DSQ_DOT,".")
        if _x_args.debug :
            print_err("# code to compile : ",lvl=1)
            print_err(code)
        xcode = compile(code,"<string>","exec")
        cobj = None
        for c in xcode.co_consts :
            if c and type(c) not in [str,int,tuple] :
                cobj = c
                break
        if not cobj :
            print_err("# no code object found.",lvl=2)
            sys.exit(-1)
        xfunc = FunctionType(cobj, globals())
        print(xfunc(_))

    if os.path.isfile(_x_args.code) :
        code = open(_x_args.code,"r").read()
    else :
        code = _x_args.code
    if re.match(r"^\s*\_\w+\s*$",code) :
        code = code + "(_)"

    xcode = code
    xcode = xcode.replace("\\n","\n")
    if any([re.match(r"^\s*return.*",ln) for ln in xcode.splitlines()]) \
       or any([re.match(r"^\s*return.*",ln) for ln in xcode.split(";")])  :
        _x_args.func = True

    if _x_args.code and not _x_args.func :
        if not (_x_args.interactive and _x_args.code == "_") :
            runcode(code,data=_)

    if _x_args.code and _x_args.func :
        x = run_as_func(code, _)
        if x :
            print(x)

    if _x_args.interactive :
        try :
            _x_session = PromptSession(lexer=PygmentsLexer(PythonLexer), completer=_x_word_completer)
        except :
            print_err("[qic] $ WARN: word completion disabled on combination of {}/{}".format(sys.platform,os.environ.get("TERM")),lvl=2)
            _x_session = None
        _x_dotkey = True
        _x_history = deque(maxlen=200)
        _x_cmd0=""
        _x_oldsin=""
        _x_block=False
        while True :
            _x_doeval=True
            res=""
            err=""
            try :
                if _x_session :
                    _x_sin = _x_session.prompt('[qic] $ ')
                else :
                    _x_sin = input('[qic] $ ')
            except KeyboardInterrupt:
                continue
            except EOFError :
                print_err("# IO Error. Pipeline intput is not supported in interactive mode, pls use (-f).",lvl=3)
                break
            if not _x_sin :
                continue
            if re.match(r"^\s*\_\w+\s*$",_x_sin) :
                _x_sin = _x_sin + "(_)"
            if _x_sin.startswith("'''")  :
                if _x_block :
                    _x_sin = _x_oldsin 
                    _x_oldsin=""
                    _x_block=False
                    _x_doeval = False
                else :
                    _x_block = True
                    continue
            if _x_block :
                if _x_oldsin :
                    _x_oldsin += "\n" + _x_sin
                else :
                    _x_oldsin += _x_sin
                continue
            lastc =[int(ord(c)) for c in _x_sin][-1]
            if lastc and lastc in [65,66,67,68] : 
                _x_sin = "\\hist"
            if _x_sin in ["quit()","\\q"] :
                break
            if _x_sin in ["dotkey"] :
                _x_dotkey = True
                continue
            if _x_sin in ["nodotkey","no dotkey"] :
                _x_dotkey = False
                continue
            mqx = re.match(r"!\s*(\S.*)",_x_sin)
            if mqx :
                res = _qx(mqx.group(1))
                show_result(res)
                continue
            if _x_sin in ["\\hist","\\history"] :
                if not _x_history :
                    print_err("# no history found.",lvl=2)
                for i,cmd in enumerate(_x_history) :
                    print_err("# {:3} : {}".format(i,cmd),lvl=1)
                continue
            _x_m1 = re.match(r"\\r (\d+)",_x_sin) 
            _x_m2 = re.match(r"\\(\d+)",_x_sin) 
            if _x_m1 or _x_m2:
                if _x_m1 :
                    ix = int(_x_m1.group(1))
                if _x_m2 :
                    ix = int(_x_m2.group(1))
                if ix < len(_x_history) :
                    _x_sin = _x_history[ix]
                else :
                    continue

            if re.search(r"\breturn\b",_x_sin) :
                x=run_as_func(_x_sin,_)
                if x :
                    print(x)
                continue

            _x_cmd0 = None
            if _x_dotkey and "." in _x_sin :
                _x_cmd0 = _x_sin
            try :
                if _x_cmd0 :
                    _x_history.append(_x_cmd0)
                elif not _x_sin.startswith("\\") :
                    _x_history.append(_x_sin)
                if _x_sin.startswith("\\") :
                    res = ""
                    err = "# command not recognized."
                else :
                    runcode(_x_sin,data=_)
            except :
                traceback.print_last()
                continue
            time.sleep(0.1)
        return 0


if __name__ == "__main__" :
    dsq_main()
