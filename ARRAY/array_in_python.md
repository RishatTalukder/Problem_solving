<h1 align="center"> Everything About ARRAY in python </h1>

I was trying to make a video on `competitive programming` where I was trying to explain `Data Structures` with python and solve some problems in `LeetCode` specifically the `blind 75` problems. But I started with `Linked List` and I realized that I need to explain `Array` first. 

So, here's everything about `Array` in python.

Pre-requisites:

- Basic knowledge of python

# content

# Introduction

An `array` is a `collection` of `items` stored at `contiguous memory locations`. The idea is to store multiple items of the same type together. This makes it `easier` to `calculate` the `position` of each `element` by simply `adding` an `offset` to a `base value`, i.e., the `memory location` of the `first element` of the `array` (generally denoted by the name of the array).

Some wierd `mumbo jumbo` I just wrote above. Just remember that `array` is a `collection` of `items`. That's it.

For example:

Let's say you have a `list` grocery items you want to buy. You can store it in a `list` like this:

- `grocery_list`
    
    1. `Onion`
    2. `Potato`
    3. `Tomato`
    4. `Cucumber`
    5. `Carrot`

SO, here the list has a `name` `grocery_list` and it has `5` items. Each item has a `name` and a `position` in the list. The `position` of the `first item` is `1` and the `position` of the `last item` is `5`.

Now, let's say you want to buy `Tomato`. We know that the `position` of `Tomato` is `3`. So, we can just remove the `3rd` item from the list and we will get `Tomato`.

Now, let's think of it as an `array`. What will happend this list is an `array`? 

Well, the `array` will look like this in python:



```python
grocery_list = [
    "Onion",
    "Potato",
    "Tomato",
    "Cucumber",
    "Carrot",
]
```

Now we cannot just `remove` the `3rd` item from this `array` because `array` is stored in a `contiguous memory location`. What we can so is we can `access` the `3rd` item from the `array` and we will get `Tomato` By doing this:


```python
grocery_list[2]
```




    'Tomato'



As you can see this gives use `Tomato` which is the `3rd` item in the `array`.

What I did here is I accessed the `3rd` item from the `array` by giving the name of the `array` followed by `[]` and inside the `[]` I gave the `position` of the `item` I want to access. In this case, I gave `2` because the `position` of `Tomato` is `3`.

Now, you might think why I did `grocery_list[2]` instead of `grocery_list[3]`. Well, that's because the `position` of the `first item` in an `array` is `0`. So, the `position` of `Tomato` is `2` not `3`.

> **Note:** The `position` of the `first item` in any `array` starts from `0` not `1`.

SO this array looks like this:

- `grocery_list`
    
    0. `Onion`
    1. `Potato`
    2. `Tomato`
    3. `Cucumber`
    4. `Carrot`

That's why I did `grocery_list[2]` instead of `grocery_list[3]`.

That's it. 

An `Array` is a `list` of `items` which we can `access` by giving the `position` of the `item` we want to `access`.

# Array in Python

In Python, there is no single `array` data structure instead It has 3 different types of `array` data structures. They are:

- `List`
- `Tuple`
- `Set`

> **Note:** `String` is also an `array` data structure but it is not a `collection` of `items` instead it is a `collection` of `characters`. So, we will not talk about `String` in this article.

# List

A `list` is a `collection` of `items` which is `mutable` and `ordered`. It is `mutable` which means we can `add`, `remove` and `change` the `items` in the `list`. It is `ordered` which means the `items` in the `list` has a `position` and we can `access` the `items` by giving the `position` of the `item` we want to `access`.

Let's see an example:




```python
bikes = [
    "Honda",
    "Yamaha",
    "Suzuki",
    "Kawasaki",
]

print(bikes[0])
print(bikes[1])
print(bikes[2])
```

    Honda
    Yamaha
    Suzuki


Here, we have a `list` of `bikes` and we can `access` the `items` in the `list` by giving the `position` of the `item` we want to `access`.

To access an `item` from a `list` we have to give the `name` of the `list` followed by `[]` and inside the `[]` we have to give the `position` of the `item` we want to `access`.

The `position` is also called `index` in python. From now on I will use the word `index` instead of `position`.

The index of a list starts from `0`. So, the index of `Honda` is `0`, the index of `Yamaha` is `1` and the index of `Suzuki` is `2`.

SO, whatever the list is if the list has `n` items then the index of the first item is `0` and the index of the last item is `n-1`.

But to make our work easier there is another way to access the items from a list. 

## Accessing items from a list using negative index



```python
print(bikes[-1]) # last item
print(bikes[-2]) # second last item
print(bikes[-3]) # third last item
```

    Kawasaki
    Suzuki
    Yamaha


SO, Python has a special index called `negative index`. The `negative index` starts from `-1`. So, the index of the last item is `-1` and the index of the first item is `-n`.

To make things a little bit more clear, 

`Python` has two indexing `peradigm`: `positive indexing` and `negative indexing`.

`Positive indexing` starts from `0` and ends at `n-1`. And it is the `default` indexing `peradigm` in `Python`. Which means `positive indexing` will access the `items` from the `list` from `left` to `right`.

`Negative indexing` starts from `-1` and ends at `-n`. Which means `negative indexing` will access the `items` from the `list` from `right` to `left`.




```python
#positive index
print(bikes[0]) # first item
print(bikes[1]) # second item

```

    Honda
    Yamaha



```python
#negetive index
print(bikes[-1]) # last item
print(bikes[-2]) # second last item
```

    Kawasaki
    Suzuki


So, this is negetive indexing.

## changing items in a list

We can also `change` the `items` in a `list`. Let's say we want to change the `item` in the `index` `0` to `Kawasaki`. We can do that by doing this:


```python
bikes[0] = "Kawasaki"

print(bikes)
```

    ['Kawasaki', 'Yamaha', 'Suzuki', 'Kawasaki']


as you can see I permanently changed the `item` in the `index` `0` to `Kawasaki`. 

So, we just have to give the `name` of the `list` followed by `[]`, inside the `[]` we have to give the `index` of the `item` we want to `change` and then we can assign a new `item` to that `index`.

The `bikes` list now has two kawsaki. One in the `index` `0` and another in the `index` `-1`(negetive for the last index).

## Adding items to a list

SO, we can access and change the `items` in a `list`. But what if we want to `add` an `item` to a `list`? Well, we can do that too.

There are couple of ways to `add` an `item` to a `list`. Let's see them one by one.

### Adding an item to the end of a list

let's say we have a `list` of `numbers` and we want to `add` a `number` to the `end` of the `list`. We can do that using the `append()` method.


```python
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# adding items to the list
list_of_nums.append(10)

print(list_of_nums)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


Now the list has a new `item` at the `end` of the `list`.

Python has no restriction on the `type` of the `item` we want to `add` to the `list`. We can `add` any `type` of `item` to the `list`.


```python
# adding my name in the list
list_of_nums.append("Rishat")

print(list_of_nums)
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Rishat']


Python has `dynamic typing` which means we don't have to specify the `type` of the `item` we want to `add` to the `list`. Python will automatically detect the `type` of the `item` and `add` it to the `list`.

### Adding an item to a specific index of a list

We can also `add` an `item` to a `specific index` of a `list`. Let's say we want to `add` `100` to the `index` `2` of the `numbers` list. We can do that by using the `insert()` method.



