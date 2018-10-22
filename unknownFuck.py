import sys
fileLoc = str(input("Enter the name of the file\nNote it must be in the same directory as this interpreter.\n"))

with open(fileLoc, 'r') as file:
    code = file.read()

brainTape = [0]*(3*10**4)

pointer = 0

def leftTape():
    """Brainfuck equivalent of <"""
    global pointer
    if pointer <=0:
        raise ValueError("Segmentation fault")
    pointer-=1

def rightTape():
    """Brainfuck equivalent of <"""
    global pointer
    if pointer >=(3*10**4):
        raise ValueError("Segmentation fault")
    pointer+=1

def plus():
    """Brainfuck equivalent of +"""
    global pointer
    brainTape[pointer] = ((brainTape[pointer]+1) % 256) #Modulus 256 in case of overflow

def sub():
    """Brainfuck equivalent of -"""
    global pointer
    brainTape[pointer] = ((brainTape[pointer] - 1) % 256) #Modulus 256 in case of underflow

def dot():
    """Brainfuck equivalent of output ASCII character aka ."""
    global pointer
    sys.stdout.write(chr(brainTape[pointer]))

def comma():
    """Brainfuck equivalent of input ASCII character aka ,"""
    global pointer
    c = sys.stdin.read(1) #gets ASCII code of character input
    if c != 26: #EOF Character
        brainTape[pointer] = c
        
def parseBrackets(code):
    opening = []
    loop = {}
    for i, c in enumerate(code):
        if c == "[":
            opening.append(i)
        elif c == "]":
            try:
                begin = opening.pop()
                loop[begin] = i
            except IndexError:
                raise ValueError("Supplied string unbalanced. Too many ['s")
    if opening != []:
        raise ValueError("Supplied string unbalanced. Too many ]'s")
    else:
        return loop

#Primitives to handle easily
handle_directly = {"?": dot, "C": comma, "{": leftTape, "}": rightTape, "U": plus, "T": sub}

def evaluateBrainFuck(code):
    global pointer
    loop = parseBrackets(code)
    pc = 0
    stack = []
    while pc < len(code):
        instruction = code[pc]
        if instruction in handle_directly:
            handle_directly[instruction]()
        elif instruction == "[":
            if brainTape[pointer] > 0:
                stack.append(pc)
            else:
                pc = loop[pc]
        elif instruction == "]":
            pc = stack.pop() - 1
        pc+=1

evaluateBrainFuck(code)
