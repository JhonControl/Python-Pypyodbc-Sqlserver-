import pypyodbc

cnxn = pypyodbc.connect("DRIVER={SQL Server};SERVER=SERVER-PC\SQLEXPRESS;DATABASE=conexion;UID=sa;PWD=server")

cursor = cnxn.cursor()

cursor.execute("insert into tabla (datos) values ('DATOS INSERTADOS CORRECTAMENTE') ")

print"insercion correcta"

cnxn.commit()
  