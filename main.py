import tkinter as tk
from tkinter import messagebox, ttk
from password_generator.generate_password import generate_password, update_strength_indicator
from password_generator.save_password import save_password
from password_generator.expiration_reminder import set_expiration_reminder

def validate_inputs():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        min_letters = int(min_letters_entry.get()) if letters_var.get() else 0
        min_digits = int(min_digits_entry.get()) if digits_var.get() else 0
        min_punctuation = int(min_punctuation_entry.get()) if punctuation_var.get() else 0

        if length < (min_letters + min_digits + min_punctuation):
            raise ValueError("Password length should be at least the sum of minimum counts for each character type.")
        
        return length, min_letters, min_digits, min_punctuation
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))
        return None

def on_generate():
    inputs = validate_inputs()
    if inputs:
        length, min_letters, min_digits, min_punctuation = inputs
        use_letters = letters_var.get()
        use_digits = digits_var.get()
        use_punctuation = punctuation_var.get()

        password = generate_password(length, use_letters, use_digits, use_punctuation, min_letters, min_digits, min_punctuation)
        result_label.config(text=f"Generated password: {password}")
        update_strength_indicator(password, strength_label)
        update_strength_bar(password)
        set_expiration_reminder()

def on_copy():
    try:
        password = result_label.cget("text").split(": ")[1]
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    except IndexError:
        messagebox.showerror("Copy Error", "No password to copy.")

def on_save():
    try:
        password = result_label.cget("text").split(": ")[1]
        if password:
            save_password(password)
            messagebox.showinfo("Saved", "Password saved to passwords.txt")
    except IndexError:
        messagebox.showerror("Save Error", "No password to save.")

def toggle_min_fields(*args):
    min_letters_label.grid() if letters_var.get() else min_letters_label.grid_remove()
    min_letters_entry.grid() if letters_var.get() else min_letters_entry.grid_remove()
    
    min_digits_label.grid() if digits_var.get() else min_digits_label.grid_remove()
    min_digits_entry.grid() if digits_var.get() else min_digits_entry.grid_remove()
    
    min_punctuation_label.grid() if punctuation_var.get() else min_punctuation_label.grid_remove()
    min_punctuation_entry.grid() if punctuation_var.get() else min_punctuation_entry.grid_remove()

def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip.wm_geometry("+0+0")
    label = tk.Label(tooltip, text=text, background="lightyellow", relief="solid", borderwidth=1, wraplength=200)
    label.pack()
    tooltip.withdraw()

    def on_enter(event):
        x, y, _, _ = widget.bbox("insert")
        x += widget.winfo_rootx() + 25
        y += widget.winfo_rooty() + 25
        tooltip.wm_geometry(f"+{x}+{y}")
        tooltip.deiconify()

    def on_leave(event):
        tooltip.withdraw()

    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

