


```sql
create database flask_user;
create table users (
    id int not null auto_increment,
    username varchar(40) not null,
    password varchar(40) not null,
    primary key(id)
);
```

question:
1.未持久化到数据库中
2.删除无效