import pymysql
con=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=con.cursor()
def create_table():

    try:
        query='''
        create table emp(
        id int primary key,
        name varchar(100),
        mobile bigint unique,
        email varchar(50)
        );
        '''
        cursor.execute(query)
    except pymysql.err.operationalError as e:
        print(f'{e}')

def insert_records():
    query= '''insert into emp(id,name,mobile,email)
    values(1,'hemanth',7815939981,'hemanth@gmail.com')'''    
    cursor.execute(query)
    con.commit()

def get_records():
    query = 'select * from emp'
    cursor.execute(query)
    records = cursor.fetchall()
    for i in records:
        print(i)
    
def  insert_dynamic(id,name,mobile,email):
    record=(id,name,mobile,email)
    query="insert into emp(id,name,mobile,email) valus(%s,%s,%s,%s)"
    cursor.execute(query)
    con.commit()
   
def drop_record(id):
    query=f'delect from emp where id id ={id}'
    cursor.execute(query)
    con.commit()
    print('record removed')   