letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

length=len(letter)

key=5
raw = "hello"
encrypt = ""

raw = raw.lower()

for char in raw:
	pointer = letter.index(char)
	shift=pointer+key
	actual = shift - length*int(shift/length)
	encrypt = encrpt+letter[actual]

print(peice)
