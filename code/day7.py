#!/usr/bin/python3

from statistics import median, mean


def optimal_fuel_spend(positions):
    """--- Day 7: The Treachery of Whales ---"""
    # positions.sort()  # median does not required sorted data
    med = median(positions)
    total_fuel_cost = 0
    for crab in positions:
        total_fuel_cost += abs(crab - med)
    return total_fuel_cost


def optimal_fuel_spend_non_linear(positions):
    """--- Part Two ---"""
    mn = int(mean(positions))  # round(mean(positions) wrong value
    total_fuel_cost = 0
    for crab in positions:
        cost = sum(list(range(1, abs(crab - mn) + 1)))
        total_fuel_cost += cost
        # print(f"Move from {crab} to {mn}: {cost}")
    return total_fuel_cost


if __name__ == "__main__":
    with open("input/day7.txt", "r") as f:
        # data = f.read().splitlines()
        data = f.readline()
    positions = list(map(int, data.split(",")))
    linear_spend = optimal_fuel_spend(positions)
    non_linear_spend = optimal_fuel_spend_non_linear(positions)
    print(f"Optimal fuel spend (median alignment): {int(linear_spend)}")
    print(f"Optimal fuel spend (mean alignment): {int(non_linear_spend)}")
