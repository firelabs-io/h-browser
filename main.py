import sys

class htmlpar:
    def __init__(self):
        self.index = 0
    def buildom(self, pro):
        if self.index >= len(pro):
            return None
        dom = []
        while self.index < len(pro):
            tag_dict = pro[self.index]
            tag = list(tag_dict.keys())[0]
            if tag == '/':
                return dom
            atributes, content = tag_dict[tag]
            self.index += 1
            children = self.buildom(pro)
            dom.append({"tag": tag, "atributes": atributes, "content": content, "children": children})
    def evaLine(self, line):
        i = 0
        tag = None
        atributes = {}
        content = []
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
            else:
                if line[i] not in '></':
                    content.append(line[i])
            i += 1
        return {tag: [atributes, content]}
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
    dom = par.evapro(tokens)
    print(par.buildom(dom))
