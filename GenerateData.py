import csv
import random
from datetime import datetime, timedelta

#introduce randomness
now = datetime.now()
timestamp = int(now.timestamp())
random.seed(timestamp)

customer_types = ['Axiom', 'Pix-Vue', 'Fumahol', 'Buy Yogurt', 'Large Industries', 'AL\'S', 'Zazzle.com' , 'St. Vintage Hospital'] 
status_types = ['Closed', 'Active', 'Cancelled', 'Pending']
product_types = ['Others', 'Power', 'Lighting', 'Chargers']
ontime_types = ['YES', "NO"]
automation_status_types = ['Automated']
shipping_location_types = ["North America", "South America", "Europe", "Asia"]
numCust = 8

# Function to generate random 12-digit integers
def generate_random_integer():
    return random.randint(100000000000, 999999999999)

# Function to generate random 6-digit integers
def generate_random_item():
    return random.randint(000000, 899999)

# Function to generate random date in the past 12 months
def generate_random_date():
    today = datetime.now()
    start_date = today - timedelta(days=500)
    random_days = random.randint(1, 365)
    return start_date + timedelta(days=random_days)

# Function to generate random 'customer'
def generate_random_customer():
    return random.choice(customer_types)

# Function to generate random 'status'
def generate_random_status():
    if random.random() < 0.4:
        return status_types[1]
    elif random.random() < 0.8:
        return status_types[0]
    elif random.random() < 0.9:
        return status_types[2]
    else:
        return status_types[3]

# Function to generate 'customer bill to'
def generate_random_bill_id( customer ):
    return hash(customer) % numCust + 1

# Function to generate 'customer ship id'
def generate_random_ship_id( customer ):
    return hash(customer) % numCust + 1

# Function to generate random 'Product Type'
def generate_random_product_type():
    return random.choice(product_types)

# Function to generate random 'shipping location'
def generate_random_shipping_location():
    return random.choice(shipping_location_types)

# Function to generate random 'Ontime'
def generate_random_ontime_type():
    return ontime_types[0] if random.random() < .8 else ontime_types[1]

# Function to generate random 'automation status'
def generate_random_automation_status():
    return random.choice(automation_status_types) if random.random() < .93 else None

# Number of rows in the CSV files
num_rows_SupplyChain = random.randint(40000,60000)
num_rows_Automation = num_rows_SupplyChain
num_rows_Invoice = random.randint(40000,60000)
num_rows_OrderManagement = num_rows_Invoice

# Custom column names
columnsOrderManagement = ["Bill Customer ID", "Customer Description", "Ship Customer ID", "Ordered Quantity", "Ordered Date", "Shipping Location","Line Number", "Status", "Scheduled Delivery Date", "Scheduled Ship Date", "Actual Ship Date","Order Number", "Line ID","Product Number","Item", "Product Type"]
columnsInvoice = ["Invoice Number", "Shipping Location", "Contended Invoice", "Invoice Date", "Product Type", "Ordered Date"]
columnsAutomated = ["Automation Status", "Manual Status", "Product", "Customer", "Ordered Date", "Line ID","Shipping Location"]
columnsSupplyChain = ["Scheduled Ship Date", "Ideal Ship Date", "Ideal Arrival Date", "Ontime", "Ordered Date", "Line ID","Line Status", "Ordered Quanity", "Quantity Ordered Available", "Item", "Shipping Location", "Product"]


# Generate random dataOrderManagement for each row
dataOrderManagement = []
dataSupplyChain = []
dataAutomation = []
dataInvoice = []

for _ in range(num_rows_OrderManagement):
    random_days = random.randint(1, 40)
    line_id = generate_random_integer()
    location = generate_random_shipping_location()
    disputed_invoice = generate_random_integer() if random.random() < 0.5 else None  # Make 90% values not null
    product_type = generate_random_product_type()
    line_number = random.randint(1,20)
    order_number = random.randint(1,20)
    ordered_quantity = random.randint(1, 5000)
    item = generate_random_item()
    product_number = generate_random_item()
    status = generate_random_status()
    customer_description = generate_random_customer()
    bill_customer_id = generate_random_bill_id(customer_description)
    ship_customer_id = generate_random_ship_id(customer_description)
    
    ordered_date = generate_random_date()
    scheduled_ship_date = ordered_date + timedelta(days=random_days) if random.random() < 0.88 else None
    actual_ship_date = scheduled_ship_date + timedelta(days=random.randint(-5, 20)) if scheduled_ship_date else ordered_date + timedelta(days=random.randint(5,25)) 
    scheduled_delivery_date = actual_ship_date + timedelta(days=random.randint(1, 10)) 
    
    #format dates
    ordered_date_str = ordered_date.strftime('%Y-%m-%d')
    scheduled_ship_date_str = scheduled_ship_date.strftime('%Y-%m-%d') if scheduled_ship_date else None

    dataOrderManagement.append([bill_customer_id, customer_description, ship_customer_id, ordered_quantity, ordered_date, location, line_number, status, scheduled_delivery_date, scheduled_ship_date, actual_ship_date, order_number, line_id, product_number, item, product_type])

