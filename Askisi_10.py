#ΕΔΩ ΘΑ ΑΠΟΘΗΚΕΥΤΟΥΝ ΟΙ ΧΑΡΑΚΤΗΡΕΣ ΠΟΥ ΕΧΟΘΝ ΜΕΤΑΤΡΑΠΕΙ ΣΕ ΔΥΑΔΙΚΟ ΜΗΚΟΣ 7, ΧΩΡΙΣΜΕΝΟΙ ΑΝΑ 7#
characters = []
#ΕΔΩ ΘΑ ΑΠΟΘΗΚΕΥΤΟΥΝ ΤΑ 2 ΠΡΩΤΑ ΚΑΙ ΤΕΛΕΥΤΑΙΑ ΨΗΦΙΑ ΤΟΥ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΤΗΣ ΛΙΣΤΑ characters#
newCharacters = []
#ΕΔΩ ΘΑ ΑΠΟΘΗΚΕΥΤΟΥΝ ΤΑ ΣΤΟΙΧΕΙΑ ΤΗΣ ΛΙΣΤΑΣ newCharacters ΜΕΤΕΤΡΑΜΕΝΑ ΣΕ 16bits#
newnewCharacters = []
#ΕΔΩ ΟΡΙΖΟΝΤΑΙ ΟΙ ΜΕΤΡΗΤΕΣ ΠΟΥ ΘΑ ΧΡΗΣΜΟΠΟΙΗΣΟΥΜΕ ΓΙΑ ΝΑ ΒΡΟΥΜΕ ΤΑ ΠΟΣΟΣΤΑ ΠΟΥ ΖΗΤΟΥΝΤΑΙ#
countZigoi = 0
countdiairountai3 = 0
countdiairountai5 = 0
countdiairountai7 = 0
#ΕΔΩ ΑΝΟΙΓΩ ΤΟ ΑΡΧΕΙΟ ΜΕ ASCII ΧΑΡΑΚΤΗΡΕΣ ΚΑΙ ΤΟ ΜΕΤΑΤΡΕΠΟΥΜΕ ΣΕ ΧΑΡΑΚΤΗΡΕΣ ΔΥΑΔΙΚΟΥ ΜΗΚΟΥΣ 7# 
f = open("two_cities_ascii.txt")
lines = f.read()
byte_array = lines.encode()
binary_int = int.from_bytes(byte_array, "big")
binary_string = bin(binary_int)
#ΕΔΩ ΔΕΝ ΠΕΡΙΛΑΜΒΑΝΩ ΣΤΟ binary_string ΤΑ ΠΡΩΤΑ 2 ΨΗΦΙΑ ΓΙΑΤΙ ΤΟ ΔΕΥΤΕΡΟ ΗΤΑΝ ΤΟ ΓΡΑΜΜΑ "b"#
binary_string = binary_string[2:]
a = len(binary_string)
#ΕΔΩ ΑΠΟΘΗΚΕΥΩ ΣΤΟ numberofcharacters ΤΟ ΠΟΣΟΙ ΧΑΡΑΚΤΗΡΕΣ ΥΠΑΡΧΟΥΝ#
numberofcharacters = a // 7
f.close

#ΕΔΩ ΧΩΡΙΖΩ ΤΗΝ ΑΛΛΗΛΟΥΧΙΑ ΜΗΔΕΝΙΚΩΝ ΚΑΙ ΑΣΩΝ ΣΕ ΚΟΜΜΑΤΙΑ ΤΩΝ 7 ΚΑΙ ΤΑ ΕΙΣΑΓΩ ΣΤΗΝ ΛΙΣΤΑ characters#
for i in range(0, a-1):
    if i % 7 == 0:
        c = i - 7
        characters.append(binary_string[c:i])

#ΕΔΩ ΕΙΣΑΓΩ ΤΑ 2 ΠΡΩΤΑ ΚΑΙ ΤΕΛΕΥΤΑΙΑ ΨΗΦΙΑ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΚΑΙ ΤΑ ΕΙΣΑΓΩ ΣΤΗ ΛΙΣΤΑ newCharacters#
for i in (characters):
    newCharacters.append(i[0:2] + i[5:7])

