import mysql.connector as mys
import random 



mycon=mys.connect(host='localhost',user='root',passwd='harsh',database='oasis')
if (mycon.is_connected()):
    print("=============================================================")
    print("Connected To the Sql")
    print("=============================================================")



def get_admin_details(admin_id):
    admin_details_cursor = mycon.cursor()
    admin_details_cursor.execute("select * from administrator where admin_id=%s", (admin_id,))
    admin_details = admin_details_cursor.fetchone()
    print("=============================================================")
    print("Admin Details")
    print("Admin ID: ", admin_details[0])
    print("Admin First Name: ", admin_details[1])
    print("Admin Middle Name: ", admin_details[2])
    print("Admin Last Name: ", admin_details[3])
    print("Admin Phone Number: ", admin_details[4])
    print("Admin Email: ", admin_details[5])
    print("=============================================================")
    return 0

def print_product_admin():
    print("=============================================================")
    print("What do you Want")
    print("1. Print all products")
    print("2. Print a particular product")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("=============================================================")
        print("Product Details")
        product_details_cursor = mycon.cursor()
        product_details_cursor.execute("select * from product")
        product_details = product_details_cursor.fetchall()
        for product in product_details:
            print("Product ID: ", product[0])
            print("Product Price: ", product[1])
            print("Product Discount: ", product[2])
            print("Product Quantity: ", product[3])
            print("Product Weight: ", product[4])
            print("Product User Rating: ", product[5])
            print("Product Brand ID: ", product[6])
            print("Product Category ID: ", product[7])
            print("=============================================================")
    elif option == 2:
        product_id = int(input("Enter the product id: "))
        product_details_cursor = mycon.cursor()
        product_details_cursor.execute("select * from product where product_id=%s", (product_id,))
        product_details = product_details_cursor.fetchone()
        print("=============================================================")
        print("Product Details")
        print("Product ID: ", product_details[0])
        print("Product Price: ", product_details[1])
        print("Product Discount: ", product_details[2])
        print("Product Quantity: ", product_details[3])
        print("Product Weight: ", product_details[4])
        print("Product User Rating: ", product_details[5])
        print("Product Brand ID: ", product_details[6])
        print("Product Category ID: ", product_details[7])
        print("=============================================================")
    else:
        print("Invalid Choice")
    return 0


def add_product_admin():
    # check for brand id and category id exist or not 
    print("Add Product Details")
    print("Enter the product details")
    product_id = int(input("Enter the product id: "))
    product_price = float(input("Enter the product price: "))
    product_discount=int(input("Enter the product discount: "))
    product_quantity = int(input("Enter the product quantity: "))
    product_weight=int(input("Enter the product weight: "))
    product_user_rating=int(input("Enter the product user rating: "))
    product_brand_id = str(input("Enter the product brand ID: "))
    product_category_id = str(input("Enter the product category ID: "))
    product_details = (product_id, product_price, product_discount, product_quantity, product_weight, product_user_rating, product_brand_id, product_category_id)
    product_details_cursor_add = mycon.cursor()
    product_details_cursor_add.execute("insert into product values(%s,%s,%s,%s,%s,%s,%s,%s)", product_details)
    mycon.commit()
    print("Product Details Added Successfully")
    return 0

def update_product_admin():
    print("Update Product Details")
    print("Enter the product details")
    product_id = int(input("Enter the product id: "))
    # check if product exists
    product_details_cursor_check_exist = mycon.cursor()
    product_details_cursor_check_exist.execute("select * from product where product_id=%s", (product_id,))
    product_details_check_exist = product_details_cursor_check_exist.fetchone()
    if product_details_check_exist != None:
        update_what=int(input("What do you want to update? \n 1. Product Price\n 2. Product Discount\n 3. Product Quantity\n 4. Product Weight\n 5. Product User Rating\n 6. Product Brand ID\n 7. Product Category ID"))
        option=int(input("Enter your choice: "))
        if option==1:
            product_price = int(input("Enter the product price: "))
            product_details_cursor_update = mycon.cursor()
            product_details_cursor_update.execute("update product set product_price=%s where product_id=%s", (product_price, product_id))
            mycon.commit()
            print("Product Price Updated Successfully")
        elif option==2:
            product_discount=int(input("Enter the product discount: "))
            product_details_cursor_update = mycon.cursor()
            product_details_cursor_update.execute("update product set product_discount=%s where product_id=%s", (product_discount, product_id))
            mycon.commit()
            print("Product Discount Updated Successfully")
        elif option==3:
            product_quantity = int(input("Enter the product quantity: "))
            product_details_cursor_update = mycon.cursor()
            product_details_cursor_update.execute("update product set product_quantity=%s where product_id=%s", (product_quantity, product_id))
            mycon.commit()
            print("Product Quantity Updated Successfully")
        elif option==4:
            product_weight=int(input("Enter the product weight: "))
            product_details_cursor_update = mycon.cursor()
            product_details_cursor_update.execute("update product set product_weight=%s where product_id=%s", (product_weight, product_id))
            mycon.commit()
            print("Product Weight Updated Successfully")
        elif option==5:
            product_user_rating=int(input("Enter the product user rating: "))
            product_details_cursor_update = mycon.cursor()
            product_details_cursor_update.execute("update product set product_user_rating=%s where product_id=%s", (product_user_rating, product_id))
            mycon.commit()
            print("Product User Rating Updated Successfully")
        elif option==6:
            product_brand_id = str(input("Enter the product brand ID: "))
            product_details_cursor_update = mycon.cursor()
            product_details_cursor_update.execute("update product set product_brand_id=%s where product_id=%s", (product_brand_id, product_id))
            mycon.commit()
            print("Product Brand ID Updated Successfully")
        elif option==7:
            product_category_id = str(input("Enter the product category ID: "))
            product_details_cursor_update = mycon.cursor()
            product_details_cursor_update.execute("update product set product_category_id=%s where product_id=%s", (product_category_id, product_id))
            mycon.commit()
            print("Product Category ID Updated Successfully")
        else:
            print("Invalid Choice")