for _ in range(num_rows_SupplyChain):
    line_id = generate_random_integer()
    ordered_quantity = random.randint(1, 30)
    shipping_location = generate_random_shipping_location()
    line_status = generate_random_status()
    ordered_date = generate_random_date()
    ontime = generate_random_ontime_type()
    product = generate_random_product_type()
    ordered_quantity_available = ordered_quantity if random.random() < 0.9 else 0 
    item = generate_random_item()
    
    # Calculate dates using timedelta
    random_days = random.randint(1, 40)
    scheduled_ship_date = ordered_date + timedelta(days=random_days) if random.random() < 0.88 else None
    ideal_ship_date = (scheduled_ship_date + timedelta(days=random.randint(-5, 0))) if ontime == "NO" and scheduled_ship_date else ( (scheduled_ship_date + timedelta(days=random.randint(1, 7)))  if ontime == "YES" and scheduled_ship_date else ordered_date + timedelta(days=random.randint(5,25)) )
    ideal_arrival_date = ideal_ship_date + timedelta(days=random.randint(1, 10)) 
    
    # Format dates
    ordered_date_str = ordered_date.strftime('%Y-%m-%d')
    scheduled_ship_date_str = scheduled_ship_date.strftime('%Y-%m-%d') if scheduled_ship_date else None
    ideal_ship_date_str = ideal_ship_date.strftime('%Y-%m-%d') if ideal_ship_date else None
    ideal_arrival_date_str = ideal_arrival_date.strftime('%Y-%m-%d') if ideal_arrival_date else None
    
    dataSupplyChain.append([scheduled_ship_date_str, ideal_ship_date_str, ideal_arrival_date_str, ontime, ordered_date_str, line_id, line_status, ordered_quantity, ordered_quantity_available, item, shipping_location, product])

for _ in range(num_rows_Automation):
    
    line_id = generate_random_integer()
    shipping_location = generate_random_shipping_location()
    automation_status = generate_random_automation_status()
    Manual_status = "Automated" if automation_status == "Automated" else "Partial" if random.random() < .5 else "Manual"
    ordered_date = generate_random_date().strftime('%Y-%m-%d')
    product = generate_random_product_type()
    customer = generate_random_customer()

    dataAutomation.append([automation_status, Manual_status, product , customer, ordered_date, line_id, shipping_location])

for _ in range(num_rows_Invoice):
    invoice_number = generate_random_integer()
    shipping_location = generate_random_shipping_location()
    contended_invoice = generate_random_integer() if random.random() < 0.05 else None  # Make 5% values not null
    invoice_date = generate_random_date()
    product = generate_random_product_type()
    ordered_date = invoice_date - timedelta(days=random.randint(1, 40))

    dataInvoice.append([invoice_number, shipping_location, contended_invoice, invoice_date.strftime('%Y-%m-%d'), product, ordered_date.strftime('%Y-%m-%d')])

# Write the to the CSV files
filenameOrderManagement = "OMC.csv"
filenameSupplyChain = "ATF.csv"
filenameInvoice = "Invoice.csv"
filenameAutomated = "Automated.csv"

with open(filenameAutomated, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(columnsAutomated)
    writer.writerows(dataAutomation)

with open(filenameInvoice, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(columnsInvoice)
    writer.writerows(dataInvoice)

with open(filenameSupplyChain, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(columnsSupplyChain)
    writer.writerows(dataSupplyChain)

with open(filenameOrderManagement, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(columnsOrderManagement)
    writer.writerows(dataOrderManagement)


#print successful output
print(f"'{filenameOrderManagement}' CSV file with {num_rows_OrderManagement} rows has been created.")
print(f"'{filenameSupplyChain}' CSV file with {num_rows_SupplyChain} rows has been created.")
print(f"'{filenameInvoice}' CSV file with {num_rows_Invoice} rows has been created.")
print(f"'{filenameAutomated}' CSV file with {num_rows_Automation} rows has been created.")
