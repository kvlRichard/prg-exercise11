import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

values = random_numbers(10)  # 10 čísel v rozsahu 0–100
small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20


def selection_sort(values):

    for x in range(len(values)):
        min_idx = x
        min_value = values[min_idx]
        for i in range(x,len(values)):
            if values[i] < min_value:
                min_idx = i
                min_value = values[i]
        values[x],values[min_idx] = values[min_idx], values[x]
        print(values)


if __name__ == "__main__":
    values = random_numbers(10)
    small = random_numbers(5,0,20)
    selection_sort(values)