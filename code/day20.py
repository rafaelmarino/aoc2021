#!/usr/bin/python3

from utils import read_input, chunks, write_txt
from collections import Counter
import numpy as np


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
    T = False
    test, actual = "test/day20", "input/day20"
    data = read_input(test) if T else read_input(actual)
    algo, _, *img = data  # img is square
    img = np.array([list(i) for i in img])
    # print(img)


def enhance_image(algo, img, t=2):
    """--- Day 20: Trench Map ---"""
    switch = False
    for i in range(t):
        s = "." if not switch else "#"
        img = np.pad(img, pad_width=(1), mode="constant", constant_values=s)
        output_img = []
        for i, row in enumerate(img):
            # i = 0
            # row = img[0]
            for j, col in enumerate(row):
                # j = 0
                value = ""
                for (ni, nj) in neighbours(i, j):
                    if ni <= -1 or ni >= len(img) or nj <= -1 or nj >= len(img):
                        value += s
                    else:
                        value += img[ni][nj]
                value = value.replace("#", "1").replace(".", "0")
                algo_value = algo[int(value, 2)]
                output_img.append(algo_value)
        img = chunks(output_img, len(img))
        switch = not switch
    return output_img


t = 50
enhanced_img = enhance_image(algo, img, t=t)
enhanced_img = chunks(enhanced_img, len(img) + (2 * t))
# print(enhanced_img)
# write_txt(enhanced_img, "extras/day20.txt")
print(f"Part: { Counter([p for row in enhanced_img for p in row])['#'] }")
# print(f"{}")