```python
list_of_nums.insert(0, "Rishat")

print(list_of_nums)
```

    ['Rishat', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Rishat']


The `insert()` methos takes two arguments. The first argument is the `index` where we want to `add` the `item` and the second argument is the `item` we want to `add` to the `list`.

So, if we want to add an item to the `46th` index of the `list` we can just do `list_name.insert(46, item)` and the `item` will be added to the `46th` index of the `list`.

### Adding multiple items to a list

We can also `add` multiple `items` to a `list` at once. Let's say we want to `add` `100`, `200` and `300` to the `numbers` list. We can do that by using the `extend()` method.



```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki"]
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

## adding multiple items to the list
bikes.extend(list_of_nums)

print(bikes)
```

    ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 1, 2, 3, 4, 5, 6, 7, 8, 9]


AS you can see all the items of `list_of_nums` is added to the `bikes` list. 

We can also `add` multiple `items` to a `list` by using the `+` operator. Let's say we want to `add` `100`, `200` and `300` to the `numbers` list. We can do that by using the `+` operator.


```python
list_of_names = ["Bob", "Alice", "John", "Mary", "Bob", "John"]
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#adding using +
print(list_of_names + list_of_nums)
```

    ['Bob', 'Alice', 'John', 'Mary', 'Bob', 'John', 1, 2, 3, 4, 5, 6, 7, 8, 9]


but this is not the best way to `add` multiple `items` to a `list` because the values are not `added` to the `list` permanently. They are just printed. If we want to `add` the `items` permanently to the `list` we have to do this:



```python

list_of_names = ["Bob", "Alice", "John", "Mary", "Bob", "John"]
list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#adding using +
list_of_names = list_of_names + list_of_nums

print(list_of_names)
```

    ['Bob', 'Alice', 'John', 'Mary', 'Bob', 'John', 1, 2, 3, 4, 5, 6, 7, 8, 9]


now the `items` are `added` to the `list` permanently which can also be removed from the `list`.

### Adding items to a list using list comprehension

`list comprehension` is a feature of `python` which allows us to `add` `items` to a `list` in a `single line`. Let's say we want to make a `list` of `numbers` from `1` to `1000000`. We cannot hard code it because it will take a lot of time. 

We can do this by a `for loop` like this:
```python
numbers = []

for i in range(1, 1000001):
    numbers.append(i)

print(numbers)
```

this will `add` all the `numbers` from `1` to `1000000` to the `numbers` list on by one. But this will take a lot of time.

But we can do this in a `single line` using `list comprehension` like this:




