import mysql.connector
import os


def load_Files(load_file_location, mycursor):
    i = 1
    try:
        for entry in os.scandir(load_file_location):
            if (entry.path.endswith(".csv")
            and entry.is_file()):

                print('File processing:  ' + entry.path)
                sql = """LOAD DATA INFILE \"""" + entry.path + """\" 
                INTO TABLE new_schema.excel_dedup_table 
                FIELDS TERMINATED BY ','	
                ENCLOSED BY '\"'
                ESCAPED BY '\"'
                LINES TERMINATED BY '\\n'
                 IGNORE 1 LINES;"""

                mycursor.execute(sql)
                mydb.commit()
                #print(mycursor)
                print('Files processed: ' + str(i))
                i += 1
    except Exception as e:
        print("Error occurred while loading csv into sql. Files prior to this error have already been processed.")
        print("Specific error: " + str(e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    mycursor = mydb.cursor()
    load_file_location = "C:/ProgramData/MySQL/MySQL Server 8.0/Data/new_schema/"
    load_Files(load_file_location, mycursor)

