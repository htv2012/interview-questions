#!/usr/bin/env python3
# https://leetcode.com/problems/basic-calculator/description/
import operator
import queue
import re


def tokenize(text: str) -> list:
    pattern = re.compile(r"\d+|[-+()]")
    tokens = pattern.findall(text)
    return tokens


def change_sign(number: int):
    return 0 - number


def precedence(op: str) -> int:
    li = [("(",), (operator.add, operator.sub), (change_sign,)]
    for index, ops in enumerate(li):
        if op in ops:
            return index
    raise ValueError(op)


def top_of_stack(stack: queue.Queue):
    value = stack.get_nowait()
    stack.put(value)
    return value


def infix_to_rpn(expr: str) -> list:
    operator_translation = {
        "+": operator.add,
        "-": operator.sub,
    }
    que = []  # Hold RPN tokens
    stack = queue.LifoQueue()  # Holds operators
    prev = None

    for index, token in enumerate(tokenize(expr)):
        if token.isnumeric():
            que.append(int(token))
            prev = token
            continue

        token = operator_translation.get(token, token)
        if token == "(":
            stack.put(token)
        elif token == ")":
            while top_of_stack(stack) != "(":
                que.append(stack.get_nowait())
            stack.get_nowait()  # Get rid of the left paren
        elif token == operator.add:
            while not stack.empty() and precedence(top_of_stack(stack)) >= precedence(
                token
            ):
                que.append(stack.get_nowait())
            stack.put(token)

        elif token == operator.sub:
            if index == 0 or prev in {operator.add, operator.sub, "("}:
                stack.put(change_sign)
            else:
                while not stack.empty() and precedence(
                    top_of_stack(stack)
                ) >= precedence(token):
                    que.append(stack.get_nowait())
                stack.put(token)
        prev = token
    while not stack.empty():
        que.append(stack.get_nowait())

    return que


def evaluate_rpn(rpn: list):
    unary_operators = {change_sign}
    binary_operators = {operator.add, operator.sub}
    stack = queue.LifoQueue()
    for token in rpn:
        if isinstance(token, int):
            stack.put(token)
        elif token in unary_operators:
            number = stack.get_nowait()
            number = token(number)
            stack.put(number)
        elif token in binary_operators:
            right = stack.get_nowait()
            left = stack.get_nowait()
            number = token(left, right)
            stack.put(number)
        else:
            raise ValueError(f"Unrecognized operator: {token}")

    return stack.get_nowait()


class Solution:
    def calculate(self, s: str) -> int:
        rpn = infix_to_rpn(s)
        out = evaluate_rpn(rpn)
        return out
