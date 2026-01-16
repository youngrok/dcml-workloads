# MiniLambda basic syntax & evaluation smoke tests

## case: int literal 0
<<<
0
>>>
OK 0

## case: int literal 42
<<<
42
>>>
OK 42

## case: boolean true
<<<
true
>>>
OK true

## case: boolean false
<<<
false
>>>
OK false

## case: parentheses
<<<
(1)
>>>
OK 1

## case: precedence 1 + 2 * 3
<<<
1 + 2 * 3
>>>
OK 7

## case: grouping (1 + 2) * 3
<<<
(1 + 2) * 3
>>>
OK 9

## case: left assoc division 8 / 4 / 2
<<<
8 / 4 / 2
>>>
OK 1

## case: comparison with precedence
<<<
1 + 2 * 3 == 7
>>>
OK true

## case: comparison 1 < 2
<<<
1 < 2
>>>
OK true

## case: comparison 2 <= 1
<<<
2 <= 1
>>>
OK false

## case: let binding
<<<
let x = 2 in x + 3
>>>
OK 5

## case: nested let
<<<
let x = 2 in let y = x * 10 in y + x
>>>
OK 22

## case: if true
<<<
if true then 1 else 2
>>>
OK 1

## case: if with comparison
<<<
if 1 < 2 then 10 else 20
>>>
OK 10

## case: application
<<<
(fn x -> x + 1)(2)
>>>
OK 3

## case: closures
<<<
let add = fn x -> fn y -> x + y in add(2)(3)
>>>
OK 5

## case: unbound variable
<<<
x
>>>
ERR UNBOUND_VAR


