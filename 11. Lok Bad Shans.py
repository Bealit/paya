import re
def inverted_calculater(expr):
    rep = {'1': '7', '2' : '8', '3' : '9', '7' : '1', '8' : '2', '9' : '3'}
    exp = ''.join(rep.get(i, i) for i in expr)
    exp = re.sub(r'\s+', '', exp)
    exp = re.sub(r'(?<=\d)-', ' -', exp)
    exp = re.sub(r'(?<=\()-', '0-', exp)
    try:
        result = eval(exp, {'__builtins__': None})
    except Exception as e:
        return f"Error: {e}"
    return result

exp = input()
print(inverted_calculater(exp))