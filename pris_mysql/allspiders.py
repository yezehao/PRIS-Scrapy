import schedule
import time
import subprocess

def run_spider():
    # define the list of spiders
    spiders = ['pris_age', 'pris_type', 'pris_region', 'pris_trend', 'pris_type']
    # run the sipders countinuously
    for spider in spiders:
        command = f"scrapy crawl {spider}"
        subprocess.run(command, shell=True)

# # run the programme at 12:00 A.M. everyday
# schedule.every().day.at("00:00").do(run_spider)
# run the programme every minute for testing
schedule.every().minute.do(run_spider)

while True:
    schedule.run_pending()
    time.sleep(1)
