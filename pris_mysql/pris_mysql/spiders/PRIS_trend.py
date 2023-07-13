import scrapy

# execute command save in json file: scrapy crawl pris_trend -o pris_trend.json

class PRISTrend(scrapy.Spider):
    name = "pris_trend"
    start_urls = [
        'https://pris.iaea.org/PRIS/WorldStatistics/WorldTrendNuclearPowerCapacity.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/WorldTrendinEnergyAvailabilityFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/WorldTrendinUnitCapabilityFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/WorldTrendinUnplannedCapabilityLossFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/WorldTrendinAverageLoadFactor.aspx',
        'https://pris.iaea.org/PRIS/WorldStatistics/WorldTrendinElectricalProduction.aspx',
    ]

    def parse(self, response):
        # Extract data for "Nuclear Power Capacity Trend" section
        in_operation_table = response.css('.box:contains("Nuclear Power Capacity Trend") + table')
        in_operation_rows = in_operation_table.css('tbody tr')
        for row in in_operation_rows:
            age = row.css('td:nth-child(1)::text').get()
            TNEC = row.css('td:nth-child(2)::text').get()
            reactors_operated = row.css('td:nth-child(3)::text').get()
            TNEC_yearend = row.css('td:nth-child(4)::text').get()
            reactors_operated_yearend = row.css('td:nth-child(5)::text').get()
            yield {
                'category': 'Nuclear Power Capacity Trend',
                'age': age.strip(),
                'TNEC': TNEC.strip(),
                'reactors_operated': reactors_operated.strip(),
                'TNEC_yearend': TNEC_yearend.strip(),
                'reactors_operated_yearend': reactors_operated_yearend.strip()
            }

        # Extract data for "Energy Availability Factor Trend" section
        suspended_operation_table = response.css('.box:contains("Energy Availability Factor Trend") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            year = row.css('td:nth-child(1)::text').get()
            EAF = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'EAF Trend',
                'year': year.strip(),
                'EAF [%]': EAF.strip()
            }

        # Extract data for "Unit Capability Factor Trend" section
        suspended_operation_table = response.css('.box:contains("Unit Capability Factor Trend") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            year = row.css('td:nth-child(1)::text').get()
            UCF = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'UCF Trend',
                'year': year.strip(),
                'UCF [%]': UCF.strip()
            }

        # Extract data for "Unplanned Capability Loss Factor Trend" section
        suspended_operation_table = response.css('.box:contains("Unplanned Capability Loss Factor Trend") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            year = row.css('td:nth-child(1)::text').get()
            UCL = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'UCL Trend',
                'year': year.strip(),
                'UCL [%]': UCL.strip()
            }

        # Extract data for "Load Factor Trend" section
        suspended_operation_table = response.css('.box:contains("Load Factor Trend") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            year = row.css('td:nth-child(1)::text').get()
            LF = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'LF Trend',
                'year': year.strip(),
                'LF [%]': LF.strip()
            }
    

        # Extract data for "Trend in Electricity Supplied" section
        suspended_operation_table = response.css('.box:contains("Trend in Electricity Supplied") + table')
        suspended_operation_rows = suspended_operation_table.css('tbody tr')
        for row in suspended_operation_rows:
            year = row.css('td:nth-child(1)::text').get()
            TES = row.css('td:nth-child(4)::text').get()
            yield {
                'category': 'Trend in Electricity Supplied',
                'year': year.strip(),
                'Electricity Supplied [TW.h]': TES.strip()
            }