def print_brand_admin():
    print("=============================================================")
    print("What do you Want")
    print("1. Print all brands")
    print("2. Print a particular brand")
    print("3. Add a brand")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("=============================================================")
        print("Brand Details")
        brand_details_cursor = mycon.cursor()
        brand_details_cursor.execute("select * from brand")
        brand_details = brand_details_cursor.fetchall()
        for row in brand_details:
            print("Brand ID: ", row[0])
            print("Brand Name: ", row[1])
            print("=============================================================")
    elif option == 2:
        print("=============================================================")
        brand_id = str(input("Enter the brand id: "))
        brand_details_cursor = mycon.cursor()
        brand_details_cursor.execute("select * from brand where brand_id=%s", (brand_id,))
        brand_details = brand_details_cursor.fetchone()
        print("Brand ID: ", brand_details[0])
        print("Brand Name: ", brand_details[1])
        print("=============================================================")
    elif option == 3:
        print("=============================================================")
        print("Add Brand Details")
        brand_id = str(input("Enter the brand id: "))
        brand_name = str(input("Enter the brand name: "))
        brand_details = (brand_id, brand_name)
        brand_details_cursor_add = mycon.cursor()
        brand_details_cursor_add.execute("insert into brand values(%s,%s)", brand_details)
        mycon.commit()
        print("Brand Details Added Successfully")
    else:
        print("Invalid Choice")
    return 0

def print_category_admin():
    print("=============================================================")
    print("What do you Want")
    print("1. Print all categories")
    print("2. Print a particular category")
    print("3. Add a category")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("=============================================================")
        print("Category Details")
        category_details_cursor = mycon.cursor()
        category_details_cursor.execute("select * from category")
        category_details = category_details_cursor.fetchall()
        for row in category_details:
            print("Category ID: ", row[0])
            print("Category Name: ", row[1])
            print("=============================================================")
    elif option == 2:
        print("=============================================================")
        category_id = str(input("Enter the category id: "))
        category_details_cursor = mycon.cursor()
        category_details_cursor.execute("select * from category where category_id=%s", (category_id,))
        category_details = category_details_cursor.fetchone()
        print("Category ID: ", category_details[0])
        print("Category Name: ", category_details[1])
        print("=============================================================")
    elif option == 3:
        print("=============================================================")
        category_id = str(input("Enter the category id: "))
        category_name = str(input("Enter the category name: "))
        category_details_cursor = mycon.cursor()
        category_details_cursor.execute("insert into category values(%s, %s)", (category_id, category_name))
        mycon.commit()
        print("Category Added Successfully")
        print("=============================================================")
    else:
        print("Invalid Choice")
    return 0

def print_delivery_partner_admin():
    print("=============================================================")
    print("What do you Want")
    print("1. Print all delivery partners")
    print("2. Print a particular delivery partner")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("=============================================================")
        print("Delivery Partner Details")
        delivery_partner_details_cursor = mycon.cursor()
        delivery_partner_details_cursor.execute("select * from delivery_partner")
        delivery_partner_details = delivery_partner_details_cursor.fetchall()
        for row in delivery_partner_details:
            print("Delivery Partner ID: ", row[0])
            print("Delivery Partner First Name: ", row[1])
            print("Delivery Partner Middle Name: ", row[2])
            print("Delivery Partner Last Name: ", row[3])
            print("Delivery Partner Phone Number: ", row[4])
            print("Delivery Partner Email: ", row[5])
            print("Delivery Partner Address: ", row[6])
            print("Delivery Partner DOB: ", row[7])
            print("=============================================================")
    elif option == 2:
        print("=============================================================")
        delivery_partner_id = str(input("Enter the delivery partner id: "))
        delivery_partner_details_cursor = mycon.cursor()
        delivery_partner_details_cursor.execute("select * from delivery_partner where partner_id=%s", (delivery_partner_id,))
        delivery_partner_details = delivery_partner_details_cursor.fetchone()
        print("Delivery Partner ID: ", delivery_partner_details[0])
        print("Delivery Partner First Name: ", delivery_partner_details[1])
        print("Delivery Partner Middle Name: ", delivery_partner_details[2])
        print("Delivery Partner Last Name: ", delivery_partner_details[3])
        print("Delivery Partner Phone Number: ", delivery_partner_details[4])
        print("Delivery Partner Email: ", delivery_partner_details[5])
        print("Delivery Partner Address: ", delivery_partner_details[6])
        print("Delivery Partner DOB: ", delivery_partner_details[7])
        print("=============================================================")
    else:
        print("Invalid Choice")
    return 0

