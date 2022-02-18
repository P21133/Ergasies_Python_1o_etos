#ΕΔΩ ΑΝΟΙΓΩ ΤΟ ΑΡΧΕΙΟ ΜΕ ASCII ΧΑΡΑΚΤΗΡΕΣ ΚΑΙ ΤΟ ΜΕΤΑΤΡΕΠΟΥΜΕ ΣΕ ΧΑΡΑΚΤΗΡΕΣ ΔΥΑΔΙΚΟΥ ΜΗΚΟΥΣ 7# 
f = open("two_cities_ascii.txt")
lines = f.read()
byte_array = lines.encode()
binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)
binary_string = binary_string[2:]
f.close
#ΕΔΩ ΟΡΙΖΟΝΤΑΙ ΟΙ ΜΕΤΡΗΤΕΣ ΠΟΥ ΘΑ ΧΡΗΣΜΟΠΟΙΗΣΟΥΜΕ ΓΙΑ ΝΑ ΒΡΟΥΜΕ ΤΑ ΑΠΟΤΕΛΕΣΜΑΤΑ ΠΟΥ ΖΗΤΟΥΝΤΑΙ#
Megaliteriseira1 = 0
Count1 = 0
Megaliteriseira0 = 0
Count0 = 0

#ΕΔΩ ΕΛΕΓΧΟΥΜΕ ΑΝ ΤΟ ΚΑΘΕ ΨΗΦΙΟ ΕΙΝΑΙ ΙΣΟ ΜΕ "1", ΑΝ ΕΙΝΑΙ ΑΥΞΑΝΕΤΑΙ ΤΟ Count1 ΚΑΙ ΑΝ ΤΟ Count1 ΕΙΝΑΙ ΜΕΓΑΛΥΤΕΡΟ ΑΠΟ ΤΟ Megaliteriseira1 ΤΟΤΕ ΤΟ Megaliteriseira1 ΠΑΙΡΝΕΙ ΤΗΝ ΤΙΜΗ ΤΟΥ Count1#
for i in binary_string:
    if i == "1":
        Count1 += 1
        Megaliteriseira1 = max(Megaliteriseira1, Count1)
    else:
        Count1 = 0

#ΠΑΡΟΜΟΙΑ ΜΕ ΤΙΣ 7 ΠΑΡΑΠΑΝΩ ΓΡΑΜΜΕΣ ΚΩΔΙΚΑ#
for i in binary_string:
    if i == "0":
        Count0 += 1
        Megaliteriseira0 = max(Megaliteriseira0, Count0)
    else:
        Count0 = 0

#ΤΕΛΟΣ ΕΚΤΠΩΝΟΥΜΕ ΤΑ ΖΗΤΟΥΜΕΝΑ#
print(Megaliteriseira1)
print(Megaliteriseira0)