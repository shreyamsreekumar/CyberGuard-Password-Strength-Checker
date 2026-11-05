import tkinter as tk
import re
import math
import string

# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("520x600")
root.configure(bg="#0b1120")
root.resizable(False, False)

# Colors
BG = "#0b1120"
CARD = "#172033"
ACCENT = "#00e5c3"
TEXT = "#ffffff"
MUTED = "#cbd5e1"

# Heading
title_label = tk.Label(
    root,
    text="PASSWORD STRENGTH CHECKER",
    font=("Arial", 18, "bold"),
    bg=BG,
    fg=ACCENT
)
title_label.pack(pady=(25, 10))

# Instructions
instruction_label = tk.Label(
    root,
    text="Check how strong your password is",
    font=("Arial", 11),
    bg=BG,
    fg=MUTED
)
instruction_label.pack(pady=8)

# Password input
password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14),
    show="*",
    bg=CARD,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat"
)
password_entry.pack(pady=15, ipady=8)

# Show/hide password
show_password = tk.BooleanVar(value=False)


def toggle_password():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


show_check = tk.Checkbutton(
    root,
    text="Show password",
    variable=show_password,
    command=toggle_password,
    bg=BG,
    fg=MUTED,
    selectcolor=CARD,
    activebackground=BG,
    activeforeground=TEXT
)
show_check.pack()

# Strength meter
strength_label = tk.Label(
    root,
    text="Password strength: Not checked",
    font=("Arial", 12, "bold"),
    bg=BG,
    fg=TEXT
)
strength_label.pack(pady=(20, 8))

strength_bar = tk.Canvas(
    root,
    width=350,
    height=14,
    bg=CARD,
    highlightthickness=0
)
strength_bar.pack()

bar = strength_bar.create_rectangle(
    0, 0, 0, 14,
    fill=ACCENT,
    width=0
)

# Feedback
feedback_label = tk.Label(
    root,
    text="Enter a password and click CHECK STRENGTH",
    font=("Arial", 10),
    bg=BG,
    fg=MUTED,
    wraplength=430
)
feedback_label.pack(pady=15)


def check_password():
    password = password_entry.get()

    if not password:
        strength_label.config(
            text="Password strength: Not checked",
            fg=TEXT
        )
        feedback_label.config(
            text="Please enter a password.",
            fg="#ff6b6b"
        )
        strength_bar.coords(bar, 0, 0, 0, 14)
        return

    score = 0
    suggestions = []

    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1

    # Character variety
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Common password checks
    common_passwords = {
        "password",
        "password123",
        "12345678",
        "qwerty123",
        "admin123"
    }

    if password.lower() in common_passwords:
        score = 0
        suggestions = [
            "Avoid common passwords. Choose a unique password."
        ]

    # Check for repeated characters
    if len(password) >= 4 and len(set(password)) == 1:
        score = 0
        suggestions = [
            "Avoid passwords made from one repeated character."
        ]

    # Strength levels
    if score <= 2:
        level = "WEAK"
        color = "#ff4d6d"
        width = 100

    elif score <= 4:
        level = "MEDIUM"
        color = "#ffbd4a"
        width = 225

    else:
        level = "STRONG"
        color = "#00e5c3"
        width = 350

    strength_label.config(
        text=f"Password strength: {level}",
        fg=color
    )

    strength_bar.itemconfig(bar, fill=color)
    strength_bar.coords(bar, 0, 0, width, 14)

    if suggestions:
        feedback_label.config(
            text="Suggestions:\n• " + "\n• ".join(suggestions),
            fg=MUTED
        )
    else:
        feedback_label.config(
            text="Good character variety and length!",
            fg=ACCENT
        )


# Check button
check_button = tk.Button(
    root,
    text="CHECK STRENGTH",
    font=("Arial", 11, "bold"),
    bg=ACCENT,
    fg=BG,
    activebackground="#00b89c",
    activeforeground=TEXT,
    relief="flat",
    cursor="hand2",
    command=check_password
)
check_button.pack(pady=15, ipadx=20, ipady=8)

# Clear button
def clear_fields():
    password_entry.delete(0, tk.END)
    strength_label.config(
        text="Password strength: Not checked",
        fg=TEXT
    )
    feedback_label.config(
        text="Enter a password and click CHECK STRENGTH",
        fg=MUTED
    )
    strength_bar.coords(bar, 0, 0, 0, 14)
    show_password.set(False)
    password_entry.config(show="*")


clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 10),
    bg=CARD,
    fg=TEXT,
    activebackground="#263449",
    relief="flat",
    cursor="hand2",
    command=clear_fields
)
clear_button.pack(pady=5, ipadx=25, ipady=5)

# Footer
footer = tk.Label(
    root,
    text="Cybersecurity Beginner Project | Python + Tkinter",
    font=("Arial", 9),
    bg=BG,
    fg="#64748b"
)
footer.pack(side="bottom", pady=15)

# Run application
root.mainloop()