import sys

class htmlpar:
    def __init__(self):
        ...
    # make sure things are correct, also puts each tag and its atributes
    # the atual will be added soon
    def evaLine(self, line):
        i = 0
        tag = None
        atributes = {}
        while i < len(line):
            token = line[i]
            if token == '=':
                atrname = line[i-1]
                atrval = []
                j = i # skip the '"'
                print(line[j+1])
                while j < len(line):
                    if line[j] == '"':
                        break
                    atrval.append(line[j+2]) # i mean it works, i woulnt argue until breaks
                    j += 1
                atributes[atrname] = atrval
            elif token == '<':
                j = i + 1
                tag = line[j]
                print(tag)
            i += 1
        return {tag: atributes}
    def evapro(self, pro):
        ast = [] # not ast real, just small
        for line in pro:
            ast.append(self.evaLine(line))
        return ast
class htmltok:
    def __init__(self):
        self.tokens = []
    def tokline(self, line):
        j = 0
        tokens = []
        for i in range(len(line)):
            if line[i] in '</>=" ':
                if j < i:
                    tokens.append(line[j:i])
                tokens.append(line[i])
                j = i+1
        return [token for token in tokens if token.strip()]
    def tokpro(self, program):
        tokens=[]
        for line in program:
            tokens.append(self.tokline(line))
        return tokens
if __name__ == '__main__':
    tok = htmltok()
    par = htmlpar()
    filename = sys.argv[1]
    program = []
    with open(filename, 'r') as file:
        for line in file:
            program.append(line.strip())
    tokens = tok.tokpro(program)
    ast = par.evapro(tokens)
    print(tokens)
    print(ast)
