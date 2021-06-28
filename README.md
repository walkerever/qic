# qic - Query In Console or Command line

JSON/YAML/XML comand line query tool with support of interactive mode.

By design, it only process a few common situations and there's a lot compromise which may need some attention.  It's not intending to embed a fully working syntax/sementic engine and only provide a few "sugar" features.   For too complicated situation, other than introducing very long single line expression, please try  code blocks where you can use any python syntax.

For detail, look into the [Wiki](https://github.com/laowangv5/qic/wiki)

[![brief with video](https://github.com/laowangv5/qic/blob/master/doc/images/qic_eg_2.png)](http://www.youtube.com/watch?v=NBARRnsKnbk)


-----

## Installation


it's available from pip.

`pip install qic --upgrade`

you can run it as,

`python -mqic`

or just,

`qic`

note, if you install it as non-root user, it's placed in ~/.local/bin folder, so either refer the full path or add to your **PATH**.

note 2, by default, qic read output from pipe line or a file specified by -f, so, use `qic -h` for help info. If you just type qic followed by enter, you will find it "hang" there:) 

```bash
[~]$ sudo python3 -mpip install qic --upgrade
WARNING: Running pip install with root privileges is generally not a good idea. Try `python3 -m pip install --user` instead.
Collecting qic
  Using cached qic-1.0.9.tar.gz (14 kB)
Requirement already satisfied: wcwidth in /usr/local/lib/python3.9/site-packages (from qic) (0.2.5)
Requirement already satisfied: pyyaml in /usr/local/lib64/python3.9/site-packages (from qic) (5.4.1)
Requirement already satisfied: xmltodict in /usr/local/lib/python3.9/site-packages (from qic) (0.12.0)
Requirement already satisfied: dicttoxml in /usr/local/lib/python3.9/site-packages (from qic) (1.7.4)
Requirement already satisfied: pygments in /usr/local/lib/python3.9/site-packages (from qic) (2.9.0)
Requirement already satisfied: prompt_toolkit in /usr/local/lib/python3.9/site-packages (from qic) (3.0.19)
Using legacy 'setup.py install' for qic, since package 'wheel' is not installed.
Installing collected packages: qic
    Running setup.py install for qic ... done
Successfully installed qic-1.0.9
[~]$ 
[~]$ 
[~]$ which qic
/usr/local/bin/qic
[~]$ 
[~]$ qic -h
usage: qic [-h] [-f INFILE] [-t SRCTYPE] [-i INDENT] [-l ROWS] [-m MODULES] [-K KEYS_INCLUDED] [-E KEYS_EXCLUDED] [-F] [-s] [-I] [-p] [-c]
           [-C] [-X]
           [code]

positional arguments:
  code                  code to compile. may be a file.

optional arguments:
  -h, --help            show this help message and exit
  -f INFILE, --infile INFILE
                        input file
  -t SRCTYPE, --srctype SRCTYPE
                        JSON,YAML or XML
  -i INDENT, --indent INDENT
                        how many spaces for indent. default 4.
  -l ROWS, --rows ROWS  use this to shrink each list included. useful for DS including too many records.
  -m MODULES, --modules MODULES
                        import modules.
  -K KEYS_INCLUDED, --keys KEYS_INCLUDED
                        only keep these keys.
  -E KEYS_EXCLUDED, --nokeys KEYS_EXCLUDED
                        these keys should be excluded.
  -F, --functionize     wrap code into an internal function
  -s, --rawstr          output raw stings for easy grep
  -I, --interactive     interactive mode
  -p, --plain           force no color code
  -c, --compact         dump data structure in compact mode
  -C, --keepcolor       do not remove ANSI color code from input stream.
  -X, --debug           debug mode

```

![test json content](https://github.com/laowangv5/qic/blob/master/doc/images/qic_eg_1.png)

![test query on given json content](https://github.com/laowangv5/qic/blob/master/doc/images/qic_eg_2.png)



## Input Stream

please be noted, due to the lack of colored text support from markdown language, the terminal output is much less impressive than in real world.  good thing is that there's still minimum support of font styles which make it different than plain console output. so if not extremely necessary, I will just paste what I got from "copy as HTML" than capturing a lot screenshots.

here, we have a test json file as below,

```json
[{
  "_id": {
    "$oid": "5968dd23fc13ae04d9000001"
  },
  "product_name": "sildenafil citrate",
  "supplier": "Wisozk Inc",
  "quantity": 261,
  "unit_cost": "$10.47"
}, {
  "_id": {
    "$oid": "5968dd23fc13ae04d9000002"
  },
  "product_name": "Mountain Juniperus ashei",
  "supplier": "Keebler-Hilpert",
  "quantity": 292,
  "unit_cost": "$8.74"
}, {
  "_id": {
    "$oid": "5968dd23fc13ae04d9000003"
  },
  "product_name": "Dextromathorphan HBr",
  "supplier": "Schmitt-Weissnat",
  "quantity": 211,
  "unit_cost": "$20.53"
}]

```

we can feed qic in a few ways,

1. through a pipe
2. specified by -f
3. type or paste ad-hoc text 

```bash
[yx@mtp qic]$cat test/s1.json  | qic 
[
  {
    "_id": {
      "$oid": "5968dd23fc13ae04d9000001"
    },
    "product_name": "sildenafil citrate",
    "supplier": "Wisozk Inc",
    "quantity": 261,
    "unit_cost": "$10.47"
  },
  {
    "_id": {
      "$oid": "5968dd23fc13ae04d9000002"
    },
    "product_name": "Mountain Juniperus ashei",
    "supplier": "Keebler-Hilpert",
    "quantity": 292,
    "unit_cost": "$8.74"
  },
  {
    "_id": {
      "$oid": "5968dd23fc13ae04d9000003"
    },
    "product_name": "Dextromathorphan HBr",
    "supplier": "Schmitt-Weissnat",
    "quantity": 211,
    "unit_cost": "$20.53"
  }
]

[yx@mtp qic]$
[yx@mtp qic]$qic -f test/s1.json 
[
  {
    "_id": {
      "$oid": "5968dd23fc13ae04d9000001"
    },
    "product_name": "sildenafil citrate",
    "supplier": "Wisozk Inc",
    "quantity": 261,
    "unit_cost": "$10.47"
  },
  {
    "_id": {
      "$oid": "5968dd23fc13ae04d9000002"
    },
    "product_name": "Mountain Juniperus ashei",
    "supplier": "Keebler-Hilpert",
    "quantity": 292,
    "unit_cost": "$8.74"
  },
  {
    "_id": {
      "$oid": "5968dd23fc13ae04d9000003"
    },
    "product_name": "Dextromathorphan HBr",
    "supplier": "Schmitt-Weissnat",
    "quantity": 211,
    "unit_cost": "$20.53"
  }
]

```

in below example, JSON is pasted directly, then followed by a CTL+D to end the input. \
we can notice the first part is of "plain format" while the QIC output has some style -- it's actually much more beautiful in a terminal supporting ansi colors. 

<pre>[yx@mtp qic]$qic
[
  {
    &quot;_id&quot;: {
      &quot;$oid&quot;: &quot;5968dd23fc13ae04d9000001&quot;
    },
    &quot;product_name&quot;: &quot;sildenafil citrate&quot;,
    &quot;supplier&quot;: &quot;Wisozk Inc&quot;,
    &quot;quantity&quot;: 261,
    &quot;unit_cost&quot;: &quot;$10.47&quot;
  },
  {
    &quot;_id&quot;: {
      &quot;$oid&quot;: &quot;5968dd23fc13ae04d9000002&quot;
    },
    &quot;product_name&quot;: &quot;Mountain Juniperus ashei&quot;,
    &quot;supplier&quot;: &quot;Keebler-Hilpert&quot;,
    &quot;quantity&quot;: 292,
    &quot;unit_cost&quot;: &quot;$8.74&quot;
  },
  {
    &quot;_id&quot;: {
      &quot;$oid&quot;: &quot;5968dd23fc13ae04d9000003&quot;
    },
    &quot;product_name&quot;: &quot;Dextromathorphan HBr&quot;,
    &quot;supplier&quot;: &quot;Schmitt-Weissnat&quot;,
    &quot;quantity&quot;: 211,
    &quot;unit_cost&quot;: &quot;$20.53&quot;
  }
]
[
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;Mountain Juniperus ashei&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$8.74&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;Dextromathorphan HBr&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$20.53&quot;</font>
  }
]

[yx@mtp qic]$
</pre>



## Access 

Qic is made by python and it supports python syntax naturally.  

### _ means doc root
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_&quot;
[
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;Mountain Juniperus ashei&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$8.74&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;Dextromathorphan HBr&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$20.53&quot;</font>
  }
]

</pre>

### Access List
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[0]&quot;
{
  <font color="#008700"><b>&quot;_id&quot;</b></font>: {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
  },
  <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
  <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>,
  <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
  <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
}

[yx@mtp qic]$qic -f test/s1.json &quot;_[0:2]&quot;
[
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;Mountain Juniperus ashei&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$8.74&quot;</font>
  }
]

</pre>

### Access DICT 

#### use python "['key']" syntax
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[0][&apos;supplier&apos;]&quot;
Wisozk Inc

[yx@mtp qic]$qic -f test/s1.json &quot;_[0][&apos;unit_cost&apos;]&quot;
$10.47
</pre>

##### use . 
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[0].supplier&quot;
Wisozk Inc

[yx@mtp qic]$qic -f test/s1.json &quot;_[0].unit_cost&quot;
$10.47
</pre>

####  what if we want multiple keys?

1.  use "{}" key select syntax
    we can see with -X option, qic actually has translated the brief syntax into standard python way.
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[0].{unit_cost,quantity}&quot;
{
  <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>,
  <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>
}

[yx@mtp qic]$qic -f test/s1.json &quot;_[0].{unit_cost,quantity}&quot; -X
<font color="#33C7DE"># run : </font>
{&apos;unit_cost&apos;:_[0][&apos;unit_cost&apos;],&apos;quantity&apos;:_[0][&apos;quantity&apos;]}
{
  <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>,
  <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>
}
</pre>

2.  use -K keys including options.

<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[0]&quot; -K unit_cost,quantity
{
  <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
  <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
}
</pre>



# List Expansion

## Let's check python list comprehension first,

<pre>[yx@mtp qic]$qic -f test/s1.json &quot;[i[&apos;quantity&apos;] for i in _]&quot;
[
  <font color="#626262">261</font>,
  <font color="#626262">292</font>,
  <font color="#626262">211</font>
]

[yx@mtp qic]$qic -f test/s1.json &quot;[{&apos;quantity&apos;:i[&apos;quantity&apos;],&apos;supplier&apos;:i[&apos;supplier&apos;]} for i in _]&quot;
[
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>
  }
]

