# Tkinter is used to create the graphical user interface (GUI)
import tkinter as tk
from tkinter import *

# sqlite3 is used to connect and interact with the SQLite database
import sqlite3

# Import separate modules for CRUD operations
import AddProduct
import UpdateProduct
import DeleteProduct

# XML library used to parse and modify product XML data
import xml.etree.ElementTree as ET

# Decryption function for encrypted product names
from crypto_utils import decrypt_text


# Creates and returns a database connection
def connect_db():
    return sqlite3.connect("OnlineShopping.db")


# Main application window
root = tk.Tk()
root.title("Products")

# Make the window full screen
root.geometry("{0}x{1}+0+0".format(
    root.winfo_screenwidth(),
    root.winfo_screenheight()
))


# Main container frame
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Frame that holds the product table
top_frame = tk.Frame(content_frame)
top_frame.pack(side="left", anchor="n")

# Bottom frame for the Add Product button
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

# Right frame for Update and Delete buttons
right_frame = tk.Frame(content_frame)
right_frame.pack(side="left", anchor="n", padx=30)


# Class responsible for displaying products in a table format
class Table:
    def __init__(self, parent):
        self.parent = parent

        # Table column headers
        column_names = [
            'Product ID',
            'Category Name',
            'Product Name',
            'Price Per Unit',
            'Stock'
        ]

        # Create header row
        for j in range(total_columns):
            headercell = Entry(top_frame, width=20, font=('Arial', 16, 'bold'))
            headercell.grid(row=0, column=j)
            headercell.insert(END, column_names[j])

        # Populate table with product data
        for i in range(total_rows):
            for j in range(total_columns):
                tablecell = Entry(top_frame, width=20, font=('Arial', 16))
                tablecell.grid(row=i + 1, column=j)
                tablecell.insert(END, lst[i][j])


# Load products from the database
def load_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()

    # Decrypt product names before displaying
    return [
        (row[0], row[1], decrypt_text(row[2]), row[3], row[4])
        for row in rows
    ]


# Refresh the table after add/update/delete
def refresh_table():
    # Clear existing widgets
    for widget in top_frame.winfo_children():
        widget.destroy()

    global lst, total_rows, total_columns
    lst = load_products()

    if lst:
        total_rows = len(lst)
        total_columns = len(lst[0])
        Table(root)


# Initial table load
lst = load_products()
total_rows = len(lst)
total_columns = len(lst[0]) if total_rows > 0 else 0
Table(root)


# Open Add Product window
def open_window_add_product():
    AddProduct.open_add_product_window(root, refresh_table)


Button(
    bottom_frame,
    text="Add Product",
    command=open_window_add_product
).pack(pady=10)


# Open Update Product window
def open_window_update_product():
    UpdateProduct.open_update_product_window(root, refresh_table)


Button(
    right_frame,
    text="Update Product",
    width=15,
    command=open_window_update_product
).pack(side="left", padx=10, pady=30)


# Open Delete Product window
def open_window_delete_product():
    DeleteProduct.open_window_delete_product(root, refresh_table)


Button(
    right_frame,
    text="Delete Product",
    width=15,
    command=open_window_delete_product
).pack(side="left", padx=10, pady=30)


# Parse XML product details
def parse_product_xml(xml_data):
    xml_root = ET.fromstring(xml_data)
    return {
        "Supplier": xml_root.findtext("Supplier"),
        "Warranty": xml_root.findtext("Warranty"),
        "Origin": xml_root.findtext("Origin")
    }


# Load and display products including XML data
def load_products_with_xml():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT product_id, product_name, price_per_unit, product_xml
        FROM products
    """)
    rows = cursor.fetchall()
    conn.close()

    for row in rows:
        xml_info = parse_product_xml(row[3])
        print(
            row[0],
            decrypt_text(row[1]),
            row[2],
            xml_info["Supplier"],
            xml_info["Warranty"],
            xml_info["Origin"]
        )


# Update warranty value inside the XML field
def update_product_xml(product_id, new_warranty):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT product_xml FROM products WHERE product_id = ?",
        (product_id,)
    )

    xml_data = cursor.fetchone()[0]
    xml_root = ET.fromstring(xml_data)

    xml_root.find("Warranty").text = new_warranty

    updated_xml = ET.tostring(xml_root, encoding="unicode")

    cursor.execute("""
        UPDATE products
        SET product_xml = ?
        WHERE product_id = ?
    """, (updated_xml, product_id))

    conn.commit()
    conn.close()


# Start the GUI event loop
root.mainloop()
