import sqlite
import hashlib
import os
import gatepass
class Online_Shopping:
    def init.self_'('self')':
self.current_user=None
self.db name= "Njeru shop"
self.int.database()
self.load_products
def init.database(self):
conn=sqlite.connect(self.db_name)
cursor=conn.cursor()
cursor.execute()
conn.close()
print("database initialized")
def load.product(self):
conn=sqlite.connect(self.db_name)
cursor=conn.cursor()
cursor.execute("select count(*)from products")
product_count=cursor.fetchone()[0]
if product_count=o:
products=['charger',100,'earphones',50]
cursor.executemany(products)
conn.commit()
 print("products loaded") 
conn.close
def hash_password(self,password)
 return 
hashlib.sha256(password.encode()).hexdigest()
def register_user(self):
 print("/n==USER REGISTRATION")
 username=input("username;")
 password=getpass.getpass("Password;")
 cursor.execute(username,password)
 conn.commit()
 conn.close()
 print("Registration Successful")
 return True
except sqlite.IntegrityError:
print("Username exists")
return False
def display products(self):
conn= sqlite.connect(self.db name)
cursor=conn.cursor()
cursor.execute(SELECT* from products)
products=cursor.fetchall()
conn.close()
print("/n===available products")
for product in products:
 print(f"ID:{PRODUCT[0]}, {PRODUCT[1]}")
 return products
def add to cart(self):
if not self.current user:
print("please login")
return False
self.display_products()
try:
 product name=int(input("enter product name"))
 quantity=int(input(enter quantity))
 conn=sqlite.connect(self.db_name)
 cursor=conn.cursor()
 cursor.execute("select name from products")
 product=cursor.fetchone()
 if not product:
  print("not found")
  return False
 if product[1]<quantity:
  print("low on stock")
  return False
 cursor.execute(Insert into cart)
 (self.current user,product name,quantity)
conn.commit()
conn.close()
print("added {quantity}*{product[0]} to cart")
return True
except Valueerror:
print("invalid values")
return False
def view_cart(self):
 conn=sqlite.connect(self.db_name)
 cursor=conn.cursor()
 cursor.execute()
 cart items=fetchall()
 conn.close()
 if not cart_items:
 print("cart is empty")
 return None
total=0
for item in cart_items:
 item total=item[0]*100, item[1]*50
 total+=item_total
 print(f"{item[0]} *100 + {item[1]*KES 50}"=kes{item_total})
 print(f"/n TOTAL:KES{total}")
 return cart_items , total
def Mpesa Payment(amount, phone number)
print(f"/n ===Mpesa Payment)
      print(f"Amount:KES{amount}")
      print(f"phone{phone number}")
      try:
      mpesa pin=getpass.getpass("Enter Your Mpesa pin")
      if not mpesa pin=4
      or not mpesa pin.isdigit()
      print("Invalid Pin")
      return {"failed"}
      mpesa pin=0000
      return {"successful payment"}
      def checkout(self):
      cart info=self.view_cart()
      if not cart_info:
      return False
      cart_items, total= cart info
      print("checkout")
      if 
      payment method=Mpesa
      phone number=input("enter mpesa number")
      self.mpesa payment.stimulate_mpesa(phone number, total amount)
      payment result=self.mpesa payment.process_payment(total amount,phone number)
      print("THANK YOU FOR SHOPPING")


            