```python
numbers = [i for i in range(1, 1000001)]
numbers
```




    [1,
     2,
     3,
     4,
     5,
     6,
     7,
     8,
     9,
     10,
     11,
     12,
     13,
     14,
     15,
     16,
     17,
     18,
     19,
     20,
     21,
     22,
     23,
     24,
     25,
     26,
     27,
     28,
     29,
     30,
     31,
     32,
     33,
     34,
     35,
     36,
     37,
     38,
     39,
     40,
     41,
     42,
     43,
     44,
     45,
     46,
     47,
     48,
     49,
     50,
     51,
     52,
     53,
     54,
     55,
     56,
     57,
     58,
     59,
     60,
     61,
     62,
     63,
     64,
     65,
     66,
     67,
     68,
     69,
     70,
     71,
     72,
     73,
     74,
     75,
     76,
     77,
     78,
     79,
     80,
     81,
     82,
     83,
     84,
     85,
     86,
     87,
     88,
     89,
     90,
     91,
     92,
     93,
     94,
     95,
     96,
     97,
     98,
     99,
     100,
     101,
     102,
     103,
     104,
     105,
     106,
     107,
     108,
     109,
     110,
     111,
     112,
     113,
     114,
     115,
     116,
     117,
     118,
     119,
     120,
     121,
     122,
     123,
     124,
     125,
     126,
     127,
     128,
     129,
     130,
     131,
     132,
     133,
     134,
     135,
     136,
     137,
     138,
     139,
     140,
     141,
     142,
     143,
     144,
     145,
     146,
     147,
     148,
     149,
     150,
     151,
     152,
     153,
     154,
     155,
     156,
     157,
     158,
     159,
     160,
     161,
     162,
     163,
     164,
     165,
     166,
     167,
     168,
     169,
     170,
     171,
     172,
     173,
     174,
     175,
     176,
     177,
     178,
     179,
     180,
     181,
     182,
     183,
     184,
     185,
     186,
     187,
     188,
     189,
     190,
     191,
     192,
     193,
     194,
     195,
     196,
     197,
     198,
     199,
     200,
     201,
     202,
     203,
     204,
     205,
     206,
     207,
     208,
     209,
     210,
     211,
     212,
     213,
     214,
     215,
     216,
     217,
     218,
     219,
     220,
     221,
     222,
     223,
     224,
     225,
     226,
     227,
     228,
     229,
     230,
     231,
     232,
     233,
     234,
     235,
     236,
     237,
     238,
     239,
     240,
     241,
     242,
     243,
     244,
     245,
     246,
     247,
     248,
     249,
     250,
     251,
     252,
     253,
     254,
     255,
     256,
     257,
     258,
     259,
     260,
     261,
     262,
     263,
     264,
     265,
     266,
     267,
     268,
     269,
     270,
     271,
     272,
     273,
     274,
     275,
     276,
     277,
     278,
     279,
     280,
     281,
     282,
     283,
     284,
     285,
     286,
     287,
     288,
     289,
     290,
     291,
     292,
     293,
     294,
     295,
     296,
     297,
     298,
     299,
     300,
     301,
     302,
     303,
     304,
     305,
     306,
     307,
     308,
     309,
     310,
     311,
     312,
     313,
     314,
     315,
     316,
     317,
     318,
     319,
     320,
     321,
     322,
     323,
     324,
     325,
     326,
     327,
     328,
     329,
     330,
     331,
     332,
     333,
     334,
     335,
     336,
     337,
     338,
     339,
     340,
     341,
     342,
     343,
     344,
     345,
     346,
     347,
     348,
     349,
     350,
     351,
     352,
     353,
     354,
     355,
     356,
     357,
     358,
     359,
     360,
     361,
     362,
     363,
     364,
     365,
     366,
     367,
     368,
     369,
     370,
     371,
     372,
     373,
     374,
     375,
     376,
     377,
     378,
     379,
     380,
     381,
     382,
     383,
     384,
     385,
     386,
     387,
     388,
     389,
     390,
     391,
     392,
     393,
     394,
     395,
     396,
     397,
     398,
     399,
     400,
     401,
     402,
     403,
     404,
     405,
     406,
     407,
     408,
     409,
     410,
     411,
     412,
     413,
     414,
     415,
     416,
     417,
     418,
     419,
     420,
     421,
     422,
     423,
     424,
     425,
     426,
     427,
     428,
     429,
     430,
     431,
     432,
     433,
     434,
     435,
     436,
     437,
     438,
     439,
     440,
     441,
     442,
     443,
     444,
     445,
     446,
     447,
     448,
     449,
     450,
     451,
     452,
     453,
     454,
     455,
     456,
     457,
     458,
     459,
     460,
     461,
     462,
     463,
     464,
     465,
     466,
     467,
     468,
     469,
     470,
     471,
     472,
     473,
     474,
     475,
     476,
     477,
     478,
     479,
     480,
     481,
     482,
     483,
     484,
     485,
     486,
     487,
     488,
     489,
     490,
     491,
     492,
     493,
     494,
     495,
     496,
     497,
     498,
     499,
     500,
     501,
     502,
     503,
     504,
     505,
     506,
     507,
     508,
     509,
     510,
     511,
     512,
     513,
     514,
     515,
     516,
     517,
     518,
     519,
     520,
     521,
     522,
     523,
     524,
     525,
     526,
     527,
     528,
     529,
     530,
     531,
     532,
     533,
     534,
     535,
     536,
     537,
     538,
     539,
     540,
     541,
     542,
     543,
     544,
     545,
     546,
     547,
     548,
     549,
     550,
     551,
     552,
     553,
     554,
     555,
     556,
     557,
     558,
     559,
     560,
     561,
     562,
     563,
     564,
     565,
     566,
     567,
     568,
     569,
     570,
     571,
     572,
     573,
     574,
     575,
     576,
     577,
     578,
     579,
     580,
     581,
     582,
     583,
     584,
     585,
     586,
     587,
     588,
     589,
     590,
     591,
     592,
     593,
     594,
     595,
     596,
     597,
     598,
     599,
     600,
     601,
     602,
     603,
     604,
     605,
     606,
     607,
     608,
     609,
     610,
     611,
     612,
     613,
     614,
     615,
     616,
     617,
     618,
     619,
     620,
     621,
     622,
     623,
     624,
     625,
     626,
     627,
     628,
     629,
     630,
     631,
     632,
     633,
     634,
     635,
     636,
     637,
     638,
     639,
     640,
     641,
     642,
     643,
     644,
     645,
     646,
     647,
     648,
     649,
     650,
     651,
     652,
     653,
     654,
     655,
     656,
     657,
     658,
     659,
     660,
     661,
     662,
     663,
     664,
     665,
     666,
     667,
     668,
     669,
     670,
     671,
     672,
     673,
     674,
     675,
     676,
     677,
     678,
     679,
     680,
     681,
     682,
     683,
     684,
     685,
     686,
     687,
     688,
     689,
     690,
     691,
     692,
     693,
     694,
     695,
     696,
     697,
     698,
     699,
     700,
     701,
     702,
     703,
     704,
     705,
     706,
     707,
     708,
     709,
     710,
     711,
     712,
     713,
     714,
     715,
     716,
     717,
     718,
     719,
     720,
     721,
     722,
     723,
     724,
     725,
     726,
     727,
     728,
     729,
     730,
     731,
     732,
     733,
     734,
     735,
     736,
     737,
     738,
     739,
     740,
     741,
     742,
     743,
     744,
     745,
     746,
     747,
     748,
     749,
     750,
     751,
     752,
     753,
     754,
     755,
     756,
     757,
     758,
     759,
     760,
     761,
     762,
     763,
     764,
     765,
     766,
     767,
     768,
     769,
     770,
     771,
     772,
     773,
     774,
     775,
     776,
     777,
     778,
     779,
     780,
     781,
     782,
     783,
     784,
     785,
     786,
     787,
     788,
     789,
     790,
     791,
     792,
     793,
     794,
     795,
     796,
     797,
     798,
     799,
     800,
     801,
     802,
     803,
     804,
     805,
     806,
     807,
     808,
     809,
     810,
     811,
     812,
     813,
     814,
     815,
     816,
     817,
     818,
     819,
     820,
     821,
     822,
     823,
     824,
     825,
     826,
     827,
     828,
     829,
     830,
     831,
     832,
     833,
     834,
     835,
     836,
     837,
     838,
     839,
     840,
     841,
     842,
     843,
     844,
     845,
     846,
     847,
     848,
     849,
     850,
     851,
     852,
     853,
     854,
     855,
     856,
     857,
     858,
     859,
     860,
     861,
     862,
     863,
     864,
     865,
     866,
     867,
     868,
     869,
     870,
     871,
     872,
     873,
     874,
     875,
     876,
     877,
     878,
     879,
     880,
     881,
     882,
     883,
     884,
     885,
     886,
     887,
     888,
     889,
     890,
     891,
     892,
     893,
     894,
     895,
     896,
     897,
     898,
     899,
     900,
     901,
     902,
     903,
     904,
     905,
     906,
     907,
     908,
     909,
     910,
     911,
     912,
     913,
     914,
     915,
     916,
     917,
     918,
     919,
     920,
     921,
     922,
     923,
     924,
     925,
     926,
     927,
     928,
     929,
     930,
     931,
     932,
     933,
     934,
     935,
     936,
     937,
     938,
     939,
     940,
     941,
     942,
     943,
     944,
     945,
     946,
     947,
     948,
     949,
     950,
     951,
     952,
     953,
     954,
     955,
     956,
     957,
     958,
     959,
     960,
     961,
     962,
     963,
     964,
     965,
     966,
     967,
     968,
     969,
     970,
     971,
     972,
     973,
     974,
     975,
     976,
     977,
     978,
     979,
     980,
     981,
     982,
     983,
     984,
     985,
     986,
     987,
     988,
     989,
     990,
     991,
     992,
     993,
     994,
     995,
     996,
     997,
     998,
     999,
     1000,
     ...]



Okh, this is a little bit confusing. Let's break it down.

The `list comprehension` is a `single line` `for loop` which `adds` the `items` to the `list` in a `single line`.

The `list comprehension` starts with `[]` which means it is a `list`. Inside the `[]` we have a `for loop` which `adds` the `items` to the `list`.

In a `list comprehension` we have to give the `item` we want to `add` to the `list` followed by a `for loop` which will `add` the `items` to the `list`.

so, the `list comprehension` will look like this:

`[item for item in iterable]`

Here, `item` is the `item` we want to `add` to the `list` and `iterable` is the `iterable` object which will `add` the `items` to the `list`.

In our case, the `item` is `i` and the `iterable` is `range(1, 1000001)`.

And that's how we can `add` `items` to a `list` using `list comprehension`.

> **Note:** `list comprehension` is a very important feature of `python` and it is used a lot in `competitive programming`. So, make sure you understand it properly. And list comprehension is not only limited to `list`. We can also use `list comprehension` in `tuple` and `set`. Study `list comprehension` properly.

## Removing items from a list

As, we can add an `Item` to a `list` we can also `remove` an `item` from a `list`. Let's see how we can `remove` an `item` from a `list`.

there are couple of ways to `remove` an `item` from a `list`. Let's see them one by one.

### Removing an item from a list using the remove() method

We can `remove` an `item` from a `list` by using the `remove()` method. Let's say we want to `remove` `Honda` from the `bikes` list. We can do that by using the `remove()` method.


```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki"]

#removing items from the list using remove()
bikes.remove("Honda")

print(bikes)
```

    ['Yamaha', 'Suzuki', 'Kawasaki']


`remove()` method takes one argument which is the `item` we want to `remove` from the `list`.

But if you have multiple `items` with the same `value` in the `list` then the `remove()` method will `remove` the `first item` with that `value` from the `list`.


```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki", "Honda"]

#removing items from the list using remove()
bikes.remove("Honda")

print(bikes)
```

    ['Yamaha', 'Suzuki', 'Kawasaki', 'Honda']


