import sys

class htmlpar:
    def __init__(self):
        ...
    # make sure things are correct, also puts each tag and its atributes
    # the atual will be added soon
    def evaLine(self, line):
        i = 0
        tags = {}
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
            elif token == '<' and line[i+1] != '/':
                # im gonna not for now auto matcially put tag atr
                # so it will only get tag name
                tagname = line[i+1]
                tags[tagname] = None
            i += 1
        return tags, atributes
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

if __name__ == '__main__':
    tok = htmltok()
    par = htmlpar()
    tokens = tok.tokline("<p> hello </p>")
    tokens2 = tok.tokline("</img src=\"image.png\" alt=\"image\"")
    ast = par.evaLine(tokens)
    ast2 = par.evaLine(tokens2)
    print(tokens, ast)
    print(tokens2, ast2)
