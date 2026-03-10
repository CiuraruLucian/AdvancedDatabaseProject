Project Usage Guide

# A. Setup Instructions

## Step 1:

Unzip the project folder.

## Step 2:

Open the COM519 project folder in PyCharm.

## Step 3:

The project contains the following files:

index.py

AddProduct.py

UpdateProduct.py

DeleteProduct.py

crypto_utils.py

## Step 4:

Set up your Python interpreter:

In PyCharm, go to File > Settings > Project: COM519 > Python Interpreter.

Click the gear icon, then Add....

Select Virtualenv Environment.

If a .venv folder already exists, choose Select existing interpreter and browse to the .venv\Scripts\python.exe file inside the project folder.

If no .venv exists, generate a new one using Python 3.13 (or your installed version).

## Step 5:

Install project dependencies by running in the terminal:

python -m pip install -r requirements.txt

If the cryptography package is not included in requirements.txt, install it separately:

python -m pip install cryptography

## Step 6:

Run the index.py file to start the application.
---------
# B. Application Overview

After running the program, a main window will appear displaying:

A table containing all available products.

Three buttons:

Add Product

Update Product

Delete Product

------
## C. The Process of Creating the Database

### **1. Creating the Flat File**  
Start by gathering all the raw data into a single flat file, which will serve as the foundation for normalization.  

![Flat File](https://github.com/user-attachments/assets/7e076783-a259-4c02-9261-f0d7bef6f991)

---

### **2. First Normal Form (1NF)**  
Organize the data so that each column contains atomic values and each row is unique. This eliminates repeating groups and ensures consistency.  

![1NF](https://github.com/user-attachments/assets/82435b21-e807-4932-9e1b-dce9ad7e3688)

---

### **3. Second Normal Form (2NF)**  
Ensure that all non-key attributes are fully functionally dependent on the primary key. This step removes partial dependencies and reduces redundancy.  

![2NF](https://github.com/user-attachments/assets/0e6e2a32-de50-4707-8eb1-be412f08d94a)

---

### **4. Third Normal Form (3NF)**  
Remove transitive dependencies so that every non-key attribute depends only on the primary key. This helps maintain data integrity and simplifies updates.  

![3NF](https://github.com/user-attachments/assets/2bd71043-fd91-452d-a1fd-8ebd60f92343)

---

### **5. Entity-Relationship Diagram (ERD)**  
Visualize the structure of the database, showing entities, attributes, and relationships to clarify how tables are connected.  

![ERD](https://github.com/user-attachments/assets/2d77fd3d-f232-4ed9-aea9-635dcb9fe5e4)

---

### **6. Data Diagram**  
Provide a final overview of the normalized database, showing tables, keys, and relationships for easy reference.  

![Data Diagram](https://github.com/user-attachments/assets/44b42500-8824-4ecb-9971-219e7b4c399c)

---

# D. How to Use the Application

## Add a Product

Click the Add Product button.

Fill in the required product details.

Click Browse Files and select a file (you may use the example file provided).

Click the Add Product button again to confirm.

If successful, you will see the message:
"Product added successfully."

## Update a Product

Click the Update Product button (top-right).

Enter the product details you want to modify.

Click Save Update.

If successful, you will see:
"Product updated successfully."

The updated information will appear in both:

The table

The database

## Delete a Product

Click the Delete Product button (top-right).

Enter the Product ID of the product you want to delete.

Confirm the deletion when prompted.

If successful, you will see:
"Product deleted successfully."

The product will be removed from both:

The table

The database
