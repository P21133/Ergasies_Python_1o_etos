#ΕΔΩ ΧΡΗΣΜΟΠΟΙΩ ΤΗ ΒΙΒΛΙΟΘΗΚΗ random ΓΙΑ ΝΑ ΜΠΟΡΟΥΝ ΤΑ ΠΙΟΝΙΑ ΝΑ ΤΠΟΘΕΤΗΘΟΥΝ ΤΥΧΑΙΑ#
import random

#ΕΔΩ ΑΥΤΕΣ ΤΙΣ ΛΙΣΤΕΣ ΟΥΣΙΑΣΤΙΚΑ ΑΝΑΠΑΡΗΣΤΟΥΝ ΜΙΑ ΣΚΑΚΙΕΡΑ ΑΦΟΥ ΜΕ ΤΙΣ ΣΥΝΕΤΑΓΜΕΝΕΣ ΜΙΑΣ ΣΚΑΚΙΕΡΑΣ ΜΠΟΡΩ ΝΑ ΥΠΟΔΕΙΞΩ ΟΠΟΙΑΔΗΠΟΤΕ ΘΕΣΗ ΤΗΣ#
YpsosSkakieras = [1,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,]
MhkosSkakieras = [1, 2, 3, 4, 5, 6, 7, 8]

#ΕΔΩ ΟΡΙΖΩ ΤΟΥΣ ΜΕΤΡΗΤΕΣ ΒΑΘΜΩΝ ΤΩΝ 2 ΠΑΙΧΤΩΝ ΓΙΑ ΚΑΘΕ ΠΑΡΤΙΔΑ ΑΛΛΑ ΚΑΙ ΓΙΑ ΟΛΕΣ ΤΙΣ ΠΑΡΤΙΔΕΣ#
TotalVathmoiAsprou = 0
TotalVathmoiMavrou = 0

VathmoiPartidasAsprou = 0
VathmoiPartidasMavrou = 0

T = True 

for i in range(0, 100):
    #ΕΔΩ ΔΙΝΟΝΤΑΙ ΣΤΑ 2 ΠΙΟΝΙΑ ΤΥΧΑΙΕΣ ΘΕΣΕΙΣ, ΧΡΗΣΜΟΠΟΙΩ ΤΟΝ ΒΡΟΧΟ while ΩΣΤΕ ΣΤΗΝ ΠΕΡΙΠΤΩΣΗ ΠΟΥ ΔΩΘΕΙ Η ΙΔΙΑ ΘΕΣΗ ΓΙΑ ΤΑ 2 ΠΙΟΝΙΑ ΝΑ ΕΠΑΝΑΛΗΦΘΕΙ Η ΔΙΑΔΙΚΑΣΙΑ ΑΠΟΔΟΣΗΣ ΘΕΣΕΩΝ ΜΕΧΡΙ ΑΥΤΕΣ ΝΑ ΕΙΝΑΙ ΔΙΑΦΟΡΕΤΙΚΕΣ ΜΕΤΑΞΥ ΤΟΥΣ#
    while T == True:
        YpsosPirgou = random.choice(YpsosSkakieras)
        MhkosPirgou = random.choice(MhkosSkakieras)
        YpsosAksiomatikou = random.choice(YpsosSkakieras)
        MhkosAksiomatikou = random.choice(MhkosSkakieras)
        #ΕΔΩ ΓΙΝΕΤΑΙ Ο ΕΛΕΓΧΟΣ ΑΝ ΟΙ ΘΕΣΕΙΣ ΤΩΝ ΠΙΟΝΙΩΝ ΕΙΝΑΙ ΟΙ ΙΔΙΕΣ#
        if (YpsosPirgou != YpsosAksiomatikou or MhkosPirgou != MhkosAksiomatikou):
            break
    #ΕΔΩ ΕΛΕΓΧΕΤΑΙ Ο ΠΥΡΓΟΣ ΜΠΟΡΕΙ ΝΑ ΦΑΕΙ ΤΟΝ ΑΞΙΩΜΑΤΙΚΟ#
    if (YpsosPirgou == YpsosAksiomatikou or MhkosPirgou == MhkosAksiomatikou):
        VathmoiPartidasAsprou += 1
    #ΕΔΩ ΕΛΕΓΧΕΤΑΙ Ο ΑΞΙΩΜΑΤΙΚΟΣ ΜΠΟΡΕΙ ΝΑ ΦΑΕΙ ΤΟΝ ΠΥΡΓΟ#
    if (abs(YpsosPirgou - YpsosAksiomatikou) == (abs(MhkosPirgou - MhkosAksiomatikou))):
        VathmoiPartidasMavrou += 1

    #ΕΔΩ ΠΡΟΣΘΕΤΩ ΤΟΥΣ ΒΑΘΜΟΥΣ ΠΑΡΤΙΔΑΣ ΤΟΥ ΚΑΘΕΝΑ ΣΤΟΥΣ ΣΥΝΟΛΙΚΟΥΣ#
    TotalVathmoiAsprou += VathmoiPartidasAsprou
    TotalVathmoiMavrou += VathmoiPartidasMavrou
    
    #ΕΔΩ ΜΗΔΕΝΙΖΩ ΞΑΝΑ ΤΟΥΣ ΒΑΘΜΟΥΣ ΠΑΡΤΙΔΑΣ ΤΟΥ ΚΑΘΕΝΑ ΓΙΑΤΙ ΤΕΛΕΙΩΣΕ Η ΣΥΓΚΕΚΡΙΜΕΝΗ ΠΑΡΤΙΔΑ#
    VathmoiPartidasAsprou = 0
    VathmoiPartidasMavrou = 0


