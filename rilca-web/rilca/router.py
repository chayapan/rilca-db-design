
"""
See
https://shirishweb.wordpress.com/2018/02/06/python-django-using-multiple-database-inspectdb-and-admin-for-existing-database/

Used in settings.py
"""

class MyDatabaseRouter:

    non_boad_attribute_tables = ['auth', 'admin', 'contenttypes', 'sessions', 'messages', 'staticfiles', 'migrations']
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.non_boad_attribute_tables:
            return 'sqlite'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.non_boad_attribute_tables:
            return 'sqlite'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.non_boad_attribute_tables or obj1._meta.app_label in self.non_boad_attribute_tables:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.non_boad_attribute_tables:
            return db=='sqlite'
        return None
