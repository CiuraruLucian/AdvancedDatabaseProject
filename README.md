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
# C. The process of creating the database :

**Creating the flat file**
<img width="940" height="131" alt="image" src="https://github.com/user-attachments/assets/7e076783-a259-4c02-9261-f0d7bef6f991" />
**1 NF**
<img width="1070" height="116" alt="image" src="https://github.com/user-attachments/assets/82435b21-e807-4932-9e1b-dce9ad7e3688" />
**2 NF** 
<img width="940" height="305" alt="image" src="https://github.com/user-attachments/assets/0e6e2a32-de50-4707-8eb1-be412f08d94a" />
**3 NF**
<img width="940" height="347" alt="image" src="https://github.com/user-attachments/assets/2bd71043-fd91-452d-a1fd-8ebd60f92343" />
**ERD**
<img width="940" height="582" alt="image" src="https://github.com/user-attachments/assets/2d77fd3d-f232-4ed9-aea9-635dcb9fe5e4" />
**Data Diagram**
<img width="940" height="573" alt="image" src="https://github.com/user-attachments/assets/44b42500-8824-4ecb-9971-219e7b4c399c" />

------
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
