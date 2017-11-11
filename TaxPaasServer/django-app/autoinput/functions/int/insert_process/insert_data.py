import sqlite3
from autoinput.functions.decorator import timeit

__all__ = ('insert_data', )


@timeit
def insert_data(rdbs):
    key_list = []
    value_list = []
    for key in rdbs:
        key_list.append(key)
    key_list = sorted(key_list, key=lambda t :int(t))

    for key in key_list:
        value = '' if rdbs[key] == [] else rdbs[key]
        value = str(value) if type(value) != str else value
        value_list.append(value)
    table_name = rdbs['2']
    print("데이터 입력을 시작합니다.")
    conn = sqlite3.connect('TAX.db')
    curs = conn.cursor()
    curs.execute('create table {table_name} (t1 primary key, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18, t19, t20, t21, t22, t23, t24, t25, t26, t27, t28, t29, t30, t31, t32, t33, t34, t35, t36, t37, t38, t39)'.format(table_name=table_name))
    curs.execute('insert into {table_name} values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'.format(table_name=table_name), tuple(value_list))
    conn.commit()
    conn.close()
    print("데이터 입력을 마쳤습니다.")