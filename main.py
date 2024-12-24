import time
import matplotlib.pyplot as plt
from tabulate import tabulate

coffee_shops = [
    {
        "Nama Kafe": "et al Coffee Purwokerto",
        "Rating Kafe": 4.9,
       
    },
    {
        "Nama Kafe": "Colony Coffee",
        "Rating Kafe": 4.6,
    },
    {
        "Nama Kafe": "Lav Cafe Purwokerto",
        "Rating Kafe": 4.8,
    },
    {
        "Nama Kafe": "Arasta Alpha",
        "Rating Kafe": 4.0,
    },
    {
        "Nama Kafe": "Angkringan Sangkara",
        "Rating Kafe": 3.7,
    },
    {
        "Nama Kafe": "Irman Coffe",
        "Rating Kafe": 3.1,
    },
    {
        "Nama Kafe": "Ruang Temu Coffe & Space",
        "Rating Kafe": 4.7,
    },
    {
        "Nama Kafe": "Langitan",
        "Rating Kafe": 3.0,
    },
    {
        "Nama Kafe": "Kopi Bintang",
        "Rating Kafe": 4.5,
    },
    {
        "Nama Kafe": "ROBOKOP",
        "Rating Kafe": 4.3,
    },
    {
        "Nama Kafe": "Kopi Kenangan",
        "Rating Kafe": 4.4,
    },
    {
        "Nama Kafe": "Loja De Cafe",
        "Rating Kafe": 4.1,
    },
]

# Iterative Sort (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]["Rating Kafe"] < arr[j+1]["Rating Kafe"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Recursive Sort (Selection Sort)
def selection_sort(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr

    max_idx = 0
    for i in range(1, n):
        if arr[i]["Rating Kafe"] > arr[max_idx]["Rating Kafe"]:
            max_idx = i

    arr[max_idx], arr[n-1] = arr[n-1], arr[max_idx]
    selection_sort(arr, n-1)
    return arr

def measure_time(sort_func, data):
    start = time.time()
    sorted_data = sort_func(data.copy())
    end = time.time()
    return sorted_data, end - start

iter_sorted, iter_time = measure_time(bubble_sort, coffee_shops)
recur_sorted, recur_time = measure_time(selection_sort, coffee_shops)

# Display Results (Table Format)
iter_table = [[shop["Nama Kafe"], shop["Rating Kafe"]] for shop in iter_sorted]
recur_table = [[shop["Nama Kafe"], shop["Rating Kafe"]] for shop in recur_sorted]

print("\nIterative Sort Result:")
print(tabulate(iter_table, headers=["Nama Kafe", "Rating Kafe"], tablefmt="grid"))

print("\nRecursive Sort Result:")
print(tabulate(recur_table, headers=["Nama Kafe", "Rating Kafe"], tablefmt="grid"))

# Performance Comparison Table
data = [["Iterative Sort", iter_time], ["Recursive Sort", recur_time]]
headers = ["Sort Method", "Execution Time (s)"]
print("\nPerformance Comparison:")
print(tabulate(data, headers=headers, tablefmt="grid"))

# Plotting
labels = [shop["Nama Kafe"] for shop in iter_sorted]
ratings_iter = [shop["Rating Kafe"] for shop in iter_sorted]
ratings_recur = [shop["Rating Kafe"] for shop in recur_sorted]

plt.figure(figsize=(10, 5))
plt.plot(labels, ratings_iter, label="Iterative Sort", marker='o')
plt.plot(labels, ratings_recur, label="Recursive Sort", marker='x')
plt.title("Coffee Shop Ratings - Iterative vs Recursive Sort")
plt.xlabel("Nama Kafe")
plt.ylabel("Rating Kafe")
plt.legend()
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()