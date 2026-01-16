## case: empty
<<<

>>>

## case: single
<<<
7
>>>
7

## case: whitespace
<<<
3 1
2	5
4
>>>
1
2
3
4
5

## case: duplicates_negatives
<<<
0 -1 5 -1 2 0
>>>
-1
-1
0
0
2
5

## case: invalid_token
<<<
1 2 x 3
>>>
ERR INVALID_INPUT
