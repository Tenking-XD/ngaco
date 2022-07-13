import os
if __name__ == "__main__":
   try:
       os.system('git pull')
       try:os.mkdir("Data")
       except:pass
       __import__("ige2")
       mengecek_()
       login_kamu()
   except Exception as e:
       exit(str(e))