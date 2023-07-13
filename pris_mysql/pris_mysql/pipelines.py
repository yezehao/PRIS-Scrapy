# Define your item pipelines here
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class PrisMysqlPipeline:
    def process_item(self, item, spider):
        return item

# MySQL Database pris Table PRIS_age
class MySQLPipelineAge:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD')
        )

    def open_spider(self, spider):
        self.cnx = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.cnx.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()

    def process_item(self, item, spider):
        # queries template
        select_query = "SELECT age FROM PRIS_age WHERE age = %s"
        update_query = " UPDATE PRIS_age SET `reactor number` = %s, `Total Net Electrical Capacity [MW]` = %s WHERE age = %s"
        insert_query = "INSERT INTO PRIS_age (age, `reactor number`, `Total Net Electrical Capacity [MW]`) VALUES (%s, %s, %s)"
        update_data = (item['reaNo_age'], item['TNEC_age'], item['age'])
        insert_data = (item['age'], item['reaNo_age'], item['TNEC_age'])
        self.cursor.execute(select_query, (item['age'],))
        existing_record = self.cursor.fetchone()

        if existing_record:
            self.cursor.execute(update_query, update_query)
        else:
            self.cursor.execute(insert_query, insert_data)

        self.cnx.commit()
        return item
    

# MySQL Database pris Table PRIS_region
class MySQLPipelineRegion:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD')
        )

    def open_spider(self, spider):
        self.cnx = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.cnx.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.cnx.close()

    def process_item(self, item, spider):
        category = item['category']
        # queries template
        select_query = "SELECT region FROM PRIS_region WHERE region = %s"
        update_query = f"UPDATE PRIS_region SET `reactor number {item['category']}` = %s, `Total Net Electrical Capacity [MW] {item['category']}` = %s WHERE region = %s"
        insert_query = f"INSERT INTO PRIS_region (region, `reactor number {item['category']}`, `Total Net Electrical Capacity [MW] {item['category']}`) VALUES (%s, %s, %s)"

        # reactors in operation
        if category == 'in operation':
            update_data = (item['reaNo_io'], item['TNEC_io'],item['region_io'])
            insert_data = (item['region_io'], item['reaNo_io'], item['TNEC_io'])
            self.cursor.execute(select_query, (item['region_io'],))
            # existing_record = self.cursor.fetchone()
        # reactors suspended operation
        elif category == 'suspended':
            update_data = (item['reaNo_so'], item['TNEC_so'], item['region_so'])
            insert_data = (item['region_so'], item['reaNo_so'], item['TNEC_so'])
            self.cursor.execute(select_query, (item['region_so'],))
            # existing_record = self.cursor.fetchone()
        # reactors under construction 
        elif category == 'under construction':
            update_data = (item['reaNo_uc'], item['TNEC_uc'], item['region_uc'])
            insert_data = (item['region_uc'], item['reaNo_uc'], item['TNEC_uc'])
            self.cursor.execute(select_query, (item['region_uc'],))
            # existing_record = self.cursor.fetchone()
        # reactors permanent shurdown
        elif category == 'permanent shutdown':
            update_data = (item['reaNo_ps'], item['TNEC_ps'], item['region_ps'])
            insert_data = (item['region_ps'], item['reaNo_ps'], item['TNEC_ps'])
            self.cursor.execute(select_query, (item['region_ps'],))

        existing_record = self.cursor.fetchone()
        if existing_record:
            self.cursor.execute(update_query, update_data)
        else:
            self.cursor.execute(insert_query, insert_data)

        self.cnx.commit()
        return item
