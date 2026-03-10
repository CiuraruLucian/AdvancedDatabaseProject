# Tkinter is used to create the GUI window and dialogs
import tkinter as tk
from tkinter import messagebox

# sqlite3 is used to interact with the SQLite database
import sqlite3

# Encryption function for protecting sensitive product names
from crypto_utils import encrypt_text


# Creates and returns a database connection
def connect_db():
    return sqlite3.connect("OnlineShopping.db")


# Updates an existing product in the database
def update_product(
        product_id_entry,
        category_entry,
        product_name_entry,
        price_entry,
        stock_entry,
        refresh_callback,
        window
):
    # Retrieve user input from entry fields
    product_id = product_id_entry.get()
    category_id = category_entry.get()
    product_name = encrypt_text(product_name_entry.get())
    price = price_entry.get()
    stock = stock_entry.get()

    # Connect to the database
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to update product details
    cursor.execute("""
        UPDATE products
        SET product_name   = ?,
            price_per_unit = ?,
            category_id    = ?,
            stock          = ?
        WHERE product_id = ?
    """, (product_name, price, category_id, stock, product_id))

    # Save changes and close connection
    conn.commit()
    conn.close()

    # Inform user of success
    messagebox.showinfo("Success", "Product updated successfully.")

    # Refresh product table in main window
    refresh_callback()

    # Close update window
    window.destroy()


# Opens the Update Product window
def open_update_product_window(parent, refresh_callback):
    # Create a new window on top of the main application
    window = tk.Toplevel(parent)
    window.title("Update Product")
    window.geometry("500x500")

    # Product ID input
    tk.Label(window, text="Product ID").pack()
    product_id_entry = tk.Entry(window)
    product_id_entry.pack()

    # Category ID input
    tk.Label(window, text="Category ID").pack()
    category_entry = tk.Entry(window)
    category_entry.pack()

    # Product name input
    tk.Label(window, text="Product Name").pack()
    product_name_entry = tk.Entry(window)
    product_name_entry.pack()

    # Price input
    tk.Label(window, text="Price per Unit").pack()
    price_entry = tk.Entry(window)
    price_entry.pack()

    # Stock input
    tk.Label(window, text="Stock").pack()
    stock_entry = tk.Entry(window)
    stock_entry.pack()

    # Button to save updated product
    tk.Button(
        window,
        text="Save Update",
        command=lambda: update_product(
            product_id_entry,
            category_entry,
            product_name_entry,
            price_entry,
            stock_entry,
            refresh_callback,
            window
        )
    ).pack(pady=10)
