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
    """ Tokenize accepts a string and returns an array of tokens that mal accepts

    Tokenize creates tokens based on the following rules:
    - captures strings via double quotes. Also includes unclosed strings.
    - captures the "~@" character
    - captures the single special characters ()[]{}'`~^@
    - captures all other sequences of non special characters
    - does not capture whitespace or commas, when not in string
    - does not capture anything after the ";" character, when not in string

    """
    tokens = []
    building_str = False
    temp_str = ''
    building_non_special = False
    temp_non_special = ''
    building_two_char = False
    special = ["(", ")", "[", "]", "{", "}", "'", "`", "~", "^", "@"]

    for idx, char in enumerate(str):
        # handle last character cases:
        # if in the middle of building string or nonspecial string, append what we have
        # if we're building the "~@" character, append it
        # otherwise if character is valid, append it
        if idx == len(str) - 1:
            if building_str:
                temp_str += char
                tokens.append(temp_str)
            elif building_non_special:
                temp_non_special += char
                tokens.append(temp_non_special)
            elif char == "@" and building_two_char:
                tokens.append("~@")
            elif char == '"' or char != ";" and not char.isspace():
                tokens.append(char)
        # when we first see a doublequote, start building a string
        # when we see another doublequote, finish building string and tokenize what we have
        elif char == '"':
            if not building_str:
                building_str = True
                temp_str += char
            elif building_str:
                building_str = False
                temp_str += char
                tokens.append(temp_str)
                temp_str = ''
        elif building_str:
            temp_str += char
        # break on comment
        elif not building_str and not building_non_special and char == ";":
            break
        # capture the '~@' character
        elif char == "~":
            # peek to see if next char is "@"
            next_char = str[idx + 1]
            if next_char == "@":
                building_two_char = True
        elif char == "@" and building_two_char:
            building_two_char = False
            tokens.append("~@")
        # capture any characters that match our specials array as a single token (except for when building string)
        elif char in special:
            if building_non_special:
                tokens.append(temp_non_special)
                temp_non_special = ''
                building_non_special = False
            tokens.append(char)
        # when we see whitespace after a nonspecial string, append the nonspecial string we've built up, other
        elif char.isspace() and building_non_special:
            tokens.append(temp_non_special)
            temp_non_special = ''
            building_non_special = False
        elif char.isspace() or char == "," and not building_non_special:
            # skip whitespace or commas, when not in string
            continue
        # start building a nonspecial string, or continuing to add to an existing one
        elif not building_non_special:
            building_non_special = True
            temp_non_special += char
        else:
            temp_non_special += char
    return tokens