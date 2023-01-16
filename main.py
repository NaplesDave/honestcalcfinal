# Honest Calculator
# Challenge JetBrains Academy - Flow Chart programming
# David A. King  Jan 16, 2023 - 5/5  -  FINAL PASSING CODE
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
oper = ["+", "-", "*", "/"]
memory = 0.0
result = 0.0


def is_one_digit(v):
    try:
        num = float(v)
    except ValueError:
        return False
    else:
        if num > -10 and num < 10 and num.is_integer():
            return True
        else:
            return False


def check(x, y, op):
    # print(x, y, op)
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6

    if x == 1 or y == 1 and op == '*':
        msg = msg + msg_7

    if (x == 0 or y == 0) and (op == "*" or op == "+" or op == "-"):
        msg = msg + msg_8

    if msg != "":
        print(msg_9 + msg)


def check_operands(xy):
    if xy.upper() == 'M':
        return True
    else:
        return False


def check_isnumeric(x):
    if isinstance(x, float):
        return True
    elif isinstance(x, str):
        if x.replace(".", "", 1).isdigit():
            return True
        else:
            return False


def check_oper(oppassed):
    if oppassed not in oper:
        return False
    else:
        check(x, y, op)


def do_add():
    return (x + y)


def do_sub():
    return (x - y)


def do_mult():
    return (x * y)


def do_div():
    return (x / y)


def do_math():
    # Do the math
    if op == "+":
        return do_add()
    elif op == "-":
        return do_sub()
    elif op == "*":
        return do_mult()
    elif op == "/":
        return do_div()


def save_quest(result_in):
    if is_one_digit(result_in):
        global memory
        msg_index = 10
        lupctl = True
        while lupctl:
            ans = input(msg_[msg_index])
            if ans.lower() == 'y' and msg_index < 12:
                msg_index = msg_index + 1
                # print("top of loop index < 12")
                # print("result_in = ", result_in)
                # print("msg index = ", msg_index)
            elif ans.lower() == 'n' and msg_index == 12:
                lupctl = False
            elif ans.lower() == 'n':
                lupctl = False
            else:
                memory = result_in
                # print("memory = ", memory)
                lupctl = False


while True:
    calc = input(msg_0)
    # print(calc)
    x, op, y = calc.split()
    # print(x, op, y)
    if check_operands(x) == True:
        x = memory
        # print("x is memory" , x, memory)
    if check_operands(y) == True:
        y = memory

    if check_isnumeric(x):
        x = float(x)
    else:
        print(msg_1)
        continue

    if check_isnumeric(y):
        y = float(y)
    else:
        print(msg_1)
        continue

    if check_oper(op) == False:
        print(msg_2)
        continue

    if op == "/" and y == 0:
        print(msg_3)
        continue
    else:

        result = do_math()
        print(result)
        store = input(msg_4)

        if store.lower() == 'y' and is_one_digit(result) == False:
            memory = result
            # print("memory.1 - result", memory, result)
        elif store.lower() == 'n':
            pass
        else:
            save_quest(result)
            # print("memory.2 - result", memory, result)

    more = input(msg_5)
    if more == 'y':
        continue
    else:
        break
