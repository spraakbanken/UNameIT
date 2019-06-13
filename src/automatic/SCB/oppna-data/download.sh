
# Detta skript hämtar statistik om namn på skolenheter och personnamn

DATE=`date +"%Y-%m-%d"`

# API för Skolenhetsregistret
# http://api.scb.se/UF0109/v2/Help

# Hämtar en lista innehållande alla skolenhetskoder

wget https://api.scb.se/UF0109/v2/skolenhetsregister/sv/skolenhet
mv skolenhet skolenheter-$DATE.json

# API för Statistikdatabasen
# https://www.scb.se/om-scb/om-scb.se-och-anvandningsvillkor/oppna-data-api/api-for-statistikdatabasen/

# BE0001G = Samtliga folkbokförda
# http://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0001/BE0001G/..

# BE0001T06AR = Tilltalsnamn, de 10 och 100 vanligaste bland folkbokförda 31 december respektive år. År 1999 - 2018
# BE0001TNamn10 = Tilltalsnamn med minst 10 bärare bland folkbokförda 31 december respektive år. År 1999 - 2018
# BE0001T100 = Tilltalsnamn, de 100 vanligaste för folkbokförda kvinnor och män den 31 december 2018. Födelseår 1919 - 2018
# BE0001T08AR = Tilltalsnamn efter medelålder bland folkbokförda 31 december respektive år. År 2005 - 2018
# BE0001T07AR = Förnamn, de 10 och 100 vanligaste bland folkbokförda 31 december respektive år. År 1980 - 2018
# BE0001FNamn10 = Förnamn med minst 10 bärare bland folkbokförda 31 december respektive år. År 1999 - 2018
# BE0001F100 = Förnamn, de 100 vanligaste för folkbokförda kvinnor och män den 31 december 2018. Födelseår 1919 - 2018
# BE0001T03Ar = Efternamn, de 10 och 100 vanligaste bland folkbokförda 31 december respektive år. År 1980 - 2018
# BE0001ENamn10 = Efternamn med minst 10 bärare bland folkbokförda 31 december respektive år. År 1999 - 2018

wget http://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0001/BE0001G/BE0001TNamn10
mv BE0001TNamn10 tilltalsnamn-$DATE.json

wget http://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0001/BE0001G/BE0001FNamn10
mv BE0001FNamn10 fornamn-$DATE.json

wget http://api.scb.se/OV0104/v1/doris/sv/ssd/BE/BE0001/BE0001G/BE0001ENamn10
mv BE0001ENamn10 efternamn-$DATE.json


