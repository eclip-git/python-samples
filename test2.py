def isvalid(s):

    opens = s.count('{') + s.count('[') + s.count('(')
    closes = s.count('}') + s.count(']') + s.count(')')

    return opens-closes


print(isvalid("{dsnndn}[abc](((def))"))
