import os
os.system('git pull')
if __name__ == "__main__":
   try:
       __import__("ige2.py").mengecek_()
   except Exception as e:
       exit(str(e))