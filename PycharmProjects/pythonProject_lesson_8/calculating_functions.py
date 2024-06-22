import custom_exceptions


def addition(first, second):
    return first + second


def subtraction(first, second):
    return first - second


def multiplication(first, second):
    return first * second


def division(first, second):
    custom_exceptions.except_devision(first, second)
    return first / second


def exponentiation(first, second):
    return first ** second