def print_customer_admin():
    print("=============================================================")
    print("What do you Want")
    print("1. Print all customers")
    print("2. Print a particular customer")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("=============================================================")
        print("Customer Details")
        customer_details_cursor = mycon.cursor()
        customer_details_cursor.execute("select * from customer")
        customer_details = customer_details_cursor.fetchall()
        for row in customer_details:
            print("Customer ID: ", row[0])
            print("Customer First Name: ", row[1])
            print("Customer Middle Name: ", row[2])
            print("Customer Last Name: ", row[3])
            print("Customer Phone Number: ", row[4])
            print("Customer Email: ", row[5])
            print("Customer Address: ", row[6])
            print("Customer DOB: ", row[7])
            print("=============================================================")
    elif option == 2:
        print("=============================================================")
        customer_id = str(input("Enter the customer id: "))
        customer_details_cursor = mycon.cursor()
        customer_details_cursor.execute("select * from customer where customer_id=%s", (customer_id,))
        customer_details = customer_details_cursor.fetchone()
        print("Customer ID: ", customer_details[0])
        print("Customer First Name: ", customer_details[1])
        print("Customer Middle Name: ", customer_details[2])
        print("Customer Last Name: ", customer_details[3])
        print("Customer Phone Number: ", customer_details[4])
        print("Customer Email: ", customer_details[5])
        print("Customer Address: ", customer_details[6])
        print("Customer DOB: ", customer_details[7])
        print("=============================================================")
    else:
        print("Invalid Choice")
    return 0

def print_order_admin():
    print("=============================================================")
    print("What do you Want")
    print("1. Print all orders")
    print("2. Print a particular order")
    # maybe do it print orderof a particular customer
    print("3. Print all orders of a particular customer")
    option = int(input("Enter your choice: "))
    if option == 1:
        print("=============================================================")
        print("Order Details")
        order_details_cursor = mycon.cursor()
        order_details_cursor.execute("select * from orders")
        order_details = order_details_cursor.fetchall()
        for row in order_details:
            print("Order ID: ", row[0])
            print("Total Amount: ", row[1])
            print("Payment Mode: ", row[2])
            print("Delivery Address: ", row[3])
            print("Order Delivery Status: ", row[4])
            print("=============================================================")
    elif option == 2:
        print("=============================================================")
        order_id = str(input("Enter the order id: "))
        order_details_cursor = mycon.cursor()
        order_details_cursor.execute("select * from orders where order_id=%s", (order_id,))
        order_details = order_details_cursor.fetchone()
        print("Order ID: ", order_details[0])
        print("Total Amount: ", order_details[1])
        print("Payment Mode: ", order_details[2])
        print("Delivery Address: ", order_details[3])
        print("Order Delivery Status: ", order_details[4])
        print("=============================================================")
    elif option == 3:
        print("=============================================================")
        customer_id = int(input("Enter the customer id: "))
        order_details_customer_cursor = mycon.cursor()
        order_details_customer_cursor.execute("select * from order_products where customer_id=%s", (customer_id,))
        order_details_customer = order_details_customer_cursor.fetchall()
        orders=[]
        for row in order_details_customer:
            orders.append(row[0])
        for i in orders:
            order_details_cursor = mycon.cursor()
            order_details_cursor.execute("select * from orders where order_id=%s", (i,))
            order_details = order_details_cursor.fetchone()
            print("Order ID: ", order_details[0])
            print("Total Amount: ", order_details[1])
            print("Payment Mode: ", order_details[2])
            print("Delivery Address: ", order_details[3])
            print("Order Delivery Status: ", order_details[4])
            print("=============================================================")
    else:
        print("Invalid Choice")
    return 0

def total_sales_admin():
    print("=============================================================")
    print("Total Sales:")
    total_sales_cursor = mycon.cursor()
    total_sales_cursor.execute("SELECT payment_method,COUNT(*) AS Transaction_Type_Count,ROUND(SUM(total_cost),2) AS Total_Earning FROM orders GROUP BY payment_method;")
    total_sales = total_sales_cursor.fetchall()
    for rows in total_sales:
        print("Payment Method: ", rows[0])
        print("Total Tranction Count ", rows[1])
        print("Total Earning: ", rows[2])
        print("=============================================================")
    return 0


def admin_login_menu():
    # //enter admin details
    print("=============================================================")
    admin_id = int(input("Enter your admin id: "))
    admin_phone = str(input("Enter your admin phone number: "))
    mycon=mys.connect(host='localhost',user='root',passwd='harsh',database='oasis')
    cur=mycon.cursor()
    query="select * from administrator where admin_id={}".format(admin_id)
    cur.execute(query)
    # cur.execute("select * from administrator where admin_id={}".format(admin_id))
    # nrows=cur.rowcount
    # print("Number of rows returned: ",nrows)
    row=cur.fetchone()
    #print(row)
    #print(row[0])
    #print(row[4])
    if row!=None:
        if row[0]==admin_id and row[4]==admin_phone:
            print("=============================================================")
            print("Login Successful")
            print("=============================================================")
            while True:
                print("Welcome to Oasis - An online shopping Platform")
                print("=============================================================")
                print("1. Your Details (Admin Details) ")
                print("2. Print the Product (Print the Product Details)")
                print("3. Add Product (Add Product Details) ")
                print("4. Update Product (Update Product Details) ")
                print("5. Print the Brand Details or Add Brand (Print the Brand Details) ")
                print("6. Print the Category or Add Category (Print the Category Details) ")
                print("7. Print the delivery partner (Print the delivery partner Details) ")
                print("8. Print the customer (Print the customer Details) ")
                print("9. Print the order (Print the order Details) ")
                print("10. Total Sales (Total Sales Details) ")
                print("11. Back to Main Menu ")
                option = int(input("Enter your choice: "))
                if option == 1:
                    get_admin_details(admin_id)
                elif option == 2:
                    print_product_admin()
                elif option == 3:
                    add_product_admin()
                elif option == 4:
                    update_product_admin()
                elif option == 5:
                    print_brand_admin()
                elif option == 6:
                    print_category_admin()
                elif option == 7:
                    print_delivery_partner_admin()
                elif option == 8:
                    print_customer_admin()
                elif option == 9:
                    print_order_admin()
                elif option == 10:
                    total_sales_admin()
                elif option == 11:
                    print("Going back to Main Menu")
                    break
        else:
            print("Login Unsuccessful Please try again")
    else:
        print("No Data Found")
    return 0

