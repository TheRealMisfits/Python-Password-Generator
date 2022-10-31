# Import Libraries
import secrets
import sys
import string
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Define Alphabet
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

# Print Logo
print(Fore.BLUE+"        .__         _____.__  __             ")
print(Fore.BLUE+"  _____ |__| ______/ ____|___/  |_ ______    ")
print(Fore.BLUE+" /     \|  |/  ___\   __\|  \   __/  ___/    ")
print(Fore.BLUE+"|  Y Y  |  |\___ \ |  |  |  ||  | \___ \     ")
print(Fore.BLUE+"|__|_|  |__/____  >|__|  |__||__|/____  > /\ ")
print(Fore.BLUE+"      \/        \/                    \/  \/")
print(Fore.BLUE+" ")
print(Fore.BLUE+"Powered by Python // Created by themisfits.ml")
print(Fore.BLUE+" ")

# Ask Password Length
length = int(input(Fore.WHITE+"Enter Password Length: " + Fore.BLUE))

# Generate Password
if length == 1: 
  sys.exit(Fore.RED+"Cannot Generate Password.")

while True:
  pwd = ''
  for i in range(length):
    pwd += ''.join(secrets.choice(alphabet))

  if (any(char in special_chars for char in pwd) and 
      sum(char in digits for char in pwd)>=2):
          break
print(Fore.WHITE+"Generated Password: " + Fore.BLUE + pwd)