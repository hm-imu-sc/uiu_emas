import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'uiu_emas.settings')
import django
django.setup()

from django.db import connection
from django.conf import settings
import json
from .exceptions import DBFieldsFileNotFound

cursor = connection.cursor()

class MySql:
    
    # database = None

    def __init__(self):
        pass

    # def db(self):
    #     if self.database is None:
    #         self.database = MySql()
    #     return self.database

    def get(self, table_name, field_names = ["*"], conditions = None, condition_connector = "and", other_clauses=[]):

        table_fields = self.__get_fields(table_name) if field_names[0] == "*" else field_names

        fields = ""

        for i in range(len(table_fields)):
            fields += table_fields[i]
            if i+1 < len(table_fields):
                fields += ", "

        query = f"select {fields} from {table_name}"

        if conditions is not None:
            query = f"{query} where {self.__prepare_conditions(conditions, condition_connector)}"

        for claus in other_clauses:
            query += f" {claus}"

        data_tuple = self.__query(query)

        return self.__fetch_dict(table_name, data_tuple)

    def exists(self, table_name, conditions, condition_connector="and"):
        return True if self.count(table_name, conditions, condition_connector) else False

    def find(self, table_name, conditions, condition_connector="and"):
        data = self.get(table_name, conditions=conditions, condition_connector=condition_connector)
        return {
            "count": len(data),
            "data": data
        }

    def count(self, table_name, conditions=None, condition_connector="and"):
        query = f"select count(*) from {table_name}"
        if conditions is not None:
            query = f"{query} where {self.__prepare_conditions(conditions, condition_connector)}"
        return self.__query(query)[0][0]

    def insert(self, table_name, rows):

        for field_values in rows:

            fields = "("
            values = "values ("

            field_names = list(field_values.keys())
            for i in range(len(field_names)):
                fields += field_names[i]
                values += f"'{field_values[field_names[i]]}'"
                if i+1 < len(field_names):
                    fields += ", "
                    values += ", "

            fields += ")"
            values += ")"

            query = f"insert into {table_name}{fields} {values}"
            self.__query(query)

    def update(self, table_name, field_values, conditions = None, condition_connector = "and"):
        field_sets = ""

        field_names = list(field_values.keys())

        for i in range(len(field_names)):
            field_sets += f"{field_names[i]}='{field_values[field_names[i]]}'"
            if i+1 < len(field_names):
                field_sets += ", "

        query = f"update {table_name} set {field_sets}"

        if conditions is not None:
            query = f"{query} where {self.__prepare_conditions(conditions, condition_connector)}"

        self.__query(query)

    def delete(self, table_name, conditions = None, condition_connector = "and"):
        query = f"delete from {table_name}"
        if conditions is not None:
            query = f"{query} where {self.__prepare_conditions(conditions, condition_connector)}"
        print(f"[+] Query: {query}")
        return
        self.__query(query)

    def query(self, query):
        return self.__query(query)

    def __prepare_conditions(self, conditions, condition_connector):
        condition_fields = list(conditions.keys())

        condition = ""

        for i in range(len(condition_fields)):
            condition += f"{condition_fields[i]} like '{conditions[condition_fields[i]]}' "
            if i+1 < len(condition_fields):
                condition += f"{condition_connector} "

        return condition

    def __query(self, query):
        cursor.execute(query)
        return cursor.fetchall()

    def __get_fields(self, table_name):
        file = None

        try:
            file = open(settings.BASE_DIR / "db_fields.json", "r")
        except FileNotFoundError:
            raise DBFieldsFileNotFound()

        tables = json.load(file)
        return tables[table_name]

    def __fetch_dict(self, table_name, data_tuple):
        table_fields = self.__get_fields(table_name)

        all_data = []

        for data in data_tuple:
            all_data.append({})
            for i in range(len(data)):
                all_data[-1][table_fields[i]] = data[i]

        return all_data
