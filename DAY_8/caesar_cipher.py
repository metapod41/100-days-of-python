from art import art

print(art)

alphabets =[
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']




def caesar(message , shift , encode_or_decode):
    res = ""
    if encode_or_decode=='decode':
        shift *= -1
    for char in message:
        if char not in alphabets:
            res+=char
        else:
            res+=alphabets[(alphabets.index(char)+shift)%26]
    print(f"here is your {encode_or_decode}d text {res}")

should_continue = True

while should_continue:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("type the shift number:\n"))
    caesar(message=text , shift=shift , encode_or_decode=direction)

    restart = input("do you like to go again, type 'y' for yes and 'n' for no\n").lower()

    if restart == 'n':
        should_continue = False
        print("Goodbye!\n")