As you can see the `remove()` methos only removed the `first item` with the value `Honda` from the `list`.

### Removing an item from a list using the pop() method

`Pop()` method removes an `Item` according to their `index`. Let's say we want to `remove` the `item` in the `index` `1` from the `bikes` list. We can do that by using the `pop()` method.


```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki", "Honda"]

#removing items from the list using pop()
bikes.pop(1)

print(bikes)
```

    ['Honda', 'Suzuki', 'Kawasaki', 'Honda']


`pop(1)` removes the item in the `index` `1` from the `list`.

But if we don't give any `index` to the `pop()` method then it will `remove` the `last item` from the `list`.


```python
print(bikes)

bikes.pop()

print(bikes)
```

    ['Honda', 'Suzuki', 'Kawasaki', 'Honda']
    ['Honda', 'Suzuki', 'Kawasaki']


the last item from the `list` is `Honda` and it is removed from the `list`.

> there are some extra things about the `pop()` method too.

When we remove an item from a list using the `pop()` method it returns the `item` which is removed from the `list`. Let's say we want to `remove` the `item` in the `index` `2` from the `bikes` list and store it in a variable. We can do that by using the `pop()` method.


```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki",]

popped_value = bikes.pop(2)

print(bikes)
print(f"popped value: {popped_value}")
```

    ['Honda', 'Yamaha', 'Kawasaki']
    popped value: Suzuki


This can be useful in some cases.

### Removing an item from a list using the del keyword

We can also `remove` an `item` from a `list` by using the `del` keyword. Let's say we want to `remove` the `item` in the `index` `0` from the `bikes` list. We can do that by using the `del` keyword.

`del` keyword takes the `index` of the `item` we want to `remove` from the `list`.


```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki",]

#removing items from the list using del

del bikes[2]

print(bikes)
```

    ['Honda', 'Yamaha', 'Kawasaki']


> **Note:** `del` is a keyword in `python` so we have to be provide the `index` of the `item` we along with the list name. We cannot use `del` keyword and just the `index`. we have to use `del list_name[index]`.

### Removing all the items from a list using the clear() method

We can also `remove` all the `items` from a `list` by using the `clear()` method. Let's say we want to `remove` all the `items` from the `bikes` list. We can do that by using the `clear()` method.

`clear()` method removes all the `items` from the `list`.


```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki",]

#removing items from the list using clear

bikes.clear()

print(bikes)
```

    []


the list is now empty.

## Copying a list

We can also `copy` a `list`. Let's say we want to `copy` the `bikes` list and store it in a new list called `bikes_copy`. We can do that by using the `copy()` method.

`copy()` method copies the `list` and stores it in a new `list`.

now might think why we need the `copy()` method at all. Well, let's say we want to `copy` the `bikes` list and store it in a new list called `bikes_copy`. We can do that by using the `=` operator.



```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki",]

bike_copy = bikes

print(f"bikes: {bikes}")
print(f"bike_copy: {bike_copy}")
```

    bikes: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
    bike_copy: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']


Looks the list is copied perfectly. lets try to `change` the `bikes_copy` list and see what happens.


```python
bike_copy.append("Ducati")

print(f"bikes: {bikes}")
print(f"bike_copy: {bike_copy}")
```

    bikes: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'Ducati']
    bike_copy: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'Ducati']


Huh?! The `bikes` list is also changed. But we only changed the `bikes_copy` list. Why did the `bikes` list changed too?

It's because when we use the `=` operator to `copy` a `list` it doesn't `copy` the `list`. It just creates a `reference` to the `list`. So, when we `change` the `bikes_copy` list it also `changes` the `bikes` list because they are the same `list`. 

***`Even though we changed the bikes_copy list, the bikes list also changed because they are the same list.`***

So, to get a `copy` of a `list` we have to use the `copy()` method.



```python
bikes = ["Honda", "Yamaha", "Suzuki", "Kawasaki",]
bike_copy = bikes.copy()

print(f"bikes: {bikes}")
print(f"bike_copy: {bike_copy}")
```

    bikes: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
    bike_copy: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']



