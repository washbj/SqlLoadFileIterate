# SqlLoadFileIterate
Loads file from the designated folder into given db/table

## Requirements before run
1. Update database credentials under:
  ```
 mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
```
2. Update file location under (ensure sql has access to this file location): 
  ```
    load_file_location = "C:/ProgramData/MySQL/MySQL Server 8.0/Data/new_schema/"
```

## Considerations
1. Files are processed one at a time. If an issue is encountered on the 101st file, the previous 100 files will have been loaded. Remove them from your load folder to prevent duplicate data.
2. Ensure database table is created and ready before load.
