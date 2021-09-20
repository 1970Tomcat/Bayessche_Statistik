#Bayessche Statistik
#
#           P(B|A) P(A)
# P(A|B) = --------------
#              P(B)
#
# P(A|B)
# A-posteriori Wahrscheinlichkeit der Variablen A nach Beobachtung Evidenz B
#
# P(B|A)
# Likelihood: Wahrscheinlichkeit von Auftreten B, wenn A bereits eingetroffen ist
#
# P(A): Prior, Wahrscheinlichkeit für Eintritt A
#
#P(B)
# Wahrscheinlichkeit des Auftretens aller möglichen Werte von B, gewichtet nach Glaubwürdigkeit


# CORONA TEST
# A-Posteriori Wahrscheinlichkeit: Fragestellung
# Wie wahrscheinlich ist es, dass bei einem positiven Test (A), der Proband wirklich positiv ist (B)?
# P(A|B) A: True Positiv    Evidenz B: Testresultat positiv

# Prior Corona
# Wahrscheinlichkeit für Eintritt A
# 7 Tage Inzidenz
import math

Inzidenz = 172
prior = 172/100000

# Likelihood Corona
# Ereignis A ist eingetroffen; Wie wahrscheinlich ist der Corona Test?
likelihood = 0.999

#alle mögliche Ereignisse B
#Fall positiv, Test positiv
fall1B = prior * likelihood

#Fall negativ, Test posotiv
fall2B = (1-prior) * (1-likelihood)

pB = fall1B + fall2B

pAB = prior * likelihood/ pB*100
print()
print("CORANA TEST")
print()
print("Bei einer aktuellen 7 Tages Inzidenz von " + str(Inzidenz) + " und einer Genauigkeit des PCR-Tests von " + str(likelihood*100) + "%, ")
print("beträgt die Wahrscheinlichkeit, dass bei einem positiven Test die Testperson wirklich positiv ist: ")
print()
print(str(math.ceil(pAB)) + '%')


