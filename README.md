# SYMBDIFF v1

## Scope of the program

This program is part of a thesis submitted in partial fulfillment of the requirements for the degree of Mathematics at the University of Oviedo. The idea was to implement an algorithm that could compute the symbolic derivative of a given mathematical expression.

## General idea

Natural numbers (positive integers) are treated as strings, `'9'`, negative numbers are stored as lists `['-', '0', '3']` and fractions are stored also as lists `['/', '1', '2']`. In case the fraction was negative, the sign would only affect the numerator, hence `['/', ['-', '0', '1'], '2']`.

The key idea was to store mathematical expressions as nested lists, and this was motivated by the first reference included at the end. In order to do so, there are different steps to follow:

1. The user can input a parenthesized mathematical expression consisting of the symbols: `+, *, -, /, ^` and/or the functions `cos(), sin(), exp(), log()`as well as parentheses, square brackets, numbers or letters.

2. This expression is tokenized using `tokenizer.py`.

3. Once it has been tokenized it is transformed into reverse polish notation (RPN)  making use of the Shunting Yard Algorithm, which is implemented in `SYA.py`.

4. It is then converted in what we call Square Polish Reverse Notation (SQPRN) using `SQRPN.py`, which basically transforms the expression into a collection of nested lists. Each list is either a triple like `['+','2','x']` wich stands for 2+x, or a pair `['cos', 'x']` which stands for cos(x).

5. Using `diff2.py` we compute the derivative of the expression written in SQRPN form.

6. Once it has been differentiated, `simplify.py` takes care of simplifying the expression to eliminate redundant information or easy calculations such as 0*x.

7. Lastly, `infix.py` returns the fully parenthesized derivative of the expression.

Special attention should be taken when dealing with the exponentiation operator `^`, because `['^', 'a', 'b']` stands for a^b. We also note that the unary minus in -1 is treated as `['-', '0', '1']`.

## Instructions

- This program requires Python 3 to run, so make sure you have it installed in your computer.
- To run the program execute symbdiff.py and follow the steps
- To terminate the program type `exit`

## Notes

The program has been tested with many kinds of symbolic expressions, but please understand that in spite of the many hours of work devoted to it, there might still be errors. I have tried to produce a readable code, and although it is not full of comments, it should not be too difficult to follow. I am a student of Mathematics and Physics, so please take that into consideration when judging my code. All the coding in python is my own work, with the exception of the Shunting yard Algorithm.



## References
- https://source-academy.github.io/sicp/chapters/2.3.2.html (last access: 05/05/2021)
- https://www.andr.mu/logs/the-shunting-yard-algorithm/ (last access: 05/05/2021)