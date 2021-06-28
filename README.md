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

by default it will validate, reformat and color the JSON stream. \

"_" means the document root.  This is the default value. 

<pre>(py3) [me@mtp qic]$ cat test/s1.json | qic  # _
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

query its conent, \

<pre>(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[0]&quot;
{
  <font color="#008700"><b>&quot;_id&quot;</b></font>: {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
  },
  <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
  <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>,
  <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
  <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
}

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[0]._id&quot;
{
  <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
}

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[0].product_name&quot;
sildenafil citrate

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[0].{product_name, quantity, unit_cost}&quot;
{
  <font color="#008700"><b>&quot;product_name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
  <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
  <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
}

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[]._id&quot;
[
  {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
  }
]

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[].{_id,quantity}&quot;
[
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
    },
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
    },
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
    },
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>
  }
]
</pre>

----

## check expanded code

<pre>(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[]._id&quot; -X
<font color="#33C7DE"># run : </font>
[ _umy[&apos;_id&apos;] for _umy in _ ]
[
  {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
  }
]

(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;[ _[0].product_name ]&quot; -X
<font color="#33C7DE"># run : </font>
[ _[0][&apos;product_name&apos;] ]
[
  <font color="#AF0000">&quot;sildenafil citrate&quot;</font>
]

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[].{_id,quantity}&quot; -X
<font color="#33C7DE"># run : </font>
[ {&apos;_id&apos;:_emt[&apos;_id&apos;],&apos;quantity&apos;:_emt[&apos;quantity&apos;]} for _emt in _ ]
[
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
    },
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
    },
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
    },
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>
  }
]


(py3) [me@mtp qic]$ cat test/s1.json | qic  &quot;_[0].{_id,quantity}&quot; -X
<font color="#33C7DE"># run : </font>
{&apos;_id&apos;:_[0][&apos;_id&apos;],&apos;quantity&apos;:_[0][&apos;quantity&apos;]}
{
  <font color="#008700"><b>&quot;_id&quot;</b></font>: {
    <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
  },
  <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>
}
</pre>

-----

## keys with special chars

look at below changed JSON, `product_name` is renamed to `product.name`. This will break the dot expansion QiC is using. In this situation, use `<>` to mark content within is a single unit.

<pre>(py3) [me@mtp qic]$ qic -f test/s1x.json 
[
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000001&quot;</font>
    },
    <font color="#008700"><b>&quot;product.name&quot;</b></font>: <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Wisozk Inc&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">261</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$10.47&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000002&quot;</font>
    },
    <font color="#008700"><b>&quot;product.name&quot;</b></font>: <font color="#AF0000">&quot;Mountain Juniperus ashei&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Keebler-Hilpert&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">292</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$8.74&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;_id&quot;</b></font>: {
      <font color="#008700"><b>&quot;$oid&quot;</b></font>: <font color="#AF0000">&quot;5968dd23fc13ae04d9000003&quot;</font>
    },
    <font color="#008700"><b>&quot;product.name&quot;</b></font>: <font color="#AF0000">&quot;Dextromathorphan HBr&quot;</font>,
    <font color="#008700"><b>&quot;supplier&quot;</b></font>: <font color="#AF0000">&quot;Schmitt-Weissnat&quot;</font>,
    <font color="#008700"><b>&quot;quantity&quot;</b></font>: <font color="#626262">211</font>,
    <font color="#008700"><b>&quot;unit_cost&quot;</b></font>: <font color="#AF0000">&quot;$20.53&quot;</font>
  }
]

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ qic -f test/s1x.json  &quot;_[].product.name&quot;
<font color="#E9AD0C"># expanded code :</font>
<font color="#E9AD0C">[ _kom[&apos;product&apos;][&apos;name&apos;] for _kom in _ ]</font>
<font color="#E9AD0C"># KeyError: &apos;product&apos;</font>
(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ qic -f test/s1x.json  &quot;_[].&lt;product.name&gt;&quot;
[
  <font color="#AF0000">&quot;sildenafil citrate&quot;</font>,
  <font color="#AF0000">&quot;Mountain Juniperus ashei&quot;</font>,
  <font color="#AF0000">&quot;Dextromathorphan HBr&quot;</font>
]
</pre>

-----

## Interactive Mode

`-I` enable interactive mode.  \
Qic will read user input from sys.stdin.  so, for input stream, it could not be from unix pipe, instead use `-f` opiton.   \
when type `_` , a small menu is promptec all internal functions started with `_`.   \
Before prompted for user input, all keys in the JSON are stored for word completion prompt -- as you may have noticed, they're case insenstive.



<pre>(py3) [me@mtp qic]$ qic -f test/s6.json  -I
[qic] $ _
         <span style="background-color:#BCBCBC"><font color="#000000"> _         </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _fl       </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _flatlist </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _j        </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _l        </font></span><span style="background-color:#A8A8A8"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _l2pt     </font></span><span style="background-color:#A8A8A8"><font color="#000000"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#000000"> _l2t      </font></span><span style="background-color:#A8A8A8"><font color="#000000"> </font></span>

</pre>

<pre>[qic] $ _<font color="#626262">.</font>users[<font color="#626262">0</font>]<font color="#626262">.</font>f
                    <span style="background-color:#BCBCBC"><font color="#000000"> firstname </font></span><span style="background-color:#444444"><font color="#000000"> </font></span>
</pre>
<pre>[qic] $ _<font color="#626262">.</font>users[<font color="#626262">0</font>]<font color="#626262">.</font>firstname
Krish</pre>

_l2t is an internal function which print "standard" table.   \

<pre>
[qic] $ _l2t(_<font color="#626262">.</font>users)
<b>userId firstName lastName phoneNumber emailAddress</b>
------------------------------------------------------------------------
1      Krish     Lee      123456      krish.lee@learningcontainer.com
2      racks     jacson   123456      racks.jacson@learningcontainer.com
3      denial    roast    33333333    denial.roast@learningcontainer.com
4      devid     neo      222222222   devid.neo@learningcontainer.com
5      jone      mac      111111111   jone.mac@learningcontainer.com

</pre>

use `'''` to mark code block start and end.

<pre>[qic] $
[qic] $ <font color="#AF0000">&apos;&apos;&apos;</font>
[qic] $ guys <font color="#626262">=</font> <font color="#AF0000">&quot;&quot;</font>
[qic] $ <font color="#008700"><b>for</b></font> i <font color="#AF00FF"><b>in</b></font> _<font color="#626262">.</font>users :
[qic] $     guys <font color="#626262">+=</font> i<font color="#626262">.</font>firstname <font color="#626262">+</font> i<font color="#626262">.</font>lastname <font color="#626262">+</font> <font color="#AF0000">&quot;, &quot;</font>
[qic] $ <font color="#008700">print</font>(<font color="#AF0000">&quot;List :&quot;</font>, guys<font color="#626262">.</font>rstrip())
[qic] $
[qic] $ <font color="#AF0000">&apos;&apos;&apos;</font>
List : KrishLee, racksjacson, denialroast, devidneo, jonemac,
[qic] $
[qic] $
</pre>

use `\q` or `quit()` to leave Qic.

<pre>(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ qic -f test/s6.json  -I
[qic] $
[qic] $ \q
(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ qic -f test/s6.json  -I
[qic] $ quit()
(py3) [me@mtp qic]$ 
</pre>
















