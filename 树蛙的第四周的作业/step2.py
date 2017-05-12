import MySQLdb

# 方法：去掉头尾和空格，把整型处理成字符型 返回
def prc_line(line):
    _result = line.decode("utf-8").strip().split(" ")
    _result[2] = int(_result[2])
    return _result

def prc_line1(line):
    _result = line.decode("utf-8").strip().split(" ")
    _result[0] = int(_result[0])
    _result[3] = int(_result[3])
    return _result

def prc_line2(line):
    _result = line.decode("utf-8").strip().split(" ")
    _result[0] = int(_result[0])
    _result[2] = int(_result[2])
    return _result

def insertdata():
    # 连接数据库
    conn = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = 'wq43621549fg',
        charset = 'utf8',
        db = 'university',
    )
    # 获取游标
    cur = conn.cursor()
    # 打开师兄给的数据文件
    with open('/home/qin/homework/university/department.txt','r') as fff:
        # 读取全部的行
        content = fff.readlines()
        # 用上面的方法函数把每行的头尾和空格去掉，并且把整型转化为字符串型放进datas里面
        datas = [prc_line(line) for line in content]
        # 取出datas中的元素按类型插入数据库
        for d in datas:
            cur.execute("insert into department (dept_name,building,budget) VALUES ('%s','%s','%d')"%(d[0],d[1],d[2]))
            # 提交请求
            conn.commit()

    # 重复上面操作存入下一张表
    with open('/home/qin/homework/university/student.txt','r') as ff:
        content = ff.readlines()
        datass = [prc_line1(line) for line in content]
        for c in datass:
            cur.execute("insert into student (ID,name,sex,age,emotion_state,dept_name) VALUES ('%d','%s','%s','%d','%s','%s')"%(c[0],c[1],c[2],c[3],c[4],c[5]))
            conn.commit()

    # 重复上面操作存入下一张表
    with open('/home/qin/homework/university/exam.txt','r') as fff:
        content = fff.readlines()
        datas = [prc_line2(line) for line in content]
        for b in datas:
            cur.execute("insert into exam (student_id,exam_Name,grade) VALUES ('%d','%s','%d')"%(b[0],b[1],b[2]))
            conn.commit()

# 调用函数
insertdata()
