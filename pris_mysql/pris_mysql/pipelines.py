# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PrisMysqlPipeline:
    def process_item(self, item, spider):
        return item

# ReactorInOperationByCountryPipeline
import mysql.connector
class ReactorInOperationByCountryPipeline:
    def __init__(self, mysql_host, mysql_user, mysql_password, mysql_database):
        self.mysql_host = mysql_host
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database

    @classmethod
    def from_crawler(cls, crawler):
        mysql_host = crawler.settings.get('MYSQL_HOST')
        mysql_user = crawler.settings.get('MYSQL_USER')
        mysql_password = crawler.settings.get('MYSQL_PASSWORD')
        mysql_database = crawler.settings.get('MYSQL_DATABASE')

        return cls(mysql_host, mysql_user, mysql_password, mysql_database)

    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host=self.mysql_host,
            user=self.mysql_user,
            password=self.mysql_password,
            database=self.mysql_database
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        sql_select = "SELECT country FROM pris.PRIS_country WHERE country = %s"
        values_select = (item['Country'],)
        self.cursor.execute(sql_select, values_select)
        result = self.cursor.fetchone()

        if result:
            # 国家已存在，更新记录
            sql_update = "UPDATE pris.PRIS_country SET `reactor number in operation` = %s, `Total Net Electrical Capacity [MW] in operation` = %s WHERE country = %s"
            values_update = (item['ReactorNo'], item['ENTC'], item['Country'])
            self.cursor.execute(sql_update, values_update)
        else:
            # 国家不存在，插入新记录
            sql_insert = "INSERT INTO pris.PRIS_country (country, `reactor number in operation`, `Total Net Electrical Capacity [MW] in operation`) VALUES (%s, %s, %s)"
            values_insert = (item['Country'], item['ReactorNo'], item['ENTC'])
            self.cursor.execute(sql_insert, values_insert)

        self.connection.commit()
        return item


# ReactorSuspendedByCountryPipeline    
import mysql.connector
class ReactorSuspendedByCountryPipeline:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE')
        )

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        sql_select = "SELECT country FROM pris.PRIS_country WHERE country = %s"
        values_select = (item['Country'],)
        self.cursor.execute(sql_select, values_select)
        result = self.cursor.fetchone()

        if result:
            # 国家已存在，更新记录
            sql_update = "UPDATE pris.PRIS_country SET `reactor number suspended` = %s, `Total Net Electrical Capacity [MW] suspended` = %s WHERE country = %s"
            values_update = (item['ReactorNo'], item['ENTC'], item['Country'])
            self.cursor.execute(sql_update, values_update)
        else:
            # 国家不存在，插入新记录
            sql_insert = "INSERT INTO pris.PRIS_country (country, `reactor number suspended`, `Total Net Electrical Capacity [MW] suspended`) VALUES (%s, %s, %s)"
            values_insert = (item['Country'], item['ReactorNo'], item['ENTC'])
            self.cursor.execute(sql_insert, values_insert)

        self.conn.commit()
        return item