```python
bike_copy.append("Ducati")

print(f"bikes: {bikes}")
print(f"bike_copy: {bike_copy}")
```

    bikes: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki']
    bike_copy: ['Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'Ducati']


Now the main `list` and the `copied list` are two different `list` and changing the `copied list` will not affect the main `list`.

## Looping through a list

Looping through a something in python is very easy. We can loop through a `list` by using a `for loop`. Even if it's an `iterable` object we can loop through it using a `for loop`.


```python
names = ["Bob", "Alice", "John", "Mary", "Bob", "John"]

for name in names:
    print(name)
```

    Bob
    Alice
    John
    Mary
    Bob
    John


The for loop will go through each `item` in any `iterable` object and store it in a variable. We can use that variable to do something with the `item`.

The `for loop` will look like this:

```python
for item in iterable:
    # do something with the item
```

Here, `item` is the variable which will store the `item` from the `iterable` object and `iterable` is the `iterable` object we want to loop through.

This can be a little problematic if we want to loop through a `list` and also want to know the `index` of the `item` we are looping through.


```python
for i in range(len(names)):
    print(names[i])
```

    Bob
    Alice
    John
    Mary
    Bob
    John


`range(len(list))` will give us a `range` object which will start from `0` and end at `n-1` where `n` is the length of the `list`. So, we can use this `range` object to loop through the `list` and also get the `index` of the `item` we are looping through.

this can be a little confusing too. 

SO, I loop through a `list/iterable` object like this.


```python
for ind, name in enumerate(names):
    print(f"{ind}: {name}")
```

    0: Bob
    1: Alice
    2: John
    3: Mary
    4: Bob
    5: John


`enumerate()` method takes an `iterable` object and returns a `tuple` of `index` and `item` of the `iterable` object.

So, I get both the `index` and the `item` of the `iterable` object at the same time.

## Sorting a list

We can also `sort` a `list`. Let's say we want to `sort` the `numbers` list. We can do that by using the `sort()` method.


```python
#making a random list of 100 numbers
import random

random_list = [random.randint(1, 100) for i in range(100)]

print(random_list)
```

    [6, 83, 9, 31, 96, 8, 51, 99, 93, 31, 27, 61, 98, 95, 24, 50, 43, 92, 71, 19, 44, 58, 75, 5, 36, 54, 42, 12, 1, 63, 75, 87, 47, 85, 58, 80, 70, 51, 64, 91, 39, 29, 65, 9, 84, 34, 1, 55, 96, 77, 83, 91, 26, 43, 84, 73, 78, 6, 73, 65, 32, 36, 85, 1, 76, 70, 48, 43, 35, 7, 82, 61, 95, 56, 61, 15, 52, 95, 14, 29, 32, 72, 93, 75, 62, 96, 41, 42, 83, 87, 41, 49, 86, 46, 74, 99, 81, 19, 89, 7]


Here, i made a list of 100 random numbers now I want to sort the list. I can do that by using the `sort()` method.


```python
random_list.sort()

print(random_list)
```

    [1, 1, 1, 5, 6, 6, 7, 7, 8, 9, 9, 12, 14, 15, 19, 19, 24, 26, 27, 29, 29, 31, 31, 32, 32, 34, 35, 36, 36, 39, 41, 41, 42, 42, 43, 43, 43, 44, 46, 47, 48, 49, 50, 51, 51, 52, 54, 55, 56, 58, 58, 61, 61, 61, 62, 63, 64, 65, 65, 70, 70, 71, 72, 73, 73, 74, 75, 75, 75, 76, 77, 78, 80, 81, 82, 83, 83, 83, 84, 84, 85, 85, 86, 87, 87, 89, 91, 91, 92, 93, 93, 95, 95, 95, 96, 96, 96, 98, 99, 99]


And **BOOM** the list is sorted.

`sort()` method sorts the `list` in `ascending` order by default. But we can also sort the `list` in `descending` order by using the `reverse` argument of the `sort()` method like this `sort(reverse=True)`.

Try it yourself to see what happens.

> **Note:** `sort()` method only works with `list` and it doesn't return anything. It just sorts the `list` permanently.

> **Note:** `sort()` method uses `Timsort` algorithm to sort the `list`. `Timsort` is a combination of `Merge sort` and `Insertion sort` algorithm. `Timsort` is the fastest sorting algorithm in python.



## List Methods

Heres a list of all the `list` methods in python:

| Method | Description |
| ------ | ----------- |
| append() | Adds an element at the end of the list |
| clear() | Removes all the elements from the list |
| copy() | Returns a copy of the list |
| count() | Returns the number of elements with the specified value |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index() | Returns the index of the first element with the specified value |
| insert() | Adds an element at the specified position |
| pop() | Removes the element at the specified position |
| remove() | Removes the item with the specified value |
| reverse() | Reverses the order of the list |
| sort() | Sorts the list |


## List slicing

I almost forgot to tell you about `list slicing`. `List slicing` is a very important feature of `python` and it is used a lot in `competitive programming`. So, make sure you understand it properly.

`List slicing` is a way to `slice` a `list` into `sub-lists`. Let's say we have a `list` of `numbers` from `1` to `100`. We can `slice` the `list` into `sub-lists` like this:

`list_name[start:stop:step]`

Here, `start` is the `index` of the `list` where we want to `start` the `slice`. `stop` is the `index` of the `list` where we want to `stop` the `slice`. And `step` is the `step size` of the `slice`.

> **Note:** `start` is inclusive and `stop` is exclusive. Which means the `start` index will be included in the `slice` but the `stop` index will not be included in the `slice`.

Let's say we want to `slice` the `numbers` list from `index` `0` to `index` `100`. We can do that by doing this:


```python
numbers = [i for i in range(0, 101)]

# slicing the list from 30 to 50
print(numbers[30:51])
```

    [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]


Here, the `start` index is `30` and the `stop` index is `71`. So, the `slice` will start from `index` `30` and end at `index` `70`. And the `step size` is not given so, the `step size` is `1` by default. The default `start` index is `0` and the default `stop` index is `n` where `n` is the length of the `list`.(the `stop` index is `n` because the `stop` index is exclusive).

lets see some more examples:


```python
print(numbers[:42:1]) # start = 0(default), end = 42, step = 1
print(numbers[42:]) # start = 42, end = end of the list(default), step = 1(default)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]



```python
print(numbers[::2]) # start = 0(default), end = end of the list(default), step = 2
print(numbers[::3]) # start = 0(default), end = end of the list(default), step = 3
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]



```python
print(numbers[32::5]) # start = 32, end = end of the list(default), step = 5
```

    [32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97]


ANNNDDD there you go `list slicing` in a nutshell.

> **Note:** `list slicing` is not only limited to `list`. We can also use `list slicing` in `tuple` , `set` and `string`. Study `list slicing` properly.

That's it for `list`. Now let's talk about `tuple`.


# Tuple

A `tuple` is a `collection` of `items` which is `immutable` and `ordered`. It is `immutable` which means we cannot `add`, `remove` or `change` the `items` in the `tuple`. It is `ordered` which means the `items` in the `tuple` has a `position` and we can `access` the `items` by giving the `position` of the `item` we want to `access`.

Basically, a `tuple` is a `list` where we cannot `add`, `remove` or `change` the `items`.

Let's see an example:
```python
berries = ("Strawberry", "Blueberry", "Raspberry", "Blackberry")
```

Here, we have a `tuple` of `berries`. How do we know it's a `tuple`? Well, it's because it has `()` instead of `[]`. So, a list has `[]` and a `tuple` has `()`.

## Accessing items from a tuple

We can `access` the `items` from a `tuple` just like we `access` the `items` from a `list`. Let's say we want to `access` the `item` in the `index` `1` from the `berries` tuple. We can do that by doing this:

```python
print(berries[1])

```

As you can see we can `access` the `items` from a `tuple` just like we `access` the `items` from a `list`.

also it has the same `indexing` system as a `list`. The `index` of the `first item` is `0` and the `index` of the `last item` is `n-1` where `n` is the length of the `tuple`.

it also has `negative indexing` like a `list`. The `index` of the `last item` is `-1` and the `index` of the `first item` is `-n` where `n` is the length of the `tuple`.




```python
berries = ("Strawberry", "Blueberry", "Raspberry", "Blackberry")

print(berries[-1])
```

    Blackberry


Accessing is the same as a `list`. So, I am not going to talk about it anymore.

## Changing items in a tuple

We cannot `change` the `items` in a `tuple`. Let's say we want to `change` the `item` in the `index` `0` to `Cherry`. We cannot do that because `tuple` is `immutable`.

But we can `change` a `tuple` to a `list` and then `change` the `items` in the `list` and then `change` the `list` back to a `tuple`. Let's see how we can do that.


```python
berries = ("Strawberry", "Blueberry", "Raspberry", "Blackberry")

berries_list = list(berries)

print(berries)

berries_list.append("Gooseberry")

berries = tuple(berries_list)

print(berries)
```

    ('Strawberry', 'Blueberry', 'Raspberry', 'Blackberry')
    ('Strawberry', 'Blueberry', 'Raspberry', 'Blackberry', 'Gooseberry')


First, we have to `change` the `tuple` to a `list` by using the `list()` method.

Now we can `change` the `items` in the `list` like we `change` the `items` in a `list`.

Now we have to `change` the `list` back to a `tuple` by using the `tuple()` method.

Now the `tuple` is `changed` to a `list` and the `items` in the `list` is `changed` and the `list` is `changed` back to a `tuple`.

Now i leave the rest to you to figure out how to `add` and `remove` `items` from a `tuple`.

## Unpacking a tuple

We can also `unpack` a `tuple`. Let's say we have a `tuple` of `coordinates` and we want to `unpack` the `tuple` and store the `items` in a variable. We can do that by doing this:


```python
coordinates = (1, 2, 3)

#unpacking the tuple
x, y, z = coordinates

print(x)
print(y)
print(z)
```

    1
    2
    3


`(1,2,3)` is the coordinates `tuple` and `x, y, z` are the variables where we want to store the `items` from the `tuple`.

SO, we can `unpack` a `tuple` and store the `items` in a variable. The number of variables should be equal to the number of `items` in the `tuple`. Otherwise, we will get an error. 

The veriables corresponding to the `items` in the `tuple` will store the `items` from the `tuple`. SO, the first variable will store the first item, the second variable will store the second item and so on.

### Using * to unpack a tuple

