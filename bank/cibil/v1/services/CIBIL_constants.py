ACCOUNT_SUMMARY_STARTER = 'summary:'
FIRST_ACCOUNT_SUMMARY_RECTIFIER = 'account dates amounts status'
ACCOUNT_SUMMARY_SPLITTER = r'days past due/asset classification'
ACCOUNT_SUMMARY_RECTIFIER = r'\(up to 36 months; left to right\)(.*)member name:'
ACCOUNT_DBP_REGEX = r'[a-z,0-9]{3} \d{2}-\d{2}'

LOAN_ACCOUNT_ENQUIRY_STARTER = 'enquiries:'
LOAN_ACCOUNT_ENQUIRY_FINISHER = 'end of report on'
LOAN_ACCOUNT_ENQUIRY_AMOUNT_CLEANER = r'\d{2}-\d{2}-\d{4}'

ADDRESS_DATA_SPLITTER = r'address[\(e\)]*:'

LOAN_ACCOUNT_ENQUIRY_CLEANERS = {
    'footer': r'(2016|2017|2018) transunion cibil limited\. \(formerly: credit information bureau \(india\) limited\)\. all rights reserved\. page \d{1,2} of transunion cibil cin : u72300mh2000plc128359 \d{1,2} consumer cir consumer: [a-z,\s]+ member id: nb75031001_1 member reference number:',
    'header': r'date:\d{2}-\d{2}-\d{4} time: \d{2}:\d{2}:\d{2} control number: [0-9,\,]+',
    'footer_partial': r'(2016|2017|2018) transunion cibil limited\. \(formerly: credit information bureau \(india\) limited\)\. all rights reserved\. page \d{1,2} of transunion cibil cin : u72300mh2000plc128359',
    'header_date': r'date:\d{2}-\d{2}-\d{4}',
    'header_time': r'time: \d{2}:\d{2}:\d{2}',
    'header_control_number': r'control number: [0-9,\,]+',
}

