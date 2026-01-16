# MiniLambda type error tests

## case: if condition must be boolean (int is not allowed)
<<<
if 0 then 1 else 2
>>>
ERR TYPE_ERROR

## case: arithmetic operands must be integers (bool + int)
<<<
true + 1
>>>
ERR TYPE_ERROR

## case: ordering comparison operands must be integers (bool < int)
<<<
true < 1
>>>
ERR TYPE_ERROR

## case: equality requires same type (bool == int)
<<<
true == 1
>>>
ERR TYPE_ERROR

## case: calling non-function is TYPE_ERROR
<<<
1(2)
>>>
ERR TYPE_ERROR


