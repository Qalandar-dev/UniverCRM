from django.db import connection
from contextlib import closing

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
            dict(zip(columns,row)) for row in cursor.fetchall()
        ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns,row))
    ]

def get_faculties():
    with closing(connection.cursor())as cursor:
        cursor.execute("SELECT * FROM adminapp_faculty")
        faculties = dictfetchall(cursor)
        return faculties

def get_kafedra():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM adminapp_kafedra")
        kafedra = dictfetchall(cursor)
        return kafedra

def get_subject():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM adminapp_subject")
        subject = dictfetchall(cursor)
        return subject

def get_teacher():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM adminapp_teacher")
        teacher = dictfetchall(cursor)
        return teacher

def get_group():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM adminapp_group")
        group = dictfetchall(cursor)
        return group

def get_student():
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM adminapp_student")
        student = dictfetchall(cursor)
        return student