CIBIL_ATTRIBUTES = {
    'cibil_score_data': {
        'attribute_list': [
            'cibil_score',
            'cibil_comments',
        ],
        'attribute_data': {
            'cibil_score': {
                'regex': r'cibil\s*transunion\s*score\s*version\s*2.0\s*(\d{1,3}|-1)',
                'name': 'CIBIL Score',
                'explanation': 'The CIBIL Score of the User',
                'attribute_type': 'integer'
            },
            'cibil_comments': {
                'regex': r'cibil transunion score version 2.0 -1|\d{1,3} (1: [0-9,a-z,:,\.,\s,\,-]+) possible range',
                'name': 'CIBIL Comments',
                'explanation': 'The Comments on the customers CIBIL Report',
                'attribute_type': 'string'
            },
        },
        'info': 'CIBIL 2.0 Score of the User, Given by Transunion',
    },
    'cibil_contact_data': {
        'attribute_list': [
            'telephone_type',
            'telephone_number',
            'email',
            'address_category',
            'address_code',
            'address_report_date',
        ],
        'attribute_data': {
            'telephone_email_data': {
                'regex': r'(telephone type .* address\(es\):)',
                'name': 'Telephone Data',
                'explanation': 'Telephone Data',
                'attribute_type': 'string'
            },
            'telephone_type': {
                'regex': r'[a-z]+ phone[\(e\)]* |not classified[\(e\)]* telephone number',
                'name': 'Telephone Number Type',
                'explanation': 'Telephone Number Type',
                'attribute_type': 'string'
            },
            'telephone_number': {
                'regex': r' (\d{8,15})',
                'name': 'Telephone Number',
                'explanation': 'Telephone Number',
                'attribute_type': 'string'
            },
            'email': {
                'regex': r'(\b[\w.-]+?@\w+?\.\w+?\b)',
                'name': 'Email',
                'explanation': 'Email of the User',
                'attribute_type': 'string'
            },
            'address_data': {
                'regex': r'(address\(es\): .* employment information\s*:)',
                'name': 'Telephone Number',
                'explanation': 'Telephone Number',
                'attribute_type': 'string'
            },
            'address_category': {
                'regex': r'category:([a-z]+ [a-z]+)',
                'name': 'Address Category',
                'explanation': 'Address Category',
                'attribute_type': 'string'
            },
            'address_code': {
                'regex': r'residence code:([a-z,0-9]*)',
                'name': 'Address Code',
                'explanation': 'Address Code',
                'attribute_type': 'string'
            },
            'address_report_date': {
                'regex': r'date reported:(\d{2}-\d{2}-\d{4})',
                'name': 'Address Report Date',
                'explanation': 'Address Report Date',
                'attribute_type': 'date'
            },

        },
        'info': 'Contact data of the User',
    },
    'cibil_kyc_data': {
        'attribute_list': [
            'name',
            'birth_date',
            'gender',
            'pan',
            'pan_issue_date',
            'pan_expiry_date',
            'aadhaar',
            'aadhaar_issue_date',
            'aadhaar_expiry_date',
            'driving_license',
            'driving_license_issue_date',
            'driving_license_expiry_date',
            'passport_number',
            'passport_number_issue_date',
            'passport_number_expiry_date',
            'voter_id',
            'voter_id_issue_date',
            'voter_id_expiry_date',
            'ration_card',
            'ration_card_issue_date',
            'ration_card_expiry_date',
        ],
        'attribute_data': {
            'name': {
                'regex': r'consumer information: name:([a-z,0-9,/,-,:,\s]+) date of birth: \d{2}-\d{2}-\d{4}',
                'name': 'Customer Name',
                'explanation': 'The name of the User',
                'attribute_type': 'string'
            },
            'birth_date': {
                'regex': r'consumer information: name:[a-z,0-9,/,-,:,\s]+ date of birth: (\d{2}-\d{2}-\d{4})',
                'name': 'Birth Date',
                'explanation': 'Birth date of the User',
                'attribute_type': 'date'
            },
            'gender': {
                'regex': r'gender\s*:\s*([a-z]+)',
                'name': 'Gender',
                'explanation': 'Gender of the User',
                'attribute_type': 'string'
            },
            'pan': {
                'regex': r'income tax id number \(pan\) ([a-z]{5}\d{4}[a-z]{1}) ',
                'name': 'PAN',
                'explanation': 'PAN of the User',
                'attribute_type': 'string'
            },
            'pan_issue_date': {
                'regex': r'income tax id number \(pan\) [a-z]{5}\d{4}[a-z]{1} (\d{2}-\d{2}-\d{4}) ',
                'name': 'PAN Issue date',
                'explanation': 'PAN Issue date of the User',
                'attribute_type': 'date'
            },
            'pan_expiry_date': {
                'regex': r'income tax id number \(pan\) [a-z]{5}\d{4}[a-z]{1} \d{2}-\d{2}-\d{4} (\d{2}-\d{2}-\d{4}) ',
                'name': 'PAN Expiry date',
                'explanation': 'PAN Expiry date of the User',
                'attribute_type': 'date'
            },
            'aadhaar': {
                'regex': r'universal id number \(uid\) (\d{12})',
                'name': 'AADHAAR',
                'explanation': 'AADHAAR of the User',
                'attribute_type': 'string'
            },
            'aadhaar_issue_date': {
                'regex': r'universal id number \(uid\) \d{12} (\d{2}-\d{2}-\d{4}) ',
                'name': 'AADHAAR Issue date',
                'explanation': 'AADHAAR Issue date of the User',
                'attribute_type': 'date'
            },
            'aadhaar_expiry_date': {
                'regex': r'universal id number \(uid\) \d{12} \d{2}-\d{2}-\d{4} (\d{2}-\d{2}-\d{4}) ',
                'name': 'AADHAAR Expiry date',
                'explanation': 'AADHAAR Expiry date of the User',
                'attribute_type': 'date'
            },
            'driving_license': {
                'regex': r'driver\'s license number[\(e\)]* ([a-z,0-9,/,-]+[0-9,\s]+) ',
                'name': 'Driving License',
                'explanation': 'Driving License of the User',
                'attribute_type': 'string'
            },
            'driving_license_issue_date': {
                'regex': r'driver\'s license number[\(e\)]* [a-z,0-9,/,-]+[0-9,\s]+ (\d{2}-\d{2}-\d{4}) ',
                'name': 'Driving License Issue date',
                'explanation': 'Driving License Issue date of the User',
                'attribute_type': 'date'
            },
            'driving_license_expiry_date': {
                'regex': r'driver\'s license number[\(e\)]* [a-z,0-9,/,-]+[0-9,\s]+ \d{2}-\d{2}-\d{4} (\d{2}-\d{2}-\d{4}) ',
                'name': 'Driving License Expiry date',
                'explanation': 'Driving License Expiry date of the User',
                'attribute_type': 'date'
            },
            'passport_number': {
                'regex': r'passport number[\(e\)]* ([a-z,0-9]+) ',
                'name': 'Passport Number',
                'explanation': 'Passport Number of the User',
                'attribute_type': 'string'
            },
            'passport_number_issue_date': {
                'regex': r'passport number[\(e\)]* [a-z,0-9]+ (\d{2}-\d{2}-\d{4}) ',
                'name': 'Passport Number Issue date',
                'explanation': 'Passport Number Issue date of the User',
                'attribute_type': 'date'
            },
            'passport_number_expiry_date': {
                'regex': r'passport number[\(e\)]* [a-z,0-9]+ \d{2}-\d{2}-\d{4} (\d{2}-\d{2}-\d{4}) ',
                'name': 'Passport Number Expiry date',
                'explanation': 'Passport Number Expiry date of the User',
                'attribute_type': 'date'
            },
            'voter_id': {
                'regex': r'voter id number[\(e\)]* ([a-z,0-9]+) ',
                'name': 'Voter Id',
                'explanation': 'Voter Id of the User',
                'attribute_type': 'string'
            },
            'voter_id_issue_date': {
                'regex': r'voter id number[\(e\)]* [a-z,0-9]+ (\d{2}-\d{2}-\d{4}) ',
                'name': 'Voter Id Issue date',
                'explanation': 'Voter Id Issue date of the User',
                'attribute_type': 'date'
            },
            'voter_id_expiry_date': {
                'regex': r'voter id number[\(e\)]* [a-z,0-9]+ \d{2}-\d{2}-\d{4} (\d{2}-\d{2}-\d{4}) ',
                'name': 'Voter Id Expiry date',
                'explanation': 'Voter Id Expiry date of the User',
                'attribute_type': 'date'
            },
            'ration_card': {
                'regex': r'ration card number[\(e\)]* (\d+) ',
                'name': 'Ration Card',
                'explanation': 'Ration Card of the User',
                'attribute_type': 'string'
            },
            'ration_card_issue_date': {
                'regex': r'ration card number[\(e\)]* \d+ (\d{2}-\d{2}-\d{4}) ',
                'name': 'Ration Card Issue date',
                'explanation': 'Ration Card Issue date of the User',
                'attribute_type': 'date'
            },
            'ration_card_expiry_date': {
                'regex': r'ration card number[\(e\)]* \d+ \d{2}-\d{2}-\d{4} (\d{2}-\d{2}-\d{4}) ',
                'name': 'Ration Card Expiry date',
                'explanation': 'Ration Card Expiry date of the User',
                'attribute_type': 'date'
            },
        },
        'info': 'KYC data obtained from CIBIL 2.0 Report, Given by Transunion',
    },
    'loan_accounts_summary_data': {
        'attribute_list': [
            'total_loan_accounts',
            'total_loan_accounts_overdue',
            'total_loan_accounts_zero_balance',
            'total_amount_sanctioned',
            'total_amount_current',
            'total_amount_overdue',
            'last_reporting_date',
            'credit_history_since_date',
        ],
        'attribute_data': {
            'total_loan_accounts': {
                'regex': r'accounts\s*total:\s*(\d*)\s*overdue:\s*\d*\s*zero-balance:\s*\d*',
                'name': 'Total Loan Accounts',
                'explanation': 'Number of Loan Accounts the User have had up till the generation of the report.',
                'attribute_type': 'integer'
            },
            'total_loan_accounts_overdue': {
                'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*(\d*)\s*zero-balance:\s*\d*',
                'name': 'Total Loan Accounts Over',
                'explanation': 'Number of Loan Accounts the User have and loan repayment is running late',
                'attribute_type': 'integer'
            },
            'total_loan_accounts_zero_balance': {
                'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*\d*\s*zero-balance:\s*(\d*)',
                'name': 'Total Loan Accounts Zero Balance',
                'explanation': 'Number of Loan Accounts the User have and which has successfulled repaid and closed',
                'attribute_type': 'integer'
            },
            'total_amount_sanctioned': {
                'regex': r'high\s*cr/sanc\.\s*amt:\s*([0-9,\,]+)\s*current:\s*[0-9,\,]+\s*overdue:\s*[0-9,\,]+',
                'name': 'Total Amount Sanctioned',
                'explanation': 'Total Loans Amount disbursed to the User.',
                'attribute_type': 'amount'
            },
            'total_amount_current': {
                'regex': r'high\s*cr/sanc\.\s*amt:\s*[0-9,\,]+\s*current:\s*([0-9,\,]+)\s*overdue:\s*[0-9,\,]+',
                'name': 'Total Amount Current',
                'explanation': ' Total Loans Amount which is yet to be paid by the User',
                'attribute_type': 'amount'
            },
            'total_amount_overdue': {
                'regex': r'high\s*cr/sanc\.\s*amt:\s*[0-9,\,]+\s*current:\s*[0-9,\,]+\s*overdue:\s*([0-9,\,]+)',
                'name': 'Total Amount Over Due',
                'explanation': 'Total Loans Amount which is not paid by the User and is overdue',
                'attribute_type': 'amount'
            },
            'last_reporting_date': {
                'regex': r'recent:\s*(\d{2}-\d{2}-\d{4})\s*oldest:\s*\d{2}-\d{2}-\d{4}',
                'name': 'Last Reporting Date',
                'explanation': 'Date at which the last CIBIL enquiry was made for the User',
                'attribute_type': 'date'
            },
            'credit_history_since_date': {
                'regex': r'recent:\s*\d{2}-\d{2}-\d{4}\s*oldest:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Credit History Since Date',
                'explanation': 'Date at which the first CIBIL enquiry was made for the User',
                'attribute_type': 'date'
            },
        },
        'info': 'Summary of all the Loan accounts of the User',
    },
    'loan_enquiry_summary_data': {
        'attribute_list': [
            'total_loan_enquiries',
            'total_loan_enquiries_30_days',
            'total_loan_enquiries_12_months',
            'total_loan_enquiries_24_months',
            'last_date_of_enquiry',
        ],
        'attribute_data': {
            'total_loan_enquiries': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*(\d*)\s*\d*\s*\d*\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Total',
                'attribute_type': 'integer'
            },
            'total_loan_enquiries_30_days': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*(\d*)\s*\d*\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 30 Days',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in past 30 Days',
                'attribute_type': 'integer'
            },
            'total_loan_enquiries_12_months': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*(\d*)\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 12 Months',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 12 Months',
                'attribute_type': 'integer'
            },
            'total_loan_enquiries_24_months': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*\d*\s*(\d*)\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 24 Months',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 24 Months',
                'attribute_type': 'integer'
            },
            'last_date_of_enquiry': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*\d*\s*\d*\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Last Date of Loan Enquiry',
                'explanation': 'Last date of loan enquiry which has been made by lender for the given user',
                'attribute_type': 'date'
            },
        },
        'info': 'Summary of the Loan Enquiry made by the Lenders for the User',
    },
    'loan_accounts_data': {
        'attribute_list': [
            'account_type',
            'account_ownership',
            'account_open_date',
            'account_close_date',
            'account_last_reported_date',
            'account_emi_start_date',
            'account_emi_end_date',
            'credit_card_highest_amount',
            'current_balance',
            'credit_card_credit_limit',
            'credit_card_cash_limit',
            'sanctioned_amount',
            'overdue_amount',
            'emi_frequency',
            'emi',
            'interest_rate',
            'actual_payment',
            'last_payment',
            'write_off',
            'write_off_total',
            'write_off_principal',
            'collateral_type',
            'repayment_tenure',
        ],
        'attribute_data': {
            'account_type': {
                'regex': r'type:\s*(other|[a-zA-z,-,\s]+ card|overdraft|[a-zA-z,-,\s]+ loan)',
                'name': 'Loan Account Type',
                'explanation': 'Loan account type in the Loan accounts information for the Users',
                'attribute_type': 'string'
            },
            'account_ownership': {
                'regex': r'ownership:\s*(individual|authorized\s*user|guarantor|joint)',
                'name': 'Loan Account Ownership',
                'explanation': 'Loan account ownership in the Loan accounts information for the Users',
                'attribute_type': 'string'
            },
            'account_open_date': {
                'regex': r'opened:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account Open Date',
                'explanation': 'Date the account was opened. For credit cards and fleet cards, this is the date the card becomes active',
                'attribute_type': 'date'
            },
            'account_close_date': {
                'regex': r'closed:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account Close Date',
                'explanation': 'Date the account was Closed',
                'attribute_type': 'date'
            },
            'account_last_reported_date': {
                'regex': r'reported\s*and\s*certified:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account Last Reported Date',
                'explanation': 'The most recent date the reporting member reported information about the account to CIBIL',
                'attribute_type': 'date'
            },
            'account_emi_start_date': {
                'regex': r'pmt\s*hist\s*start:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account EMI Start Date',
                'explanation': 'EMI start Date for this Loan Account',
                'attribute_type': 'date'
            },
            'account_emi_end_date': {
                'regex': r'pmt\s*hist\s*end:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account EMI End Date',
                'explanation': 'EMI End Date for this Loan Account',
                'attribute_type': 'date'
            },
            'credit_card_highest_amount': {
                'regex': r'high\s*credit:\s*([0-9,\,]+)',
                'name': 'Highest Amount Drawn from Credit Card',
                'explanation': 'Highest Amount Drawn from Credit Card. This applies in case of Credit Card account',
                'attribute_type': 'amount'
            },
            'current_balance': {
                'regex': r'current\s*balance:\s*([0-9,\,]+)',
                'name': 'Current Balance of the Loan Account',
                'explanation': 'The sum of the entire amount of credit/loan outstanding, including the current and overdue portion, if any, together with interest last applied for all the accounts. A negative sign indicates a credit balance',
                'attribute_type': 'amount'
            },
            'credit_card_credit_limit': {
                'regex': r'credit\s*limit:\s*([0-9,\,]+)',
                'name': 'Credit Limit for Credit Card. This applies in case of Credit Card account',
                'explanation': 'Credit Limit for Credit Card',
                'attribute_type': 'amount'
            },
            'credit_card_cash_limit': {
                'regex': r'cash\s*limit:\s*([0-9,\,]+)',
                'name': 'Cash Limit for Credit Card. This applies in case of Credit Card account',
                'explanation': 'Cash Limit for Credit Card',
                'attribute_type': 'amount'
            },
            'sanctioned_amount': {
                'regex': r'sanctioned:\s*([0-9,\,]+)',
                'name': 'Total amount Sanctioned',
                'explanation': 'Total amount Sanctioned for this Loan account',
                'attribute_type': 'amount'
            },
            'overdue_amount': {
                'regex': r'overdue:\s*([0-9,\,]+)',
                'name': 'Total amount the account is past due',
                'explanation': 'Total amount the account is past due for this Loan account',
                'attribute_type': 'amount'
            },
            'emi_frequency': {
                'regex': r'pmt\s*freq:\s*([weekly|fortnightly|monthly|quarterly]+)',
                'name': 'EMI Frequency',
                'explanation': 'EMI Frequency for the given Loan Account',
                'attribute_type': 'string'
            },
            'emi': {
                'regex': r'emi:\s*([0-9,\,]+)',
                'name': 'EMI Amount',
                'explanation': 'EMI Amount for the given Loan Account',
                'attribute_type': 'amount'
            },
            'interest_rate': {
                'regex': r'interest\s*rate:\s*(\d{2}\.\d{3})',
                'name': 'Interest Rate',
                'explanation': 'Interest Rate for the given Loan Account',
                'attribute_type': 'decimal'
            },
            'actual_payment': {
                'regex': r'actual\s*payment:\s*([0-9,\,]+)',
                'name': 'Actual Payment',
                'explanation': 'Actual Payment done for the given Loan Account',
                'attribute_type': 'amount'
            },
            'last_payment': {
                'regex': r'last payment:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Last Payment',
                'explanation': 'Last Payment date for the given Loan Account',
                'attribute_type': 'date'
            },
            'write_off': {
                'regex': r'written\s*off\s*/\s*settled\s*status:\s*(written-off|settled|[0-9,\,]+)',
                'name': 'Write off or Settled',
                'explanation': 'Is the Loan Account Written off or Settled',
                'attribute_type': 'string'
            },
            'write_off_total': {
                'regex': r'written\s*off\s*\(total\)\s*:\s*([0-9,\,]+)',
                'name': 'Write off Total',
                'explanation': 'Total Write off Amount for the Loan Account',
                'attribute_type': 'amount'
            },
            'write_off_principal': {
                'regex': r'written\s*off\s*\(principal\)\s*:\s*([0-9,\,]+)',
                'name': 'Write off Principal',
                'explanation': 'Principal Write off Amount for the Loan Account',
                'attribute_type': 'amount'
            },
            'collateral_type': {
                'regex': r'collateral\s*type:\s*(no collateral|[a-zA-z,-,\s]+)',
                'name': 'Collateral Type',
                'explanation': 'Type of collateral used in the loan',
                'attribute_type': 'string'
            },
            'repayment_tenure': {
                'regex': r'repayment tenure:\s*(\d+)',
                'name': 'Repayment Tenure',
                'explanation': 'No of Repayment Cycles',
                'attribute_type': 'integer'
            },
        },
        'info': 'Loan Accounts Information of the User, Given by CIBIL 2.0 Transunion',
    },
    'loan_accounts_dpd_data': {
        'attribute_list': [
            'dpd',
            'dpd_month',
            'dpd_year',
        ],
        'attribute_data': {
            'dpd': {
                'regex': r'([a-z,0-9]{3}) \d{2}-\d{2}',
                'name': 'Days Past Due or The Code',
                'explanation': 'Number of days past due or the code',
                'attribute_type': 'string'
            },
            'dpd_month': {
                'regex': r'[a-z,0-9]{3} (\d{2})-\d{2}',
                'name': 'Month',
                'explanation': 'Month of the DPD',
                'attribute_type': 'integer'
            },
            'dpd_year': {
                'regex': r'[a-z,0-9]{3} \d{2}-(\d{2})',
                'name': 'Year',
                'explanation': 'Year of the DPD',
                'attribute_type': 'integer'
            },
        },
        'info': 'CIBIL 2.0 Score of the User, Given by Transunion',
    },
    'loan_accounts_enquiry_data': {
        'attribute_list': [
            'enquiry_date',
            'enquiry_amount',
            'enquiry_purpose',
        ],
        'attribute_data': {
            'enquiry_date': {
                'regex': r'(\d{2}-\d{2}-\d{4})',
                'name': 'Date of Enquiry',
                'explanation': 'Date of Enquiry',
                'attribute_type': 'date'
            },
            'enquiry_amount': {
                'regex': r'([0-9,\,]*\d{1}\,\d{3}|\d{1,3}) ',
                'name': 'Enquiry Amount',
                'explanation': 'Enquiry Amount',
                'attribute_type': 'decimal'
            },
            'enquiry_purpose': {
                'regex': r'(other|[a-z]+ card|[a-z]+ loan)',
                'name': 'Purpose of Enquiry',
                'explanation': 'Purpose of Enquiry',
                'attribute_type': 'string'
            },
        },
        'info': 'Enqiry Data Loan account wise',
    },
}
