# Tkinter is used for GUI elements and dialog boxes
import tkinter as tk
from tkinter import messagebox

# sqlite3 is used to connect to the database
import sqlite3


# Creates and returns a database connection
def connect_db():
    return sqlite3.connect("OnlineShopping.db")


# Deletes a product from the database
def delete_product(product_id_entry, refresh_callback, window):
    # Get product ID from input field
    product_id = product_id_entry.get()

    # Validate input
    if not product_id:
        messagebox.showerror("Error", "Product ID not found.")
        return

    # Ask user for confirmation before deleting
    confirm = messagebox.askyesno(
        "Confirmation",
        "Are you sure you want to delete this product?"
    )
    if not confirm:
        return

    # Connect to database
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to delete the product
    cursor.execute(
        "DELETE FROM products WHERE product_id = ?",
        (product_id,)
    )

    # Save changes and close connection
    conn.commit()
    conn.close()

    # Notify user of success
    messagebox.showinfo("Success", "Product deleted.")

    # Refresh the main product table
    refresh_callback()

    # Close delete window
    window.destroy()


# Opens the Delete Product window
def open_window_delete_product(parent, refresh_callback):
    # Create a new popup window
    window = tk.Toplevel(parent)
    window.title("Delete Product")
    window.geometry("500x500")

    # Product ID input
    tk.Label(window, text="Product ID").pack()
    product_id_entry = tk.Entry(window)
    product_id_entry.pack()

    # Delete button
    tk.Button(
        window,
        text="Delete Product",
        fg="red",
        command=lambda: delete_product(
            product_id_entry,
            refresh_callback,
            window
        )
    ).pack(pady=20)
