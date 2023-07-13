import scrapy

# execute command save in json file: scrapy crawl pris_type -o pris_type.json

class PRISType(scrapy.Spider):
    name = "pris_type"
    start_urls = [
        'https://pris.iaea.org/PRIS/WorldStatistics/OperationalReactorsByType.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/UnderConstructionReactorsByType.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/ShutdownReactorsByType.aspx',
    ]

    def parse(self, response):
        # Extract data for "In Operation" section
        in_operation_table = response.css('.box:contains("In Operation Reactors") + table')
        in_operation_rows = in_operation_table.css('tbody tr')
        for row in in_operation_rows:
            type = row.css('td:nth-child(1)::text').get()
            description = row.css('td:nth-child(2)::text').get()
            capacity = row.css('td:nth-child(3)::text').get()
            reactors = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'In Operation',
                'type': type.strip(),
                'description': description.strip(),
                'capacity': capacity.strip(),
                'reactors': reactors.strip()
            }

        # Extract data for "Suspended Operation" section
        suspended_operation_table = response.css('.box:contains("Suspended Operation Reactors") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            type = row.css('td:nth-child(1)::text').get()
            description = row.css('td:nth-child(2)::text').get()
            capacity = row.css('td:nth-child(3)::text').get()
            reactors = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'Suspended Operation',
                'type': type.strip(),
                'description': description.strip(),
                'capacity': capacity.strip(),
                'reactors': reactors.strip()
            }

        # Extract data for "Under Construction" section
        construction_table = response.css('.box:contains("Under Construction Reactors") + table')
        construction_rows = construction_table.css('tbody tr')
        for row in construction_rows:
            type = row.css('td:nth-child(1)::text').get()
            description = row.css('td:nth-child(2)::text').get()
            capacity = row.css('td:nth-child(3)::text').get()
            reactors = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'Under Construction',
                'type': type.strip(),
                'description': description.strip(),
                'capacity': capacity.strip(),
                'reactors': reactors.strip()
            }

        # Extract data for "Permanent Shutdown" section
        construction_table = response.css('.box:contains("Permanent Shutdown Reactors") + table')
        construction_rows = construction_table.css('tbody tr')
        for row in construction_rows:
            type = row.css('td:nth-child(1)::text').get()
            description = row.css('td:nth-child(2)::text').get()
            capacity = row.css('td:nth-child(3)::text').get()
            reactors = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'Permanent Shutdown',
                'type': type.strip(),
                'description': description.strip(),
                'capacity': capacity.strip(),
                'reactors': reactors.strip()
            }