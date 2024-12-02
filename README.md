# Assignment-9
#This is the columns and types of data recorded in my dataset Loan dataset columns: customer_id: Unique identifier for each customer customer_age: Age of the customer customer_income: Annual income of the customer home_ownership: Home ownership status (e.g., RENT, OWN, MORTGAGE) employment_duration: Duration of employment in months loan_intent: Purpose of the loan (e.g., PERSONAL, EDUCATION, MEDICAL, VENTURE) loan_grade: Grade assigned to the loan loan_amnt: Loan amount requested loan_int_rate: Interest rate of the loan term_years: Loan term in years historical_default: Indicates if the customer has a history of default (Y/N) cred_hist_length: Length of the customer's credit history in years Current_loan_status: Current status of the loan (DEFAULT, NO DEFAULT)
#This is what I was trying to accomplish
Write a function that creates dictionaries of customers based on their cred_hist_length and writes these dictionaries to a new CSV file.

#This is how my code roughly works
This module reads and writes to a CSV file. It starts by making an empty list to store each row or client row from the CSV file. Opens the CSv file and converts each row into a dictionary. Then appends each row dictionary to the customers list. An empty dictionary stores customers gruoped by their credit history length. Iterates over each customer dictionary in the llist. Retreives the credit history in the data file. Then function writes the grouped customer data to a new CSV file. Opens the output file and defines the column names for the CSV file. Then writes the headers, writes all the credit history dictionary, and then credit history length and its customers to the CSV file.

#Examples of dictionaries in code
# Dictionary representing a person's basic information
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Dictionary containing nested dictionaries
employee = {
    "name": "John",
    "role": "Developer",
    "skills": {
        "languages": ["Python", "JavaScript"],
        "frameworks": ["Django", "React"]
    }
}

# Dictionary where values are lists
student_scores = {
    "Math": [95, 88, 92],
    "Science": [87, 90, 85],
    "English": [78, 83, 88]
}
