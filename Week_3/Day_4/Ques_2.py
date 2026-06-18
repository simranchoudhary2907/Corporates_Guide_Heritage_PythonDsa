def is_balanced(expression):
    stack = []

    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in expression:

        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":

            if not stack:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0


# Test Cases
tests = [
    "{[()()]}",
    "{[(])}",
    "((()))",
    "[{]}"
]

for t in tests:
    if is_balanced(t):
        print(t, "-> Balanced")
    else:
        print(t, "-> Not Balanced")