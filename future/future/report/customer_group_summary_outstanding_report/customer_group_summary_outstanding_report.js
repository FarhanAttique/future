// Copyright (c) 2024, Farhan and contributors
// For license information, please see license.txt

frappe.query_reports["Customer-Group-Summary-Outstanding-Report"] = {
	"filters": [
		{
			"fieldname": "posting_date",
			"label": __("Posting Date"),
			"fieldtype": "Date",
			"reqd": 0
		},
		{
			"fieldname": "customer_group",
			"label": __("Customer Group"),
			"fieldtype": "Link",
			"options": "Customer Group",
			"reqd": 0
		}
	]
};