# ==================================================================================================================================================================================================================

def get_delivery_partner_details(delivery_partner_id):
    print("=============================================================")
    delivery_partner_details_cursor = mycon.cursor()
    delivery_partner_details_cursor.execute("select * from delivery_partner where partner_id=%s", (delivery_partner_id,))
    delivery_partner_details = delivery_partner_details_cursor.fetchone()
    print("Delivery Partner ID: ", delivery_partner_details[0])
    print("Delivery Partner First Name: ", delivery_partner_details[1])
    print("Delivery Partner Middle Name: ", delivery_partner_details[2])
    print("Delivery Partner Last Name: ", delivery_partner_details[3])
    print("Delivery Partner Phone Number: ", delivery_partner_details[4])
    print("Delivery Partner Email: ", delivery_partner_details[5])
    print("Delivery Partner Address: ", delivery_partner_details[6])
    print("Delivery Partner DOB: ", delivery_partner_details[7])
    print("=============================================================")
    return 0    

def get_delivery_partner_orders(delivery_partner_id):
    print("=============================================================")
    delivery_partner_orders_cursor = mycon.cursor()
    delivery_partner_orders_cursor.execute("select * from order_delivery where partner_id=%s", (delivery_partner_id,))
    delivery_partner_orders = delivery_partner_orders_cursor.fetchall()
    orders_del=[]
    for rows in delivery_partner_orders:
        orders_del.append(rows[0])
    for i in orders_del:
        order_details_cursor = mycon.cursor()
        order_details_cursor.execute("select * from orders where order_id=%s", (i,))
        order_details = order_details_cursor.fetchall()
        for rows in order_details:
            print("Order ID: ", rows[0])
            print("Order Total_Cost: ", rows[1])
            print("Order Payment_Method: ", rows[2])
            print("Order Delivery Address: ", rows[3])
            print("Order Delivery Status: ", rows[4])
            print("=============================================================")
    return 0

def update_order_status(delivery_partner_id):
    print("=============================================================")
    delivery_partner_orders_cursor = mycon.cursor()
    delivery_partner_orders_cursor.execute("select * from order_delivery where partner_id=%s", (delivery_partner_id,))
    delivery_partner_orders = delivery_partner_orders_cursor.fetchall()
    order_id = int(input("Enter the order id: "))
    order_status = str(input("Enter the order status: Yes or No : "))
    if order_status == "Yes"or "yes":
        order_status="Delivered"
    elif order_status == "No" or "no":
        order_status="Not Delivered"
    orders_del=[]
    for rows in delivery_partner_orders:
        orders_del.append(rows[0])
    for i in orders_del:
        if i==order_id:
            order_update_cursor = mycon.cursor()
            order_update_cursor.execute("update orders set order_delivery_status=%s where order_id=%s", (order_status, order_id))
            mycon.commit()
            print("Order Status Updated")
            print("=============================================================")
    return 0
    

def delivery_partner_login_menu():
    print("=============================================================")
    delivery_partner_id = int(input("Enter your delivery partner id: "))
    delivery_partner_phone = str(input("Enter your delivery partner phone number: "))
    mycon=mys.connect(host='localhost',user='root',passwd='harsh',database='oasis')
    del_cur=mycon.cursor()
    del_cur.execute("select * from delivery_partner where partner_id={}".format(delivery_partner_id))
    # nrows=cur.rowcount
    # print("Number of rows returned: ",nrows)
    row=del_cur.fetchone()
    #print(row)
    #print(row[0])
    #print(row[4])
    if row!=None:
        if row[0]==delivery_partner_id and row[4]==delivery_partner_phone:
            print("=============================================================")
            print("Login Successful")
            print("=============================================================")
            while True:
                print("Welcome to Oasis - An online shopping Platform")
                print("1. Your Details (Delivery Partner Details) ")
                print("2. Your Orders (Order Details) ")
                print("3. Update Order Status (Update Order Status)")
                print("4. Back to Main Menu ")
                option = int(input("Enter your choice: "))
                if option == 1:
                    get_delivery_partner_details(delivery_partner_id)
                elif option == 2:
                    get_delivery_partner_orders(delivery_partner_id)
                elif option == 3:
                    update_order_status(delivery_partner_id)
                elif option == 4:
                    print("Going back to Main Menu")
                    break
    return 0       

# ==================================================================================================================================================================================================================


