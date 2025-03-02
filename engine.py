import sys
import render as r
import time

class htmlpar:
    def __init__(self):
        pass
    def buildom(self, pro, index=0):
        dom = []
        while index < len(pro):
            tag_dict = pro[index]
            tag = list(tag_dict.keys())[0]
            if tag == '/':
                return dom
            atributes, content = tag_dict[tag]
            index += 1
            children = self.buildom(pro, index)    
            dom.append({"tag": tag, "atributes": atributes, "content": content, "children": children})
        return []
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
                #print(line[j+1])
                while j < len(line):
                    if line[j] == '"':
                        break
                    atrval.append(line[j+2]) # i mean it works, i woulnt argue until breaks
                    j += 1
                atributes[atrname] = atrval
            elif token == '<':
                j = i+2
                tag = line[j]
                #print(tag)
            else:
                #print(line[i])
                if line[i] not in '></' and len(line) > i+1:
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
    
def render(root, dom):
    for d in dom:  
        if d['tag'] == 'head':
            continue
        if d['tag'] == 'p':
            _ = "".join(d["content"])
            r.pc(root, _)
        elif d['tag'] == 'input':
            r.inpc(root)
        elif d['tag'] == 'h1':
            _ = "".join(d["content"])
            r.h1c(root, _)
        
        if len(d['children']) > 0:
            for child in d['children']:
                render(root, [child])  
if __name__ == '__main__':
    tok = htmltok()
    par = htmlpar()
    filename = sys.argv[1]
    program = []
    with open(filename, 'r') as file:
        for line in file:
            program.append(line.strip())
    tokens = tok.tokpro(program)
    print(tokens)
    dom = par.evapro(tokens)
    print(dom)
    #root = r.initgui()
    print(par.buildom(dom))
    #render(root, par.buildom(dom))
    #r.loop(root)
    