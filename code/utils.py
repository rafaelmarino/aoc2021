def grid_to_dict(grid):
    return {(i, j): v for j, row in enumerate(grid) for i, v in enumerate(row)}


def neighbours(i, j, diag=False):
    yield (i - 1, j)
    yield (i + 1, j)
    yield (i, j - 1)
    yield (i, j + 1)
    if diag:
        yield (i - 1, j - 1)
        yield (i - 1, j + 1)
        yield (i + 1, j - 1)
        yield (i + 1, j + 1)


# def neighbours(i, j, diag=False):
#     yield from [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
#     if diag:
#         yield from [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
