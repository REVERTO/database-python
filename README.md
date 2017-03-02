# 参考
[HerokuでFlask](http://shkh.hatenablog.com/entry/2013/01/01/192857)  
[PostgreSQLを用いたFlaskアプリのHerokuデプロイ(Flask-SQLAlchemy)](http://qiita.com/takechanman/items/917e2eb47fa21f866cb4)  

# ローカルで

# Heroku上で


```python
# DBの作成
% heroku run python
>> from main import db
>> db.create_all()
```