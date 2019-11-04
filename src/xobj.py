from sys import argv

version = "XOBJ 0.0.1a"

if argv[1] == "help" or len(argv) <= 1:
    pass

elif argv[1] == "translate":
    from xobj_lexer import lexical_analyzer
    path = argv[2]
    print(f"TRANSLATING {path}")
    lexical_analyzer(path)

else:
    print(f"UNKNOWN ARGUMENT {argv[0]}")