def get_customer_details(customer_id):
    print("=============================================================")
    customer_details_cursor = mycon.cursor()
    customer_details_cursor.execute("select * from customer where customer_id=%s", (customer_id,))
    customer_details = customer_details_cursor.fetchone()
    print("Customer ID: ", customer_details[0])
    print("Customer First Name: ", customer_details[1])
    print("Customer Middle Name: ", customer_details[2])
    print("Customer Last Name: ", customer_details[3])
    print("Customer Phone Number: ", customer_details[4])
    print("Customer Email: ", customer_details[5])
    print("Customer Address: ", customer_details[6])
    print("Customer DOB: ", customer_details[7])
    print("=============================================================")
    print("Want to Change your details? Yes Or No")
    change_details = str(input("Enter your choice: "))
    if change_details == "Yes" or "yes":
        print("What do you want to change? ")
        print("1. First Name ")
        print("2. Middle Name ")
        print("3. Last Name ")
        print("4. Phone Number ")
        print("5. Email ")
        print("6. Address ")
        print("7. DOB ")
        option=int(input("Enter your choice: "))
        if option == 1:
            customer_first_name = str(input("Enter your new first name: "))
            customer_details_cursor.execute("update customer set first_name=%s where customer_id=%s", (customer_first_name, customer_id))
            mycon.commit()
            print("First Name Updated")
            print("=============================================================")
        elif option == 2:
            customer_middle_name = str(input("Enter your new middle name: "))
            customer_details_cursor.execute("update customer set middle_name=%s where customer_id=%s", (customer_middle_name, customer_id))
            mycon.commit()
            print("Middle Name Updated")
            print("=============================================================")
        elif option == 3:
            customer_last_name = str(input("Enter your new last name: "))
            customer_details_cursor.execute("update customer set last_name=%s where customer_id=%s", (customer_last_name, customer_id))
            mycon.commit()
            print("Last Name Updated")
            print("=============================================================")
        elif option == 4:
            customer_phone = str(input("Enter your new phone number: "))
            customer_details_cursor.execute("update customer set phone_number=%s where customer_id=%s", (customer_phone, customer_id))
            mycon.commit()
            print("Phone Number Updated")
            print("=============================================================")
        elif option == 5:
            customer_email = str(input("Enter your new email: "))
            customer_details_cursor.execute("update customer set email=%s where customer_id=%s", (customer_email, customer_id))
            mycon.commit()
            print("Email Updated")
            print("=============================================================")
        elif option == 6:
            customer_address = str(input("Enter your new address: "))
            customer_details_cursor.execute("update customer set address=%s where customer_id=%s", (customer_address, customer_id))
            mycon.commit()
            print("Address Updated")
            print("=============================================================")
        elif option == 7:
            customer_dob = str(input("Enter your new DOB: "))
            customer_details_cursor.execute("update customer set dob=%s where customer_id=%s", (customer_dob, customer_id))
            mycon.commit()
            print("DOB Updated")
            print("=============================================================")
        else:
            print("Invalid Option")
            print("=============================================================")
            return 0
    elif change_details == "No" or "no":
        print("=============================================================")
        return 0
    

def brouse_products():
    print("=============================================================")
    print("1. All Products")
    print("2. Brouse Products by Category")
    print("3. Brouse Products by Brand")
    option = int(input("Enter your choice: "))
    if option == 1:
        product_details_cursor = mycon.cursor()
        product_details_cursor.execute("select * from product")
        product_details = product_details_cursor.fetchall()
        for product in product_details:
            print("=============================================================")
            print("Product ID: ", product[0])
            print("Product Price: ", product[1])
            print("Product Discount: ", product[2])
            print("Product User Rating: ", product[5])
            print("Product Brand ID: ", product[6])
            print("Product Category ID: ", product[7])
            print("=============================================================")
    elif option == 2:
        Category_name=str(input("Enter the Category Name: "))
        product_details_category_cursor = mycon.cursor()
        product_details_category_cursor.execute("select * from category where name=%s", (Category_name,))
        category_id_found=product_details_category_cursor.fetchone()
        product_details_category_cursor.execute("select * from product where category_id=%s", (category_id_found[0],))
        product_details_category = product_details_category_cursor.fetchall()
        print("=============================================================")
        print("Products in Category: ", Category_name)
        print("=============================================================")
        for product in product_details_category:
            print("=============================================================")
            print("Product ID: ", product[0])
            print("Product Price: ", product[1])
            print("Product Discount: ", product[2])
            print("Product User Rating: ", product[5])
            print("Product Brand ID: ", product[6])
            print("Product Category ID: ", product[7])
            print("=============================================================")


    elif option == 3:
        Brand_name=str(input("Enter the Brand Name: "))
        product_details_brand_cursor = mycon.cursor()
        product_details_brand_cursor.execute("select * from brand where name=%s", (Brand_name,))
        brand_id_found=product_details_brand_cursor.fetchone()
        product_details_brand_cursor.execute("select * from product where brand_id=%s", (brand_id_found[0],))
        product_details_brand = product_details_brand_cursor.fetchall()
        print("=============================================================")
        print("Products in Brand: ", Brand_name)
        print("=============================================================")
        for product in product_details_brand:
            print("=============================================================")
            print("Product ID: ", product[0])
            print("Product Price: ", product[1])
            print("Product Discount: ", product[2])
            print("Product User Rating: ", product[5])
            print("Product Brand ID: ", product[6])
            print("Product Category ID: ", product[7])
            print("=============================================================")
    else:
        print("Invalid Option")
        print("=============================================================")
        return 0

def add_to_cart(customer_id):
    print("=============================================================")
    print("Enter Product ID to add to cart")
    product_id=int(input("Enter Product ID: "))
    #product to add to cart
    product_Add_cursor = mycon.cursor()
    product_Add_cursor.execute("select * from product where product_id=%s", (product_id,))
    product_Add = product_Add_cursor.fetchone()
    if product_Add!=None:
        print("=============================================================")
        print("Product ID: ", product_Add[0])
        print("Product Price: ", product_Add[1])
        print("Product Brand ID: ", product_Add[6])
        print("Product Category ID: ", product_Add[7])
        print("=============================================================")
        print("Are you sure you want to add this product to cart?")
        print("1. Yes")
        print("2. No")
        option = int(input("Enter your choice: "))
        if option == 1:
            product_Add_cursor.execute("insert into cart_products(customer_id, product_id) values(%s, %s)", (customer_id, product_id))
            mycon.commit()
            print("Product Added to Cart")
            print("=============================================================")
        elif option == 2:
            print("Cancelled")
            print("=============================================================")
            return 0
    else:
        print("Product ID not found")
        print("Please try Again")
        print("=============================================================")
        return 0

