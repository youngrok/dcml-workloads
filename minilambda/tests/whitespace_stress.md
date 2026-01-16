# MiniLambda whitespace/newline stress tests

## case: leading spaces
<<<
   1
>>>
OK 1

## case: extra spaces around tokens
<<<
(   1    +   2   )   *  3
>>>
OK 9

## case: no spaces around operators/keywords
<<<
let   x=2    in   x+3
>>>
OK 5

## case: multiline if/then/else
<<<
if   true
then   1
else   2
>>>
OK 1

## case: multiline let/fn/if
<<<
let fact =
  fn n ->
    if n == 0 then 1 else n * fact(n - 1)
in
  fact(6)
>>>
OK 720

## case: multiline let with closure
<<<
let x =
  10
in
  let f = fn y -> x + y in
    f(5)
>>>
OK 15


