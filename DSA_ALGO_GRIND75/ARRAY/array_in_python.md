<h1 align="center"> Everything About ARRAY in python </h1>

I was trying to make a video on `competitive programming` where I was trying to explain `Data Structures` with python and solve some problems in `LeetCode` specifically the `blind 75` problems. But I started with `Linked List` and I realized that I need to explain `Array` first. You can follow me on linkedin to get updates regularly and give a visit to my youtube channel too.

Linkedin: https://www.linkedin.com/in/md-rishat-talukder-a22157239/
Github: https://github.com/RishatTalukder/leetcoding
Youtube: https://www.youtube.com/@itvaya

So, here's everything about `Array` in python.

Pre-requisites:

- Basic knowledge of python

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

- `grocery_list` 0. `Onion`
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

## <a name='Accessingitemsfromalistusingnegativeindex'></a>Accessing items from a list using negative index

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

## <a name='changingitemsinalist'></a>changing items in a list

We can also `change` the `items` in a `list`. Let's say we want to change the `item` in the `index` `0` to `Kawasaki`. We can do that by doing this:

```python
bikes[0] = "Kawasaki"

print(bikes)
```

    ['Kawasaki', 'Yamaha', 'Suzuki', 'Kawasaki']

as you can see I permanently changed the `item` in the `index` `0` to `Kawasaki`.

So, we just have to give the `name` of the `list` followed by `[]`, inside the `[]` we have to give the `index` of the `item` we want to `change` and then we can assign a new `item` to that `index`.

The `bikes` list now has two kawsaki. One in the `index` `0` and another in the `index` `-1`(negetive for the last index).

## <a name='Addingitemstoalist'></a>Adding items to a list

SO, we can access and change the `items` in a `list`. But what if we want to `add` an `item` to a `list`? Well, we can do that too.

There are couple of ways to `add` an `item` to a `list`. Let's see them one by one.

### <a name='Addinganitemtotheendofalist'></a>Adding an item to the end of a list

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

### <a name='Addinganitemtoaspecificindexofalist'></a>Adding an item to a specific index of a list

We can also `add` an `item` to a `specific index` of a `list`. Let's say we want to `add` `100` to the `index` `2` of the `numbers` list. We can do that by using the `insert()` method.

