import re
from itertools import chain

cat = "".join
flatten = chain.from_iterable

# import timeit
# print(timeit.timeit(main, number=1))


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


def neighbours9(i, j):
    """Return 3x3 neighbors starting from top left corner, clockwise."""
    yield from [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)]  # above
    yield from [(i, j - 1), (i, j), (i, j + 1)]  # level
    yield from [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]  # below


# def neighbours(i, j, diag=False):
#     yield from [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
#     if diag:
#         yield from [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]


def mapl(f, iterable):
    return list(map(f, iterable))


def mapt(f, iterable):
    return tuple(map(f, iterable))


def filterl(f, iterable):
    return list(filter(f, iterable))


def read_input(filename, datatype=str, sep="\n"):
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"{filename}.txt") as f:
        # with open(f"input/{filename}.txt") as f:
        contents = f.read().strip().split(sep)
        return mapl(datatype, contents)


def read_input_line(filename, sep=""):
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"{filename}.txt") as f:
        # with open(f"input/{filename}.txt") as f:
        contents = f.read().strip()
        return contents if not sep else contents.split(sep)


def digits(line):
    return mapl(int, line)


def integers(text, negative=True):
    return mapt(int, re.findall(r"-?\d+" if negative else r"\d+", text))


def n_chunks(lst, n):
    """Return/yield successive n-sized chunks from lst."""
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i : i + n])
        # yield lst[i : i + n]
    return result


def write_txt(data, path):
    """Write eight capital letters to text"""
    with open(path, "w") as f:
        for row in data:
            row = "".join(map(str, row))
            # row = row.replace("0", " ")
            # row = row.replace("1", "#")
            _ = f.write(row + "\n")
