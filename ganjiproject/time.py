import time
from geturl import urls
from geturl import info

while True:
    print(str(urls.find().count())+'  '+str(info.find().count()))
    time.sleep(1)