I said the number of variables should be equal to the number of `items` in the `tuple`. But what if we want to `unpack` a `tuple` and store the `items` in a variable but we don't know how many `items` are there in the `tuple`? Well, we can use `*` to `unpack` the `tuple` and store the `items` in a variable. Let's see how we can do that.



```python
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
```

    apple
    banana
    ['cherry', 'strawberry', 'raspberry']


So, the `*` will `unpack` the `tuple` and store the `items` in a variable. The `items` will be stored in a `list` and the `list` will be stored in the variable.

Try to `unpack` a `tuple` and store the `items` in a variable using `*` in the middle variable and see what happens.

## Joining tuples and looping through tuples

We can also `join` two `tuples` and `loop` through a `tuple` Just like we `join` two `lists` and `loop` through a `list`


```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1 + list2

print(f"list3: {list3}")

for ind,val in enumerate(list3):
    print(f"{ind}; {val}")
```

    list3: [1, 2, 3, 4, 5, 6]
    0; 1
    1; 2
    2; 3
    3; 4
    4; 5
    5; 6


## Tuple Methods

Heres a list of all the `tuple` methods in python:

| Method | Description |
| ------ | ----------- |
| count() | Returns the number of times a specified value occurs in a tuple |
| index() | Searches the tuple for a specified value and returns the position of where it was found |


That's it for `tuple`. Now let's talk about `set`.

# Set

A `set` is a `collection` of `items` which is `mutable` and `unordered`. It is `mutable` which means we can `add` and `remove` the `items` in the `set`. It is `unordered` which means the `items` in the `set` has no `position` and we cannot `access` the `items` by giving the `position` of the `item` we want to `access`.

SO, a `set` is a `list` where we cannot `access` the `items` by giving the `position` of the `item` we want to `access` but we can `add` and `remove` the `items` in the `set`.

> **Note:** A `set` is a `collection` of `unique` `items` which is `unordered`, `unindexed` and `mutable`. There cannot be two `items` with the same `value` in a `set`.



```python
a_set_of_fruts = {"apple", "banana", "cherry"}

print(a_set_of_fruts)
```

    {'banana', 'apple', 'cherry'}



```python
print(a_set_of_fruts[0])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[41], line 1
    ----> 1 print(a_set_of_fruts[0])


    TypeError: 'set' object is not subscriptable


AS, you can see we cannot access the `items` in a `set` by giving the `position` of the `item` we want to `access`. 

let's see if we can have a `set` with two `items` with the same `value`.


```python
a_set_of_random_values = {"Honda",3.5, 1, True, "Honda"}

print(a_set_of_random_values)
```

    {1, 3.5, 'Honda'}


So, no matter how many times we `add` the `item` with the same `value` to the `set` it will only be added once.

But what happened to the `True` value in the set.

> **Note:** `True` and `False` are the `boolean` values in python. `True` means `1` and `False` means `0`. SO, if you add both `True` and `1` to a `set` it will only be added once because they have the same `value`.

So, in our set the `True` value is replaced by `1` because they have the same `value`.

## Adding items to a set

We can `add` an `item` to a `set` by using the `add()` method. Let's say we want to `add` `Apple` to the `fruits` set. We can do that by using the `add()` method.


```python
a_set_of_foods = {"pizza", "burger", "pasta", "pizza"}

print(a_set_of_foods)

a_set_of_foods.add("salad")

print(a_set_of_foods)
```

    {'pizza', 'pasta', 'burger'}
    {'pizza', 'salad', 'pasta', 'burger'}


`add()` method takes one argument which is the `item` we want to `add` to the `set`. It's like the `append()` method of a `list` but it adds the `item` to the `set` without any `index`.

But there is another way to `add` an `item` to a `set`. 

`update()` method takes one or more arguments which are the `items` we want to `add` to the `set`. Let's say we want to `add` `Apple`, `Banana` and `Cherry` to the `fruits` set. We can do that by using the `update()` method.


```python
this_is_a_set = {"apple", "banana", "cherry"}
this_is_another_set = {"google", "microsoft", "apple"}

this_is_a_set.update(this_is_another_set)

print(this_is_a_set)
```

    {'banana', 'apple', 'google', 'microsoft', 'cherry'}


We can also use the `update()` method to `add` a `list` to a `set`. Let's say we want to `add` the `fruits_list` to the `fruits` set. We can do that by using the `update()` method.


```python
this_is_a_set = {"apple", "banana", "cherry"}
this_is_a_list = ["Honda", "Yamaha", "Suzuki"]

this_is_a_set.update(this_is_a_list)            

print(this_is_a_set)
```

    {'banana', 'apple', 'Suzuki', 'Yamaha', 'cherry', 'Honda'}


## Removing items from a set

There are couple of ways to `remove` an `item` from a `set`. Let's see them one by one.

### Removing an item from a set using the remove() method

We can `remove` an `item` from a `set` by using the `remove()` method. Let's say we want to `remove` `Apple` from the `fruits` set. We can do that by using the `remove()` method.


```python
a_set_of_fruts = {"apple", "banana", "cherry"}

print(a_set_of_fruts)

a_set_of_fruts.remove("apple")

print(a_set_of_fruts)
```

    {'banana', 'apple', 'cherry'}
    {'banana', 'cherry'}


`remove()` method takes one argument which is the `item` we want to `remove` from the `set`. So, if we want to `remove` a `item` from a `set` we have to give the `item` we want to `remove` to the `remove()` method.

> But if we give an `item` which is not in the `set` to the `remove()` method then we will get an error.

### Removing an item from a set using the discard() method

We can also `remove` an `item` from a `set` by using the `discard()` method. Let's say we want to `remove` `Apple` from the `fruits` set. We can do that by using the `discard()` method.


```python
a_set_of_fruts.discard("apple")
print(a_set_of_fruts)
```

    {'banana', 'cherry'}


As you can see `discard()` method works the same as the `remove()` method. But if we give an `item` which is not in the `set` to the `discard()` method then we will not get an `error` like the `remove()` method.

### Removing an item from a set using the pop() method

If you want to remove `random` `item` from a `set` then we can use the `pop()` method. Let's say we want to `remove` a `random` `item` from the `fruits` set. We can do that by using the `pop()` method.


```python
a_set_of_fruts = {"apple", "banana", "cherry", "strawberry", "raspberry"}

a_set_of_fruts.pop()
```




    'banana'



The `pop()` method removed the `first item` instead of the last item like it does in a `list`. Because a `set` is `unordered` so, there is no `first item` or `last item` in a `set`. So, the `pop()` method removes a `random item` from the `set`.

## Looping through a set

We can also `loop` through a `set`. Let's say we want to `loop` through the `fruits` set. We can do that by using a `for loop`. It's just as the same as `looping` through a `list`.

## Joining two sets

This is the interesting part. 

If you about `set` in `math` then this will be very easy for you to understand. If you don't know about `set` in `math` then no worries.

### Union of two sets

Let's say we have two `sets` `set1` and `set2`. We want to `join` the two `sets` and store it in a new `set` called `set3`. We can do that by using the `union()` method.

`union()` method takes one argument which is the `set` we want to `join` with the `set` we are using the `union()` method on.

`Union` means `joining` two `sets` and removing the `duplicate items`. So, the `union()` method `joins` the two `sets` and removes the `duplicate items` and stores it in a new `set`.

So, the `union()` method `joins` the two `sets` and stores it in a new `set`.


```python
set1 = {1, 2, 3}
set2 = {"a", "b", "c",1}

