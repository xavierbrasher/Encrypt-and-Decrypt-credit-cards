with open("encrypted.txt", "w", encoding="utf-8") as file:
    creditNumber = input("Enter your credit card number: ")
    expireDate = input("Enter your expiration date: ")
    cvv = input("Enter your CVV: ")
    encriptionKey = input("Enter your encription key: ")
    message = "Credit Card Number: " + creditNumber + "\n" + "Expiration Date: " + expireDate + "\n" + "CVV: " + cvv
    ## encrypt the message with encription key
    encryptedMessage = ""
    for i in range(len(message)):
        encryptedMessage += chr(ord(message[i]) + int(encriptionKey))
    ## write the encrypted message to a file
    file.write(encryptedMessage)