class Config:
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST',"mysql-3f7d74b9-julianramirezsena7-16bb.e.aivencloud.com")
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', "avnadmin")
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', "AVNS_KWS3RBthHw3PbdsYsfV")
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', "defaultdb")
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 23026))

mysql = MySQL(app)
