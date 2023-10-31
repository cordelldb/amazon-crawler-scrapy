import mysql.connector
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


# class DatabasePipeline(object):
    
    # def __init__(self):
    #     self.create_connection()
    
    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host = '74.208.230.203',
    #         user = 'janusipm',
    #         password = 'Sunflower$33ds',
    #         database = 'Dioskouroi'
    #     )
    #     self.curr = self.conn.cursor()
        
    # def process_item(self, item, spider):
    #     self.store_in_db(item)
    #     return item
    
    
    # def store_in_db(self, item):
    #     self.curr.execute(""" insert into products values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
    #         item.get("id", ""),
    #         item.get("product_id", ""),
    #         item.get("product_title", ""),
    #         item.get("price", ""),
    #         str(item.get("brand", "")),
    #         str(item.get("color", "")),
    #         str(item.get("material", "")),
    #         str(item.get("style", "")),
    #         str(item.get("model_number", "")),
    #         str(item.get("model_name", "")),
    #         str(item.get("weight", "")),
    #         str(item.get("capacity", "")),
    #         item.get("product_url", ""),
    #         item.get("image_url", ""),
    #     ))
    #     self.conn.commit() 


class DuplicatesPipeline:

    def __init__(self):
        self.products_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['product_id'] in self.products_seen:
            raise DropItem(f"Duplicate item found: {item!r}")
        else:
            self.products_seen.add(adapter['product_id'])
            return item