def brouse_products_add_to_cart(customer_id):
    print("=============================================================")
    print("1. Brouse Products")
    print("2. Add to Cart")
    print("3. Back to Main Menu")
    option = int(input("Enter your choice: "))
    if option == 1:
        brouse_products()
    elif option == 2:
        add_to_cart(customer_id)
    elif option == 3:
        print("Going Back")
        return 0
    else:
        print("Invalid Option")
        print("=============================================================")
        return 0



def get_customer_orders(customer_id):
    print("=============================================================")
    customer_orders_cursor = mycon.cursor()
    customer_orders_cursor.execute("select * from order_products where customer_id=%s", (customer_id,))
    customer_orders = customer_orders_cursor.fetchall()
    customer_order=set()
    customer_products=[] #saving all product ids for delivery the customer
    for i in customer_orders:
        customer_order.add(i[0])
        customer_products.append(i[1])

    # //print the products ordered by the customer all
    # for i in customer_products:
    #     product_details_cursor = mycon.cursor()
    #     product_details_cursor.execute("select * from product where product_id=%s", (i,))
    #     product_details = product_details_cursor.fetchone()
    #     print("Product ID: ", product_details[0])
    #     print("Product Price: ", product_details[1])
    #     print("Product Brand ID: ", product_details[2])
    #     print("Product Category ID: ", product_details[3])

    # print("=============================================================")
    print("Your Orders are: ")
    for i in customer_order:
        # print all the order details of the customer
        print("=============================================================")
        cust_order_details_cursor = mycon.cursor()
        cust_order_details_cursor.execute("select * from orders where order_id=%s", (i,))
        cust_order_details = cust_order_details_cursor.fetchone()
        print("Order ID: ", cust_order_details[0])
        print("Order Total_Cost: ", cust_order_details[1])
        print("Order Payment_Method: ", cust_order_details[2])
        print("Order Delivery Address: ", cust_order_details[3])
        print("Order Delivery Status: ", cust_order_details[4])
        #get the delivery person details 
        delivery_person_details_cursor = mycon.cursor()
        delivery_person_details_cursor.execute("select * from order_delivery where order_id=%s", (cust_order_details[0],))
        delivery_person_details = delivery_person_details_cursor.fetchone()
        oder_delvery_person_id = delivery_person_details[1]
        delivery_person_details_cursor.execute("select * from delivery_partner where partner_id=%s", (oder_delvery_person_id,))
        delivery_person_details = delivery_person_details_cursor.fetchone()
        print("Order Delivery Partner ID: ", delivery_person_details[0])
        print("Order Delivery Partner Name: ", delivery_person_details[1])
        print("Order Delivery Partner Phone Number: ", delivery_person_details[4])
        print("Order Delivery Partner Email: ", delivery_person_details[5])
        print("=============================================================")
    return 0

def checkout_customer(customer_id):
    # print("=============================================================")
    # print("Are you sure you want to checkout?")
    # print("1. Yes")
    # print("2. No")
    # option = int(input("Enter your choice: "))
    # if option == 1:
        print("=============================================================")
        print("Checkout")
        print("=============================================================")
        print("")
        print("")
        get_customer_coupons(customer_id)
        print("Enter Coupon ID you have or type NONE: ")
        coupon_code = input()
        #geting the all in the customer cart
        customer_cart_cursor = mycon.cursor()
        customer_cart_cursor.execute("select * from cart_products where customer_id=%s", (customer_id,)) #got product_id of the cart
        customer_cart = customer_cart_cursor.fetchall()
        #get the total cost of the cart
        total_cost=0
        for i in customer_cart:
            product_details_cursor = mycon.cursor()
            product_details_cursor.execute("select * from product where product_id=%s", (i[1],))
            product_details = product_details_cursor.fetchone()
            product_cost=product_details[1]-(product_details[1]*(product_details[2]/100))
            total_cost=total_cost+product_cost
        #get the coupon code details
        coupon_discout=0
        if coupon_code.isdigit():
            coupon_code_cursor = mycon.cursor()
            coupon_code_cursor.execute("select * from coupon where coupon_id=%s", (coupon_code,))
            coupon_code_details = coupon_code_cursor.fetchone()
            custom_id=coupon_code_details[0]
            if custom_id==customer_id:
                coupon_discout=coupon_code_details[1]
                total_cost=total_cost-((coupon_discout/100)*total_cost)
        total_cost=round(total_cost,2)

        print("=============================================================")
        print("Total Checkout Cost: ", total_cost)
        print("=============================================================")

        print("")
        print("")
        print("Confirm Checkout?")
        print("1. Yes")
        print("2. No")
        option = int(input("Enter your choice: "))
        if option == 1:
            #get the customer address
            customer_address_cursor = mycon.cursor()
            customer_address_cursor.execute("select * from customer where customer_id=%s", (customer_id,))
            customer_address = customer_address_cursor.fetchone()
            customer_add=str(customer_address[6])
            #select payment method
            print("=============================================================")
            print("Select Payment Method")
            print("1. Cash on Delivery")
            print("2. UPI")
            print("3. Card")
            option = int(input("Enter your choice: "))
            if option == 1:
                pay_method="Cash on Delivery"
            elif option == 2:
                pay_method="UPI"
            elif option == 3:
                pay_method="Card"
            #insert into orders table
            customer_orders_cursor = mycon.cursor()
            customer_orders_cursor.execute("insert into orders(total_cost, payment_method, delivery_address, order_delivery_status) values(%s, %s, %s, %s)", (total_cost, pay_method, customer_add, "Not Delivered"))
            mycon.commit()
            #get the order id
            customer_orders_order_id_cursor = mycon.cursor()
            customer_orders_order_id_cursor.execute("select * from oasis.orders ORDER BY order_id DESC LIMIT 1")
            customer_orders_order_id = customer_orders_order_id_cursor.fetchone()
            order_id=customer_orders_order_id[0]
            #insert into orders_products table
            for i in customer_cart:
                customer_orders_cursor.execute("insert into order_products(order_id, product_id, customer_id) values(%s, %s, %s)", (order_id, i[1], customer_id))
                mycon.commit()
            #insert into order_delivery table
            customer_orders_cursor.execute("insert into order_delivery(order_id,partner_id) values(%s, %s)", (order_id, random.randint(1,150)))
            mycon.commit()

            #insert into order_coupons table
            customer_orders_cursor.execute("insert into order_coupons(order_id, coupon_id) values(%s, %s)", (order_id, coupon_code))
            mycon.commit()

            #update product table
            for i in customer_cart:
                product_details_cursor.execute("select * from product where product_id=%s", (i[1],))
                product_details = product_details_cursor.fetchone()
                product_quantity=product_details[3]-1
                product_details_cursor.execute("update product set quantity=%s where product_id=%s", (product_quantity, i[1]))
                mycon.commit()
            #delete from cart_products table
            customer_cart_cursor.execute("delete from cart_products where customer_id=%s", (customer_id,))
            mycon.commit()
            #delete from coupon table
            customer_cart_cursor.execute("delete from user_coupon where coupon_id=%s", (coupon_code,))
            mycon.commit()
            print("=============================================================")
            print("=============================================================")
            print("ORDER PLACED")
            print("=============================================================")
            print("=============================================================")
        elif option == 2:
            print("Cancelled Checkout")
            print("=============================================================")
            return 0
        return 0



