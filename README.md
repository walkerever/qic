## [doc on github.io](https://walkerever.github.io/)


# qic - Query In Console

![qic show](/docs/assets/images/qic.show.gif)

JSON/YAML/XML comand line query tool with interactive mode.

By design, it tries to keep simple. There're a lot compromises. It's not intending to embed a full syntax/sementic engine. For complicated situation, other than introducing very long single line expression, please try code blocks where you can use any python syntax.

This document is available with better format on github.io [QiC](https://laowangv5.github.io/qic/) where colorful text can be used for terminal output.

- [Installation](#installation)
- [Basics](#basics)
- [Check expanded code](#check-expanded-code)
- [Keys with special chars](#keys-with-special-chars)
- [Interactive mode](#interactive-mode)
- [Validate/Convert JSON/YAML/XML](#validate-and-convert-jsonxmlyaml)
- [Limit rows](#limit-rows)
- [Load extra modules](#load-extra-modules)
- [JSON/YAML/XML to HTML](#json-to-html)

----

-----

## Installation

`python -mpip install qic`

run it 

`qic` or `python -mqic`

----
## Basics

by default it will validate, reformat and color the JSON stream. 

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

query its conent, 

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

## Check expanded code

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

## Keys with special chars

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

`-I` enable interactive mode.  

Qic will read user input from sys.stdin.  so, for input stream, it could not be from unix pipe, instead use `-f` opiton.   

when type `_` , a small menu is promptec all internal functions started with `_`.   

Before prompted for user input, all keys in the JSON are stored for word completion prompt -- as you may have noticed, they're case insenstive.  



<pre>(py3) [me@mtp qic]$ qic -f test/s6.json  -I
[qic] $ _
         <span style="background-color:#BCBCBC"><font color="#FFFFFF"> _         </font></span><span style="background-color:#444444"><font color="#FFFFFF"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#FFFFFF"> _fl       </font></span><span style="background-color:#444444"><font color="#FFFFFF"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#FFFFFF"> _flatlist </font></span><span style="background-color:#444444"><font color="#FFFFFF"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#FFFFFF"> _j        </font></span><span style="background-color:#444444"><font color="#FFFFFF"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#FFFFFF"> _l        </font></span><span style="background-color:#A8A8A8"><font color="#FFFFFF"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#FFFFFF"> _l2pt     </font></span><span style="background-color:#A8A8A8"><font color="#FFFFFF"> </font></span>
         <span style="background-color:#BCBCBC"><font color="#FFFFFF"> _l2t      </font></span><span style="background-color:#A8A8A8"><font color="#FFFFFF"> </font></span>

</pre>

<pre>[qic] $ _<font color="#626262">.</font>users[<font color="#626262">0</font>]<font color="#626262">.</font>f
                    <span style="background-color:#BCBCBC"><font color="#FFFFFF"> firstname </font></span><span style="background-color:#444444"><font color="#FFFFFF"> </font></span>
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

## Validate and Convert JSON/XML/YAML

without any parameters, feed input into QiC and it will serve as a format validator ( plus foramatter, etc.). 

`-t` specify source as JSON, YAML or XML. here all examples are from JSON format and `JSON` is the default type.  Choose the right one if you're going to working with YAML or XML.  

Internal function `_json` or `-j` will dump output as well formatted JSON and this is the default behaviour.   

`_yaml` or `_y` will dump well formatted YAML, while `_xml` or `_x` will dump well formatted XML.

specify them in format of `_x($expr)`, if for full doc, say, `_x(_)`, just use `_x`.

<pre>(py3) [me@mtp qic]$ qic -f test/s6.json  _x
<font color="#AF8700">&lt;?xml version=&quot;1.0&quot; ?&gt;</font>
<font color="#008700"><b>&lt;root&gt;</b></font>
	<font color="#008700"><b>&lt;users</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;list&quot;</font><font color="#008700"><b>&gt;</b></font>
		<font color="#008700"><b>&lt;item</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;dict&quot;</font><font color="#008700"><b>&gt;</b></font>
			<font color="#008700"><b>&lt;userId</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;int&quot;</font><font color="#008700"><b>&gt;</b></font>1<font color="#008700"><b>&lt;/userId&gt;</b></font>
			<font color="#008700"><b>&lt;firstName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>Krish<font color="#008700"><b>&lt;/firstName&gt;</b></font>
			<font color="#008700"><b>&lt;lastName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>Lee<font color="#008700"><b>&lt;/lastName&gt;</b></font>
			<font color="#008700"><b>&lt;phoneNumber</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>123456<font color="#008700"><b>&lt;/phoneNumber&gt;</b></font>
			<font color="#008700"><b>&lt;emailAddress</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>krish.lee@learningcontainer.com<font color="#008700"><b>&lt;/emailAddress&gt;</b></font>
		<font color="#008700"><b>&lt;/item&gt;</b></font>
		<font color="#008700"><b>&lt;item</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;dict&quot;</font><font color="#008700"><b>&gt;</b></font>
			<font color="#008700"><b>&lt;userId</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;int&quot;</font><font color="#008700"><b>&gt;</b></font>2<font color="#008700"><b>&lt;/userId&gt;</b></font>
			<font color="#008700"><b>&lt;firstName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>racks<font color="#008700"><b>&lt;/firstName&gt;</b></font>
			<font color="#008700"><b>&lt;lastName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>jacson<font color="#008700"><b>&lt;/lastName&gt;</b></font>
			<font color="#008700"><b>&lt;phoneNumber</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>123456<font color="#008700"><b>&lt;/phoneNumber&gt;</b></font>
			<font color="#008700"><b>&lt;emailAddress</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>racks.jacson@learningcontainer.com<font color="#008700"><b>&lt;/emailAddress&gt;</b></font>
		<font color="#008700"><b>&lt;/item&gt;</b></font>
		<font color="#008700"><b>&lt;item</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;dict&quot;</font><font color="#008700"><b>&gt;</b></font>
			<font color="#008700"><b>&lt;userId</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;int&quot;</font><font color="#008700"><b>&gt;</b></font>3<font color="#008700"><b>&lt;/userId&gt;</b></font>
			<font color="#008700"><b>&lt;firstName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>denial<font color="#008700"><b>&lt;/firstName&gt;</b></font>
			<font color="#008700"><b>&lt;lastName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>roast<font color="#008700"><b>&lt;/lastName&gt;</b></font>
			<font color="#008700"><b>&lt;phoneNumber</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>33333333<font color="#008700"><b>&lt;/phoneNumber&gt;</b></font>
			<font color="#008700"><b>&lt;emailAddress</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>denial.roast@learningcontainer.com<font color="#008700"><b>&lt;/emailAddress&gt;</b></font>
		<font color="#008700"><b>&lt;/item&gt;</b></font>
		<font color="#008700"><b>&lt;item</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;dict&quot;</font><font color="#008700"><b>&gt;</b></font>
			<font color="#008700"><b>&lt;userId</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;int&quot;</font><font color="#008700"><b>&gt;</b></font>4<font color="#008700"><b>&lt;/userId&gt;</b></font>
			<font color="#008700"><b>&lt;firstName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>devid<font color="#008700"><b>&lt;/firstName&gt;</b></font>
			<font color="#008700"><b>&lt;lastName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>neo<font color="#008700"><b>&lt;/lastName&gt;</b></font>
			<font color="#008700"><b>&lt;phoneNumber</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>222222222<font color="#008700"><b>&lt;/phoneNumber&gt;</b></font>
			<font color="#008700"><b>&lt;emailAddress</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>devid.neo@learningcontainer.com<font color="#008700"><b>&lt;/emailAddress&gt;</b></font>
		<font color="#008700"><b>&lt;/item&gt;</b></font>
		<font color="#008700"><b>&lt;item</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;dict&quot;</font><font color="#008700"><b>&gt;</b></font>
			<font color="#008700"><b>&lt;userId</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;int&quot;</font><font color="#008700"><b>&gt;</b></font>5<font color="#008700"><b>&lt;/userId&gt;</b></font>
			<font color="#008700"><b>&lt;firstName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>jone<font color="#008700"><b>&lt;/firstName&gt;</b></font>
			<font color="#008700"><b>&lt;lastName</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>mac<font color="#008700"><b>&lt;/lastName&gt;</b></font>
			<font color="#008700"><b>&lt;phoneNumber</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>111111111<font color="#008700"><b>&lt;/phoneNumber&gt;</b></font>
			<font color="#008700"><b>&lt;emailAddress</b></font> <font color="#878700">type=</font><font color="#AF0000">&quot;str&quot;</font><font color="#008700"><b>&gt;</b></font>jone.mac@learningcontainer.com<font color="#008700"><b>&lt;/emailAddress&gt;</b></font>
		<font color="#008700"><b>&lt;/item&gt;</b></font>
	<font color="#008700"><b>&lt;/users&gt;</b></font>
<font color="#008700"><b>&lt;/root&gt;</b></font>

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ qic -f test/s6.json  _y
<font color="#0000FF"><b>---</b></font>
<font color="#008700"><b>users</b></font>:
- <font color="#008700"><b>emailAddress</b></font>: krish.lee@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: Krish
  <font color="#008700"><b>lastName</b></font>: Lee
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 1
- <font color="#008700"><b>emailAddress</b></font>: racks.jacson@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: racks
  <font color="#008700"><b>lastName</b></font>: jacson
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 2
- <font color="#008700"><b>emailAddress</b></font>: denial.roast@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: denial
  <font color="#008700"><b>lastName</b></font>: roast
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;33333333&apos;</font>
  <font color="#008700"><b>userId</b></font>: 3
- <font color="#008700"><b>emailAddress</b></font>: devid.neo@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: devid
  <font color="#008700"><b>lastName</b></font>: neo
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;222222222&apos;</font>
  <font color="#008700"><b>userId</b></font>: 4
- <font color="#008700"><b>emailAddress</b></font>: jone.mac@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: jone
  <font color="#008700"><b>lastName</b></font>: mac
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;111111111&apos;</font>
  <font color="#008700"><b>userId</b></font>: 5

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ qic -f test/s6.json  &apos;_y(_)&apos;
<font color="#0000FF"><b>---</b></font>
<font color="#008700"><b>users</b></font>:
- <font color="#008700"><b>emailAddress</b></font>: krish.lee@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: Krish
  <font color="#008700"><b>lastName</b></font>: Lee
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 1
- <font color="#008700"><b>emailAddress</b></font>: racks.jacson@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: racks
  <font color="#008700"><b>lastName</b></font>: jacson
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 2
- <font color="#008700"><b>emailAddress</b></font>: denial.roast@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: denial
  <font color="#008700"><b>lastName</b></font>: roast
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;33333333&apos;</font>
  <font color="#008700"><b>userId</b></font>: 3
- <font color="#008700"><b>emailAddress</b></font>: devid.neo@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: devid
  <font color="#008700"><b>lastName</b></font>: neo
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;222222222&apos;</font>
  <font color="#008700"><b>userId</b></font>: 4
- <font color="#008700"><b>emailAddress</b></font>: jone.mac@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: jone
  <font color="#008700"><b>lastName</b></font>: mac
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;111111111&apos;</font>
  <font color="#008700"><b>userId</b></font>: 5

(py3) [me@mtp qic]$ 
(py3) [me@mtp qic]$ qic -f test/s6.json  &apos;_y(_.users[:2])&apos;
<font color="#0000FF"><b>---</b></font>
- <font color="#008700"><b>emailAddress</b></font>: krish.lee@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: Krish
  <font color="#008700"><b>lastName</b></font>: Lee
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 1
- <font color="#008700"><b>emailAddress</b></font>: racks.jacson@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: racks
  <font color="#008700"><b>lastName</b></font>: jacson
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 2

(py3) [me@mtp qic]$ </pre>


## Limit rows 

when the embeded list is huge, we may only want to see a few of them.   
slice `[:$n]` can be used for specified list, but `-l $n` apply to all lists included.   

<pre>(py3) [me@mtp qic]$ qic -f test/s6.json &apos;_.users&apos; | qic _y
<font color="#0000FF"><b>---</b></font>
- <font color="#008700"><b>emailAddress</b></font>: krish.lee@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: Krish
  <font color="#008700"><b>lastName</b></font>: Lee
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 1
- <font color="#008700"><b>emailAddress</b></font>: racks.jacson@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: racks
  <font color="#008700"><b>lastName</b></font>: jacson
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 2
- <font color="#008700"><b>emailAddress</b></font>: denial.roast@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: denial
  <font color="#008700"><b>lastName</b></font>: roast
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;33333333&apos;</font>
  <font color="#008700"><b>userId</b></font>: 3
- <font color="#008700"><b>emailAddress</b></font>: devid.neo@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: devid
  <font color="#008700"><b>lastName</b></font>: neo
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;222222222&apos;</font>
  <font color="#008700"><b>userId</b></font>: 4
- <font color="#008700"><b>emailAddress</b></font>: jone.mac@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: jone
  <font color="#008700"><b>lastName</b></font>: mac
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;111111111&apos;</font>
  <font color="#008700"><b>userId</b></font>: 5

(py3) [me@mtp qic]$ qic -f test/s6.json -l2 &apos;_.users&apos; | qic _y
<font color="#33C7DE"># _[] 5 -&gt; 2</font>
<font color="#0000FF"><b>---</b></font>
- <font color="#008700"><b>emailAddress</b></font>: krish.lee@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: Krish
  <font color="#008700"><b>lastName</b></font>: Lee
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 1
- <font color="#008700"><b>emailAddress</b></font>: racks.jacson@learningcontainer.com
  <font color="#008700"><b>firstName</b></font>: racks
  <font color="#008700"><b>lastName</b></font>: jacson
  <font color="#008700"><b>phoneNumber</b></font>: <font color="#AF0000">&apos;123456&apos;</font>
  <font color="#008700"><b>userId</b></font>: 2

(py3) [me@mtp qic]$ qic -f test/s6.json -l2 &apos;_.users[:2]&apos; 
[
  {
    <font color="#008700"><b>&quot;userId&quot;</b></font>: <font color="#626262">1</font>,
    <font color="#008700"><b>&quot;firstName&quot;</b></font>: <font color="#AF0000">&quot;Krish&quot;</font>,
    <font color="#008700"><b>&quot;lastName&quot;</b></font>: <font color="#AF0000">&quot;Lee&quot;</font>,
    <font color="#008700"><b>&quot;phoneNumber&quot;</b></font>: <font color="#AF0000">&quot;123456&quot;</font>,
    <font color="#008700"><b>&quot;emailAddress&quot;</b></font>: <font color="#AF0000">&quot;krish.lee@learningcontainer.com&quot;</font>
  },
  {
    <font color="#008700"><b>&quot;userId&quot;</b></font>: <font color="#626262">2</font>,
    <font color="#008700"><b>&quot;firstName&quot;</b></font>: <font color="#AF0000">&quot;racks&quot;</font>,
    <font color="#008700"><b>&quot;lastName&quot;</b></font>: <font color="#AF0000">&quot;jacson&quot;</font>,
    <font color="#008700"><b>&quot;phoneNumber&quot;</b></font>: <font color="#AF0000">&quot;123456&quot;</font>,
    <font color="#008700"><b>&quot;emailAddress&quot;</b></font>: <font color="#AF0000">&quot;racks.jacson@learningcontainer.com&quot;</font>
  }
]
</pre>




##  load extra modules
load module/class/function from python source files.

<pre><font color="#00AFFF">yonghang</font>@<font color="#FF8700">mtp</font><font color="#00AFFF">~</font> $ cat ~/tmp/tm.py 

def xxlen(ds) :
    return str(len(ds)) + &quot; : &quot; + str(ds)

<font color="#00AFFF">yonghang</font>@<font color="#FF8700">mtp</font><font color="#00AFFF">~</font> $ curl -s walkerever.com/share/test/json/s6.json | qic -m ~/tmp/tm.py &quot;tm.xxlen(_)&quot;
1 : {&apos;users&apos;: [{&apos;userId&apos;: 1, &apos;firstName&apos;: &apos;Krish&apos;, &apos;lastName&apos;: &apos;Lee&apos;, &apos;phoneNumber&apos;: &apos;123456&apos;, &apos;emailAddress&apos;: &apos;krish.lee@learningcontainer.com&apos;}, {&apos;userId&apos;: 2, &apos;firstName&apos;: &apos;racks&apos;, &apos;lastName&apos;: &apos;jacson&apos;, &apos;phoneNumber&apos;: &apos;123456&apos;, &apos;emailAddress&apos;: &apos;racks.jacson@learningcontainer.com&apos;}, {&apos;userId&apos;: 3, &apos;firstName&apos;: &apos;denial&apos;, &apos;lastName&apos;: &apos;roast&apos;, &apos;phoneNumber&apos;: &apos;33333333&apos;, &apos;emailAddress&apos;: &apos;denial.roast@learningcontainer.com&apos;}, {&apos;userId&apos;: 4, &apos;firstName&apos;: &apos;devid&apos;, &apos;lastName&apos;: &apos;neo&apos;, &apos;phoneNumber&apos;: &apos;222222222&apos;, &apos;emailAddress&apos;: &apos;devid.neo@learningcontainer.com&apos;}, {&apos;userId&apos;: 5, &apos;firstName&apos;: &apos;jone&apos;, &apos;lastName&apos;: &apos;mac&apos;, &apos;phoneNumber&apos;: &apos;111111111&apos;, &apos;emailAddress&apos;: &apos;jone.mac@learningcontainer.com&apos;}]}
</pre>

you can load more,

<pre><font color="#00AFFF">yonghang</font>@<font color="#FF8700">mtp</font><font color="#00AFFF">~</font> $ curl -s walkerever.com/share/test/json/s6.json | qic -m ~/tmp/tm.py,json,yaml &quot;tm.xxlen(_)&quot; 
1 : {&apos;users&apos;: [{&apos;userId&apos;: 1, &apos;firstName&apos;: &apos;Krish&apos;, &apos;lastName&apos;: &apos;Lee&apos;, &apos;phoneNumber&apos;: &apos;123456&apos;, &apos;emailAddress&apos;: &apos;krish.lee@learningcontainer.com&apos;}, {&apos;userId&apos;: 2, &apos;firstName&apos;: &apos;racks&apos;, &apos;lastName&apos;: &apos;jacson&apos;, &apos;phoneNumber&apos;: &apos;123456&apos;, &apos;emailAddress&apos;: &apos;racks.jacson@learningcontainer.com&apos;}, {&apos;userId&apos;: 3, &apos;firstName&apos;: &apos;denial&apos;, &apos;lastName&apos;: &apos;roast&apos;, &apos;phoneNumber&apos;: &apos;33333333&apos;, &apos;emailAddress&apos;: &apos;denial.roast@learningcontainer.com&apos;}, {&apos;userId&apos;: 4, &apos;firstName&apos;: &apos;devid&apos;, &apos;lastName&apos;: &apos;neo&apos;, &apos;phoneNumber&apos;: &apos;222222222&apos;, &apos;emailAddress&apos;: &apos;devid.neo@learningcontainer.com&apos;}, {&apos;userId&apos;: 5, &apos;firstName&apos;: &apos;jone&apos;, &apos;lastName&apos;: &apos;mac&apos;, &apos;phoneNumber&apos;: &apos;111111111&apos;, &apos;emailAddress&apos;: &apos;jone.mac@learningcontainer.com&apos;}]}
</pre>



## JSON to HTML

_h and _zh are two functions for the convertion.  _h is to create plain HTML table while _zh makes collapse/expand possible.

<pre><font color="#00AFFF">yonghang</font>@<font color="#FF8700">mtp</font><font color="#00AFFF">~</font> $ curl -s walkerever.com/share/test/json/s6.json | qic &quot;_h&quot;
&lt;<font color="#008700"><b>tt</b></font>&gt;
&lt;<font color="#008700"><b>table</b></font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;border-collapse:collapse;;&quot;</font> <font color="#878700">border</font><font color="#626262">=</font><font color="#AF0000">1</font> &gt;
&lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-MPzoqOdFrYXQpqJzvSpl&quot;</font>&gt;
&lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;users&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
    &lt;<font color="#008700"><b>td</b></font>&gt;
        &lt;<font color="#008700"><b>table</b></font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;border-collapse:collapse;;&quot;</font> <font color="#878700">border</font><font color="#626262">=</font><font color="#AF0000">1</font> <font color="#878700">width</font><font color="#626262">=</font><font color="#AF0000">&quot;100%&quot;</font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;userId&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;1&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;firstName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;Krish&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;lastName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;Lee&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;phoneNumber&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;123456&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;emailAddress&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;krish.lee@learningcontainer.com&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;userId&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;2&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;firstName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;racks&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;lastName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;jacson&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;phoneNumber&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;123456&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;emailAddress&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;racks.jacson@learningcontainer.com&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;userId&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;3&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;firstName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;denial&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;lastName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;roast&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;phoneNumber&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;33333333&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;emailAddress&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;denial.roast@learningcontainer.com&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;userId&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;4&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;firstName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;devid&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;lastName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;neo&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;phoneNumber&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;222222222&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#F1F1F1&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;emailAddress&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;devid.neo@learningcontainer.com&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;userId&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;5&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;firstName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;jone&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;lastName&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;mac&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;phoneNumber&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;111111111&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;<font color="#008700"><b>tr</b></font> <font color="#878700">class</font><font color="#626262">=</font><font color="#AF0000">&quot;child-WvkznPHasGyCxViXFeQH&quot;</font> <font color="#878700">style</font><font color="#626262">=</font><font color="#AF0000">&quot;background-color:#FFFFFF&quot;</font>&gt;
            &lt;<font color="#008700"><b>td</b></font> <font color="#878700">valign</font><font color="#626262">=</font><font color="#AF0000">&quot;top&quot;</font>&gt;&lt;<font color="#008700"><b>b</b></font>&gt;emailAddress&lt;/<font color="#008700"><b>b</b></font>&gt;&lt;/<font color="#008700"><b>td</b></font>&gt;
            &lt;<font color="#008700"><b>td</b></font>&gt;jone.mac@learningcontainer.com&lt;/<font color="#008700"><b>td</b></font>&gt;
        &lt;/<font color="#008700"><b>tr</b></font>&gt;
        &lt;/<font color="#008700"><b>table</b></font>&gt;

    &lt;/<font color="#008700"><b>td</b></font>&gt;
&lt;/<font color="#008700"><b>tr</b></font>&gt;
&lt;/<font color="#008700"><b>table</b></font>&gt;

</pre>


_h in HTML,


<tt>
<table style="border-collapse:collapse;;" border=1 >
<tr class="child-mBrQwESdaSJxRrLHiwHb">
<td valign="top"><b>users</b></td>
    <td>
        <table style="border-collapse:collapse;;" border=1 width="100%">
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>userId</b></td>
            <td>1</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>firstName</b></td>
            <td>Krish</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>lastName</b></td>
            <td>Lee</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>emailAddress</b></td>
            <td>krish.lee@learningcontainer.com</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>userId</b></td>
            <td>2</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>firstName</b></td>
            <td>racks</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>lastName</b></td>
            <td>jacson</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>emailAddress</b></td>
            <td>racks.jacson@learningcontainer.com</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>userId</b></td>
            <td>3</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>firstName</b></td>
            <td>denial</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>lastName</b></td>
            <td>roast</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>33333333</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>emailAddress</b></td>
            <td>denial.roast@learningcontainer.com</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>userId</b></td>
            <td>4</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>firstName</b></td>
            <td>devid</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>lastName</b></td>
            <td>neo</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>222222222</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>emailAddress</b></td>
            <td>devid.neo@learningcontainer.com</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>userId</b></td>
            <td>5</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>firstName</b></td>
            <td>jone</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>lastName</b></td>
            <td>mac</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>111111111</td>
        </tr>
        <tr class="child-xbZJaLZZyftMuMkOmsrF" >
            <td valign="top"><b>emailAddress</b></td>
            <td>jone.mac@learningcontainer.com</td>
        </tr>
        </table>

    </td>
</tr>
</table>


	
_zh table,
	
	

<header>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> 
<script type="text/javascript"> 
    $(document).ready(function () { 
        $('tr.parent') .css("cursor", "pointer") .attr("title", "Click to expand/collapse") .click(function () { 
            $(this).siblings('.child-' + this.id).toggle(); 
        }); 
        $('tr[@class^=child-]').hide().children('td'); 
    }); 
</script>
</header>

<tt>
<table style="border-collapse:collapse;;" border=1 >
<tr class="parent" id="DLvJNVyrvwldSNCapYeW" title="Click to expand/collapse" style="cursor: pointer;"> <td><b>D(1)</b></td> </tr>
<tr class="child-DLvJNVyrvwldSNCapYeW">
<td valign="top"><b>users</b></td>
    <td>
        <table style="border-collapse:collapse;;" border=1 width="100%">
        <tr class="parent" id="ISMOWRxJylpBVUVUXmVJ" title="Click to expand/collapse" style="cursor: pointer;"> <td><b>L(5)</b></td> </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>userId</b></td>
            <td>1</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>firstName</b></td>
            <td>Krish</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>lastName</b></td>
            <td>Lee</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>emailAddress</b></td>
            <td>krish.lee@learningcontainer.com</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>userId</b></td>
            <td>2</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>firstName</b></td>
            <td>racks</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>lastName</b></td>
            <td>jacson</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>123456</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>emailAddress</b></td>
            <td>racks.jacson@learningcontainer.com</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>userId</b></td>
            <td>3</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>firstName</b></td>
            <td>denial</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>lastName</b></td>
            <td>roast</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>33333333</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>emailAddress</b></td>
            <td>denial.roast@learningcontainer.com</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>userId</b></td>
            <td>4</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>firstName</b></td>
            <td>devid</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>lastName</b></td>
            <td>neo</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>222222222</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>emailAddress</b></td>
            <td>devid.neo@learningcontainer.com</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>userId</b></td>
            <td>5</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>firstName</b></td>
            <td>jone</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>lastName</b></td>
            <td>mac</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>phoneNumber</b></td>
            <td>111111111</td>
        </tr>
        <tr class="child-ISMOWRxJylpBVUVUXmVJ" >
            <td valign="top"><b>emailAddress</b></td>
            <td>jone.mac@learningcontainer.com</td>
        </tr>
        </table>

    </td>
</tr>
</table>

	
	
	
	

	
	
	


... to be continued.

