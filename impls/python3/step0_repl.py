def read_lisp(s):
    return s

def eval_lisp(s):
    return s

def print_lisp(s):
    return s

def rep(input):
    return print_lisp(eval_lisp(read_lisp(input)))

while True:
    prompt = input("user> ")
    print(prompt)
    print(rep(prompt))