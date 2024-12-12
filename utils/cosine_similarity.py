import csv
import math


def dot_product(vector1, vector2):
    min_length = min(len(vector1), len(vector2))
    return sum([vector1[i] * vector2[i] for i in range(min_length)])


def magnitude(vector):
    return math.sqrt(sum([x**2 for x in vector]))


def cosine_similarity(vector1, vector2):
    return dot_product(vector1, vector2) / (
        magnitude(vector1) * magnitude(vector2)
    )


def get_cosine_similarities(vec2):
    similarities = []
    with open("./datasets/doctors_contact_list.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        next(reader_obj)
        for row in reader_obj:
            int_row = [int(num) for num in row[1:]]
            result = cosine_similarity(int_row, vec2)
            similarities.append([int(row[0]), result])

    return similarities
