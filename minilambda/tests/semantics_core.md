# MiniLambda semantics-focused tests

## case: call-by-value evaluates argument
<<<
(fn x -> 1)(1 / 0)
>>>
ERR DIV_BY_ZERO

## case: if true does not evaluate else branch
<<<
if true then 1 else 1 / 0
>>>
OK 1

## case: if false does not evaluate then branch
<<<
if false then 1 / 0 else 2
>>>
OK 2

## case: division by zero
<<<
1 / 0
>>>
ERR DIV_BY_ZERO

## case: division by zero via expression
<<<
(1 + 2) / (3 - 3)
>>>
ERR DIV_BY_ZERO

## case: closure captures lexical environment (shadowing)
<<<
let x = 1 in let f = fn y -> x + y in let x = 100 in f(2)
>>>
OK 3

## case: shadowing without closures
<<<
let x = 1 in let x = 2 in x + 10
>>>
OK 12

## case: left associative application
<<<
let sub = fn x -> fn y -> x - y in sub(10)(3)
>>>
OK 7

## case: application precedence over arithmetic
<<<
let inc = fn x -> x + 1 in inc(2) * 3
>>>
OK 9

## case: recursive let (factorial)
<<<
let fact = fn n -> if n == 0 then 1 else n * fact(n - 1) in fact(5)
>>>
OK 120

## case: recursive let (fibonacci)
<<<
let fib = fn n -> if n <= 1 then n else fib(n - 1) + fib(n - 2) in fib(8)
>>>
OK 21

## case: unbound variable inside function body
<<<
let f = fn x -> g(x) in f(1)
>>>
ERR UNBOUND_VAR


