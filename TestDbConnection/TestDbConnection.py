import psycopg2

# Update connection string information obtained from the portal

host = "postgres"
user = "postgres"
dbname = "GTE-local"
password = "Ameli@2010"
sslmode = "require"

# host = "panoptes-dev1.postgres.database.azure.com"
# user = "postgres@panoptes-dev1"
# dbname = "GTE-Dev"
# password = "peDK5E3qdFwVqf7we8p76MVGOZqO"
# sslmode = "require"


# Construct connection string
# conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
#conn = psycopg2.connect(conn_string)
conn = psycopg2.connect(host="localhost",database="GTE-local", user="postgres", password="peDK5E3qdFwVqf7we8p76MVGOZqO", port = "5433")

print ("Connection established")

cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS ClientData;")
print ("Finished dropping table (if existed)")
# UserId	serial PRIMARY KEY,	FirstName	VARCHAR(50),	LastName	VARCHAR(50),	Employer	VARCHAR(50),	EmployeeId	VARCHAR(50),	GovtID	VARCHAR(50),	Email	VARCHAR(50),	Phone	VARCHAR(50),	Mobile	VARCHAR(50),	SupervisorFirstName	VARCHAR(50),	SupervisorLastName	VARCHAR(50),	SupervisorEmail	VARCHAR(50),

# Create table
cursor.execute("CREATE TABLE ClientData (id serial PRIMARY KEY, LEI TEXT, EntityLegalName TEXT)") #
conn.commit()
print ("Finished creating table")

# Insert some data into table
#cursor.execute("INSERT INTO ClientEmployee (firstName, secondName, govtID) VALUES (%s, %s, %s);", ("red","Jones", "A150160170"))
#cursor.execute("INSERT INTO ClientEmployee (firstName, secondName, govtID) VALUES (%s, %s, %s);", ("reda","Jonesa", "B150160170"))
#cursor.execute("INSERT INTO ClientEmployee (firstName, secondName, govtID) VALUES (%s, %s, %s);", ("red","Iones", "C150160170"))
print ("Inserted 3 rows of data")

# Cleanup
conn.commit()
cursor.close()
conn.close()
