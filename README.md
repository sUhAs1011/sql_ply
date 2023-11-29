# sql_ply
My third-semester project for Automata, Formal Languages, and Logic (AFLL), the goal was to determine the validity of SQL statements entered into a terminal. To achieve this, I employed SQL constructs such as select, truncate, drop, commit, and rename.

The process began with the installation of the `ply` module using the command "pip install ply." This module facilitated the use of lex and yacc functionalities within my project. Lex played a crucial role in tokenizing the input string, breaking it down into meaningful units, while yacc was instrumental in parsing the tokenized structure for validation purposes. The combination of lex for tokenization and yacc for parsing formed the backbone of the process used to determine the validity of the SQL statements entered by the user in the terminal.
Installation of ply software in Python

```shell
pip install ply
```

