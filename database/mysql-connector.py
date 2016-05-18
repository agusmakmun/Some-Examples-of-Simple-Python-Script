# INSTALL THE MODULE: https://dev.mysql.com/downloads/connector/python/

import sys, datetime
import mysql.connector

try:
    cnx = mysql.connector.connect(
            user='root',
            password='something',
            database='perbankan',
            host='localhost'
    )
    cursor = cnx.cursor()
except:
    print 'Connection Failed!'
    sys.exit()

tanggal = datetime.datetime.now().date()

sql = ("""\
        INSERT INTO transaksi values \
        ('id_nasabahFK', 'no_rekeningFK', 'jenis_transaksi', 'tanggal', 'jumlah') \
        VALUES (%s, %s, %s, %s, %s)\
      """)

data_transaksi = [
    ('9', '100', 'kredit', tanggal, '50000'),
    ('10', '130', 'kontan', tanggal, '90300')
]

for data range(data_transaksi):
    cursor.execute(sql, data)
    cnx.commit()

cursor.close()
cnx.close()
