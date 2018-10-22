# UnknownFuck
A programming language based on BrainFuck. It's not intended to be used seriously.
## Information:
The unknownFuck.py file is an interpreter for the language.

The language is Brainfuck but with the characters replaced with other characters.

## Usage
- Move pointer left: {
- Move pointer right: }
- Increment current cell by 1: U
- Decrease current cell by 1: T
- Read a byte of input: C
- Write a byte of output in ASCII format: ?
- Loop start: \[
- Loop end: \]
## Example
```
UUUUUUUUUU Looping 10 times
[
}UUUUUUU Move pointer forward. Add 7 to cell
}UUUUUUUUUU Move pointer forward. Add 10 to cell
}UUU Move pointer forward. Add 3 to cell
}U Move pointer forward. Add 1 to cell
{{{{ Move pointer backwards 4 cells.
T End 1 loop
] Close loop
} Move pointer forward 1
?UUUUUUUUUUUUUUU Output ASCII 70 and add 15
?TTTTTTTTTTTTTTTTTT Output ASCII 85 and subtract 18
?UUUUUUUU Output ASCII 67 and add 8
?}}UU Output ASCII 75, move pointer forward twice to cell with 30. Add 2, bringing it to 32.
?{TTTTTTTTTTT Output ASCII 32, move pointer backwards once. Sub 11 to 100.
?TTTTTTTTTT Output 89. Subtract 10 from cell
?UUUUUU? Output 79, Add 6 to cell. Output 85.
```
## Is this language turing complete?
Brainfuck is turing complete. By substitution of characters, UnknownFuck is turing complete.