#ΕΔΩ ΕΚΤΥΠΩΝΩ ΤΑ ΖΗΤΟΥΜΕΝΑ ΑΠΟΤΕΛΕΣΜΑΤΑ#
print("Oi sinolikoi vathmoi tou asprou gia skakiera 8x8 einai " + str(TotalVathmoiAsprou))
print("Oi sinolikoi vathmoi tou mavrou gia skakiera 8x8 einai " + str(TotalVathmoiMavrou))


#ΚΑΝΩ ΤΟ ΙΔΙΟ ΑΠΛΑ ΓΙΑ ΣΚΑΚΙΕΡΑ 7Χ7#
import random

YpsosSkakieras = [1,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,]
MhkosSkakieras = [1, 2, 3, 4, 5, 6, 7,]

TotalVathmoiAsprou = 0
TotalVathmoiMavrou = 0

VathmoiPartidasAsprou = 0
VathmoiPartidasMavrou = 0

T = True 

for i in range(0, 100):
    while T == True:
        YpsosPirgou = random.choice(YpsosSkakieras)
        MhkosPirgou = random.choice(MhkosSkakieras)
        YpsosAksiomatikou = random.choice(YpsosSkakieras)
        MhkosAksiomatikou = random.choice(MhkosSkakieras)
        if (YpsosPirgou != YpsosAksiomatikou or MhkosPirgou != MhkosAksiomatikou):
            break
    if (YpsosPirgou == YpsosAksiomatikou or MhkosPirgou == MhkosAksiomatikou):
        VathmoiPartidasAsprou += 1
    if (abs(YpsosPirgou - YpsosAksiomatikou) == (abs(MhkosPirgou - MhkosAksiomatikou))):
        VathmoiPartidasMavrou += 1

    TotalVathmoiAsprou += VathmoiPartidasAsprou
    TotalVathmoiMavrou += VathmoiPartidasMavrou
    
    VathmoiPartidasAsprou = 0
    VathmoiPartidasMavrou = 0



print("Oi sinolikoi vathmoi tou asprou gia skakiera 7x7 einai " + str(TotalVathmoiAsprou))
print("Oi sinolikoi vathmoi tou mavrou gia skakiera 7x7 einai " + str(TotalVathmoiMavrou))



#ΚΑΝΩ ΤΟ ΙΔΙΟ ΑΠΛΑ ΓΙΑ ΣΚΑΚΙΕΡΑ 7Χ8#
import random

YpsosSkakieras = [1,
                  2,
                  3,
                  4,
                  5,
                  6,
                  7,
                  8,]
MhkosSkakieras = [1, 2, 3, 4, 5, 6, 7,]

TotalVathmoiAsprou = 0
TotalVathmoiMavrou = 0

VathmoiPartidasAsprou = 0
VathmoiPartidasMavrou = 0

T = True 

for i in range(0, 100):
    while T == True:
        YpsosPirgou = random.choice(YpsosSkakieras)
        MhkosPirgou = random.choice(MhkosSkakieras)
        YpsosAksiomatikou = random.choice(YpsosSkakieras)
        MhkosAksiomatikou = random.choice(MhkosSkakieras)
        if (YpsosPirgou != YpsosAksiomatikou or MhkosPirgou != MhkosAksiomatikou):
            break
    if (YpsosPirgou == YpsosAksiomatikou or MhkosPirgou == MhkosAksiomatikou):
        VathmoiPartidasAsprou += 1
    if (abs(YpsosPirgou - YpsosAksiomatikou) == (abs(MhkosPirgou - MhkosAksiomatikou))):
        VathmoiPartidasMavrou += 1

    TotalVathmoiAsprou += VathmoiPartidasAsprou
    TotalVathmoiMavrou += VathmoiPartidasMavrou
    
    VathmoiPartidasAsprou = 0
    VathmoiPartidasMavrou = 0



print("Oi sinolikoi vathmoi tou asprou gia skakiera 7x8 einai " + str(TotalVathmoiAsprou))
print("Oi sinolikoi vathmoi tou mavrou gia skakiera 7x8 einai " + str(TotalVathmoiMavrou))