# MiniLambda additional parse error tests

## case: two atoms without application
<<<
1 2
>>>
ERR PARSE_ERROR

## case: identifier cannot start with digit
<<<
1x
>>>
ERR PARSE_ERROR

## case: extra close paren
<<<
true)
>>>
ERR PARSE_ERROR

## case: unbalanced parens
<<<
( ( 1 )
>>>
ERR PARSE_ERROR

## case: if else branch missing expression
<<<
if true then 1 else
>>>
ERR PARSE_ERROR

## case: fn body missing
<<<
fn x ->
>>>
ERR PARSE_ERROR

## case: let missing rhs
<<<
let x = in 1
>>>
ERR PARSE_ERROR

## case: let has extra in
<<<
let x = 1 in in 2
>>>
ERR PARSE_ERROR

## case: dangling ==
<<<
1 ==
>>>
ERR PARSE_ERROR

## case: comma not in grammar
<<<
f(1, 2)
>>>
ERR PARSE_ERROR


