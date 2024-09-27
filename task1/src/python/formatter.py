import json
import xml.etree.ElementTree as ET
from datetime import datetime, date
import logging

class DataFormatter:
    @staticmethod
    def format_as_json(data):
        def default(o):
            if isinstance(o, (datetime, date)):
                return o.isoformat()
            raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')

        logging.info("Formatting data as JSON")
        return json.dumps(data, default=default, indent=4)

    @staticmethod
    def format_as_xml(data):
        root = ET.Element("data")
        for key, value_list in data.items():
            category_elem = ET.SubElement(root, key)
            for item in value_list:
                item_elem = ET.SubElement(category_elem, "item")
                for k, v in item.items():
                    child = ET.SubElement(item_elem, k)
                    child.text = str(v)
        logging.info("Formatting data as XML")
        return ET.tostring(root, encoding='unicode')