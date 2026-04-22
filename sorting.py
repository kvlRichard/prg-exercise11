import random
import matplotlib.pyplot as plt

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

def bubble_sort(values_list):
    values = values_list.copy()
    plt.ion()
    plt.show()
    for j in range(len(values)):

        for i in range(0,len(values)-j-1):
            index_highlight1 = i
            index_highlight2 = i + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if values[i] > values[i+1]:
                values[i],values[i+1] = values[i+1],values[i]

    plt.ioff()
    plt.show()
    return values






if __name__ == "__main__":
    values = random_numbers(10)
    small = random_numbers(5,0,20)
    #selection_sort(values)
    print(bubble_sort(values))