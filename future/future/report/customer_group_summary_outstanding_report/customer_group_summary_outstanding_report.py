# Copyright (c) 2024, Farhan and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    # Define the columns for the report
    columns = [
        {"label": "Customer Group", "fieldname": "customer_group", "fieldtype": "Data", "width": 150},
        {"label": "Advance Amount", "fieldname": "advance_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Invoice Amount", "fieldname": "invoice_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Paid Amount", "fieldname": "paid_amount", "fieldtype": "Currency", "width": 150},
        {"label": "Sales Return", "fieldname": "sales_return", "fieldtype": "Currency", "width": 150},
        {"label": "Outstanding Amount", "fieldname": "outstanding_amount", "fieldtype": "Currency", "width": 150}
    ]

    # Base SQL query to sum up amounts by Customer Group
    query = """
        SELECT 
            si.customer_group AS customer_group,
            SUM(si.total_advance) AS advance_amount,
            SUM(si.grand_total) AS invoice_amount,
            SUM(si.paid_amount) AS paid_amount,
            SUM(CASE WHEN si.is_return = 1 THEN si.grand_total ELSE 0 END) AS sales_return,
            SUM(si.outstanding_amount) AS outstanding_amount
        FROM
            `tabSales Invoice` si
        WHERE
            si.docstatus = 1
    """

    # Prepare the values for the query
    values = []

    # Add additional filter for customer group if provided
    if filters.get('customer_group'):
        query += " AND si.customer_group = %s"
        values.append(filters.get('customer_group'))

    # Add the posting date filter if provided
    if filters.get('posting_date'):
        query += " AND si.posting_date = %s"
        values.append(filters.get('posting_date'))

    # Group by Customer Group
    query += """
        GROUP BY
            si.customer_group
        ORDER BY
            si.customer_group
    """

    # Execute the query
    raw_data = frappe.db.sql(query, values, as_dict=True)

    # Prepare the data to return
    data = raw_data

    return columns, data