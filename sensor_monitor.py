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
    pass


def find_outliers(readings, threshold):
    pass


def display_results(stats, outliers):
    pass


def save_readings(filename, readings):
    pass


def load_readings(filename):
    pass


def plot_readings(readings, threshold, sensor_type):
    pass


def plot_histogram(readings, sensor_type):
    pass


def main():
    readings = generate_readings(10, 15, 35)
    print(readings)


if __name__ == "__main__":
    main()