def empty_cart_customer(customer_id):
    print("=============================================================")
    print("Are you sure you want to empty your cart?")
    print("1. Yes")
    print("2. No")
    option = int(input("Enter your choice: "))
    if option == 1:
        customer_cart_cursor = mycon.cursor()
        customer_cart_cursor.execute("delete from cart_products where customer_id=%s", (customer_id,))
        mycon.commit()
        print("Cart Emptied")
        print("=============================================================")
    elif option == 2:
        print("Cancelled")
        print("=============================================================")
        return 0
    else:
        print("Invalid Option")
        print("=============================================================")
        return 0


def get_customer_cart(customer_id): #left to do
    print("=============================================================")
    customer_cart_cursor = mycon.cursor()
    customer_cart_cursor.execute("select * from cart_products where customer_id=%s", (customer_id,))
    customer_cart = customer_cart_cursor.fetchall()
    customer_cart_products=[]
    for i in customer_cart:
        customer_cart_products.append(i[1])
    # print("=============================================================")
    print("Your Cart has: ")
    total_cart_price = 0
    for i in customer_cart_products:
        # print all the order details of the customer
        print("=============================================================")
        cust_cart_details_cursor = mycon.cursor()
        cust_cart_details_cursor.execute("select * from product where product_id=%s", (i,))
        cust_cart_details = cust_cart_details_cursor.fetchone()
        print("Product ID: ", cust_cart_details[0])
        print("Product Price: ", cust_cart_details[1])
        total_cart_price = total_cart_price + cust_cart_details[1]
        print("Product Brand ID: ", cust_cart_details[2])
        print("Product Category ID: ", cust_cart_details[3])
        print("=============================================================")

    print("=============================================================")
    print("Total Cart Price without Discount: ", total_cart_price)
    print("Discount and coupon Applied while checkout")
    print("=============================================================")

    print("=============================================================")
    print("What do you want to do? ")
    print("1. Checkout")
    print("2. Empty Cart")
    print("3. Back to Main Menu")
    print("")
    print("")
    
    option = int(input("Enter your choice: "))
    if option == 1:
        checkout_customer(customer_id)
    elif option == 2:
        empty_cart_customer(customer_id)
    elif option == 3:
        print("Going Back to Main Menu")
        return 0
    return 0

def get_customer_coupons(customer_id):
    print("=============================================================")
    customer_coupons_cursor = mycon.cursor()
    customer_coupons_cursor.execute("select * from user_coupon where customer_id=%s", (customer_id,))
    customer_coupons = customer_coupons_cursor.fetchall()
    customer_coupon=[]
    for i in customer_coupons:
        customer_coupon.append(i[1])
    print("Your Coupons are: ")
    for i in customer_coupon:
        # print all the order details of the customer
        print("=============================================================")
        cust_coupon_details_cursor = mycon.cursor()
        cust_coupon_details_cursor.execute("select * from coupon where coupon_id=%s", (i,))
        cust_coupon_details = cust_coupon_details_cursor.fetchone()
        print("Coupon ID: ", cust_coupon_details[0])
        print("Coupon Discount: ", cust_coupon_details[1])
        print("Coupon Expiry Date: ", cust_coupon_details[2])
        print("=============================================================")
    return 0

