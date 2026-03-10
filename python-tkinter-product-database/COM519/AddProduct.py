# Tkinter is used for GUI components
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# sqlite3 is used for database operations
import sqlite3

# Encryption function for securing product names
from crypto_utils import encrypt_text


# Global variables used across functions
selected_image_path = None
product_name_entry = None
price_entry = None
category_entry = None
stock_entry = None
window = None
refresh_callback = None


# Creates and returns a database connection
def connect_db():
    return sqlite3.connect("OnlineShopping.db")


# Opens the Add Product window
def open_add_product_window(parent, refresh_cb):
    global product_name_entry, price_entry, category_entry, stock_entry
    global window, refresh_callback

    refresh_callback = refresh_cb

    # Create new window
    window = tk.Toplevel(parent)
    window.title("Add Product")
    window.geometry("500x500")

    # Product name input
    tk.Label(window, text="Product Name").pack()
    product_name_entry = tk.Entry(window)
    product_name_entry.pack()

    # Price input
    tk.Label(window, text="Price per Unit").pack()
    price_entry = tk.Entry(window)
    price_entry.pack()

    # Category ID input
    tk.Label(window, text="Category ID").pack()
    category_entry = tk.Entry(window)
    category_entry.pack()

    # Stock input
    tk.Label(window, text="Stock").pack()
    stock_entry = tk.Entry(window)
    stock_entry.pack()

    # Buttons
    tk.Button(window, text="Add Product", command=save_product).pack(pady=20)
    tk.Button(
        window,
        text="Browse Files",
        command=lambda: open_add_file_explorer_window(window)
    ).pack(pady=20)


# Opens file explorer for selecting product image
def open_add_file_explorer_window(parent):
    dialog = tk.Toplevel(parent)
    dialog.title("File Explorer")
    dialog.geometry("500x300")

    label_file_explorer = Label(
        dialog,
        text="File Explorer using Tkinter",
        fg="blue"
    )
    label_file_explorer.pack(pady=20)

    Button(
        dialog,
        text="Browse Files",
        command=lambda: browse_image(label_file_explorer)
    ).pack(pady=20)

    Button(dialog, text="Exit", command=dialog.destroy).pack(pady=20)


# Opens file dialog and stores selected image path
def browse_image(label):
    global selected_image_path

    filename = filedialog.askopenfilename(
        title="Select image file",
        filetypes=(
            ("Image files", "*.png *.jpg *.jpeg"),
            ("All Files", "*.*")
        )
    )

    if filename:
        selected_image_path = filename
        label.configure(text="File Opened:\n" + filename)


# Converts image file to binary format for database storage
def convert_image_to_blob(image_path):
    with open(image_path, "rb") as file:
        return file.read()


# Validates user input fields
def validate_inputs():
    if not product_name_entry.get():
        messagebox.showerror("Error", "Please enter a product name.")
        return False

    try:
        float(price_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid price.")
        return False

    try:
        int(stock_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid stock number.")
        return False

    return True


# Saves a new product to the database
def save_product():
    if not validate_inputs():
        return

    if not selected_image_path:
        messagebox.showerror("Error", "Please select an image.")
        return

    # Encrypt product name
    encrypted_name = encrypt_text(product_name_entry.get())

    # Convert image to BLOB
    image_blob = convert_image_to_blob(selected_image_path)

    # Create XML metadata for the product
    def create_product_xml(supplier, warranty, origin):
        return f"""
        <ProductDetails>
            <Supplier>{supplier}</Supplier>
            <Warranty>{warranty}</Warranty>
            <Origin>{origin}</Origin>
        </ProductDetails>
        """

    product_xml = create_product_xml(
        supplier="Lucian's LTD",
        warranty="12 Months",
        origin="Romania"
    )

    # Insert product into database
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products
        (product_name, price_per_unit, category_id, stock, product_image, product_xml)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        encrypted_name,
        price_entry.get(),
        category_entry.get(),
        stock_entry.get(),
        image_blob,
        product_xml
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Product added with image.")

    # Refresh table and close window
    refresh_callback()
    window.destroy()
