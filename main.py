import matplotlib.pyplot as plt
import random
import math


hns_pattern = [0.0, 2.0, 1.0, 4.0, 3.0, 5.0, 3.0, 4.0, 0.0, 1.0]

test_data = [round(random.uniform(0.13, 0.18), 6) for i in range(100)]


def generate_sample_patterns(nodes=5):
    """ Returns a random pattern with length of int nodes of type list """

    return [random.randint(1, nodes) for i in range(nodes)]


def range_mapping(pattern, data):
    """ Maps an array with interval a, onto the interval b of another array."""

    squished_data = []

    for entry in data:
        min_diff = entry - min(data)
        normalized_diff = min_diff / (max(data) - min(data))
        squished_entry = min(pattern) + normalized_diff * (max(pattern) - min(pattern))

        squished_data.append(squished_entry)

    return squished_data


def dynamic_time_warping(pattern, data):
    """ Returns a list of locations inside a given data set, wherein the supplied pattern is found """

    cost_matrix = [[0 for x in range(len(pattern))] for y in range(len(data)-len(pattern))]

    squished_data = range_mapping(pattern, data)

    for i in range(0, len(squished_data) - len(pattern)):
        for j, k in enumerate(squished_data[i:i + len(pattern)]):

            # Calculate cell cost
            cost = math.sqrt((pattern[j] - k) ** 2)

            # DTW, Insert cell cost and neighbor value into cost matrix.
            cost_matrix[i][j] = cost + min(cost_matrix[i-1][j],    # Insertion
                                           cost_matrix[i][j-1],    # Deletion
                                           cost_matrix[i-1][j-1])  # Match

    visualize_2dmatrix(cost_matrix)


def visualize_2dmatrix(matrix):
    """ Creates a matplotlib imshow() visualization of a given 2d matrix """

    plt.imshow(matrix)
    plt.show()


dynamic_time_warping(hns_pattern, test_data)

