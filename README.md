# 美食识别系统
 本项目主要用于对美食识别，并进行菜品制作推荐与个性化模糊匹配推荐

文件结构见FileStructure.md

---

#### **文件结构**

**Dao**：用于连接数据库

**FoodRecongnition**：食物图片识别，暂时使用百度API接口

**Service**：用于与前端交互，接收图片，并返回数据库查询结果

**Utils**：编写相关词汇清洗代码（待开发）

**WordList**：用于保存数据库包含的食物材料词汇

**WordTest**：用于保存清洗数据库词汇的相关代码

---

## 初期计划

前端页面的搭建（毕）

~~美食数据库连接，查询，修改工作~~

数据库新增菜品（向）

删除菜品操作（向）

美食识别代码编写（张，李）

#### **目标**

保证在3月10日之前，能够在小程序端/网页端，现场展现**从照片上传$\Longrightarrow$获得对应菜品制作教程**

---

## 第二阶段

建立用户数据库

新增用户注册，登陆页面

对用户饮食习惯进行个性化记录

制作用户画像/用户模糊匹配智能推荐

获取更多美食数据

重构代码

清洗数据库内容

---

+ 数据库增加，删除条目
+ 食物相似度匹配
+ 相关推荐
+ 菜品词汇标签（考虑重新建立表单
+ 食物卡路里显示



前端还需要：用户登陆，注册界面，菜品搜索界面

