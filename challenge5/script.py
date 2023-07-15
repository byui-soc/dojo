import binascii
import base64

def obfuscated(x):
    func = base64.b64decode('ZGVmIHNvbWV0aGluZyhpbnB0KToKICAgIGlucHQgPSBiaW5hc2NpaS5oZXhsaWZ5KGJ5dGVzKGlucHQsIGVuY29kaW5nPSd1dGYtOCcpKQogICAgaW5wdCA9IHN0cihpbnB0KVsyOi0xXQogICAgbmV3ID0gJycKICAgIGZvciBpIGluIGlucHQ6CiAgICAgICAgbmV3ICs9IHN0cigob3JkKGkpKSkgKyAnLScKICAgIHJldHVybiBuZXdbOi0xXQ==')
    exec(bytes.decode(func), globals())
    encoded = something(x)
    return encoded

def main():
    with open('readfrom.txt', 'r') as password_file:
        password = password_file.readline().strip()
    encoded_password = obfuscated(password)

    print(f"The encoded password is :\n        {encoded_password}")
    print("Decode and submit the password, and I will give you the flag\n")
    user = input("What is the password? : ")
    
    if obfuscated(user) == encoded_password:
        with open('flag.txt', 'r') as flag_file:
            flag = flag_file.readline()
        print(f"\nNice job! Here is the flag:\n        {flag}")
    else:
        print("Wrong!!")

if __name__ == "__main__":
    main()
