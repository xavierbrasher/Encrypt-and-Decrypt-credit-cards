with open("encrypted.txt", "r", encoding="utf-8") as file:
    encryptedMessage = file.read()
    ## decrypt the message with encription key
    decryptedMessage = ""
    encriptionKey = input("Enter your encription key: ")
    for i in range(len(encryptedMessage)):
        decryptedMessage += chr(ord(encryptedMessage[i]) - int(encriptionKey))
    ## print the decrypted message
    print(decryptedMessage)