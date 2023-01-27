from StoriiParserVisitor import StoriiParserVisitor


class StoriiVisitor(StoriiParserVisitor):
    def visitWords(self, ctx):
        return ' '.join(child.getText() for child in ctx.children)



