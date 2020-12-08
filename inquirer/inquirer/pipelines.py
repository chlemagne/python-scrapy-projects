# Define your item pipelines here
#
# Don"t forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class InquirerPipeline:
    import re

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("title"):
            if adapter.get("author"):
                match = self.re.match(r"BY:\u00a0 ([^>]+)", adapter["author"])
                adapter["author"] = match.group(
                    1) if match else adapter["author"]

            return item
        else:
            raise DropItem(f"Missing title in {item}")
