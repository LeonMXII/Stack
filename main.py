from class_stack import Stack

subsequence_1 = "(((([{}]))))"
subsequence_2 = "[([])((([[[]]])))]{()}"
subsequence_3 = "{{[()]}}"
subsequence_4 = "}{}"
subsequence_5 = "{{[(])]}}"
subsequence_6 = "[[{())}]"


def elements(subse):
    lists = list(subse)
    stack = Stack()
    for el in lists:
        if el in ['(', '{', '[']:
            stack.push(el)
        elif stack.peek() == '(' and el == ')':
            stack.pop()
        elif stack.peek() == '{' and el == '}':
            stack.pop()
        elif stack.peek() == '[' and el == ']':
            stack.pop()
        else:
            stack.push(el)
            break
    if stack.size() == 0:
        print("Сбалансировано")
    else:
        print("Несбалансировано")


if __name__ == '__main__':
    elements(subsequence_1)
    elements(subsequence_2)
    elements(subsequence_3)
    elements(subsequence_4)
    elements(subsequence_5)
    elements(subsequence_6)