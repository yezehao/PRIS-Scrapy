import scrapy

# execute command save in MySQL PROS_age: scrapy crawl pris_age

class PRISAge(scrapy.Spider):
    name = "pris_age"
    start_urls = [
        'https://pris.iaea.org/PRIS/WorldStatistics/OperationalByAge.aspx',
    ]

    def parse(self, response):
        # Extract data for "Age Distribution" section
        in_operation_table = response.css('.box:contains("Age Distribution") + table')
        in_operation_rows = in_operation_table.css('tbody tr')
        for row in in_operation_rows:
            age = row.css('td:nth-child(1)::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'age': age.strip(),
                'TNEC_age': capacity.strip(),
                'reaNo_age': reactors.strip()
            }