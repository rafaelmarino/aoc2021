#!/usr/bin/python3


def simulate_lanternfish_school(school, days):
    """--- Day 6: Lanternfish ---"""
    for day in range(days):
        old_school_size = len(school)
        for i, fish_timer in enumerate(school):
            if i + 1 > old_school_size:
                continue  # new spawns start countdown the day after
            if fish_timer - 1 == -1:
                school[i] = 6
                school.append(8)  # new spawn
            else:
                school[i] -= 1
        # print(f"Day:{day+1}-School: {school}")
    return len(school)


def simulate_school_hash(school, days):
    """--- Part Two --- Hashmaps to the rescue."""
    school_hash = {i: 0 for i in range(9)}
    for fish in school:
        school_hash[fish] += 1
    # print(f"Day:0-School: {school_hash}")
    for day in range(days):
        spawned = school_hash[0]
        for i in range(len(school_hash) - 1):
            school_hash[i] = school_hash[i + 1]
        school_hash[6] += spawned
        school_hash[8] = spawned
        # print(f"Day:{day+1}-School: {school_hash}")
    return sum(school_hash.values())


if __name__ == "__main__":
    with open("input/day6.txt", "r") as f:
        # data = f.read().splitlines()
        data = f.readline()
    school = list(map(int, data.split(",")))
    days = 256
    # school_size = simulate_lanternfish_school(school, days)
    school_size = simulate_school_hash(school, days)
    print(f"After {days} days the school has grown to {school_size} fishies")
