# calclex.py

from sly import Lexer, Parser


class SqlLexer(Lexer):
    # Set of token names.   This is always required
    tokens = {ID, NUMBER, STRING, SELECT, FROM, WHERE, AND, OR}

    literals = {"(", ")", ";", "*", "+", "-", "=", "<", ">"}

    # String containing ignored characters
    ignore = " \t"

    # Regular expression rules for tokens
    STRING = r"\'[^\'\n]*\'"

    @_(r"\d+")
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    # 定义关键字
    ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
    ID["select"] = SELECT
    ID["from"] = FROM
    ID["where"] = WHERE
    ID["and"] = AND
    ID["or"] = OR

    ignore_comment = r"\#.*"

    # Line number tracking
    @_(r"\n+")
    def ignore_newline(self, t):
        self.lineno += t.value.count("\n")

    def error(self, t):
        print("Line %d: Bad character %r" % (self.lineno, t.value[0]))
        self.index += 1


# 定义Parser类
class SqlParser(Parser):
    tokens = SqlLexer.tokens

    # 定义语法产生式
    @_("select_statement")
    def statement(self, p):
        return p.select_statement

    @_("SELECT select_list FROM table_list where_clause")
    def select_statement(self, p):
        return ("select", p.select_list, p.table_list, p.where_clause)

    @_("select_item")
    def select_list(self, p):
        return [p.select_item]

    @_('select_list "," select_item')
    def select_list(self, p):
        return p.select_list + [p.select_item]

    @_('"*"')
    def select_item(self, p):
        return "*"

    @_("ID")
    def select_item(self, p):
        return p.ID

    @_("table_item")
    def table_list(self, p):
        return [p.table_item]

    @_('table_list "," table_item')
    def table_list(self, p):
        return p.table_list + [p.table_item]

    @_("ID")
    def table_item(self, p):
        return p.ID

    @_("WHERE condition")
    def where_clause(self, p):
        return ("where", p.condition)

    @_("")
    def where_clause(self, p):
        return None

    @_("condition AND condition")
    def condition(self, p):
        return ("and", p.condition0, p.condition1)

    @_("condition OR condition")
    def condition(self, p):
        return ("or", p.condition0, p.condition1)

    @_('"(" condition ")"')
    def condition(self, p):
        return p.condition

    @_('expression "=" expression')
    def condition(self, p):
        return ("=", p.expression0, p.expression1)

    @_('expression "<" expression')
    def condition(self, p):
        return ("<", p.expression0, p.expression1)

    @_('expression ">" expression')
    def condition(self, p):
        return (">", p.expression0, p.expression1)

    @_("ID")
    def expression(self, p):
        return ("id", p.ID)

    @_("NUMBER")
    def expression(self, p):
        return ("num", int(p.NUMBER))

    @_("STRING")
    def expression(self, p):
        return ("str", p.STRING)

    # 定义语法错误处理方法
    def error(self, p):
        if p:
            print(f"Syntax error at {p.value!r}")
        else:
            print("Syntax error at EOF")


if __name__ == "__main__":
    lexer = SqlLexer()
    parser = SqlParser()

    # sql = "select * from t1 "
    sql = "select * from student where name = 'Alice' and age > 18"

    result = parser.parse(lexer.tokenize(sql))
    print(result)
    # for tok in lexer.tokenize(sql):
    #     print(tok)
