import json
import hashlib

def decrypt(key, message):
    message = message.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for letter in message:
        if letter in alpha: #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

# Reading json file
with open('answer.json', 'r') as myfile:
	data = myfile.read()

jfile = json.loads(data)
message = jfile["cifrado"]
key = jfile["numero_casas"]
decrypted = decrypt(key,message)
print (decrypted)

resumo = hashlib.sha1(decrypted.encode())

print("The hexadecimal equivalent of SHA1 is : ") 
print(resumo.hexdigest()) 

jfile['decifrado'] = decrypted
jfile['resumo_criptografico'] = resumo.hexdigest()

print (jfile)

with open('answer.json', 'w') as json_file:
	json.dump(jfile, json_file)