set3 = set1.union(set2)

print(set3)
```

    {'a', 1, 2, 3, 'c', 'b'}


`union()` method also takes multiple arguments. Let's say we have three `sets` `set1`, `set2` and `set3`. We want to `join` the three `sets` and store it in a new `set` called `set4`. We can do that by using the `union()` method.

### Intersection of two sets

Let's say we have two `sets` `set1` and `set2`. We want to find the `intersection` of the two `sets` and store it in a new `set` called `set3`. We can do that by using the `intersection()` method.

`intersection()` method takes one argument which is the `set` we want to find the `intersection` with the `set` we are using the `intersection()` method on.

`Intersection` means `finding` the `common items` in two `sets`. So, the `intersection()` method `finds` the `common items` in two `sets` and stores it in a new `set`.

So, the `intersection()` method `finds` the `common items` in two `sets` and stores it in a new `set`.


```python
set1 = {1, 2, 3}
set2 = {"a", "b", "c",1}

set3 = set1.intersection(set2)
print(set3)
```

    {1}


So, this prints `{1}` because `1` is the only `common item` in the two `sets`.

### Difference of two sets

Let's say we have two `sets` `set1` and `set2`. We want to find the `difference` of the two `sets` and store it in a new `set` called `set3`. We can do that by using the `symmetric_difference()` method.

`symmetric_difference()` method takes one argument which is the `set` we want to find the `difference` with the `set` we are using the `symmetric_difference()` method on.

`Difference` means `finding` the `items` which are not in both `sets` meaning that the new `set` will only have the `items` of both `sets` but not the `common items`. 

So, the `symmetric_difference()` method `finds` the `items` which are not in both `sets` and stores it in a new `set`.


```python
set1 = {1, 2, 3,"a"}
set2 = {"a", "b", "c",1,}

set3 = set1.symmetric_difference(set2)

print(set3)
```

    {2, 3, 'c', 'b'}


There is another method named `difference()` which does the same thing as the `symmetric_difference()` method but it only returns the `items` which are not in the `set` we are using the `difference()` method on.


```python
set1 = {1, 2, 3,"a"}
set2 = {"a", "b", "c",1,}

set3 = set1.difference(set2)

print(set3)
```

    {2, 3}


So, `difference()` only return the `items` of `set1` whicha are not in `set2`.

## Set Methods

Heres a list of all the `set` methods in python:

| Method | Description |
| ------ | ----------- |
| add() | Adds an element to the set |
| clear() | Removes all the elements from the set |
| copy() | Returns a copy of the set |
| difference() | Returns a set containing the difference between two or more sets |
| difference_update() | Removes the items in this set that are also included in another, specified set |
| discard() | Remove the specified item |
| intersection() | Returns a set, that is the intersection of two other sets |
| intersection_update() | Removes the items in this set that are not present in other, specified set(s) |
| isdisjoint() | Returns whether two sets have a intersection or not |
| issubset() | Returns whether another set contains this set or not |
| issuperset() | Returns whether this set contains another set or not |
| pop() | Removes an element from the set |
| remove() | Removes the specified element |
| symmetric_difference() | Returns a set with the symmetric differences of two sets |
| symmetric_difference_update() | inserts the symmetric differences from this set and another |
| union() | Return a set containing the union of sets |
| update() | Update the set with the union of this set and others |

That's it for `set`. 

We will not talk about `dictionary` because as it is also a `collection` of `items` it is a representation of `key-value` pairs which is a little bit different from `array` and more like `hashmap`. SO, we will talk about `dictionary` in the hashmap section..

Now time for some problem solving.

# Problem solving

`Blind 75 Leetcode` is very popular among the `competitive programmers`. It is a list of 75 problems which are very important for `competitive programming`. So, I will solve all the problems from the `Blind 75 Leetcode` list in this section.

It will also help with `coding interviews` because the problems are very important for `coding interviews` too.

There are different lists of `Blind 75`. There is one in the `Leetcode` website named `leetcode 75`. There is one in the `GeeksforGeeks` website and there other lists too. But I liked the list in `techinterviewhandbook` website. it is called the `grind 75`. So, I will solve the `grind 75` list in this section.

You can find the `grind 75` list (https://www.techinterviewhandbook.org/grind75?grouping=topics).

> if you click on a problem in the list it will take you to the `leetcode` problem page. So, you can solve the problem in `leetcode` and see if your solution is correct or not.

I will solve the problems in `python` in python and in this document I will go through `array` section of the `grind 75` list.

There are `11` `array` problems in the `grind 75` list. So, I will solve all the `11` problems in this section. And discuss the solutions and the algorithms we can use to solve the problems.

so, let's do this.

## How to solve a problem in `leetcode`?

Before we start solving the problems we have to know how to solve a problem in `leetcode`. 

When we click on a problem in `leetcode` it will take us to the problem page. In the problem page we will see the problem statement and the `test cases` of the problem.

The `test cases` are the `inputs` and the `outputs` of the problem. The `inputs` are the `inputs` we will give to the `function` and the `outputs` are the `outputs` we will get from the `function`.

We have to write a `function` which will take the `inputs` and return the `outputs`. If the `outputs` are correct then we will get a `green tick` otherwise we will get a `red cross`.

You sould see something like this:

```python

class Solution:
    def function_name(self, input1, input2, input3):
        # write your code here
        return output
```

The `function` will look like this. The `function` will take the `inputs` and return the `outputs`. We have to write the `code` in the `function` which will take the `inputs` and return the `outputs`.

The `inputs` and the `outputs` will be given in the `test cases`. You don't need to worry about the `test cases`. You just have to write the `code` in the `function` which will take the `inputs` and return the `outputs`.

> **Note:** The `function` name will be given in the `test cases`. So, you don't need to worry about the `function` name. You just have to write the `code` in the `function` which will take the `inputs` and return the `outputs`.

That's it for `leetcode`. Now let's start solving the problems.

## Problem 1: Two Sum

### Problem Statement

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

### Example 2:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Example 3:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

You can find the problem in leetcode (https://leetcode.com/problems/two-sum/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`. 
> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### Approach 1: Brute Force

The first approach that comes to mind is the `brute force` approach. 

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will loop through the `nums` list again and check if the `sum` of the `item` and the `item` in the second loop is equal to the `target` or not. If it is equal to the `target` then we will return the `index` of the `item` in the first loop and the `index` of the `item` in the second loop.

***Solution steps:***

1. Loop through the `nums` list and store the `item` in a variable.

2. Loop through the `nums` list again and store the `item` in a variable.

3. Check if the `sum` of the `item` in the first loop and the `item` in the second loop is equal to the `target` or not.

4. If it is equal to the `target` then return the `index` of the `item` in the first loop and the `index` of the `item` in the second loop.

***Solution in python:***

I will just follow the steps I mentioned above.

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