def calculate_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_punctuation = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/~`" for c in password)
    
    strength = 0
    if length >= 12:
        strength += 5
    elif length >= 8:
        strength += 4
    elif length >= 5:
        strength += 2
    else:
        strength += 1
    
    if has_upper:
        strength += 2
    if has_lower:
        strength += 2
    if has_digits:
        strength += 2
    if has_punctuation:
        strength += 2
    
    return strength

def update_strength_bar(password):
    strength = calculate_strength(password)
    print(f"Password strength: {strength}")  # Debug print to check strength value
    strength_bar['value'] = strength
    if strength < 5:
        strength_bar['style'] = 'Red.Horizontal.TProgressbar'
    elif strength < 10:
        strength_bar['style'] = 'Yellow.Horizontal.TProgressbar'
    else:
        strength_bar['style'] = 'Green.Horizontal.TProgressbar'

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Add padding to the main window
root.configure(padx=10, pady=10)

# Create and place widgets
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

instructions_label = tk.Label(root, text="Fill in the details below to generate a secure password.")
instructions_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

# Create frames for better organization
length_frame = tk.Frame(root)
length_frame.grid(row=2, column=0, columnspan=2, pady=(0, 10))

options_frame = tk.Frame(root)
options_frame.grid(row=3, column=0, columnspan=2, pady=(0, 10))

min_counts_frame = tk.Frame(root)
min_counts_frame.grid(row=4, column=0, columnspan=2, pady=(0, 10))

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=5, column=0, columnspan=2, pady=(0, 10))

result_frame = tk.Frame(root)
result_frame.grid(row=6, column=0, columnspan=2, pady=(0, 10))

strength_frame = tk.Frame(root)
strength_frame.grid(row=7, column=0, columnspan=2, pady=(0, 10))

# Length input
tk.Label(length_frame, text="Password Length:").grid(row=0, column=0, sticky="e")
length_entry = tk.Entry(length_frame)
length_entry.grid(row=0, column=1)
create_tooltip(length_entry, "Enter the desired length of the password.")

# Options
letters_var = tk.BooleanVar(value=True)
letters_var.trace_add("write", toggle_min_fields)
tk.Checkbutton(options_frame, text="Include Letters", variable=letters_var).grid(row=0, column=0, sticky="w")

digits_var = tk.BooleanVar(value=True)
digits_var.trace_add("write", toggle_min_fields)
tk.Checkbutton(options_frame, text="Include Digits", variable=digits_var).grid(row=1, column=0, sticky="w")

punctuation_var = tk.BooleanVar(value=True)
punctuation_var.trace_add("write", toggle_min_fields)
tk.Checkbutton(options_frame, text="Include Punctuation", variable=punctuation_var).grid(row=2, column=0, sticky="w")

# Minimum counts
min_letters_label = tk.Label(min_counts_frame, text="Minimum Letters:")
min_letters_label.grid(row=0, column=0, sticky="e")
min_letters_entry = tk.Entry(min_counts_frame)
min_letters_entry.grid(row=0, column=1)

min_digits_label = tk.Label(min_counts_frame, text="Minimum Digits:")
min_digits_label.grid(row=1, column=0, sticky="e")
min_digits_entry = tk.Entry(min_counts_frame)
min_digits_entry.grid(row=1, column=1)

min_punctuation_label = tk.Label(min_counts_frame, text="Minimum Punctuation:")
min_punctuation_label.grid(row=2, column=0, sticky="e")
min_punctuation_entry = tk.Entry(min_counts_frame)
min_punctuation_entry.grid(row=2, column=1)

# Buttons
generate_button = tk.Button(buttons_frame, text="Generate Password", command=on_generate)
generate_button.grid(row=0, column=0, padx=5)

copy_button = tk.Button(buttons_frame, text="Copy to Clipboard", command=on_copy)
copy_button.grid(row=0, column=1, padx=5)

save_button = tk.Button(buttons_frame, text="Save Password", command=on_save)
save_button.grid(row=0, column=2, padx=5)

# Result
result_label = tk.Label(result_frame, text="", font=("Helvetica", 12, "bold"))
result_label.grid(row=0, column=0, columnspan=2, pady=(10, 0))

# Strength indicator
strength_label = tk.Label(strength_frame, text="Password Strength: ")
strength_label.grid(row=0, column=0, columnspan=2)

# Add a progress bar for password strength
style = ttk.Style()
style.theme_use('default')
style.configure("Red.Horizontal.TProgressbar", foreground='red', background='red')
style.configure("Yellow.Horizontal.TProgressbar", foreground='yellow', background='yellow')
style.configure("Green.Horizontal.TProgressbar", foreground='green', background='green')

strength_bar = ttk.Progressbar(strength_frame, length=200, mode='determinate', maximum=13)
strength_bar.grid(row=1, column=0, columnspan=2)

# Initialize the dynamic fields
toggle_min_fields()

# Run the application
root.mainloop()
