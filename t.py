import datetime
today =  datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)
tmp = str(tomorrow)
tom = tmp.split(" ")[0]

