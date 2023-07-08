import pyodbc


try:
    user_db="hary"
    pass_db="1234"
    db="DB_Test"
    ip="localhost"
    port="1433"
    cnxn = pyodbc.connect("DRIVER={SQL Server};SERVER="+ip+";PORT="+port+";DATABASE="+db+";UID="+user_db+";PWD="+pass_db+"", autocommit=True) 
    cursor = cnxn.cursor()
    print("Koneksi Berhasil")
except Exception as e:
    print("Koneksi Gagal ",e)