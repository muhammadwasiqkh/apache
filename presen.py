import re

# Symbol Table Class
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, type, value=None):
        if name not in self.symbols:
            self.symbols[name] = {'type': type, 'value': value}

    def get(self, name):
        return self.symbols.get(name, None)

    def display(self):
        for name, info in self.symbols.items():
            print(f"Name: {name}, Type: {info['type']}, Value: {info['value']}")

# Lexical Analyzer Class
class LexicalAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def tokenize(self, code):
        tokens = []
        patterns = [
            ('KEYWORD', r'\b(int|float|if|return)\b'),
            ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
            ('NUMBER', r'\b\d+\b'),
            ('FLOAT', r'\b\d+\.\d+\b'),
            ('OPERATOR', r'[+\-*/=<>]'),
            ('PUNCTUATION', r'[();{}]'),
            ('WHITESPACE', r'\s+'),
        ]

        token_specification = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in patterns)
        regex = re.compile(token_specification)
        
        line_num = 1
        line_start = 0
        for mo in regex.finditer(code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'WHITESPACE':
                continue
            elif kind == 'IDENTIFIER':
                if value not in self.symbol_table.symbols:
                    self.symbol_table.add(value, 'unknown')
            tokens.append((kind, value))
        
        return tokens

# Example Program
code = """
int main() {
    int x = 10;
    float y = 20.5;
    if (x > y) {
        x = x + 1;
    }
    return 0;
}
"""

# Lexical Analyzer
lexer = LexicalAnalyzer()
tokens = lexer.tokenize(code)

# Displaying Tokens
print("Tokens:")
for token in tokens:
    print(f"{token[0]}: {token[1]}")

# Displaying Symbol Table
print("\nSymbol Table:")
lexer.symbol_table.display()
