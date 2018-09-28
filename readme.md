 - Write an simple read-only API endpoint for companies to get the company name + street+postal_code+city from the headquarter office

 /api/companies/ --> GET
 will return a list of companies + total value of the rent (BONUS)

 - Write an simple read-only API endpoint to get all the offices for a company

 /api/company/offices/?pk=1 --> GET
 will return a list of offices for a selected company

 - Write an API endpoint to change the headquarter of the company

 /api/company/update_headquarter/ --> POST
 Request parameters:
    company_id --> Integer, required
    headquarter_id --> Integer, required

    will validate the passed values and change the company headquarter only if
        -company id is exists
        -office id is exists
        -this company owns this office

to run the tests:
    python manage.py test

