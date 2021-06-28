# qic - Query In Console

JSON/YAML/XML comand line query tool with interactive mode.

By design, it tries to keep simple. There're a lot compromises. It's not intending to embed a full syntax/sementic engine. For complicated situation, other than introducing very long single line expression, please try code blocks where you can use any python syntax.

This document is also available on github.io [QiC](https://laowangv5.github.io/qic/)

[![watch a brief on youtube](https://github.com/laowangv5/qic/blob/master/doc/images/qic_eg_2.png)](http://www.youtube.com/watch?v=NBARRnsKnbk)


-----

## Installation

`python -mpip install qic`

run it 

`qic` or `python -mqic`

----
## Baiscs

<pre>(py3) [me@mtp qic]$ cat test/s1.json | qic 
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





