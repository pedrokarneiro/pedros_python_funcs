# My Python functions.
# Not tested yet.

# Returns status message based on the given status code.
def get_mensage(my_status_code):
    if my_status_code == 100: my_mensage = 'CONTINUE'
    elif my_status_code == 101: my_mensage = 'SWITCHING PROTOCOLS'
    elif my_status_code == 200: my_mensage = 'OK'
    elif my_status_code == 201: my_mensage = 'CREATED'
    elif my_status_code == 202: my_mensage = 'ACCEPTED'
    elif my_status_code == 203: my_mensage = 'NON-AUTHORITATIVE INFORMATION'
    elif my_status_code == 204: my_mensage = 'NO CONTENT'
    elif my_status_code == 205: my_mensage = 'RESET CONTENT'
    elif my_status_code == 206: my_mensage = 'PARTIAL CONTENT'
    elif my_status_code == 300: my_mensage = 'MULTIPLE CHOICES'
    elif my_status_code == 301: my_mensage = 'MOVED PERMANENTLY'
    elif my_status_code == 302: my_mensage = 'FOUND'
    elif my_status_code == 303: my_mensage = 'SEE OTHER'
    elif my_status_code == 304: my_mensage = 'NOT MODIFIED'
    elif my_status_code == 307: my_mensage = 'TEMPORARY REDIRECT'
    elif my_status_code == 308: my_mensage = 'PERMANENT REDIRECT'
    elif my_status_code == 400: my_mensage = 'BAD REQUEST'
    elif my_status_code == 401: my_mensage = 'NAO AUTORIZADO'
    elif my_status_code == 403: my_mensage = 'PROIBIDO'
    elif my_status_code == 404: my_mensage = 'NOT FOUND'
    elif my_status_code == 405: my_mensage = 'METHOD NOT ALLOWED'
    elif my_status_code == 406: my_mensage = 'NOT ACCEPTABLE'
    elif my_status_code == 407: my_mensage = 'PROXY AUTHENTICATION REQUIRED'
    elif my_status_code == 408: my_mensage = 'REQUEST TIMEOUT'
    elif my_status_code == 409: my_mensage = 'CONFLICT'
    elif my_status_code == 410: my_mensage = 'GONE'
    elif my_status_code == 411: my_mensage = 'LENGTH REQUIRED'
    elif my_status_code == 412: my_mensage = 'PRECONDITION FAILED'
    elif my_status_code == 413: my_mensage = 'PAYLOAD TOO LARGE'
    elif my_status_code == 414: my_mensage = 'URI TOO LONG'
    elif my_status_code == 415: my_mensage = 'UNSUPPORTED MEDIA TYPE'
    elif my_status_code == 416: my_mensage = 'RANGE NOT SATISFIABLE'
    elif my_status_code == 417: my_mensage = 'EXPECTATION FAILED'
    elif my_status_code == 426: my_mensage = 'UPGRADE REQUIRED'
    elif my_status_code == 428: my_mensage = 'PRECONDITION REQUIRED'
    elif my_status_code == 429: my_mensage = 'TOO MANY REQUESTS'
    elif my_status_code == 431: my_mensage = 'REQUEST HEADER FIELDS TOO LARGE'
    elif my_status_code == 451: my_mensage = 'UNAVAILABLE FOR LEGAL REASONS'
    elif my_status_code == 500: my_mensage = 'INTERNAL SERVER ERROR'
    elif my_status_code == 501: my_mensage = 'NOT IMPLEMENTED'
    elif my_status_code == 502: my_mensage = 'BAD GATEWAY'
    elif my_status_code == 503: my_mensage = 'SERVICE UNAVAILABLE'
    elif my_status_code == 504: my_mensage = 'GATEWAY TIMEOUT'
    elif my_status_code == 505: my_mensage = 'HTTP VERSION NOT SUPPORTED'
    elif my_status_code == 511: my_mensage = 'NETWORK AUTHENTICATION REQUIRED'
    else: my_mensage = 'ERROR ' + str(my_status_code)
    return my_mensage
#end get_mensage

# Performs an insertion of a line according to the SQL INSERT instruction passed as argument.
# Default parameter: my_charset='UTF-8'
def insert_line(insert_sql, my_host, my_user, my_password, my_database, my_charset='UTF-8'):
    print '*****************'
    print insert_sql
    print '*****************'
    insert_conn = pymssql.connect(host=my_host, user=my_user, password=my_password, database=my_database)
    insert_cursor = insert_conn.cursor()
    insert_cursor.execute(insert_sql)
    insert_conn.commit()
    insert_conn.close()
#end insert_line

def fetch_transactions(account_id: str, start_date: str, end_date: str) -> list:
    '''
    Fetch transactions for a given account between specified dates. Centralized data retrieval for all reports.
    Purpose: Retrieves transactions for a given account in a specified date range.
    Reason.: Centralized data retrieval ensures consistency across reports.

    :param account_id: Unique account identifier
    :param start_date: Start date (YYYY-MM-DD)
    :param end_date: End date (YYYY-MM-DD)
    :return: List of transactions as dictionaries
    '''
    # Example: Replace with actual database query
    transactions = [
        {"date": "2024-03-01", "amount": 500.0, "type": "deposit"},
        {"date": "2024-03-02", "amount": -200.0, "type": "withdrawal"},
    ]
    return transactions
#end fetch_transactions

def generate_report(transactions: list, report_type: str = "summary") -> dict:
    """
    Generate a banking report based on transactions. Modular logic for different report types.
    Purpose: Processes transaction data and generates different report types.
    Reason.: Allows flexibility for various reports without duplicating logic.

    :param transactions: List of transaction dictionaries
    :param report_type: Type of report ("summary" or "detailed")
    :return: Dictionary containing report data
    """
    if report_type == "summary":
        total = sum(t["amount"] for t in transactions)
        return {"total_transactions": len(transactions), "net_balance": total}

    elif report_type == "detailed":
        return {"transactions": transactions}

    else:
        raise ValueError("Invalid report type. Use 'summary' or 'detailed'.")
#end generate_report

def export_report(report_data: dict, file_format: str = "csv", filename: str = "report"):
    """
    Export the report data to a specified file format. Reusable function for exporting in multiple formats.
    Purpose: Saves the generated report in different formats (CSV, JSON, PDF, etc.).
    Reason.: Provides reusability for different output needs.

    :param report_data: Report dictionary generated by generate_report()
    :param file_format: Output format ("csv" or "json")
    :param filename: Name of the output file (without extension)
    """
    import csv
    import json

    if file_format == "csv":
        with open(f"{filename}.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(report_data.keys())
            writer.writerow(report_data.values())

    elif file_format == "json":
        with open(f"{filename}.json", "w") as file:
            json.dump(report_data, file, indent=4)

    else:
        raise ValueError("Invalid format. Use 'csv' or 'json'.")

    print(f"Report saved as {filename}.{file_format}")
#end export_report