# Recursive Functions in Python

## Introduction
In Python, recursive functions are powerful tools for solving problems that can be naturally defined in a recursive manner. A recursive function calls itself during execution to break down a problem into smaller sub-problems.

## What Is a Recursive Function?
- A recursive function is one that calls itself (directly or indirectly) during its execution.
- Recursive algorithms often provide simpler solutions than other forms of algorithmic writing.
- It's essential to define a base case or termination condition to prevent infinite loops.

## Example: Factorial Calculation
The factorial of a non-negative integer `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`.

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

In this example, the function calculates the factorial of 5 by multiplying 5 with the factorial of 4, which in turn multiplies with the factorial of 3, and so on until the base case (n = 1) is reached.

## Benefits of Recursion
- Code reusability: Recursive functions can call themselves with different arguments, simplifying implementation and maintenance.
- Divide and conquer: Recursive algorithms break down problems into smaller parts, making them easier to solve.

Remember to define a base case to avoid infinite recursion.

---

Happy coding! 🚀🐍

Source:
(1) Recursividade em Python: Somatório e Fatorial Usando .... https://www.pythonprogressivo.net/2018/10/Recursividade-Somatorio-Fatorial-Funcao-Recursiva.html.
(2) . https://bing.com/search?q=funcoes+recursivas+Python.
(3) Aprendendo Funções Recursivas em Python: Guia Completo - Covil do Dev. https://www.covildodev.com.br/artigo/recursao-python.
(4) Função Recursiva em Python: Aprenda a criar algoritmos poderosos. https://awari.com.br/funcao-recursiva-em-python-aprenda-a-criar-algoritmos-poderosos/.
(5) Funções Recursivas em Python: O que são, e como funcionam?. https://www.dio.me/articles/funcoes-recursivas-em-python-o-que-sao-e-como-funcionam.
(6) undefined. https://diveintopython.org/learn/functions/recursion.
(7) undefined. https://www.w3schools.com/python/gloss_python_function_recursion.asp.