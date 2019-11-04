digits = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0", "-", "."]

class Token:
    def __init__(self, tokenType, tokenValue):
        self.tokenType = tokenType
        self.tokenValue = tokenValue

    def show(self):
        print(f"TOKEN[type: {self.tokenType}, value: {self.tokenValue}]")

def lexical_analyzer(path):
    #read the file data
    with open(path) as file:
        code = file.read()

    #convert to individual tokens
    tokens = []
    for char in code:
        if char.isalpha():
            tokens.append(Token("keyword", char))

        elif char in digits:
            tokens.append(Token("digit", char))

    
    #combine neighbouring tokens with the same type
    newtokens = []
    for i in range(len(tokens)-1):
        if tokens[i].tokenType == "digit" and tokens[i+1].tokenType == "digit":
            newtokens.append(Token("digit", tokens[i].tokenValue + tokens[i+1].tokenValue))

    for t in newtokens:
        t.show()