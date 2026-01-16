# MiniLambda harder algorithmic tests

## case: remainder via integer division
<<<
let rem = fn a -> fn b -> a - (a / b) * b in rem(17)(5)
>>>
OK 2

## case: gcd via Euclid
<<<
let rem = fn a -> fn b -> a - (a / b) * b in let gcd = fn a -> fn b -> if b == 0 then a else gcd(b)(rem(a)(b)) in gcd(1071)(462)
>>>
OK 21

## case: fast exponentiation
<<<
let rem = fn a -> fn b -> a - (a / b) * b in let isEven = fn n -> rem(n)(2) == 0 in let pow = fn a -> fn n -> if n == 0 then 1 else if isEven(n) then let t = pow(a)(n / 2) in t * t else a * pow(a)(n - 1) in pow(2)(10)
>>>
OK 1024

## case: primality test (prime)
<<<
let rem = fn a -> fn b -> a - (a / b) * b in let isDiv = fn n -> fn d -> rem(n)(d) == 0 in let isPrimeFrom = fn n -> fn d -> if d * d > n then true else if isDiv(n)(d) then false else isPrimeFrom(n)(d + 1) in let isPrime = fn n -> if n <= 1 then false else isPrimeFrom(n)(2) in isPrime(97)
>>>
OK true

## case: primality test (composite)
<<<
let rem = fn a -> fn b -> a - (a / b) * b in let isDiv = fn n -> fn d -> rem(n)(d) == 0 in let isPrimeFrom = fn n -> fn d -> if d * d > n then true else if isDiv(n)(d) then false else isPrimeFrom(n)(d + 1) in let isPrime = fn n -> if n <= 1 then false else isPrimeFrom(n)(2) in isPrime(91)
>>>
OK false


