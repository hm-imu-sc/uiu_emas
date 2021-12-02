class DBFieldsFileNotFound(Exception):
    def __str__(self):
        return "db_fields.json file required !!! format: {\"table_name\": [...field_names...], \"table_name_2\": [...field_names...],}"