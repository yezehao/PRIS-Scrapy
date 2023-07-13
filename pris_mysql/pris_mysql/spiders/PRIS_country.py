import scrapy

# execute command save in json file: scrapy crawl pris_country -o pris_country.json

class PRISCountry(scrapy.Spider):
    name = "pris_country"
    start_urls = [
        'https://pris.iaea.org/PRIS/WorldStatistics/OperationalReactorsByCountry.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/UnderConstructionReactorsByCountry.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/ShutdownReactorsByCountry.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/ThreeYrsEnergyAvailabilityFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/ThreeYrsUnitCapabilityFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/ThreeYrsUnplannedCapabilityLossFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/LifeTimeEnergyAvailabilityFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/LifeTimeUnitCapabilityFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/LifeTimeUnplannedCapabilityLossFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/NuclearShareofElectricityGeneration.aspx',
    ]

    def parse(self, response):
        # Extract data for "In Operation" section
        in_operation_table = response.css('.box:contains("In Operation") + table')
        in_operation_rows = in_operation_table.css('tbody tr')
        for row in in_operation_rows:
            country = row.css('td:nth-child(1) a::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'in operation',
                'country': country,
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }

        # Extract data for "Suspended Operation" section
        suspended_operation_table = response.css('.box:contains("Suspended Operation") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            country = row.css('td:nth-child(1) a::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'suspended',
                'country': country,
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }

        # Extract data for "Under Construction" section
        construction_table = response.css('.box:contains("Under Construction") + table')
        construction_rows = construction_table.css('tbody tr')
        for row in construction_rows:
            country = row.css('td:nth-child(1) a::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'under construction',
                'country': country.strip(),
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }

        # Extract data for "Permanent Shutdown" section
        construction_table = response.css('.box:contains("Permanent Shutdown") + table')
        construction_rows = construction_table.css('tbody tr')
        for row in construction_rows:
            country = row.css('td:nth-child(1) a::text').get()
            capacity = row.css('td:nth-child(2)::text').get()
            reactors = row.css('td:nth-child(3)::text').get()
            yield {
                'category': 'permanent shutdown',
                'country': country.strip(),
                'TNEC': capacity.strip(),
                'reaNo': reactors.strip()
            }

        # Extract data for "EAF" section
        if response.css(':contains("Energy Availability Factor")'): # check EAF
            construction_rows = response.css('#content table tbody tr')
            for row in construction_rows:
                country = row.css('td:nth-child(1)::text').get().strip()
                if response.css('h1:contains("Lifetime")'): # Lifetime EAF up to 2022
                    eaf = row.css('td:nth-child(3)::text').get()
                    category = 'lifetime EAF [%] up tp 2022'
                else: # EAF 2020-2022
                    eaf = row.css('td:nth-child(9)::text').get()
                    category = '2020-2022 EAF [%]'
                if country:
                    yield {
                        'category': category,
                        'country': country,
                        '[%]': eaf.strip() if eaf else None
                    }

        # Extract data for "UCF" section
        if response.css(':contains("Unit Capability Factor")'): # check UCF
            construction_rows = response.css('#content table tbody tr')
            for row in construction_rows:
                country = row.css('td:nth-child(1)::text').get().strip()
                if response.css('h1:contains("Lifetime")'): # Lifetime UCF up to 2022
                    ucf = row.css('td:nth-child(3)::text').get()
                    category = 'lifetime UCF [%] up to 2022'
                else: # UCF 2020-2022
                    ucf = row.css('td:nth-child(9)::text').get()
                    category = '2020-2022 UCF [%]'
                if country:
                    yield {
                        'category': category,
                        'country': country,
                        '[%]': ucf.strip() if ucf else None
                    }

        # Extract data for "UCL 2020-2022" section
        if response.css(':contains("Unplanned Capability Loss Factor")'): # check UCL
            construction_rows = response.css('#content table tbody tr')
            for row in construction_rows:
                country = row.css('td:nth-child(1)::text').get().strip()
                if response.css('h1:contains("Lifetime")'): # Lifetime UCL up to 2022
                    ucl = row.css('td:nth-child(3)::text').get()
                    category = 'lifetime UCL [%] up to 2022'
                else: # UCL 2020-2022
                    ucl = row.css('td:nth-child(9)::text').get()
                    category = '2020-2022 UCL [%]'
                if country:
                    yield {
                        'category': category,
                        'country': country,
                        '[%]': ucl.strip() if ucl else None
                    }

        # Extract data for " Nuclear Share of Electricity Generation" section
        construction_table = response.css('.box:contains(" Nuclear Share of Electricity Generation") + table')
        construction_rows = construction_table.css('tbody tr')
        for row in construction_rows:
            country = row.css('td:first-child a::text').get()
            NE_supplied = row.css('td:nth-child(4)::text').get()
            nuclear_share= row.css('td:nth-child(5)::text').get()
            yield {
                'category': 'Nuclear',
                'country': country,
                'Nuclear Electricity Supplied [GW.h]': NE_supplied.strip(),
                'Nuclear Share [%]': nuclear_share.strip()
            }