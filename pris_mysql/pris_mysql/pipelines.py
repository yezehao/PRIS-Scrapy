# Define your item pipelines here
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class PrisMysqlPipeline:
    def process_item(self, item, spider):
        return item

# ================================== #
# MySQL Database pris Table PRIS_age #
# ================================== #
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
    
# ===================================== #
# MySQL Database pris Table PRIS_region #
# ===================================== #
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
        # queries template
        select_query = "SELECT region FROM PRIS_region WHERE region = %s"
        update_query = f"UPDATE PRIS_region SET `reactor number {item['category']}` = %s, `Total Net Electrical Capacity [MW] {item['category']}` = %s WHERE region = %s"
        insert_query = f"INSERT INTO PRIS_region (region, `reactor number {item['category']}`, `Total Net Electrical Capacity [MW] {item['category']}`) VALUES (%s, %s, %s)"
        update_data = (item['reaNo'], item['TNEC'],item['region'])
        insert_data = (item['region'], item['reaNo'], item['TNEC'])
        self.cursor.execute(select_query, (item['region'],))
        existing_record = self.cursor.fetchone()
        if existing_record:
            self.cursor.execute(update_query, update_data)
        else:
            self.cursor.execute(insert_query, insert_data)

        self.cnx.commit()
        return item
# ==================================== #
# MySQL Database pris Table PRIS_trend #
# ==================================== #
class MySQLPipelineTrend:
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
        select_query = "SELECT year FROM PRIS_trend WHERE year = %s"
        update_query1 = (f"UPDATE PRIS_trend SET `reactor number operated` = %s, "
                         f"`Total Net Electrical Capacity [GW]` = %s, "
                         f"`Year-end Total Net Electrical Capacity [GW]` = %s, "
                         f"`Year-end Operational Reactors` = %s "
                         f"WHERE year = %s")
        insert_query1 = (f"INSERT INTO PRIS_trend "
                         f"(year, "
                         f"`reactor number operated`, "
                         f"`Total Net Electrical Capacity [GW]`, "
                         f"`Year-end Total Net Electrical Capacity [GW]`, "
                         f"`Year-end Operational Reactors`) "
                         f"VALUES (%s, %s, %s, %s, %s)")
        update_query2 = f"UPDATE PRIS_trend SET `{item['category']}` = %s WHERE year = %s"
        insert_query2 = f"INSERT INTO PRIS_region (year, `{item['category']}`) VALUES (%s, %s)"

        # Nuclear Power Capacity Trend
        if category == 'Nuclear Power Capacity Trend':
            update_data = (item['reactors_operated'], item['TNEC_t'], item['TNEC_yearend'], item['reactors_operated_yearend'],item['year'])
            insert_data = (item['year'], item['reactors_operated'], item['TNEC_t'], item['TNEC_yearend'], item['reactors_operated_yearend'])
            self.cursor.execute(select_query, (item['year'],))
            existing_record = self.cursor.fetchone()
            if existing_record:
                self.cursor.execute(update_query1, update_data)
            else:
                self.cursor.execute(insert_query1, insert_data)
        # |EAF [%]|UCF [%]|UCL [%]|LF [%]|Electricity Supplied [TW.h]|
        elif category == 'EAF [%]' or 'UCF [%]' or 'UCL [%]' or 'LF [%]' or 'Electricity Supplied [TW.h]':
            update_data = (item[category], item['year'])
            insert_data = (item['year'], item[category])
            self.cursor.execute(select_query, (item['year'],))
            existing_record = self.cursor.fetchone()
            if existing_record:
                self.cursor.execute(update_query2, update_data)
            else:
                self.cursor.execute(insert_query2, insert_data)

        self.cnx.commit()
        return item

# =================================== #
# MySQL Database pris Table PRIS_type #
# =================================== #
class MySQLPipelineType:
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
        select_query = "SELECT type FROM PRIS_type WHERE type = %s"
        update_query = f"UPDATE PRIS_type SET `description` = %s, `reactor number {item['category']}` = %s, `Total Net Electrical Capacity [MW] {item['category']}` = %s WHERE type = %s"
        insert_query = f"INSERT INTO PRIS_type (type, description, `reactor number {item['category']}`, `Total Net Electrical Capacity [MW] {item['category']}`) VALUES (%s, %s, %s, %s)"
        update_data = (item['description'], item['reaNo'], item['TNEC'],item['type'])
        insert_data = (item['type'], item['description'], item['reaNo'], item['TNEC'])
        self.cursor.execute(select_query, (item['type'],))
        existing_record = self.cursor.fetchone()
        if existing_record:
            self.cursor.execute(update_query, update_data)
        else:
            self.cursor.execute(insert_query, insert_data)
        self.cnx.commit()
        return item
    
# ====================================== #
# MySQL Database pris Table PRIS_country #
# ====================================== #
class MySQLPipelineCountry:
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
        # select query
        select_query = "SELECT country FROM PRIS_country WHERE country = %s"

        # Reactor Numbers & TNEC
        update_query1 = (f"UPDATE PRIS_country SET "
                        f"`reactor number {item['category']}` = %s, "
                        f"`Total Net Electrical Capacity [MW] {item['category']}` = %s "
                        f"WHERE country = %s")
        insert_query1 = (f"INSERT INTO PRIS_country (country, `reactor number {item['category']}`, "
                         f"`Total Net Electrical Capacity [MW] {item['category']}`) VALUES (%s, %s, %s)")

        # |EAF|UCF|UCL|(2020-2022 & lifetime up to 2022)   
        update_query2 = (f"UPDATE PRIS_type SET "
                        f"`{item['category']}` = %s, "
                        f"WHERE country = %s")
        insert_query2 = (f"INSERT INTO PRIS_country (country, `{item['category']}`) VALUES (%s, %s)")

        # Nuclear Electricity Supplied [GW.h] & Nuclear Share [%]
        update_query3 = (f"UPDATE PRIS_country SET "
                         f"`{item['category']} Electricity Supplied [GW.h]` = %s, "
                         f"`{item['category']} Share [%]` = %s WHERE country = %s")
        insert_query3 = (f"INSERT INTO PRIS_country (country, `{item['category']} Electricity Supplied [GW.h]`, "
                         f"`{item['category']} Share [%]`) VALUES (%s, %s, %s)")

        self.cursor.execute(select_query, (item['country'],))
        existing_record = self.cursor.fetchone()
        category = item['category']

        if category == 'in operation' or category == 'suspended' or category == 'under construction' or category == 'permanent shutdown':
            update_data1 = (item['reaNo'], item['TNEC'], item['country'])
            insert_data1 = (item['country'], item['reaNo'], item['TNEC'])
            if existing_record:
                self.cursor.execute(update_query1, update_data1)
            else:
                self.cursor.execute(insert_query1, insert_data1)
        elif category == 'EAF' or category == 'UCF' or category == 'UCL':
            update_data2 = (item['[%]'], item['country'])
            insert_data2 = (item['country'], item['[%]'])
            if existing_record:
                self.cursor.execute(update_query2, update_data2)
            else:
                self.cursor.execute(insert_query2, insert_data2)
        elif category == 'Nuclear':
            update_data3 = (item['Nuclear Electricity Supplied [GW.h]'], item['Nuclear Share [%]'], item['country'])
            insert_data3 = (item['country'], item['Nuclear Electricity Supplied [GW.h]'], item['Nuclear Share [%]'])
            if existing_record:
                self.cursor.execute(update_query3, update_data3)
            else:
                self.cursor.execute(insert_query3, insert_data3)

        self.cnx.commit()
        return item