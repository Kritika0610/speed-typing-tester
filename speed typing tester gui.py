import tkinter as tk
import time

sample = "The quick brown fox jumps over the lazy dog"

start_time = 0

def start_timer(event):
    global start_time

    if start_time == 0:
        start_time = time.time()

def submit_test(event=None):
    global start_time

    typed = text_box.get("1.0", tk.END).strip()

    end_time = time.time()

    time_taken = end_time - start_time

    words = len(typed.split())
    wpm = (words / time_taken) * 60

    correct = 0

    for i in range(min(len(sample), len(typed))):
        if sample[i] == typed[i]:
            correct += 1

    accuracy = (correct / len(sample)) * 100

    result.config(
        text=f"Time: {round(time_taken)} sec\n"
             f"WPM: {round(wpm)}\n"
             f"Accuracy: {round(accuracy)}%"
    )

    return "break"

root = tk.Tk()
root.title("Typing Speed Tester")
root.geometry("600x350")

tk.Label(root,
         text="Type the sentence below:",
         font=("Arial", 14)).pack(pady=10)

tk.Label(root,
         text=sample,
         wraplength=500).pack()

text_box = tk.Text(root,
                   height=5,
                   width=60)

text_box.pack(pady=20)

text_box.bind("<FocusIn>", start_timer)
text_box.bind("<Return>", submit_test)

result = tk.Label(root,
                  text="Click inside the box to begin",
                  font=("Arial", 12))

result.pack()

root.mainloop()
