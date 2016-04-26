import time
from spider import quanbu

while True:
    print(quanbu.find().count())
    time.sleep(5)