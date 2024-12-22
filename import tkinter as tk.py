import tkinter as tk

# Function to handle button clicks
def on_button_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())  # Evaluate the expression in the entry widget
            entry.delete(0, tk.END)    # Clear the entry widget
            entry.insert(tk.END, str(result))  # Display the result
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")  # Handle invalid expressions
    elif button_text == "C":
        entry.delete(0, tk.END)  # Clear the entry widget
    else:
        entry.insert(tk.END, button_text)  # Add button text to the entry widget

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x450")  # Set the window size

# Entry widget for displaying calculations
entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Button labels in a 4x4 grid
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create buttons dynamically
row = 1
col = 0
for button_text in buttons:
    button = tk.Button(
        root, text=button_text, font=("Arial", 18),
        padx=20, pady=20, command=lambda text=button_text: on_button_click(text)
    )
    button.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:  # Move to the next row after 4 buttons
        col = 0
        row += 1

# Run the application
root.mainloop()
