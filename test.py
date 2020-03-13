import re

raw="""--------------------------d9d48ab6bc6d7aa9
Content-Disposition: form-data; name="data"
{"url":"http://hssystem.oss-cn-shenzhen.aliyuncs.com/test/c2a062712fa525466954176bc4f86593.jpg","task_id":144384,"extend":""}
--------------------------d9d48ab6bc6d7aa9--"""

res=re.search(r'({[\w\W]+})',raw,re.M|re.I)

print(res.group(1))