# MiniLambda Language Specification

MiniLambda is a small, expression-oriented functional language designed as an **experimental workload**.  
Its purpose is to require a complete implementation pipeline — from parsing to evaluation — while remaining compact and precisely defined.

The language is designed with the following goals:

- A small and unambiguous syntax and semantics
- Non-trivial but bounded implementation complexity
- No reliance on specialized or high-level parsing/runtime libraries
- Suitability for automated testing and comparative experiments

---

## 1. Program Structure

A MiniLambda program consists of **exactly one expression**.

```text
<program> ::= <expr>
```

The value of this expression is the result of the program.

---

## 2. Core Concepts

### 2.1 Expression-Oriented Language

MiniLambda has no statements.  
Every construct in the language is an **expression** and evaluates to a value.

Examples:
```text
1 + 2
let x = 3 in x * 2
if true then 1 else 0
```

---

## 3. Values

MiniLambda supports exactly two kinds of runtime values.

### 3.1 Integers

```text
0
1
42
```

- Unsigned decimal integers
- All arithmetic is integer arithmetic

### 3.2 Booleans

```text
true
false
```

---

## 4. Variables and Identifiers

### 4.1 Identifiers

- Must start with an alphabetic character or `_`
- May contain alphanumeric characters and `_`

Examples:
```text
x
fib
_temp1
```

---

## 5. Let Bindings

### 5.1 Syntax

```text
let <name> = <expr> in <expr>
```

### 5.2 Semantics

- The bound expression is evaluated
- The resulting value is bound to `<name>`
- The body expression following `in` is evaluated in the extended environment
- **`let` itself is an expression and produces a value**

Example:
```text
let x = 2 in x + 3
```

Result:
```text
5
```

### 5.3 Recursion

MiniLambda `let` bindings are **implicitly recursive**.  
The bound identifier may be referenced within its own definition.

```text
let fib =
  fn n ->
    if n <= 1 then n else fib(n - 1) + fib(n - 2)
in
fib(10)
```

---

## 6. Conditional Expressions

### 6.1 Syntax

```text
if <cond> then <expr1> else <expr2>
```

### 6.2 Semantics

- `<cond>` must evaluate to a boolean
- Exactly one branch is evaluated

Example:
```text
if 1 < 2 then 10 else 20
```

---

## 7. Functions

### 7.1 Function Definition

```text
fn <param> -> <body>
```

- Functions take exactly one parameter
- Functions are first-class values

---

### 7.2 Function Application

```text
<expr>(<expr>)
```

- Function application is **left-associative**

Examples:
```text
f(x)
f(x)(y)
```

---

### 7.3 Closures

Functions capture the lexical environment in which they are defined.

```text
let add =
  fn x ->
    fn y -> x + y
in
add(2)(3)
```

---

## 8. Operators

### 8.1 Arithmetic Operators

| Operator | Meaning |
|--------|--------|
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division (division by zero is an error) |

### 8.2 Comparison Operators

| Operator |
|--------|
| `==` `!=` |
| `<` `<=` `>` `>=` |

All comparison operators evaluate to boolean values.

---

## 9. Operator Precedence

From highest to lowest precedence:

1. Parentheses `( )`
2. Function application
3. `*` `/`
4. `+` `-`
5. Comparison operators

Example:
```text
1 + 2 * 3 == 7
```

---

## 10. Grouping

Parentheses are used to explicitly control evaluation order.

```text
(1 + 2) * 3
```

---

## 11. Errors

MiniLambda implementations must report errors using **standardized error codes**.

| Code | Meaning |
|----|----|
| `PARSE_ERROR` | Syntax error |
| `UNBOUND_VAR` | Reference to an undefined variable |
| `DIV_BY_ZERO` | Division by zero |
| `TYPE_ERROR` | Type mismatch at runtime (e.g., non-boolean condition, arithmetic on booleans, calling a non-function) |
| `TIMEOUT` | Execution time limit exceeded |

---

## 11.1 Type Rules (Dynamic)

MiniLambda is dynamically checked but **type violations are errors** (reported as `ERR TYPE_ERROR`).

- **`if <cond> then ... else ...`**
  - `<cond>` must evaluate to a boolean (`true`/`false`), otherwise `TYPE_ERROR`.
- **Arithmetic operators** (`+ - * /`)
  - Both operands must be integers, otherwise `TYPE_ERROR`.
  - `/` with right operand 0 is `DIV_BY_ZERO` (takes precedence over `TYPE_ERROR` only after operands are confirmed integers).
- **Ordering comparisons** (`< <= > >=`)
  - Both operands must be integers, otherwise `TYPE_ERROR`.
- **Equality operators** (`== !=`)
  - Both operands must have the same type (both integers or both booleans), otherwise `TYPE_ERROR`.
- **Function application** `f(x)`
  - The left side must evaluate to a function value (closure), otherwise `TYPE_ERROR`.

## 12. Evaluation Model Summary

- Strict (eager) evaluation
- Call-by-value
- No side effects

---

## 13. Design Rationale

MiniLambda is not intended as a practical programming language.  
It is designed as a **controlled experimental workload** for comparing the cost of language implementation and reasoning.

The language intentionally requires:

- Parsing
- Scope and environment management
- Closures
- Recursion
- Error handling

while remaining small enough to be implemented autonomously by an LLM.