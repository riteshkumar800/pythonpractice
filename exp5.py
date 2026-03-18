from lark import Lark, Token, UnexpectedInput
from collections import Counter

# ---------------- Q1 ----------------
def q1():
    print("\n--- Q1: Tokenization Using EBNF Grammar ---")

    grammar = r"""
    ?start: statement+

    statement: (KEYWORD)? IDENTIFIER "=" expr ";"
    ?expr: term (OP term)*
    ?term: NUMBER | IDENTIFIER

    KEYWORD.2: "int" | "float" | "if" | "else" | "while" | "return"
    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /\d+(\.\d+)?/
    OP: "+" | "-" | "*" | "/" | "==" | "!=" | "<" | ">" | "<=" | ">="

    %ignore WS
    WS: /[ \t\n]+/
    """

    parser = Lark(grammar, parser="lalr")
    data = "int x = 10; y = x + 3.14;"
    tree = parser.parse(data)

    for token in tree.scan_values(lambda v: hasattr(v, 'type')):
        print(token.type, token.value)


# ---------------- Q2 ----------------
def q2():
    print("\n--- Q2: Ignoring Whitespace and Comments ---")

    grammar = r"""
    start: statement+

    statement: IDENTIFIER "=" NUMBER ";"

    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /\d+/

    %ignore WS
    %ignore /\/\/.*/
    %ignore /\/\*[\s\S]*?\*\//

    WS: /[ \t\n]+/
    """

    parser = Lark(grammar, parser="lalr")

    data = """
    // single line comment
    x = 10; /* multi-line comment */
    y = 20;
    """

    print(parser.parse(data))


# ---------------- Q3 ----------------
def q3():
    print("\n--- Q3: Line and Column Number Reporting ---")

    grammar = r"""
    start: WORD+
    WORD: /[a-zA-Z_]+/

    %ignore WS
    WS: /[ \t\n]+/
    """

    parser = Lark(grammar, parser="lalr", propagate_positions=True)

    data = "hello world\ncompiler lab"
    tree = parser.parse(data)

    for token in tree.scan_values(lambda v: isinstance(v, Token)):
        print(f"{token.type}: {token.value} @ line {token.line}, column {token.column}")


# ---------------- Q4 ----------------
def q4():
    print("\n--- Q4: Error Handling ---")

    grammar = r"""
    start: assignment+
    assignment: IDENTIFIER "=" NUMBER ";"

    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /\d+/

    %ignore WS
    WS: /[ \t\n]+/
    """

    parser = Lark(grammar, parser="lalr")

    data = "x = 10 y = 20;"  # missing semicolon

    try:
        parser.parse(data)
    except UnexpectedInput as e:
        print("Syntax Error at line", e.line, "column", e.column)
        print("Recovery: Assuming missing semicolon...")


# ---------------- Q5 (FIXED) ----------------
def q5():
    print("\n--- Q5: Token Categorization ---")

    grammar = r"""
    start: (IDENTIFIER | NUMBER | OPERATOR | KEYWORD)+

    IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
    NUMBER: /\d+(\.\d+)?/
    OPERATOR: "+" | "-" | "*" | "/" | "="
    KEYWORD.2: "int" | "float" | "if" | "else" | "while" | "return"

    %ignore WS
    WS: /[ \t\n]+/
    """

    parser = Lark(grammar, parser="lalr", propagate_positions=True)

    data = "int x = 10 x = x + 5 return x"
    tree = parser.parse(data)

    ids, nums, ops, keys = [], [], [], []

    for token in tree.scan_values(lambda v: isinstance(v, Token)):
        if token.type == "IDENTIFIER":
            ids.append(token.value)
        elif token.type == "NUMBER":
            nums.append(token.value)
        elif token.type == "OPERATOR":
            ops.append(token.value)
        elif token.type == "KEYWORD":
            keys.append(token.value)

    # Save into files
    open("identifiers.txt", "w").write("\n".join(ids))
    open("numbers.txt", "w").write("\n".join(nums))
    open("operators.txt", "w").write("\n".join(ops))
    open("keywords.txt", "w").write("\n".join(keys))

    # Frequency count
    print("Identifier Frequency:", Counter(ids))
    print("Number Frequency:", Counter(nums))
    print("Operator Frequency:", Counter(ops))
    print("Keyword Frequency:", Counter(keys))


# ---------------- MENU (Switch Case Style) ----------------
while True:
    print("\n==== Scanner using Lark ====")
    print("1. Tokenization")
    print("2. Ignore Comments")
    print("3. Line & Column")
    print("4. Error Handling")
    print("5. Token Categorization")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        q1()
    elif choice == "2":
        q2()
    elif choice == "3":
        q3()
    elif choice == "4":
        q4()
    elif choice == "5":
        q5()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")