from datetime import *
from dateutil.relativedelta import *
import pipdate
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)

print(pipdate.check("python-dateutil", "2.8.2"))