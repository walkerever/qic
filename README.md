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


(py3) [yonghang@mtp qic]$ cat test/s1.json \
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
(py3) [yonghang@mtp qic]$ \
(py3) [yonghang@mtp qic]$ cat test/s1.json | qic \
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



