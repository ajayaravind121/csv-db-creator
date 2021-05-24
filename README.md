# csv2DB - An Database Backend Handler
csv2DB is an python module which creates database tables from a csv file. 

## Prerequisite
- Python 3.7+
- Pip
- Git

## Instructions
1. Clone this repo and open a terminal in the repo
```bash
>>> git clone https://github.com/ajayaravind121/csv2db.git
>>> cd csv2db
```
2. Install the python dependency libraries
```
>>> pip install -r requirements.txt
```
3. Run the sample by
```
>>> cd src/
>>> python main.py
```

## Sample Output
[Sample CSV Input]() 

```
Writing CSV to DB(sqllite3)
Storing CSV Records to DB....
Passwords Found. Encrypting Passwords
Successfully written CSV to DB table 'sample'!!!


Reading top records from DB without Decryption
   username                                           password first_name last_name     phone
0     aruie  gAAAAABgq9pQ_w9p0pIoGZfdckVqlWUCesJN3YQXnFnr_f...       Ajay   Aravind  21372189
1      jack  gAAAAABgq9pQmP9_mDYe4HmLRK6wMnPCoERX_wezAcXZil...       Jack     Kirby  12389721
2  stan6969  gAAAAABgq9pQVHJnb_UzbuEm483goabi6Ym19Qg1f05nN1...       Stan       Lee  82412312


Reading DB with Decryption:
   username     password first_name last_name     phone
0     aruie  dsjkfh982hj       Ajay   Aravind  21372189
1      jack  dskjfh38924       Jack     Kirby  12389721
2  stan6969  wiueqiow217       Stan       Lee  82412312
```