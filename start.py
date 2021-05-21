import sys
import subprocess
import os
from time import sleep
from config import *

warning = "Edit your config.py file before using the bot!"

def worker(file,token):
  print(token, " ", file)
  subprocess.call(file, shell=True)
  
for char in warning:
  sleep(0.01)
  sys.stdout.write(char)
  sys.stdout.flush()
sleep(0.5)
print("Type the number for the desired type of spam:")
print("1 - Spam your own text.")
print("2 - Spam images.")

user_choice = float(input("Choose a number: "))

if user_choice == 1:
  spam_text = input("Write your text here: ")
  print('python discord_spam_text.py' + "'"+spam_text"'")
  for token in user_token:
    print("Loading Token...")
    p = subprocess.Popen(['python','discord_spam_text.py',token,spam_text],shell=True)
    sleep(1)
    print("Token Loaded.")
    print(' ')
p.wait()