def customer_login_menu():
    print("=============================================================")
    customer_id = int(input("Enter your customer id: "))
    customer_phone = str(input("Enter your customer phone number: "))
    mycon=mys.connect(host='localhost',user='root',passwd='harsh',database='oasis')
    cus_cur=mycon.cursor()
    cus_cur.execute("select * from customer where customer_id={}".format(customer_id))
    # nrows=cur.rowcount
    # print("Number of rows returned: ",nrows)
    row=cus_cur.fetchone()
    #print(row)
    #print(row[0])
    #print(row[4])
    if row!=None:
        if row[0]==customer_id and row[4]==customer_phone:
            print("=============================================================")
            print("Login Successful")
            print("=============================================================")
            while True:
                print("Welcome to Oasis - An online shopping Platform")
                print("=============================================================")
                print("1. Your Details (Customer Details) ")
                print("2. Brouse Products And Add to Cart (ALL Product Details) ")
                print("3. Your Orders (Order Details) ")
                print("4. Your Cart (Cart Details) ")
                print("5. Your Coupons (Coupon Details) ")
                print("6. Back to Main Menu ")
                option = int(input("Enter your choice: "))
                if option == 1:
                    get_customer_details(customer_id)
                elif option == 2:
                    brouse_products_add_to_cart(customer_id)
                elif option == 3:
                    get_customer_orders(customer_id)
                elif option == 4:
                    get_customer_cart(customer_id)
                elif option == 5:
                    get_customer_coupons(customer_id)
                elif option == 6:
                    print("Going Back")
                    print("=============================================================")
                    break
                else:
                    print("Invalid Option")
                    print("=============================================================")
    return 0

#=============================================================================================================================================================================================================================
def all_queries():
    print("=============================================================")
    print("ALL QUERIES IMPLEMENTED")
    print("=============================================================")
    print("SUBMISSION 4")
    print("1. To segregate the products on the basis of good (rating > 3), moderate (rating = 3) and bad (rating < 3)")
    print("2. To add a coupon worth 20% to any person with more than 1 order.")
    print("3. To give a coupon worth 30% to all customers whose birthday it is today.")
    print("4. To count the number of orders made by UPI, Card and Cash and the total cost earning from each payment method")
    print("5. To group products by categories and further group them on the basis of brand in their respective categories and then sort them according to prices.")
    print("6. To delete a category/brand if the number of products in that category/brand is 0.")
    print("7. TRIGGER To delete the order after it has been delivered")
    print("8. TRIGGER: To delete the coupons if they have expired.")
    print("9. To return top products from each category. Also we can check for the adequate quantity of product , or the admin can order more if the quantity had become less.")
    print("10. To return the maximum ordered category from different age ranges of users.")
    print("11. To remove all delivery partners whose age is > 40.")
    print("12. To display customers and their cart prices.")


    print("")
    print("=============================================================")
    print("SUBMISSION 5")
    print("OLAP Queries")
    print("=============================================================")

    print("13. Total revenue generated by each brand and category:")
    print("14. Group by user rating and Brand_ID from cube to check the sum of Quantity and Price")
    print("15. To count the number of orders made by UPI, Card and Cash and the total cost earning from each payment method")
    print("16. To get the total cost of all orders by payment method, brand, and category, with subtotals for each payment method, brand, and category:")
    print("17. To return the maximum ordered category from different age ranges of users.")
    print("18. Total loss generated from the discounts given to the user to stay on the website and buy the products used for analysis.")
    print("TRIGGERS")
    print("Already implemented in the submitted sql file")
    print("1.Set weight of item to 0 if the weight values is NULL.")
    print("""
        DELIMITER $$
            CREATE TRIGGER set_weight_to_zero
            BEFORE INSERT
            ON product FOR EACH ROW
            BEGIN
            IF NEW.weight IS NULL THEN
                SET NEW.weight = 0;
            END IF;
        END$$ )""")
    print("2.Set the price of the product to 0 if the quantity of the product gets update to 0.")

    print("""
    DELIMITER $$
        create trigger remove_product
        before update on product
        for each row
        begin
        if NEW.quantity=0 then
            set NEW.price = 0;
        End if;
    END$$""")
    print("3. To delete the order after it has been delivered")

    print("""
        DELIMITER //
        CREATE TRIGGER delete_order AFTER UPDATE ON orders
        FOR EACH ROW
            IF NEW.order_delivery_status = 'Delivered' THEN
                DELETE FROM orders WHERE Order_ID = OLD.Order_ID;
            END IF;
        //
        DELIMITER ;""")
    
    print("4. To delete the coupons if they have expired.")
    print(""" 
        CREATE TRIGGER delete_expired_coupons
        BEFORE INSERT ON Coupon
        FOR EACH ROW
        DELETE FROM Coupon
        WHERE Expiry < CURDATE();""")
    
    print("=============================================================")
    print("=============================================================")
    
    print("Select your option")
    option=int(input("Enter your choice: "))

    print("=============================================================")
    mycon=mys.connect(host='localhost',user='root',passwd='harsh',database='oasis')
    if option == 1:
       mycursor=mycon.cursor()
       mycursor.execute("SELECT product_ID,Price,Discount,Quantity,Brand_ID,Category_IDUser_Rating,CASEWHEN User_Rating > 3 THEN 'good'WHEN User_Rating = 3 THEN 'moderate'ELSE 'bad'END AS Ratings FROM product;")
       mydata=mycursor.fetchall()
       for i in mydata:
           print(i)
    #rest all in sheet






# ==================================================================================================================================================================================================================
while True:
    print("")
    print("")
    print("=============================================================")
    print("OASIS- AN ONLINE RETAIL STORE")
    print("=============================================================")
    print("Welcome to the login page")
    print("Select your option")
    print("1.Administrator")
    print("2.Customer")
    print("3.Delivery Partner")
    print("4.Exit")
    print("=============================================================")
    print("69. All queries inplemented (The submitted Queries and triggers)")
    print("=============================================================")
    print("")
    print("")
    option = int(input("Enter your choice: "))
    if option == 1:
        admin_login_menu()
    elif option == 2:
        customer_login_menu()
    elif option == 3:
        delivery_partner_login_menu()
    elif option == 4:
        print("Thank you for visiting us")
        break
    elif option == 69:
        all_queries()

    else:
        print("Wrong Option")
        print("Please try again")
        print("")
    
