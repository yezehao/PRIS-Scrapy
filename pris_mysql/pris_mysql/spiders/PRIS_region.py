import scrapy

# execute command save in MySQL PRIS_region: scrapy crawl pris_region

class PRISRegion(scrapy.Spider):
    name = "pris_region"
    start_urls = [
        'https://pris.iaea.org/PRIS/WorldStatistics/OperationalReactorsByRegion.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/UnderConstructionReactorsByRegion.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/ShutdownReactorsByRegion.aspx',
    ]

    def parse(self, response):
        # Extract data for "In Operation" section
        in_operation_table = response.css('.box:contains("In Operation Reactors") + table')
        in_operation_rows = in_operation_table.css('tbody tr')
        for row in in_operation_rows:
            region = row.css('td:nth-child(1)::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'in operation',
                'region': region.strip(),
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }

        # Extract data for "Suspended Operation" section
        suspended_operation_table = response.css('.box:contains("Suspended Operation") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            region = row.css('td:nth-child(1)::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'suspended',
                'region': region.strip(),
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }

        # Extract data for "Under Construction" section
        construction_table = response.css('.box:contains("Under Construction Reactors") + table')
        construction_rows = construction_table.css('tbody tr')
        for row in construction_rows:
            region = row.css('td:nth-child(1)::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'under construction',
                'region': region.strip(),
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }

        # Extract data for "Permanent Shutdown" section
        construction_table = response.css('.box:contains("Permanent Shutdown Reactors") + table')
        construction_rows = construction_table.css('tbody tr')
        for row in construction_rows:
            region = row.css('td:nth-child(1)::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'permanent shutdown',
                'region': region.strip(),
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }