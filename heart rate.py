import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# ================= LOGIC =================
def find_peak(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if ((mid == 0 or arr[mid] >= arr[mid - 1]) and
            (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1])):
            return arr[mid]

        elif mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

# ================= ANALYSIS =================
def analyze():
    try:
        arr = list(map(int, entry.get().split()))

        if not arr:
            raise ValueError

        peak = find_peak(arr)
        stress_index = peak ** 0.5

        # Classification
        if stress_index > 12:
            intensity = "Very High"
        elif stress_index > 9:
            intensity = "High"
        else:
            intensity = "Moderate"

        result_label.config(
            text=f"Peak: {peak} bpm\nStress Index: {round(stress_index,2)}\nIntensity: {intensity}",
            fg="#00ffcc"
        )

        # Store for graph
        global data
        data = arr

    except:
        messagebox.showerror("Error", "Enter valid numbers!")

# ================= GRAPH =================
def show_graph():
    if not data:
        messagebox.showerror("Error", "No data to display!")
        return

    plt.plot(data, marker='o')
    plt.title("Heart Rate During Workout")
    plt.xlabel("Time")
    plt.ylabel("Heart Rate (bpm)")
    plt.grid()
    plt.show()

# ================= GUI =================
root = tk.Tk()
root.title("⌚ Heart Rate Analyzer")
root.geometry("420x350")
root.configure(bg="#1e1e2f")

data = []

# Title
tk.Label(root, text="⌚ Heart Rate Analyzer",
         font=("Arial", 16, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Input
tk.Label(root, text="Enter heart-rate readings:",
         bg="#1e1e2f", fg="white").pack()

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Buttons
tk.Button(root, text="Analyze",
          command=analyze,
          bg="#4CAF50", fg="white").pack(pady=10)

tk.Button(root, text="Show Graph",
          command=show_graph,
          bg="#2196F3", fg="white").pack(pady=5)

# Result
result_label = tk.Label(root,
                        text="",
                        font=("Arial", 12, "bold"),
                        bg="#1e1e2f", fg="white")
result_label.pack(pady=15)

# Footer
tk.Label(root, text="AI-Based Fitness Analyzer",
         bg="#1e1e2f", fg="gray").pack(side="bottom", pady=5)

root.mainloop()
