import tkinter as tk
from tkinter import messagebox
from password_generator.generate_password import generate_password, update_strength_indicator
from password_generator.save_password import save_password
from password_generator.expiration_reminder import set_expiration_reminder

def on_generate():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_digits = digits_var.get()
        use_punctuation = punctuation_var.get()
        
        min_letters = int(min_letters_entry.get()) if use_letters and (use_digits or use_punctuation) else 0
        min_digits = int(min_digits_entry.get()) if use_digits and (use_letters or use_punctuation) else 0
        min_punctuation = int(min_punctuation_entry.get()) if use_punctuation and (use_letters or use_digits) else 0

        # Ensure minimum values are zero if the corresponding checkbox is unchecked
        if not use_letters:
            min_letters = 0
        if not use_digits:
            min_digits = 0
        if not use_punctuation:
            min_punctuation = 0

        if length < (min_letters + min_digits + min_punctuation):
            messagebox.showerror("Input Error", "Password length should be at least the sum of minimum counts for each character type.")
            return

        password = generate_password(length, use_letters, use_digits, use_punctuation, min_letters, min_digits, min_punctuation)
        result_label.config(text=f"Generated password: {password}")
        update_strength_indicator(password, strength_label)
        set_expiration_reminder()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def on_copy():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").split(": ")[1])
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def on_save():
    password = result_label.cget("text").split(": ")[1]
    if password:
        save_password(password)
        messagebox.showinfo("Saved", "Password saved to passwords.txt")

def toggle_min_fields(*args):
    if letters_var.get() and (digits_var.get() or punctuation_var.get()):
        min_letters_label.grid()
        min_letters_entry.grid()
    else:
        min_letters_label.grid_remove()
        min_letters_entry.grid_remove()

    if digits_var.get() and (letters_var.get() or punctuation_var.get()):
        min_digits_label.grid()
        min_digits_entry.grid()
    else:
        min_digits_label.grid_remove()
        min_digits_entry.grid_remove()

    if punctuation_var.get() and (letters_var.get() or digits_var.get()):
        min_punctuation_label.grid()
        min_punctuation_entry.grid()
    else:
        min_punctuation_label.grid_remove()
        min_punctuation_entry.grid_remove()

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place widgets
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

letters_var = tk.BooleanVar(value=True)
letters_var.trace_add("write", toggle_min_fields)
tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, columnspan=2)

digits_var = tk.BooleanVar(value=True)
digits_var.trace_add("write", toggle_min_fields)
tk.Checkbutton(root, text="Include Digits", variable=digits_var).grid(row=2, column=0, columnspan=2)

punctuation_var = tk.BooleanVar(value=True)
punctuation_var.trace_add("write", toggle_min_fields)
tk.Checkbutton(root, text="Include Punctuation", variable=punctuation_var).grid(row=3, column=0, columnspan=2)

min_letters_label = tk.Label(root, text="Minimum Letters:")
min_letters_label.grid(row=4, column=0)
min_letters_entry = tk.Entry(root)
min_letters_entry.grid(row=4, column=1)

min_digits_label = tk.Label(root, text="Minimum Digits:")
min_digits_label.grid(row=5, column=0)
min_digits_entry = tk.Entry(root)
min_digits_entry.grid(row=5, column=1)

min_punctuation_label = tk.Label(root, text="Minimum Punctuation:")
min_punctuation_label.grid(row=6, column=0)
min_punctuation_entry = tk.Entry(root)
min_punctuation_entry.grid(row=6, column=1)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.grid(row=7, column=0, columnspan=2)

copy_button = tk.Button(root, text="Copy to Clipboard", command=on_copy)
copy_button.grid(row=8, column=0, columnspan=2)

save_button = tk.Button(root, text="Save Password", command=on_save)
save_button.grid(row=9, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=2)

strength_label = tk.Label(root, text="Password Strength: ")
strength_label.grid(row=11, column=0, columnspan=2)

# Initialize the dynamic fields
toggle_min_fields()

# Run the application
root.mainloop()
