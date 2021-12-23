#!/usr/bin/python3

from utils import read_input
from collections import Counter


def neighbours(i, j):
    """Return 3x3 neighbors starting from top left corner, clockwise."""
    yield (i - 1, j - 1)
    yield (i - 1, j)
    yield (i - 1, j + 1)
    yield (i, j - 1)
    yield (i, j)
    yield (i, j + 1)
    yield (i + 1, j - 1)
    yield (i + 1, j)
    yield (i + 1, j + 1)


if __name__ == "__main__":
    T = 1
    test, actual = "test/day20", "input/day20"
    data = read_input(test) if T else read_input(actual)
    algo, _, *img = data  # img is square


def enhance_image(algo, img, times=1):
    """--- Day 20: Trench Map ---"""

    output_img = []
    for i, row in enumerate(img):
        for j, col in enumerate(row):
            value = ""
            for (ni, nj) in neighbours(i, j):
                if len(img) <= ni or ni < 0 or len(img) <= nj or nj < 0:
                    value += "."
                else:
                    value += img[ni][nj]
            value = int(value.replace("#", "1").replace(".", "0"), 2)
            output_img.append(algo[value])
    return output_img


img_E = enhance_image(algo, img)
img_E

[img_E[i : i + len(img)] for i in range(0, len(img_E), len(img))]

Counter(img_E)["#"]

# print(f"{}")
# print(f"{}")