</pre>

## use [] to save some typing
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[].quantity&quot;
[
  <font color="#626262">261</font>,
  <font color="#626262">292</font>,
  <font color="#626262">211</font>
]

[yx@mtp qic]$qic -f test/s1.json &quot;_[].{quantity,supplier}&quot;
[
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>
  }
]

</pre>

## run in debug mode to check expanded code
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[].quantity&quot; -X
<font color="#33C7DE"># run : </font>
[ _hcm[&apos;quantity&apos;] for _hcm in _ ]
[
  <font color="#626262">261</font>,
  <font color="#626262">292</font>,
  <font color="#626262">211</font>
]

[yx@mtp qic]$
[yx@mtp qic]$qic -f test/s1.json &quot;_[].{quantity,supplier}&quot; -X
<font color="#33C7DE"># run : </font>
[ {&apos;quantity&apos;:_oeu[&apos;quantity&apos;],&apos;supplier&apos;:_oeu[&apos;supplier&apos;]} for _oeu in _ ]
[
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>
  }
]

</pre>


## note, slice is also supported
<pre>[yx@mtp qic]$qic -f test/s1.json &quot;_[:2].{quantity,supplier}&quot; -X
<font color="#33C7DE"># run : </font>
[ {&apos;quantity&apos;:_jgr[&apos;quantity&apos;],&apos;supplier&apos;:_jgr[&apos;supplier&apos;]} for _jgr in _[:2] ]
[
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>
  }
]