```python
list_of_nums.insert(0, "Rishat")

print(list_of_nums)
```

    ['Rishat', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Rishat']

The `insert()` methos takes two arguments. The first argument is the `index` where we want to `add` the `item` and the second argument is the `item` we want to `add` to the `list`.

So, if we want to add an item to the `46th` index of the `list` we can just do `list_name.insert(46, item)` and the `item` will be added to the `46th` index of the `list`.

### <a name='Addingmultipleitemstoalist'></a>Adding multiple items to a list

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

### <a name='Addingitemstoalistusinglistcomprehension'></a>Adding items to a list using list comprehension

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
    .....
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

## <a name='Removingitemsfromalist'></a>Removing items from a list

As, we can add an `Item` to a `list` we can also `remove` an `item` from a `list`. Let's see how we can `remove` an `item` from a `list`.

there are couple of ways to `remove` an `item` from a `list`. Let's see them one by one.

### <a name='Removinganitemfromalistusingtheremovemethod'></a>Removing an item from a list using the remove() method

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

### <a name='Removinganitemfromalistusingthepopmethod'></a>Removing an item from a list using the pop() method

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

### <a name='Removinganitemfromalistusingthedelkeyword'></a>Removing an item from a list using the del keyword

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

### <a name='Removingalltheitemsfromalistusingtheclearmethod'></a>Removing all the items from a list using the clear() method

We can also `remove` all the `items` from a `list` by using the `clear()` method. Let's say we want to `remove` all the `items` from the `bikes` list. We can do that by using the `clear()` method.

`clear()` method removes all the `items` from the `list`.

#removing items from the list using clear

bikes.clear()

print(bikes)

````

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
````

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

**_`Even though we changed the bikes_copy list, the bikes list also changed because they are the same list.`_**

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

## Now the main `list` and the `copied list` are two different `list` and changing the `copied list` will not affect the main `list`.

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

## So, I get both the `index` and the `item` of the `iterable` object at the same time.

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

## > **Note:** `sort()` method uses `Timsort` algorithm to sort the `list`. `Timsort` is a combination of `Merge sort` and `Insertion sort` algorithm. `Timsort` is the fastest sorting algorithm in python.

Heres a list of all the `list` methods in python:

| Method    | Description                                                                  |
| --------- | ---------------------------------------------------------------------------- |
| append()  | Adds an element at the end of the list                                       |
| clear()   | Removes all the elements from the list                                       |
| copy()    | Returns a copy of the list                                                   |
| count()   | Returns the number of elements with the specified value                      |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list |
| index()   | Returns the index of the first element with the specified value              |
| insert()  | Adds an element at the specified position                                    |
| pop()     | Removes the element at the specified position                                |
| remove()  | Removes the item with the specified value                                    |
| reverse() | Reverses the order of the list                                               |
| sort()    | Sorts the list                                                               |

## | sort() | Sorts the list |

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

# That's it for `list`. Now let's talk about `tuple`.

A `tuple` is a `collection` of `items` which is `immutable` and `ordered`. It is `immutable` which means we cannot `add`, `remove` or `change` the `items` in the `tuple`. It is `ordered` which means the `items` in the `tuple` has a `position` and we can `access` the `items` by giving the `position` of the `item` we want to `access`.

Basically, a `tuple` is a `list` where we cannot `add`, `remove` or `change` the `items`.

Let's see an example:

```python
berries = ("Strawberry", "Blueberry", "Raspberry", "Blackberry")
```

Here, we have a `tuple` of `berries`. How do we know it's a `tuple`? Well, it's because it has `()` instead of `[]`. So, a list has `[]` and a `tuple` has `()`.

## Here, we have a `tuple` of `berries`. How do we know it's a `tuple`? Well, it's because it has `()` instead of `[]`. So, a list has `[]` and a `tuple` has `()`.

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

## Accessing is the same as a `list`. So, I am not going to talk about it anymore.

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

## Now i leave the rest to you to figure out how to `add` and `remove` `items` from a `tuple`.

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

### The veriables corresponding to the `items` in the `tuple` will store the `items` from the `tuple`. SO, the first variable will store the first item, the second variable will store the second item and so on.

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

## Try to `unpack` a `tuple` and store the `items` in a variable using `*` in the middle variable and see what happens.

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

## ; 6thods

Heres a list of all the `tuple` methods in python:

| Method  | Description                                                                             |
| ------- | --------------------------------------------------------------------------------------- |
| count() | Returns the number of times a specified value occurs in a tuple                         |
| index() | Searches the tuple for a specified value and returns the position of where it was found |

That's it for `tuple`. Now let's talk about `set`.

# That's it for `tuple`. Now let's talk about `set`.

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

## So, in our set the `True` value is replaced by `1` because they have the same `value`.

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

## {'banana', 'apple', 'Suzuki', 'Yamaha', 'cherry', 'Honda'}

There are couple of ways to `remove` an `item` from a `set`. Let's see them one by one.

### There are couple of ways to `remove` an `item` from a `set`. Let's see them one by one.

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

### > But if we give an `item` which is not in the `set` to the `remove()` method then we will get an error.

We can also `remove` an `item` from a `set` by using the `discard()` method. Let's say we want to `remove` `Apple` from the `fruits` set. We can do that by using the `discard()` method.

```python
a_set_of_fruts.discard("apple")
print(a_set_of_fruts)
```

    {'banana', 'cherry'}

As you can see `discard()` method works the same as the `remove()` method. But if we give an `item` which is not in the `set` to the `discard()` method then we will not get an `error` like the `remove()` method.

### As you can see `discard()` method works the same as the `remove()` method. But if we give an `item` which is not in the `set` to the `discard()` method then we will not get an `error` like the `remove()` method.

If you want to remove `random` `item` from a `set` then we can use the `pop()` method. Let's say we want to `remove` a `random` `item` from the `fruits` set. We can do that by using the `pop()` method.

```python
a_set_of_fruts = {"apple", "banana", "cherry", "strawberry", "raspberry"}

a_set_of_fruts.pop()
```

    'banana'

The `pop()` method removed the `first item` instead of the last item like it does in a `list`. Because a `set` is `unordered` so, there is no `first item` or `last item` in a `set`. So, the `pop()` method removes a `random item` from the `set`.

## The `pop()` method removed the `first item` instead of the last item like it does in a `list`. Because a `set` is `unordered` so, there is no `first item` or `last item` in a `set`. So, the `pop()` method removes a `random item` from the `set`.

We can also `loop` through a `set`. Let's say we want to `loop` through the `fruits` set. We can do that by using a `for loop`. It's just as the same as `looping` through a `list`.

## We can also `loop` through a `set`. Let's say we want to `loop` through the `fruits` set. We can do that by using a `for loop`. It's just as the same as `looping` through a `list`.

This is the interesting part.

If you about `set` in `math` then this will be very easy for you to understand. If you don't know about `set` in `math` then no worries.

### If you about `set` in `math` then this will be very easy for you to understand. If you don't know about `set` in `math` then no worries.

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

### `union()` method also takes multiple arguments. Let's say we have three `sets` `set1`, `set2` and `set3`. We want to `join` the three `sets` and store it in a new `set` called `set4`. We can do that by using the `union()` method.

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

### So, this prints `{1}` because `1` is the only `common item` in the two `sets`.

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

## So, `difference()` only return the `items` of `set1` whicha are not in `set2`.

Heres a list of all the `set` methods in python:

| Method                        | Description                                                                    |
| ----------------------------- | ------------------------------------------------------------------------------ |
| add()                         | Adds an element to the set                                                     |
| clear()                       | Removes all the elements from the set                                          |
| copy()                        | Returns a copy of the set                                                      |
| difference()                  | Returns a set containing the difference between two or more sets               |
| difference_update()           | Removes the items in this set that are also included in another, specified set |
| discard()                     | Remove the specified item                                                      |
| intersection()                | Returns a set, that is the intersection of two other sets                      |
| intersection_update()         | Removes the items in this set that are not present in other, specified set(s)  |
| isdisjoint()                  | Returns whether two sets have a intersection or not                            |
| issubset()                    | Returns whether another set contains this set or not                           |
| issuperset()                  | Returns whether this set contains another set or not                           |
| pop()                         | Removes an element from the set                                                |
| remove()                      | Removes the specified element                                                  |
| symmetric_difference()        | Returns a set with the symmetric differences of two sets                       |
| symmetric_difference_update() | inserts the symmetric differences from this set and another                    |
| union()                       | Return a set containing the union of sets                                      |
| update()                      | Update the set with the union of this set and others                           |

That's it for `set`.

We will not talk about `dictionary` because as it is also a `collection` of `items` it is a representation of `key-value` pairs which is a little bit different from `array` and more like `hashmap`. SO, we will talk about `dictionary` in the hashmap section..

Now time for some problem solving.

# Now time for some problem solving.

`Blind 75 Leetcode` is very popular among the `competitive programmers`. It is a list of 75 problems which are very important for `competitive programming`. So, I will solve all the problems from the `Blind 75 Leetcode` list in this section.

It will also help with `coding interviews` because the problems are very important for `coding interviews` too.

There are different lists of `Blind 75`. There is one in the `Leetcode` website named `leetcode 75`. There is one in the `GeeksforGeeks` website and there other lists too. But I liked the list in `techinterviewhandbook` website. it is called the `grind 75`. So, I will solve the `grind 75` list in this section.

You can find the `grind 75` list (https://www.techinterviewhandbook.org/grind75?grouping=topics).

> if you click on a problem in the list it will take you to the `leetcode` problem page. So, you can solve the problem in `leetcode` and see if your solution is correct or not.

I will solve the problems in `python` in python and in this document I will go through `array` section of the `grind 75` list.

There are `11` `array` problems in the `grind 75` list. So, I will solve all the `11` problems in this section. And discuss the solutions and the algorithms we can use to solve the problems.

so, let's do this.

## so, let's do this.blem in `leetcode`?

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

## That's it for `leetcode`. Now let's start solving the problems.

### Problem 1: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

\*\*\* Example 1:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```

\*\*\* Example 2:

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

\*\*\* Example 3:

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

You can find the problem in leetcode (https://leetcode.com/problems/two-sum/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.
> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### > If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

The first approach that comes to mind is the `brute force` approach.

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will loop through the `nums` list again and check if the `sum` of the `item` and the `item` in the second loop is equal to the `target` or not. If it is equal to the `target` then we will return the `index` of the `item` in the first loop and the `index` of the `item` in the second loop.

**_Solution steps:_**

1. Loop through the `nums` list and store the `item` in a variable.

2. Loop through the `nums` list again and store the `item` in a variable.

3. Check if the `sum` of the `item` in the first loop and the `item` in the second loop is equal to the `target` or not.

4. If it is equal to the `target` then return the `index` of the `item` in the first loop and the `index` of the `item` in the second loop.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

```

**_Explanation:_**

1. I loop through the `nums` list and store the `item` in the `i` variable.

2. I loop through the `nums` list again and store the `item` in the `j` variable.

3. I check if the `sum` of the `item` in the `i` variable and the `item` in the `j` variable is equal to the `target` or not.

4. If it is equal to the `target` then I return the `index` of the `item` in the `i` variable and the `index` of the `item` in the `j` variable.

**_Complexity Analysis:_**

- Time complexity : O(n^2)

  For each `item` in the `nums` list we loop through the `nums` list again. So, the time complexity is O(n^2).

- Space complexity : O(1)
  We are not using any extra space. So, the space complexity is O(1).

### We are not using any extra space. So, the space complexity is O(1).

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will check if the `complement` of the `item` is in the `nums` list or not. If the `complement` of the `item` is in the `nums` list then we will return the `index` of the `item` and the `index` of the `complement`.

**_Solution steps:_**

1. Loop through the `nums` list and store the `item` in a variable.

2. Check if the `complement` of the `item` is in the `nums` list or not.

3. If the `complement` of the `item` is in the `nums` list then return the `index` of the `item` and the `index` of the `complement`.

**_Solution in python:_**

```python
class Solution:
    def twoSum(self, nums, target):
        for ind, num in enumerate(nums):
            complement = target - num

            if complement in nums[ind+1:]:
                nums[ind] = None
                return [ind, nums.index(complement)]

```

**_Explanation:_**

1. I loop through the `nums` list and store the `item` in the `num` variable and the `index` of the `item` in the `ind` variable.

2. I find the `complement` of the `item` and store it in the `complement` variable.

3. I check if the `complement` of the `item` is in the `nums` list or not.

4. If the `complement` of the `item` is in the `nums` list then I return the `index` of the `item` and the `index` of the `complement`.

**_Complexity Analysis:_**

- Time complexity : O(n^2)

  For each `item` in the `nums` list we loop through the `nums` list again. So, the time complexity is O(n^2).

- Space complexity : O(1)
  We are not using any extra space. So, the space complexity is O(1).

### We are not using any extra space. So, the space complexity is O(1).

In this approach we will use a `dictionary` to solve the problem.

**_Solution steps:_**

1. Create a `dictionary`.

2. Loop through the `nums` list and store the `target - item` in the `dictionary` as the `key` and the `index` of the `item` as the `value`.

3. Loop through the `nums` list and check if the `item` is in the `dictionary` or not.

4. If the `item` is in the `dictionary` then return the `index` of the `item` and the `value` of the `item` in the `dictionary`.

**_Solution in python:_**

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

**_Explanation:_**

1. I create a `dictionary` named `dic`.

2. I loop through the `nums` list and store the `target - item` in the `dic` as the `key` and the `index` of the `item` as the `value`.

3. I loop through the `nums` list and check if the `item` is in the `dic` or not.

4. If the `item` is in the `dic` then I return the `index` of the `item` and the `value` of the `item` in the `dic`.

**_Complexity Analysis:_**

- Time complexity : O(n)

  We loop through the `nums` list twice. So, the time complexity is O(n).

- Space complexity : O(n)
  We are using a `dictionary` to store the `items` of the `nums` list. So, the space complexity is O(n).

## We are using a `dictionary` to store the `items` of the `nums` list. So, the space complexity is O(n).

### Problem 2: Best Time to Buy and Sell Stock

You are given an `array` `prices` where `prices[i]` is the `price` of a given `stock` on the `ith` day.

You want to `maximize` your `profit` by choosing a `single day` to `buy` one `stock` and choosing a `different day` in the `future` to `sell` that `stock`.

Return the `maximum profit` you can achieve from this transaction. If you cannot achieve any profit, return `0`.

\*\*\* Example 1:

```

Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation:

Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

\*\*\* Example 2:

```

Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.

```

You can find the problem in leetcode (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.
> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### > If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

The first approach that comes to mind is the `brute force` approach.

In this approach we will loop through the `prices` list and for each `item` in the `prices` list we will loop through the `prices` list again and check if the `difference` between the `item` and the `item` in the second loop is greater than the `max_profit` or not. If it is greater than the `max_profit` then we will store the `difference` in the `max_profit` variable.

**_Solution steps:_**

1. Loop through the `prices` list and store the `item` in a variable.

2. Loop through the `prices` list again and store the `item` in a variable.

3. Check if the `difference` between the `item` in the first loop and the `item` in the second loop is greater than the `max_profit` or not.

4. If it is greater than the `max_profit` then store the `difference` in the `max_profit` variable.

5. Return the `max_profit` variable.

**_Solution in python:_**

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

### So, we have to find a better approach.

In this approach we will loop through the `prices` list and for each `item` in the `prices` list we will check if the `item` is less than the `min_price` or not. If the `item` is less than the `min_price` then we will store the `item` in the `min_price` variable. Then we will check if the `difference` between the `item` and the `min_price` is greater than the `max_profit` or not. If it is greater than the `max_profit` then we will store the `difference` in the `max_profit` variable.

**_Solution steps:_**

1. Loop through the `prices` list and store the `item` in a variable.

2. Check if the `item` is less than the `min_price` or not.

3. If the `item` is less than the `min_price` then store the `item` in the `min_price` variable.

4. Check if the `difference` between the `item` and the `min_price` is greater than the `max_profit` or not.

5. If it is greater than the `max_profit` then store the `difference` in the `max_profit` variable.

6. Return the `max_profit` variable.

**_Solution in python:_**

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

**_Explanation:_**

1. I loop through the `prices` list and store the `item` in the `i` variable.

2. I check if the `item` is less than the `min_price` or not.

3. If the `item` is less than the `min_price` then I store the `item` in the `min_price` variable.

4. I check if the `difference` between the `item` and the `min_price` is greater than the `max_profit` or not.

5. If it is greater than the `max_profit` then I store the `difference` in the `max_profit` variable.

6. I return the `max_profit` variable.

**_Complexity Analysis:_**

- Time complexity : O(n)

  We loop through the `prices` list once. So, the time complexity is O(n).

- Space complexity : O(1)
  We are not using any extra space. So, the space complexity is O(1).

> `One pass` is a very popular approach in `competitive programming`. So, you should remember this approach.

It is also called `Kadane's Algorithm`. So, you should remember this name too.

### It is also called `Kadane's Algorithm`. So, you should remember this name too.

`Kadane's Algorithm` is a very popular `algorithm` in `competitive programming`. It is used to find the `maximum subarray sum` in an `array`.

Let's say we have an `array` `arr` and we want to find the `maximum subarray sum` in the `array`. We can do that by using `Kadane's Algorithm`.

**_Solution steps:_**

1. Create two variables `max_so_far` and `max_ending_here` and set both of them to `0`.

2. Loop through the `arr` and store the `item` in the `max_ending_here` variable.

3. Check if the `max_ending_here` is greater than the `max_so_far` or not.

4. If the `max_ending_here` is greater than the `max_so_far` then store the `max_ending_here` in the `max_so_far` variable.

5. Return the `max_so_far` variable.

**_Solution in python:_**

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

## It's almost the same as the `One pass` approach. The only difference is that we are not checking if the `max_ending_here` is greater than `0` or not. Because we are not finding the `maximum subarray sum` in the `array`. We are finding the `maximum profit` in the `array`.

### Problem 3: Majority Element

Given an `array` `nums` of size `n`, return the `majority element`. The `majority element` is the `element` that appears more than `⌊n / 2⌋` times. You may assume that the `majority element` always exists in the `array`.

\*\*\* Example 1:

```

Input: nums = [3,2,3]

Output: 3

```

\*\*\* Example 2:

```

Input: nums = [2,2,1,1,1,2,2]

Output: 2

```

You can find the problem in leetcode (https://leetcode.com/problems/majority-element/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.

> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### > If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

The first approach that comes to mind is the `brute force` approach.

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will loop through the `nums` list again and check if the `item` is equal to the `item` in the second loop or not. If it is equal to the `item` in the second loop then we will increase the `count` variable by `1`. If the `count` variable is greater than `n/2` then we will return the `item`.

**_Solution steps:_**

1. Loop through the `nums` list and store the `item` in a variable.

2. Loop through the `nums` list again and store the `item` in a variable.

3. Check if the `item` is equal to the `item` in the second loop or not.

4. If it is equal to the `item` in the second loop then increase the `count` variable by `1`.

5. If the `count` variable is greater than `n/2` then return the `item`.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def majorityElement(self, nums):
        n = len(nums)

        for i in range(n):
            count = 0

            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1

            if count > n/2:
                return nums[i]

```

> This is not accepted in `leetcode` because it exceeds the time limit.

So, we have to find a better approach.

### So, we have to find a better approach.

In this approach we will use a `dictionary` to solve the problem.

**_Solution steps:_**

1. Create a `dictionary`.

2. Loop through the `nums` list and store the `item` in the `dictionary` as the `key` and the `count` of the `item` as the `value`.

3. Loop through the `dictionary` and check if the `value` of the `item` is greater than `n/2` or not.

4. If the `value` of the `item` is greater than `n/2` then return the `key` of the `item`.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for key in dic:
            if dic[key] > n/2:
                return key

```

**_Explanation:_**

1. I loop through the `nums` list and store the `item` in the `num` variable.

2. I check if the `item` is in the `dic` or not.

3. If the `item` is in the `dic` then I increase the `value` of the `item` by `1`.

4. If the `item` is not in the `dic` then I store the `item` in the `dic` as the `key` and the `value` of the `item` as `1`.

5. I loop through the `dic` and check if the `value` of the `item` is greater than `n/2` or not.

6. If the `value` of the `item` is greater than `n/2` then I return the `key` of the `item`.

**_Complexity Analysis:_**

- Time complexity : O(n)

  We loop through the `nums` list once and the `dic` once. So, the time complexity is O(n).

- Space complexity : O(n)
  We are using a `dictionary` to store the `items` of the `nums` list. So, the space complexity is O(n).

### We are using a `dictionary` to store the `items` of the `nums` list. So, the space complexity is O(n).

In this approach we will sort the `nums` list and return the `n/2`th `item`.

**_Solution steps:_**

1. Sort the `nums` list.

2. Return the `n/2`th `item`.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

```

**_Explanation:_**

1. I sort the `nums` list.

2. I return the `n/2`th `item`.

**_Complexity Analysis:_**

- Time complexity : O(nlogn)

  We sort the `nums` list. So, the time complexity is O(nlogn) because the time complexity of sorting is O(nlogn).

- Space complexity : O(1)
  We are not using any extra space. So, the space complexity is O(1).

## We are not using any extra space. So, the space complexity is O(1).

### Problem 4: Contains Duplicate

Given an `integer` `array` `nums`, return `true` if any value appears at least twice in the `array`, and return `false` if every element is distinct.

\*\*\* Example 1:

```

Input: nums = [1,2,3,1]

Output: true

```

\*\*\* Example 2:

```

Input: nums = [1,2,3,4]

Output: false

```

You can find the problem in leetcode (https://leetcode.com/problems/contains-duplicate/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.

> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### > If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

The first approach that comes to mind is the `brute force` approach.

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will loop through the `nums` list again and check if the `item` is equal to the `item` in the second loop or not. If it is equal to the `item` in the second loop then we will return `true`.

**_Solution steps:_**

1. Loop through the `nums` list and store the `item` in a variable.

2. Loop through the `nums` list again and store the `item` in a variable.

3. Check if the `item` is equal to the `item` in the second loop or not.

4. If it is equal to the `item` in the second loop then return `true`.

5. If the loop ends then return `false`.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

```

You can submit this in `leetcode` and it will be accepted. But this is not the best approach.

### You can submit this in `leetcode` and it will be accepted. But this is not the best approach.

In this approach we will use a `dictionary` to solve the problem.

**_Solution steps:_**

1. Create a `dictionary`.

2. Loop through the `nums` list and store the `item` in the `dictionary` as the `key` and the `count` of the `item` as the `value`.

3. Loop through the `dictionary` and check if the `value` of the `item` is greater than `1` or not.

4. If the `value` of the `item` is greater than `1` then return `true`.

5. If the loop ends then return `false`.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def containsDuplicate(self, nums):
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        for key in dic:
            if dic[key] > 1:
                return True

        return False

```

**_Explanation:_**

1. I loop through the `nums` list and store the `item` in the `num` variable.

2. I check if the `item` is in the `dic` or not.

3. If the `item` is in the `dic` then I increase the `value` of the `item` by `1`.

4. If the `item` is not in the `dic` then I store the `item` in the `dic` as the `key` and the `value` of the `item` as `1`.

5. I loop through the `dic` and check if the `value` of the `item` is greater than `1` or not.

6. If the `value` of the `item` is greater than `1` then I return `true`.

7. If the loop ends then I return `false`.

**_Complexity Analysis:_**

- Time complexity : O(n)

  We loop through the `nums` list once and the `dic` once. So, the time complexity is O(n).

- Space complexity : O(n)
  We are using a `dictionary` to store the `items` of the `nums` list. So, the space complexity is O(n).

### We are using a `dictionary` to store the `items` of the `nums` list. So, the space complexity is O(n).

In this approach we will sort the `nums` list and check if the `item` is equal to the `item` in the next index or not. If it is equal to the `item` in the next index then we will return `true`.

**_Solution steps:_**

1. Sort the `nums` list.

2. Loop through the `nums` list and check if the `item` is equal to the `item` in the next index or not.

3. If the `item` is equal to the `item` in the next index then return `true`.

4. If the loop ends then return `false`.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def containsDuplicate(self, nums):
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False

```

**_Explanation:_**

1. I sort the `nums` list.

2. I loop through the `nums` list and check if the `item` is equal to the `item` in the next index or not.

3. If the `item` is equal to the `item` in the next index then I return `true`.

4. If the loop ends then I return `false`.

**_Complexity Analysis:_**

- Time complexity : O(nlogn)

  We sort the `nums` list. So, the time complexity is O(nlogn) because the time complexity of sorting is O(nlogn).

- Space complexity : O(1)
  We are not using any extra space. So, the space complexity is O(1).

## We are not using any extra space. So, the space complexity is O(1).

### Problem 5: Insert Interval

Given a set of `non-overlapping` `intervals`, insert a new `interval` into the `intervals` (merge if necessary).

You may assume that the `intervals` were initially sorted according to their `start` times.

\*\*\* Example 1:

```

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]

Output: [[1,5],[6,9]]

```

\*\*\* Example 2:

```

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]

Output: [[1,2],[3,10],[12,16]]

Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

```

You can find the problem in leetcode (https://leetcode.com/problems/insert-interval/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.

> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### > If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

This is the first problem I couldn't solve using the `brute force` approach. So, I will not discuss the `brute force` approach here.

### This is the first problem I couldn't solve using the `brute force` approach. So, I will not discuss the `brute force` approach here.

`Marge Intervals` is a very popular `algorithm` in `competitive programming`. It is used to `marge` the `overlapping intervals` in an `array`. It's an important `algorithm` for `competitive programming`. SO, be aware of this `algorithm`.

Let's say we have an `array` `arr` and we want to `marge` the `overlapping intervals` in the `array`. We can do that by using `Marge Intervals`.

**_Solution steps:_**

1. Sort the `arr` according to the `start` times.

2. Create a `result` list and store the `first interval` in the `result` list.

3. Loop through the `arr` and check if the `start` time of the `current interval` is less than or equal to the `end` time of the `last interval` in the `result` list or not.

4. If the `start` time of the `current interval` is less than or equal to the `end` time of the `last interval` in the `result` list then `marge` the `current interval` with the `last interval` in the `result` list.

5. If the `start` time of the `current interval` is greater than the `end` time of the `last interval` in the `result` list then store the `current interval` in the `result` list.

6. Return the `result` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def insert(self, intervals, newInterval):
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][0] <= interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result

```

this is the `Marge Intervals` `algorithm`. To, solve the problem we have to modify the `Marge Intervals` `algorithm` a little bit.

**_Solution steps:_**

- just append the `newInterval` to the `intervals` list at the very beginning.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def insert(self, intervals, newInterval):
        # just append the newInterval to the intervals list at the very beginning
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][0] <= interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result
```

**_Explanation:_**

1. I sort the `intervals` list according to the `start` times.

2. I create a `result` list and store the `first interval` in the `result` list.

3. I loop through the `intervals` list and check if the `start` time of the `current interval` is less than or equal to the `end` time of the `last interval` in the `result` list or not.

4. If the `start` time of the `current interval` is less than or equal to the `end` time of the `last interval` in the `result` list then I `marge` the `current interval` with the `last interval` in the `result` list.

5. If the `start` time of the `current interval` is greater than the `end` time of the `last interval` in the `result` list then I store the `current interval` in the `result` list.

6. I return the `result` list.

**_Complexity Analysis:_**

- Time complexity : O(nlogn)

  We sort the `intervals` list. So, the time complexity is O(nlogn) because the time complexity of sorting is O(nlogn).

- Space complexity : O(n)
  We are using a `result` list to store the `intervals`. So, the space complexity is O(n).

## We are using a `result` list to store the `intervals`. So, the space complexity is O(n).

> This is another problem that has a `algorithm` named `3 sum`.

### > This is another problem that has a `algorithm` named `3 sum`.

Given an `integer` `array` `nums`, return all the `triplets` `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate `triplets`.