```

***Explanation:***

1. I loop through the `nums` list and store the `item` in the `i` variable.

2. I loop through the `nums` list again and store the `item` in the `j` variable.

3. I check if the `sum` of the `item` in the `i` variable and the `item` in the `j` variable is equal to the `target` or not.

4. If it is equal to the `target` then I return the `index` of the `item` in the `i` variable and the `index` of the `item` in the `j` variable.

***Complexity Analysis:***

* Time complexity : O(n^2)

  For each `item` in the `nums` list we loop through the `nums` list again. So, the time complexity is O(n^2).

* Space complexity : O(1)
    
      We are not using any extra space. So, the space complexity is O(1).

### Approach 2: Finding the complement

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will check if the `complement` of the `item` is in the `nums` list or not. If the `complement` of the `item` is in the `nums` list then we will return the `index` of the `item` and the `index` of the `complement`.

***Solution steps:***

1. Loop through the `nums` list and store the `item` in a variable.

2. Check if the `complement` of the `item` is in the `nums` list or not.

3. If the `complement` of the `item` is in the `nums` list then return the `index` of the `item` and the `index` of the `complement`.

***Solution in python:***

```python
class Solution:
    def twoSum(self, nums, target):
        for ind, num in enumerate(nums):
            complement = target - num

            if complement in nums[ind+1:]:
                nums[ind] = None
                return [ind, nums.index(complement)]

```

***Explanation:***

1. I loop through the `nums` list and store the `item` in the `num` variable and the `index` of the `item` in the `ind` variable.

2. I find the `complement` of the `item` and store it in the `complement` variable.

3. I check if the `complement` of the `item` is in the `nums` list or not.

4. If the `complement` of the `item` is in the `nums` list then I return the `index` of the `item` and the `index` of the `complement`.

***Complexity Analysis:***

* Time complexity : O(n^2)

  For each `item` in the `nums` list we loop through the `nums` list again. So, the time complexity is O(n^2).

* Space complexity : O(1)
    
      We are not using any extra space. So, the space complexity is O(1).

### Approach 3: Using a dictionary(My favorite approach)

In this approach we will use a `dictionary` to solve the problem.

***Solution steps:***

1. Create a `dictionary`.

2. Loop through the `nums` list and store the `target - item` in the `dictionary` as the `key` and the `index` of the `item` as the `value`.

3. Loop through the `nums` list and check if the `item` is in the `dictionary` or not.

4. If the `item` is in the `dictionary` then return the `index` of the `item` and the `value` of the `item` in the `dictionary`.

***Solution in python:***

```python
class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for ind, num in enumerate(nums):
            if num in dic:
                return [dic[num], ind]
            else:
                dic[target - num] = ind

```

***Explanation:***

1. I create a `dictionary` named `dic`.

2. I loop through the `nums` list and store the `target - item` in the `dic` as the `key` and the `index` of the `item` as the `value`.

3. I loop through the `nums` list and check if the `item` is in the `dic` or not.

4. If the `item` is in the `dic` then I return the `index` of the `item` and the `value` of the `item` in the `dic`.

***Complexity Analysis:***

* Time complexity : O(n)

  We loop through the `nums` list twice. So, the time complexity is O(n).

* Space complexity : O(n)
    
      We are using a `dictionary` to store the `items` of the `nums` list. So, the space complexity is O(n).

## Problem 2: Best Time to Buy and Sell Stock

### Problem Statement

You are given an `array` `prices` where `prices[i]` is the `price` of a given `stock` on the `ith` day.

You want to `maximize` your `profit` by choosing a `single day` to `buy` one `stock` and choosing a `different day` in the `future` to `sell` that `stock`.

Return the `maximum profit` you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### Example 1:

```

Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation:

Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

### Example 2:

```

Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.

```

You can find the problem in leetcode (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).


> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`. 
> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### Approach 1: Brute Force

The first approach that comes to mind is the `brute force` approach.

In this approach we will loop through the `prices` list and for each `item` in the `prices` list we will loop through the `prices` list again and check if the `difference` between the `item` and the `item` in the second loop is greater than the `max_profit` or not. If it is greater than the `max_profit` then we will store the `difference` in the `max_profit` variable.

***Solution steps:***

1. Loop through the `prices` list and store the `item` in a variable.

2. Loop through the `prices` list again and store the `item` in a variable.

3. Check if the `difference` between the `item` in the first loop and the `item` in the second loop is greater than the `max_profit` or not.

4. If it is greater than the `max_profit` then store the `difference` in the `max_profit` variable.

5. Return the `max_profit` variable.

***Solution in python:***

I will just follow the steps I mentioned above.

```python

class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit

```

> This is not accepted in `leetcode` because it exceeds the time limit. 

So, we have to find a better approach.

### Approach 2: One pass

In this approach we will loop through the `prices` list and for each `item` in the `prices` list we will check if the `item` is less than the `min_price` or not. If the `item` is less than the `min_price` then we will store the `item` in the `min_price` variable. Then we will check if the `difference` between the `item` and the `min_price` is greater than the `max_profit` or not. If it is greater than the `max_profit` then we will store the `difference` in the `max_profit` variable.

***Solution steps:***

1. Loop through the `prices` list and store the `item` in a variable.

2. Check if the `item` is less than the `min_price` or not.

3. If the `item` is less than the `min_price` then store the `item` in the `min_price` variable.

4. Check if the `difference` between the `item` and the `min_price` is greater than the `max_profit` or not.

5. If it is greater than the `max_profit` then store the `difference` in the `max_profit` variable.

6. Return the `max_profit` variable.

***Solution in python:***

I will just follow the steps I mentioned above.

```python

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit

```

***Explanation:***

1. I loop through the `prices` list and store the `item` in the `i` variable.

2. I check if the `item` is less than the `min_price` or not.

3. If the `item` is less than the `min_price` then I store the `item` in the `min_price` variable.

4. I check if the `difference` between the `item` and the `min_price` is greater than the `max_profit` or not.

5. If it is greater than the `max_profit` then I store the `difference` in the `max_profit` variable.

6. I return the `max_profit` variable.

***Complexity Analysis:***

* Time complexity : O(n)

  We loop through the `prices` list once. So, the time complexity is O(n).


* Space complexity : O(1)
    
      We are not using any extra space. So, the space complexity is O(1).


> `One pass` is a very popular approach in `competitive programming`. So, you should remember this approach.

It is also called `Kadane's Algorithm`. So, you should remember this name too.

### What is Kadane's Algorithm?

`Kadane's Algorithm` is a very popular `algorithm` in `competitive programming`. It is used to find the `maximum subarray sum` in an `array`.

Let's say we have an `array` `arr` and we want to find the `maximum subarray sum` in the `array`. We can do that by using `Kadane's Algorithm`.

***Solution steps:***

1. Create two variables `max_so_far` and `max_ending_here` and set both of them to `0`.

2. Loop through the `arr` and store the `item` in the `max_ending_here` variable.

3. Check if the `max_ending_here` is greater than the `max_so_far` or not.

4. If the `max_ending_here` is greater than the `max_so_far` then store the `max_ending_here` in the `max_so_far` variable.

5. Return the `max_so_far` variable.

***Solution in python:***

I will just follow the steps I mentioned above.

```python

def maxSubArraySum(arr):
    max_so_far = 0
    max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here += arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far

```

It's almost the same as the `One pass` approach. The only difference is that we are not checking if the `max_ending_here` is greater than `0` or not. Because we are not finding the `maximum subarray sum` in the `array`. We are finding the `maximum profit` in the `array`.

## Problem 3: Majority Element

### Problem Statement

Given an `array` `nums` of size `n`, return the `majority element`.




