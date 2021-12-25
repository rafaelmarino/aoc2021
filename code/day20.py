#!/usr/bin/python3

from utils import read_input, chunks, write_txt, neighbours9
import numpy as np


def enhance_image(algo, img, t=2):
    """--- Day 20: Trench Map ---"""
    switch = False
    for _ in range(t):
        s = "." if not switch else "#"  # sentinel value
        img = np.pad(img, pad_width=(1), mode="constant", constant_values=s)
        output_img = []
        for i, row in enumerate(img):
            for j in range(len(row)):
                value = ""
                for (ni, nj) in neighbours9(i, j):
                    img_sz = len(img)
                    if ni <= -1 or ni >= img_sz or nj <= -1 or nj >= img_sz:
                        value += s
                    else:
                        value += img[ni][nj]
                value = value.replace("#", "1").replace(".", "0")
                algo_value = algo[int(value, 2)]
                output_img.append(algo_value)
        img = chunks(output_img, img_sz)
        switch = not switch
    # return output_img  # actual enhanced image
    return sum(x == "#" for row in output_img for x in row)


if __name__ == "__main__":
    T = False
    test, actual = "test/day20", "input/day20"
    data = read_input(test) if T else read_input(actual)
    algo, _, *img = data  # img is square
    img = np.array([list(row) for row in img])
    # print(img)

print(f"Part 1 -- 2x-enhancement: { enhance_image(algo, img, t=2) }")
print(f"Part 2 -- 50x-enhancement: { enhance_image(algo, img, t=50) }")

# t = 2
# enhanced_img = enhance_image(algo, img, t=t)
# enhanced_img = chunks(enhanced_img, len(img) + (2 * t))
# print(enhanced_img)
# write_txt(enhanced_img, "extras/day20.txt")
