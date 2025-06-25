import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test_db"
)
cursor = conn.cursor()

# ---------- CREATE ----------
def add_product(name, price, stock):
    sql = "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, price, stock))
    conn.commit()
    print(f"[CREATE] Added product: {name}")

# ---------- READ ----------
def read_products():
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    print("[READ] All products:")
    for row in results:
        print(row)

# ---------- UPDATE ----------
def update_product(product_id, name, price, stock):
    sql = "UPDATE products SET name=%s, price=%s, stock=%s WHERE id=%s"
    cursor.execute(sql, (name, price, stock, product_id))
    conn.commit()
    print(f"[UPDATE] Product ID {product_id} updated.")

# ---------- DELETE ----------
def delete_product(product_id):
    sql = "DELETE FROM products WHERE id=%s"
    cursor.execute(sql, (product_id,))
    conn.commit()
    print(f"[DELETE] Product ID {product_id} deleted.")

# ---------- DEMO FLOW ----------
add_product("Mouse", 499.99, 100)
add_product("Keyboard", 899.50, 50)

read_products()

update_product(1, "Wireless Mouse", 599.99, 90)

delete_product(2)

read_products()

# Cleanup
cursor.close()
conn.close()
