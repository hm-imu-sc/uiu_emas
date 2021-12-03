class DBFieldsFileNotFound(Exception):
    
    def __str__(self):
        return "db_fields.json file required !!! format: {\"table_name\": [...field_names...], \"table_name_2\": [...field_names...],}"

class FactoryNotFound(Exception):
    
    def __init__(self, factory_name):
        self.factory_name = factory_name

    def __str__(self):
        return f"'{self.factory_name}' not found !!!"