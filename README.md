# 参考
[HerokuでFlask](http://shkh.hatenablog.com/entry/2013/01/01/192857)  
[PostgreSQLを用いたFlaskアプリのHerokuデプロイ(Flask-SQLAlchemy)](http://qiita.com/takechanman/items/917e2eb47fa21f866cb4)  
[Quickstart - flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/)  

# ローカルで
```python
# ローカルと本番でDBの接続先切り替え
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
if bool(os.environ.get('LOCAL_DEV', False)):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

```

```
$ export LOCAL_DEV="1"
$ export -p
declare -x LOCAL_DEV="1"
```


# Heroku上で


```python
# DBの作成
% heroku run python
>> import model
>> model.table_init()
```

```
# 環境変数DATABASE_URLの確認
$ heroku config
=== gentle-cove-69489 Config Vars
DATABASE_URL: postgres://fehjxkgesmikqk:b437a062d9c44b6f0312e9ca8c4a84736a91d09b0bb32816e2ffedcd0a03defd@ec2-54-163-234-4.compute-1.amazonaws.com:5432/dfk7efdeih44su
```