[yx@mtp qic]$
[yx@mtp qic]$qic -f test/s1.json &quot;_[1:].{quantity,supplier}&quot; -X
<font color="#33C7DE"># run : </font>
[ {&apos;quantity&apos;:_chd[&apos;quantity&apos;],&apos;supplier&apos;:_chd[&apos;supplier&apos;]} for _chd in _[1:] ]
[
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>
  }
]

[yx@mtp qic]$
[yx@mtp qic]$qic -f test/s1.json &quot;_[:].{quantity,supplier}&quot; -X
<font color="#33C7DE"># run : </font>
[ {&apos;quantity&apos;:_wax[&apos;quantity&apos;],&apos;supplier&apos;:_wax[&apos;supplier&apos;]} for _wax in _ ]
[
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>
  }
]
</pre>




## Interactive mode

-I will bring you to interactive mode.

interactive mode will read stdin so you can not pipe json content into QiC, use -f instead.

the Input Json will be parsed and all the keys are used for word completion. 

you may have noticed, in dot(.) syntax, you can ignore the case since QiC will try to find the right one for you. Only in the case you have defined some different keys only diff from each other with case -- specify the right one.


in below case, unfortunately the color is missing in markdown. when typed "_", a few internal helper functions starts with "_" were prompted.

<pre>yx@mtp qic]$qic -f test/s1.json -I
[qic] $ _
         <span style="background-color:#BCBCBC"><font color="#000000"> _         </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _fl       </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _flatlist </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _id       </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _j        </font></span><span style="background-color:#A8A8A8"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _l        </font></span><span style="background-color:#A8A8A8"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _l2pt     </font></span><span style="background-color:#A8A8A8"><font color="#000000"> </font></span>
