from datetime import datetime as dt
filePath = 'C:\Windows\System32\drivers\etc\hosts'
websiteList = ['www.facebook.com','www.twitter.com','www.youtube.com']
baseIP = '127.0.0.1'


min_value = (dt.now().year,dt.now().month,dt.now().day,8,0,0)
max_value = (dt.now().year,dt.now().month,dt.now().day,17,30,0)
dt.now().timestamp


current_time = (dt.now().year,dt.now().month,dt.now().day,dt.now().hour,dt.now().minute,dt.now().second)

if min_value < current_time < max_value:
  with open(filePath,'a+', encoding='utf-8') as file:
    for website in websiteList:
      file.write(baseIP + " " + website + '\n')
    file.close()

else:
  with open(filePath,encoding='utf-8') as file:
    file.seek(0)
    fileContentList = file.readlines()
  file.close()

  with open(filePath,'w',encoding='utf-8') as file:
    finalContent = ''
    for line in fileContentList:
      status = False
      for website in websiteList:
        if baseIP + " " + website in line:
          status = True

      if status:
        continue
      finalContent = finalContent + line
    file.write(finalContent)

  file.close()



            
        

  

