import hmac
import hashlib
import base64
# This code can be used to verify that a webhook message originated from Videra Health

# Never hard-code secrets in public code
SECRET = bytes('DX5Q3XXaQ5VEGiW224Xwg5GLicKWGDw/+hw9YDYTCvk=', 'UTF8')
timestamp = '1635513507'
passed_signature = 'wnraKDv+Oh6FsBNtLt8c+Lp+L0CvFUnn4RZZFslteNw='
body = '{"events":[{"eventType":"XXX"}]}'

body_and_timestamp = bytes(timestamp+body, 'UTF8')
digest = hmac.new(SECRET, msg=body_and_timestamp, digestmod=hashlib.sha256).digest()
computed_signature = base64.b64encode(digest).decode()

assert computed_signature == passed_signature