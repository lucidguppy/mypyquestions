from foo.add import add


def mult(a: int, b: int) -> int:
    result = b  # type: int
    for ii in range(a-1):
        result = add(result, b)

    return result
