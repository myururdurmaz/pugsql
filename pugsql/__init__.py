"""
PugSQL is an anti-ORM that facilitates interacting with databases using SQL
in files. A minimal usage example:

    # create a module from sql files on disk
    queries = pugsql.module('path/to/sql/files')

    # connect to the database and use the sql queries as functions
    queries.connect(connection_string)
    queries.update_username(user_id=42, username='mcfunley')

"""
from . import compiler

__version__ = '0.3.4'


def module(sqlpath=None, sqlstr=None, encoding=None):
    """
    Compiles a set of SQL files in the directory specified by sqlpath, and
    returns a module. The module contains a function for each named query
    found in the files.

        # create a module from sql files on disk
        queries = pugsql.module('path/to/sql/files')

        # create a module from sql str
        sqlstr = '''-- :name user_for_id :one
        select * from users where user_id = :user_id'''
        queries = pugsql.module(sqlstr=sqlstr)

        # connect to the database and use the sql queries as functions
        queries.connect(connection_string)
        queries.update_username(user_id=42, username='mcfunley')
    """
    return compiler.Module(sqlpath, sqlstr=sqlstr, encoding=encoding)


__all__ = ['__version__', 'module',]
