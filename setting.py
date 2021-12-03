AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
STREAM_NAME = "demo-ds"
REGION = 'cn-northwest-1'
# 发送间隔，毫秒数s
SEND_INTERVAL = 1000

if not AWS_ACCESS_KEY_ID or AWS_ACCESS_KEY_ID == 'your access key id':
    raise ValueError("AWS_ACCESS_KEY_ID should be set")

if not AWS_SECRET_ACCESS_KEY or AWS_SECRET_ACCESS_KEY == 'your secret key':
    raise ValueError("AWS_SECRET_ACCESS_KEYc should be set")
