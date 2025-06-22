#arthimetic operations using python in tkinter
import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get()) if entry1.get() != "Enter number" else 0
        num2 = float(entry2.get()) if entry2.get() != "Enter number" else 0
        op = operation_var.get()
        if op == "Add":
            result = num1 + num2
        elif op == "Subtract":
            result = num1 - num2
        elif op == "Multiply":
            result = num1 * num2
        elif op == "Divide":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            result_label.config(text="Unknown operation.")
            return
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # Handle the case where the input is not a number
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry1.insert(0, "Enter number")
        entry2.insert(0, "Enter number")
        entry1.config(fg="grey")
        entry2.config(fg="grey")
        result_label.config(text="Please enter valid numbers.")

def entry_placeholder(entry):
    def on_focus_in(event):
        if entry.get() == "Enter number":
            entry.delete(0, tk.END)
            entry.config(fg="black")
    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, "Enter number")
            entry.config(fg="grey")
    entry.insert(0, "Enter number")
    entry.config(fg="grey")
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Create the main window
root = tk.Tk()
root.title("Arithmetic Operations")
root.geometry("300x350")
root.configure(bg="white")

# set window display center of screen
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 350
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Entry 1
frame1 = tk.Frame(root, bg="white")
frame1.pack(pady=10, fill=tk.X, padx=20)
label1 = tk.Label(frame1, text="Enter first number:", bg="white", anchor="w")
label1.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry1 = tk.Entry(frame1, width=15, bg="white")
entry1.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)
entry_placeholder(entry1)

# Entry 2
frame2 = tk.Frame(root, bg="white")
frame2.pack(pady=10, fill=tk.X, padx=20)
label2 = tk.Label(frame2, text="Enter second number:", bg="white", anchor="w")
label2.pack(side=tk.LEFT, fill=tk.X, expand=True)
entry2 = tk.Entry(frame2, width=15, bg="white")
entry2.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)
entry_placeholder(entry2)

# Dropdown menu for operations
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0])
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.config(bg="#ADD8E6", fg="black", font=("Arial", 10, "bold"))
operation_menu.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Calculate", bg="#4CAF50", fg="white", command=calculate)
submit_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", bg="white", bd=1, relief="solid")
result_label.pack(pady=10, padx=5)

root.mainloop()
