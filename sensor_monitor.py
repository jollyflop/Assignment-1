import csv
import random

import matplotlib.pyplot as plt
import numpy as np


def get_float(prompt):
    pass


def get_positive_int(prompt):
    pass


def get_user_input():
    pass



def generate_readings(count, min_value, max_value, seed=42):
    random.seed(seed)

    readings = []

    for _ in range(count):
        value = round(random.uniform(min_value, max_value), 2)
        readings.append(value)

    return readings



def calculate_statistics(readings, threshold):
    values = np.array(readings)

    stats = {
        "count": len(values),
        "mean": np.mean(values),
        "min": np.min(values),
        "max": np.max(values),
        "std": np.std(values),
        "above": int(np.sum(values > threshold)),
    }

    return stats


def find_outliers(readings, threshold):
    outliers = []

    for number, value in enumerate(readings, start=1):
        if value > threshold:
            outliers.append((number, value))

    return outliers


def display_results(stats, outliers):
    print("\n--- Results ---")
    print(f"Count: {stats['count']}")
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Min: {stats['min']:.2f}")
    print(f"Max: {stats['max']:.2f}")
    print(f"Std: {stats['std']:.2f}")
    print(f"Above threshold: {stats['above']}")
    print("Readings above threshold:")

    for number, value in outliers:
        print(f"Sample {number}: {value}")


def save_readings(filename, readings):
    pass


def load_readings(filename):
    pass


def plot_readings(readings, threshold, sensor_type):
    pass


def plot_histogram(readings, sensor_type):
    pass


def main():
    readings = [10, 20, 30]
    stats = calculate_statistics(readings, 15)
    outliers = find_outliers(readings, 15)
    display_results(stats, outliers)

if __name__ == "__main__":
    main()
