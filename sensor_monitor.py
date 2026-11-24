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

    mask = values > threshold
    high_readings = values[mask]

    stats = {
        "count": len(values),
        "mean": np.mean(values),
        "min": np.min(values),
        "max": np.max(values),
        "std": np.std(values),
        "above": len(high_readings),
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
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["sample", "reading"])

            for sample_number, reading in enumerate(readings, start=1):
                writer.writerow([sample_number, reading])

    except OSError as error:
        print("Could not access the file:", error)

def load_readings(filename):
    readings = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                readings.append(float(row["reading"]))

    except (OSError, ValueError, KeyError) as error:
        print("Could not load the CSV:", error)
        return []

    return readings


def plot_readings(readings, threshold, sensor_type):
    plt.figure()
    sample_number = np.arange(len(readings)) + 1

    plt.plot(
        sample_number,
        readings,
        marker="o",
        label="Reading"
    )

    plt.axhline(
        threshold,
        linestyle="--",
        label="Threshold"
    )

    plt.xlabel("Sample number")
    plt.ylabel("Value")
    plt.title(f"{sensor_type} Readings and Threshold")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_histogram(readings, sensor_type):
    plt.figure()
    plt.hist(readings, bins=5, edgecolor="black")

    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(f"Distribution of {sensor_type} Readings")
    plt.grid(axis="y")
    plt.show()


def main():
    print(load_readings("readings.csv"))
    print(load_readings("no_file.csv"))

if __name__ == "__main__":
    main()
