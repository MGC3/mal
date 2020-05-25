class Reader:
    def __init__(self, tokens, position):
        pass
    
    def next(self):
        pass

    def peek(self):
        pass

def read_str(str):
    pass

def tokenize(str):
    # todo:
    # [x] ignore whitespace and commas
    # [ ] capture '~@' token
    # [ ] capture single special chars as token, one of []{}()'`~^@
    # [ ] capture double quote strings, accounting for both backslashed and unbalanced quotes
    # [ ] captures any sequence of characters beginning with ;
    # [ ] captures sequence of zero or more non special characters
    arr = [char for char in str if char != "," and not char.isspace()]
    return arr
