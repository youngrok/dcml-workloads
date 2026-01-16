# MiniLambda parse error tests

## case: empty input
<<<
>>>
ERR PARSE_ERROR

## case: lone open paren
<<<
(
>>>
ERR PARSE_ERROR

## case: dangling plus
<<<
1 +
>>>
ERR PARSE_ERROR

## case: if missing else
<<<
if true then 1
>>>
ERR PARSE_ERROR

## case: malformed if keywords
<<<
if true else 1 then 2
>>>
ERR PARSE_ERROR

## case: fn missing parameter
<<<
fn -> 1
>>>
ERR PARSE_ERROR

## case: let missing in
<<<
let x = 1 x
>>>
ERR PARSE_ERROR

## case: let missing body
<<<
let x = 1 in
>>>
ERR PARSE_ERROR

## case: empty argument list not allowed
<<<
f()
>>>
ERR PARSE_ERROR


