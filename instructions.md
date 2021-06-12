# 创建超级管理员用户
python manage.py createsuperuser

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 运行程序
python manage.py runserver 127.0.0.1:8000

# 创建应用模块
python manage.py startapp book