#ΕΔΩ ΕΠΕΙΔΗ ΓΙΑ ΚΑΠΟΙΟ ΛΟΓΟ Η 1η ΘΕΣΗ ΤΗΣ ΛΙΣΤΑΣ newCharacters ΗΤΑΝ ΚΕΝΗ ΚΑΙ ΔΕΝ ΔΟΥΛΕΥΑΝ ΟΙ 2 ΠΑΡΑΠΑΝΩ ΓΡΑΜΜΕΣ ΚΩΔΙΚΑ ΕΒΑΛΑ ΣΤΗ ΘΕΣΗ ΑΥΤΗ ΤΟ 1 ΚΑΘΩΣ ΔΕΝ ΕΠΗΡΕΑΖΕΙ ΤΑ ΠΟΣΟΣΤΑ ΠΟΥ ΖΗΤΟΥΝΤΑΙ#
newCharacters[0] = "1"

#ΕΔΩ ΜΕΤΑΤΡΕΠΩ ΤΑ ΣΤΟΙΧΕΙΑ ΤΗΣ ΛΙΣΤΑΣ newcharacters ΣΕ ΑΡΙΘΜΟΥΣ ΤΩΝ 16bits KAI ΤΟΥΣ ΕΙΣΑΓΩ ΣΤΗ ΛΙΣΤΑ newnewCharacters#
for i in (newCharacters):
    newnewCharacters.append(int(i, 16))

#ΕΔΩ ΥΠΟΛΟΓΙΖΩ ΠΟΣΑ ΑΠΟ ΤΑ ΣΤΟΙΧΕΙΑ ΤΗΣ ΛΙΣΤΑΣ newnewCharacters ΕΙΝΑΙ ΖΥΓΟΙ, ΔΙΑΙΡΟΥΝΤΑΙ ΑΚΡΙΒΩΣ ΜΕ ΤΟ 3, ΔΙΑΙΡΟΥΝΤΑΙ ΑΚΡΙΒΩΣ ΜΕ ΤΟ 5 ΚΑΙ ΠΟΣΑ ΔΙΑΙΡΟΥΝΤΑΙ ΑΚΡΙΒΩΣ ΜΕ ΤΟ 7#
for i in (newnewCharacters):
    if i % 2 == 0:
        countZigoi += 1
    if i % 3 == 0:
        countdiairountai3 += 1
    if i % 5 == 0:
        countdiairountai5 += 1
    if i % 7 == 0:
        countdiairountai7 += 1

#ΕΔΩ ΜΕΤΑΤΡΕΠΩ ΣΕ ΠΟΣΟΣΤΑ ΤΟΙΣ ΕΚΑΤΟ ΤΑ ΑΠΟΤΕΛΣΜΑΤΑ ΤΩΝ 10 ΠΑΡΑΠΑΝΩ ΓΡΑΜΜΩΝ ΚΩΔΙΚΑ#
posostoZigwn = (countZigoi / numberofcharacters) * 100
posostodiairetewn3 = (countdiairountai3 / numberofcharacters) * 100
posostodiairetewn5 = (countdiairountai5 / numberofcharacters) * 100
posostodiairetewn7 = (countdiairountai7 / numberofcharacters) * 100

#ΤΕΛΟΣ ΕΚΤΥΠΩΝΟΥΜΕ ΤΑ ΖΗΤΟΥΜΕΝΑ ΣΤΑΤΙΣΤΙΚΑ#
print("To pososto poy einai zigoi einai " + str(posostoZigwn) + "%")
print("To pososto poy einai diairountai akrivws me to 3 einai " + str(posostodiairetewn3) + "%")
print("To pososto poy einai diairountai akrivws me to 5 einai " + str(posostodiairetewn5) + "%")
print("To pososto poy einai diairountai akrivws me to 7 einai " + str(posostodiairetewn7) + "%")