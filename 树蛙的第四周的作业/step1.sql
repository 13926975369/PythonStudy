/*
一.
（1）首先要建一个university的库，来分析一下。
（2）首先要有一个学校，需要先有学院，所以我们先建立学院的表department，学院的名字dept_name是首要的，学生表中有一个学院名，肯定是参照学院表中的学院的名字，是学院表的一个外键，所以学院表中的dept_name得是主键。所以我们这里定义dept_name为主键，类型当然是字符啦，长度给一个45差不多，因为是主键不能为空，定义不为空，现在再来分析表中的其他属性，building教学楼，类型取字符，原始的定义为空，可能教学楼还在建设。。budget预算给整形10位就够了，因为预算肯定是数字嘛，十位数的预算已经很夸张了，无符号数，因为预算不可能算成负的吧。。编码格式utf8
（3）这样子我们就有了学院的表了，有了学院的表，再来分析一波，学生和考试的表哪个应该先有，谁参照谁，首先，要有考试得要有学生吧，谁来考试的有个id，每个考试至少得有学生的id吧，要不这个考试不就没意义了嘛。所以exam表的student_ID做学生表的外键，所以学生表的id为主键。
	I.属性ID作为主键，类型为整型，ID嘛，数字嘛，不超过11位嘛。。主键不能为空
	II.属性名字字符型，定义非空，性别字符型一位，m和f表示，年龄整型，情感经历整型，都非空
	III.属性dept_name学院名，字符型，类型和学院表的主键一直，定义为外码，参照学院表中的dept_name项
（4）最后是考试表，定义学生是主键和外键，至少要有学生嘛，所以ID主键外键不能为空，参照学生表中的id，类型相同，然后是考试名字也是主键，因为一个人可以参加多个考试，一个考试可以多个学生，为了避免重复我们要设两个主键，字符型，非空，年级整型无符号（不可能为负嘛），非空
（5）这样子三个表就建好了，相互关联。
*/



/*
-- 学院表
-- dept_name为主键，字符，非空
-- building，类型取字符（45），可空
-- budget，整形10位，无符号，可空
*/

CREATE TABLE `department` (
  `dept_name` varchar(45) NOT NULL,
  `building` varchar(45) DEFAULT NULL,
  `budget` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`dept_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8



/*
-- 学生表
-- ID为主键，整型，非空
-- name，类型取字符（45），非空
-- 性别，类型取短字符（1），非空
-- age，整形11位，非空
-- emotion_state，类型取字符（45），非空
-- dept_name为外键，参照学院表，字符，非空
*/


CREATE TABLE `student` (
  `ID` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `sex` char(1) NOT NULL,
  `age` int(11) NOT NULL,
  `emotion_state` varchar(45) NOT NULL,
  `dept_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `fk_student_1_idx` (`dept_name`),
  CONSTRAINT `fk_student_1` FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8


/*
-- 考试表
-- student_id为主键，字符，非空，外键参照学生表
-- exam_Name，类型取字符（45），非空
-- grade，整形10位，无符号，非空
*/


CREATE TABLE `exam` (
  `student_id` int(11) NOT NULL,
  `exam_Name` varchar(45) NOT NULL,
  `grade` int(10) unsigned NOT NULL,
  PRIMARY KEY (`student_id`,`exam_Name`),
  CONSTRAINT `fk_exam_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8



