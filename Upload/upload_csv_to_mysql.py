import csv
import pymysql


CONFIG_PATH = '../config.ini'
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

host = config["DATABASE"]["HOST"]
port = config["DATABASE"]["PORT"]
user = config["DATABASE"]["USER"]
passwd = config["DATABASE"]["PASSWD"]
database = config["DATABASE"]["DB"]

db = pymysql.connect(
    host=host,
    port=int(port),
    user=user,
    passwd=passwd,
    db=database,
    # charset='utf8'
)
cursor = db.cursor()


filepath = "../Food_data/IFood_Food_CH.csv"

with open(filepath, encoding='gb18030') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:       # row: list
        i = i+1
        id = row[0]
        FoodName = row[1]
        Url = row[2]
        Ingredients = row[3]
        Ingredients_Pic = row[4]
        Steps = row[5]
        Steps_Pic = row[6]
        sql = "insert into `1`(`id`,`FoodName`,`Url`,`Ingredients`,`Ingredients_Pic`,`Steps`,`Steps_Pic`) values(%s,%s,%s,%s,%s,%s,%s)"
        values = (id, FoodName, Url, Ingredients, Ingredients_Pic, Steps, Steps_Pic)
        cursor.execute(sql, values)
# sql = "DELETE FROM `1`"
# cursor.execute(sql)
# 提交之前的操作，如果之前已经执行多次的execute，那么就都进行提交
db.commit()

# 关闭cursor对象
cursor.close()
# 关闭connection对象
db.close()
