import csv

def read_csv(file_path):
    customers = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            customers.append(row)
    return customers

def create_dictionaries(customers):
    customer_dict = {}
    for customer in customers:
        cred_hist_length = customer['cred_hist_length']
        if cred_hist_length not in customer_dict:
            customer_dict[cred_hist_length] = []
        customer_dict[cred_hist_length].append(customer)
    return customer_dict

def write_csv(customer_dict, output_file_path):
    with open(output_file_path, mode='w', newline='') as file:
        fieldnames = ['cred_hist_length', 'customers']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for cred_hist_length, customers in customer_dict.items():
            writer.writerow({'cred_hist_length': cred_hist_length, 'customers': customers})

# Example usage
input_file_path = 'C:/Users/thoma\Downloads/Finished Data USE.csv'
output_file_path = 'C:/Users/thoma\Downloads/Finished_New_Data.csv'

customers = read_csv(input_file_path)
customer_dict = create_dictionaries(customers)
write_csv(customer_dict, output_file_path)