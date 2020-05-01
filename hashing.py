import random 

def hash(message):
	rand_array = [69,75,71,81,79,78,70,53,67,61,59,57,55,83,73,74]
	hex_string = ''
	if len(message) % 16 != 0: 
		for i in range(0, 16 - len(message)%16): message+=chr(31)

	mul_total = 1
	for i in range(0, len(message), 16):
		total = 0
		for j in range(0, 16):
			total += ord(message[i+j]) ** rand_array[j]

		mul_total*=total
	hex_string = hex(mul_total % (7 ** 145))
	return hex_string[len(hex_string)-50:]

def get_salt(num_char):
	salt = ''
	for i in range(0, num_char): salt += chr(random.randint(40,126))
	return salt

def encode(message):
	salt = get_salt(32)
	return [hash(message + salt), salt, message]

def hash_file(path):
	file = open(path, "r")
	hash_string = file.read()
	return hash(hash_string)


print(hash_file('hash-file.txt'))

# print(hash('aaaa'))