\*\*\* Example 1:

```

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

```

\*\*\* Example 2:

```

Input: nums = []

Output: []

```

\*\*\* Example 3:

```

Input: nums = [0]

Output: []

```

You can find the problem in leetcode (https://leetcode.com/problems/3sum/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.

> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### > If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

The first approach that comes to mind is the `brute force` approach.

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will loop through the `nums` list again and for each `item` in the second loop we will loop through the `nums` list again and check if the `sum` of the `item` in the first loop, the `item` in the second loop and the `item` in the third loop is equal to `0` or not. If it is equal to `0` then we will store the `triplet` in the `result` list.

**_Solution steps:_**

1. Loop through the `nums` list and store the `item` in a variable.

2. Loop through the `nums` list again and store the `item` in a variable.

3. Loop through the `nums` list again and check if the `sum` of the `item` in the first loop, the `item` in the second loop and the `item` in the third loop is equal to `0` or not.

4. If it is equal to `0` then store the `triplet` in the `result` list.

5. Return the `result` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def threeSum(self, nums):
        result = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()

                        if triplet not in result:
                            result.append(triplet)

        return result

```

> This is not accepted in `leetcode` because it exceeds the time limit. And this is not a good approach because it has the `time complexity` of `O(n^3)`. WHich is not good.

So, we have to find a better approach.

### So, we have to find a better approach.

`3 sum` is a very popular `algorithm` in `competitive programming`. It is used to find the `triplets` `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

It's the same as the `problem statement`. So, we can use this `algorithm` to solve the problem.

**_Solution steps:_**

1. Sort the `nums` list.

2. Create a `result` list.

3. Loop through the `nums` list and store the `item` in the `i` variable.

4. Create two variables `left` and `right` and set `left` to `i+1` and `right` to `len(nums)-1`.

5. Loop while `left` is less than `right`.

6. Check if the `sum` of the `item` in the `i` variable, the `item` in the `left` variable and the `item` in the `right` variable is equal to `0` or not.

7. If it is equal to `0` then store the `triplet` in the `result` list.

8. If the `sum` is less than `0` then increase the `left` variable by `1`.

9. If the `sum` is greater than `0` then decrease the `right` variable by `1`.

10. Return the `result` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplet.sort()

                    if triplet not in result:
                        result.append(triplet)

                    left += 1
                    right -= 1

                elif sum < 0:
                    left += 1

                else:
                    right -= 1

        return result

```

**_Explanation:_**

This is a tricky algorithm. So, I will explain it in detail.

IT's `2 sum` with a little bit of modification. So, you should know `2 sum` to understand this algorithm.

In the first `loop` we are looping through the `nums` list and storing the `item` in the `i` variable.

Now, we have to find `two other values` from the `nums` list such that the `sum` of the two values would be equal to the `item` in the `i` variable.

In two sum the list was not sorted. So, we had to use a `dictionary` to find the `two other values`. But in this problem the list is sorted. So, we don't need to use a `dictionary`. But if you implement the two sum inside the first loop it's will be almost the same time complexity but slower. when the list is sorted we can use `two pointer` to find the `two other values`. It's faster than using a `dictionary`.

So, we create two variables `left` and `right` and set `left` to `i+1` and `right` to `len(nums)-1`.

Now, we loop while `left` is less than `right`.

In the `loop` we check if the `sum` of the `item` in the `i` variable, the `item` in the `left` variable and the `item` in the `right` variable is equal to `0` or not.

If it is equal to `0` then we store the `triplet` in the `result` list.

If the `sum` is less than `0` then we increase the `left` variable by `1`.

If the `sum` is greater than `0` then we decrease the `right` variable by `1`.

**_Complexity Analysis:_**

- Time complexity : O(n^2)

  We loop through the `nums` list twice. So, the time complexity is O(n^2).

- Space complexity : O(n)
  We are using a `result` list to store the `triplets`. So, the space complexity is O(n).

## We are using a `result` list to store the `triplets`. So, the space complexity is O(n).

### Problem 7: Product of Array Except Self

Given an `integer` `array` `nums`, return an `array` `answer` such that `answer[i]` is equal to the `product` of all the `elements` of `nums` except `nums[i]`.

The `product` of any prefix or suffix of `nums` is `guaranteed` to fit in a `32-bit` `integer`.

You must write an algorithm that runs in `O(n)` time and without using the `division` operation.

\*\*\* Example 1:

```

Input: nums = [1,2,3,4]

Output: [24,12,8,6]

```

\*\*\* Example 2:

```

Input: nums = [-1,1,0,-3,3]

Output: [0,0,9,0,0]

```

You can find the problem in leetcode (https://leetcode.com/problems/product-of-array-except-self/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.

> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

### > If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

The first approach that comes to mind is the `brute force` approach.

In this approach we will loop through the `nums` list and for each `item` in the `nums` list we will loop through the `nums` list again and check if the `item` is equal to the `item` in the second loop or not. If it is not equal to the `item` in the second loop then we will multiply the `item` in the second loop with the `product` variable. After the second loop ends we will store the `product` variable in the `result` list.

**_Solution steps:_**

1. Loop through the `nums` list and store the `item` in a variable.

2. Create a `product` variable and set it to `1`.

3. Loop through the `nums` list again and store the `item` in a variable.

4. Check if the `item` is not equal to the `item` in the second loop or not.

5. If it is not equal to the `item` in the second loop then multiply the `item` in the second loop with the `product` variable.

6. After the second loop ends store the `product` variable in the `result` list.

7. Return the `result` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def productExceptSelf(self, nums):
        result = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result

```

> This is not accepted in `leetcode` because it exceeds the time limit. And this is not a good approach because it has the `time complexity` of `O(n^2)`. WHich is not good.

So, we have to find a better approach. A better approach would be `O(n)`. So, we have to find a `O(n)` approach. and dictionary is not allowed. So, we have to find a `O(n)` approach without using a `dictionary`.

### So, we have to find a better approach. A better approach would be `O(n)`. So, we have to find a `O(n)` approach. and dictionary is not allowed. So, we have to find a `O(n)` approach without using a `dictionary`.

In this approach we will use two `arrays` `prefix` and `postfix` to solve the problem.

**_Solution steps:_**

1. Create a `result` list with the same length as the `nums` list.

2. create a variable `product` and set it to `1`.

3. Loop through the `nums` list.

4. Store the `product` in the `result` list using `postfix` product in `inde+1` index.

5. Create a variable `postfix` and set it to `1`.

6. Loop through the `nums` list in reverse order.

7. Store the `product` in the `result` list using `prefix` product in `index-1` index.

8. Return the `result` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def productExceptSelf(self, nums):
        result = [0] * len(nums)
        product = 1

        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

```

**_Explanation:_**

AS, we have to find the product of all the `elements` of `nums` except `nums[i]` in `O(n)` time and without using the `division` operation. It becomes a little bit tricky.

So, this is another tricky algorithm.

In this algorithm we are using two `arrays` `prefix` and `postfix` to store the `prefix` and `postfix` product of the `nums` list.

In the first `loop` we are looping through the `nums` list and storing the `product` in the `result` list using `postfix` product in `inde+1` index.

In the second `loop` we are looping through the `nums` list in reverse order and storing the `product` in the `result` list using `prefix` product in `index-1` index.

SO, this way the prefix will give the first `i` `elements` product and the postfix will give the last `i` `elements` product.

This will automatically give the product of all the `elements` of `nums` except `nums[i]`.

**_Complexity Analysis:_**

- Time complexity : O(n)

  We loop through the `nums` list twice. So, the time complexity is O(n).

- Space complexity : O(n)
  We are using a `result` list to store the `product`. So, the space complexity is O(n).

## We are using a `result` list to store the `product`. So, the space complexity is O(n).

### Problem 8: Combination Sum

Given an `array` of `distinct` `integers` `candidates` and a `target` `integer` `target`, return a `list` of all `unique` `combinations` of `candidates` where the `chosen` `numbers` sum to `target`. You may return the `combinations` in `any order`.

The `same` `number` may be chosen from `candidates` an `unlimited` `number` of `times`. Two `combinations` are unique if the `frequency` of at least one of the `chosen` `numbers` is different.

It is `guaranteed` that the `number` of `unique` `combinations` that sum up to `target` is less than `150` `combinations` for the given input.

\*\*\* Example 1:

```

Input: candidates = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation:

2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.

7 is a candidate, and 7 = 7.

These are the only two combinations.

```

\*\*\* Example 2:

```

Input: candidates = [2,3,5], target = 8

Output: [[2,2,2,2],[2,3,3],[3,5]]

```

This looks familiar. We did something like this in threesome. But it's not the same but more critical.

You can find the problem in leetcode (https://leetcode.com/problems/combination-sum/).

> Remember, Always read the problem statement carefully and understand the problem properly, Try to solve the problem in your head first and then try to solve it in `leetcode`.

> If you can't then see the solution and try to understand the solution. Then try to solve the problem again by yourself. If you can't then see the solution again and try to understand the solution. Do this until you can solve the problem by yourself.

I couldn't some up with a `brute force` solution for this because it's a backtracking problem. So, I will not discuss the `brute force` approach here.

And give you the most efficient solution using `backtracking`. But first you need to know what is `backtracking`.

**WHAT IS BACKTRACKING??**

`Backtracking` is a `algorithm` that is used to solve `constraint satisfaction problems`. It is a `recursive` `algorithm`. It tries to build a solution incrementally, one piece at a time. Whenever the `backtracking` `algorithm` needs to decide between multiple alternatives to the next component of the solution, it `backtracks`, removing all the choices it had made when it placed the previous component, and tries the alternatives one by one. If a particular alternative does not lead to a solution, the `backtracking` `algorithm` undoes the choice that it had made before and tries the next alternative.

### `Backtracking` is a `algorithm` that is used to solve `constraint satisfaction problems`. It is a `recursive` `algorithm`. It tries to build a solution incrementally, one piece at a time. Whenever the `backtracking` `algorithm` needs to decide between multiple alternatives to the next component of the solution, it `backtracks`, removing all the choices it had made when it placed the previous component, and tries the alternatives one by one. If a particular alternative does not lead to a solution, the `backtracking` `algorithm` undoes the choice that it had made before and tries the next alternative.

In this approach we will use `DFS` to solve the problem, which is a `backtracking` `algorithm`.

It is a recursive algorithm. It tries to build a solution incrementally, one piece at a time. Whenever the `backtracking` `algorithm` needs to decide between multiple alternatives to the next component of the solution, it `backtracks`, removing all the choices it had made when it placed the previous component, and tries the alternatives one by one. If a particular alternative does not lead to a solution, the `backtracking` `algorithm` undoes the choice that it had made before and tries the next alternative.

**_Solution steps:_**

1. Create a `result` list.

2. Create a `dfs` function that takes `index`, `current` and `total` as arguments.

3. Check if the `total` is equal to the `target` or not.

4. If the `total` is equal to the `target` then store the `current` in the `result` list.

5. If the `total` is greater than the `target` then return.

6. Loop through the `candidates` list from `index` to the `length` of the `candidates` list.

7. Call the `dfs` function with `i` as the `index`, `current + [candidates[i]]` as the `current` and `total + candidates[i]` as the `total`.

8. Return the `result` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def combinationSum(self, candidates, target):
        # create a result list
        result = []

        # create a dfs function that takes index, current and total as arguments
        def dfs(index, current, total):
            # check if the total is equal to the target or not
            if total == target:
                result.append(current.copy())
                return
            # check if the total is greater than the target or not
            if total > target or index >= len(candidates):
                return

            current.append(candidates[index]) # append the current item to the current list

            dfs(index, current, total+candidates[index]) # call the dfs function with index, current and total+candidates[index] as arguments

            current.pop() # remove the last item from the current list

            dfs(index+1, current, total) # call the dfs function with index+1, current and total as arguments

        dfs(0, [], 0) # call the dfs function with 0, [], 0 as arguments

        return result

```

**_Explanation:_**

DFS is one of the most important `algorithms` for graphs and trees problems.

This problem is a `backtracking` problem which is solved using `DFS`.

> Here I named the function DFS but it's not the `DFS` algorithm. But a modified version of the `DFS` algorithm. So, don't get confused.

This makes a `decision tree` and tries to find the `target` by `backtracking` which is done by `recursion`.

I cannot explain much in detail about how this works. To learn more about `this problem` and `backtracking` you can watch this video (https://www.youtube.com/watch?v=GBKI9VSKdGg).

**_Complexity Analysis:_**

- Time complexity : O(2^target)

  We are using `backtracking` to solve the problem. So, the time complexity is O(2^target). Because we are making a `decision tree` and trying to find the `target` by `backtracking` the `decision tree` can have `2^target` nodes.

- Space complexity : O(target)
  We are using a `result` list to store the `combinations`. So, the space complexity is O(target).

## We are using a `result` list to store the `combinations`. So, the space complexity is O(target).

This is the algorithm we used in the `insert interval` problem. So, I will not discuss the `algorithm` here.

You can find the problem in leetcode (https://leetcode.com/problems/merge-intervals/).

### You can find the problem in leetcode (https://leetcode.com/problems/merge-intervals/).

Given an `array` of `intervals` where `intervals[i] = [starti, endi]`, merge all `overlapping` `intervals`, and return an `array` of the `non-overlapping` `intervals` that cover all the `intervals` in the input.

\*\*\* Example 1:

```

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]

Output: [[1,6],[8,10],[15,18]]

Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

```

\*\*\* Example 2:

```

Input: intervals = [[1,4],[4,5]]

Output: [[1,5]]

Explanation: Intervals [1,4] and [4,5] are considered overlapping.

```

**_Solution steps:_**

1. Sort the `intervals` list according to the `start` times.

2. Create a `result` list and store the `first interval` in the `result` list.

3. Loop through the `intervals` list and check if the `start` time of the `current interval` is less than or equal to the `end` time of the `last interval` in the `result` list or not.

4. If the `start` time of the `current interval` is less than or equal to the `end` time of the `last interval` in the `result` list then `marge` the `current interval` with the `last interval` in the `result` list.

5. If the `start` time of the `current interval` is greater than the `end` time of the `last interval` in the `result` list then store the `current interval` in the `result` list.

6. Return the `result` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1][0] <= interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result

```

**_Explanation:_**

It's the algorithm to `marge` the `overlapping intervals` in an `array`.

**_Complexity Analysis:_**

- Time complexity : O(nlogn)

  We sort the `intervals` list. So, the time complexity is O(nlogn) because the time complexity of sorting is O(nlogn).

- Space complexity : O(n)

  We are using a `result` list to store the `intervals`. So, the space complexity is O(n).

## We are using a `result` list to store the `intervals`. So, the space complexity is O(n).

### Problem 10: Sort colors

Given an `array` `nums` with `n` `objects` colored `red`, `white`, or `blue`, sort them `in-place` so that `objects` of the `same color` are `adjacent`, with the `colors` in the order `red`, `white`, and `blue`.

We will use the integers `0`, `1`, and `2` to represent the `color` `red`, `white`, and `blue`, respectively.

You must solve this problem without using the `library`'s `sort` function.

\*\*\* Example 1:

```

Input: nums = [2,0,2,1,1,0]

Output: [0,0,1,1,2,2]

```

\*\*\* Example 2:

```

Input: nums = [2,0,1]

Output: [0,1,2]

```

> You can use any sorting algorithm to solve the problem.

### > You can use any sorting algorithm to solve the problem.

In this approach we will use `bubble sort` to solve the problem.

**_Solution steps:_**

1. Loop through the `nums` list.

2. Loop through the `nums` list again.

3. Check if the `item` in the first loop is greater than the `item` in the second loop or not.

4. If the `item` in the first loop is greater than the `item` in the second loop then swap the `item` in the first loop with the `item` in the second loop.

5. Return the `nums` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def sortColors(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums

```

**_ Complexity Analysis:_**

- Time complexity : O(n^2)

  We loop through the `nums` list twice. So, the time complexity is O(n^2).

- Space complexity : O(1)

  We are not using any extra space. So, the space complexity is O(1).

### We are not using any extra space. So, the space complexity is O(1).

This is a advanced sorting algorithm. the concept is easy but the implementation is a little bit tricky. It's a little faster than `bubble sort` because the time complexity of `quick sort` is `O(nlogn)` and the time complexity of `bubble sort` is `O(n^2)`.

**_Solution steps:_**

1. Create a `partition` function that takes `nums`, `low` and `high` as arguments.

2. Create a variable `pivot` and set it to the `item` in the `high` index.

3. Create a variable `i` and set it to `low-1`.

4. Loop through the `nums` list from `low` to `high`.

5. Check if the `item` in the `index` is less than or equal to the `pivot` or not.

6. If the `item` in the `index` is less than or equal to the `pivot` then increase the `i` variable by `1` and swap the `item` in the `index` with the `item` in the `i` index.

7. After the loop ends swap the `item` in the `i+1` index with the `item` in the `high` index.

8. Return the `i+1` index.

9. Create a `quick_sort` function that takes `nums`, `low` and `high` as arguments.

10. Check if the `low` is less than the `high` or not.

11. If the `low` is less than the `high` then call the `partition` function with `nums`, `low` and `high` as arguments and store the `partition` index in a variable `pi`.

12. Call the `quick_sort` function with `nums`, `low` and `pi-1` as arguments.

13. Call the `quick_sort` function with `nums`, `pi+1` and `high` as arguments.

14. Return the `nums` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def sortColors(self, nums):
        def partition(nums, low, high):
            pivot = nums[high]
            i = low-1

            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[high] = nums[high], nums[i+1]

            return i+1

        def quick_sort(nums, low, high):
            if low < high:
                pi = partition(nums, low, high)

                quick_sort(nums, low, pi-1)
                quick_sort(nums, pi+1, high)

        quick_sort(nums, 0, len(nums)-1)

        return nums

```

> this also uses recursion. To understand this algorithm you have to know recursion.

To inderstand this better you can check out this video (https://www.youtube.com/watch?v=4xbWSRZHqac).

**_Complexity Analysis:_**

- Time complexity : O(nlogn)

  We loop through the `nums` list twice. So, the time complexity is O(nlogn).

- Space complexity : O(1)

  We are not using any extra space. So, the space complexity is O(1).

## Problem 11: Container With Most Water

### Problem 11: Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

\*\*\* Example 1:

```

Input: height = [1,8,6,2,5,4,8,3,7]

Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

```

\*\*\* Example 2:

```

Input: height = [1,1]

Output: 1

```

> this porblem should look fimiliar. Because we did something like this in `2nd problem` named `Best Time to Buy and Sell Stock`. But if you think that it's the same then you are wrong. It's a little bit misleading. We won't use the maximum subarray algorithm here.

You can find the problem in leetcode (https://leetcode.com/problems/container-with-most-water/).

### You can find the problem in leetcode (https://leetcode.com/problems/container-with-most-water/).

In this problem we will use `sliding window` to solve the problem.

The Idea behind a `sliding window` is to `slide` the `window` through the `array` and find the `maximum` or `minimum` value in the `window`. It's a very popular `algorithm` and used in many problems.

In this problems case we will use `two pointers` to solve the problem. We will use `left` and `right` pointers. We will set `left` to `0` and `right` to `len(height)-1`. Then we will loop while `left` is less than `right`. In the loop we will check if the `height` in the `left` index is less than or equal to the `height` in the `right` index or not. If it is less than or equal to the `height` in the `right` index then we will calculate the `area` and store it in a variable `area`. Then we will increase the `left` variable by `1`. If the `height` in the `left` index is greater than the `height` in the `right` index then we will calculate the `area` and store it in a variable `area`. Then we will decrease the `right` variable by `1`. After the loop ends we will return the `area`.

**_Solution steps:_**

1. Create a variable `left` and set it to `0`.

2. Create a variable `right` and set it to `len(height)-1`.

3. Create a variable `area` and set it to `0`.

4. Loop while `left` is less than `right`.

5. Check if the `height` in the `left` index is less than or equal to the `height` in the `right` index or not.

6. If it is less than or equal to the `height` in the `right` index then calculate the `area` and store it in a variable `area`.

7. Increase the `left` variable by `1`.

8. If the `height` in the `left` index is greater than the `height` in the `right` index then calculate the `area` and store it in a variable `area`.

9. Decrease the `right` variable by `1`.

10. After the loop ends return the `area`.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        area = 0

        while left < right:
            if height[left] <= height[right]:  # Check if height at left index is less than or equal to height at right index
                area = max(area, height[left] * (right-left))  # Calculate area and update maximum area
                left += 1  # Move left pointer to the right
            else:
                area = max(area, height[right] * (right-left))  # Calculate area and update maximum area
                right -= 1  # Move right pointer to the left

        return area  # Return maximum area

```

**_Complexity Analysis:_**

- Time complexity : O(n)

  We loop through the `height` list once. So, the time complexity is O(n).

- Space complexity : O(1)

  We are not using any extra space. So, the space complexity is O(1).



# That's It for now

This is the end of the `leetcode` problems and everything I know about `arrays` and `algorithms`. I hope you learned something from this. If you have any questions or suggestions feel free to ask me in the comment section. I will try to answer all of your questions.


Happy Coding :)
