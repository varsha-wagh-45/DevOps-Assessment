#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

try:
    import pysqlite3
    sys.modules["sqlite3"] = pysqlite3
except ImportError:
    pass

# Patch Django 6.0 compatibility with pysqlite3
try:
    from django.db.backends.sqlite3.features import DatabaseFeatures
    import sqlite3
    
    @property
    def patched_max_query_params(self):
        try:
            return self.connection.connection.getlimit(sqlite3.SQLITE_LIMIT_VARIABLE_NUMBER)
        except (AttributeError, Exception):
            return 999
            
    DatabaseFeatures.max_query_params = patched_max_query_params
except (ImportError, Exception):
    pass


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