</pre>
 

here, when typed "q", "quantity" was promoted.

<pre>
[qic] $ _[<font color="#626262">0</font>]<font color="#626262">.</font>q
              <span style="background-color:#BCBCBC"><font color="#000000"> quantity </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>


in case you want to write some complicated logic with multiple lines, use "'''" to start and end your block.

<pre>[qic] $
[qic] $ <font color="#AF0000">&apos;&apos;&apos;</font>
[qic] $ <font color="#008700">sum</font><font color="#626262">=0</font>
[qic] $ <font color="#008700"><b>for</b></font> i <font color="#AF00FF"><b>in</b></font> _ :
[qic] $     cost <font color="#626262">=</font> <font color="#008700">float</font>(i<font color="#626262">.</font>unit_cost<font color="#626262">.</font>replace(<font color="#AF0000">&quot;$&quot;</font>,<font color="#AF0000">&quot;&quot;</font>))
[qic] $     <font color="#008700">sum</font> <font color="#626262">+=</font> <font color="#008700">int</font>(i<font color="#626262">.</font>quantity) <font color="#626262">*</font> cost
[qic] $ <font color="#008700">print</font>(<font color="#AF0000">&quot;total = &quot;</font>, <font color="#008700">sum</font>)
[qic] $ <font color="#AF0000">&apos;&apos;&apos;</font>
total =  9616.58
[qic] $
[qic] $
</pre>

</pre>

-----

### quit

just type "\q"

#### test json file

<pre>[yx@mtp qic]$qic -f test/s1.json 
[
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;Mountain Juniperus ashei&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$8.74&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
    },
    <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;Dextromathorphan HBr&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$20.53&quot;</font>
  }
]
</pre>
