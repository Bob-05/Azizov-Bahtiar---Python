import tkinter as tk
from tkinter import ttk


def create_register_form():
    root = tk.Tk()
    root.title("Elegant Login and Register forms")

    # Main title
    title_label = ttk.Label(root, text="Elegant Login and Register forms", font=('Helvetica', 14, 'bold'))
    title_label.pack(pady=10)

    # Section title
    section_label = ttk.Label(root, text="1. Register", font=('Helvetica', 12))
    section_label.pack(pady=5)

    # Create a frame for the form
    form_frame = ttk.Frame(root, padding="20")
    form_frame.pack()

    # Form fields
    fields = [
        "First Name",
        "Last Name",
        "Email Address",
        "User Name",
        "Password-1",
        "Password-2",
    ]

    entries = []
    for field in fields:
        frame = ttk.Frame(form_frame)
        frame.pack(fill='x', pady=2)

        label = ttk.Label(frame, text=f"- {field}", width=20, anchor='w')
        label.pack(side='left')

        entry = ttk.Entry(frame)
        entry.pack(side='left', fill='x', expand=True)
        entries.append(entry)

    # Checkbox
    checkbox_frame = ttk.Frame(form_frame)
    checkbox_frame.pack(fill='x', pady=10)

    checkbox_var = tk.IntVar()
    checkbox = ttk.Checkbutton(checkbox_frame, text="- I agree to the Terms and Conditions", variable=checkbox_var)
    checkbox.pack(anchor='w')

    # Button
    button_frame = ttk.Frame(form_frame)
    button_frame.pack(fill='x', pady=10)

    button = ttk.Button(button_frame, text="Sign Me Up >", command=lambda: print("Register clicked"))
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    create_register_form()