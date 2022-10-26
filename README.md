# Ølsalg
Tar du deg selv i å bli så opphengt i SIGSEGVs og code reviews at du helt glemmer at Norge har uforståelige regler for utsalg av alkohol? Fortvil ikke, med dette programmet får du en veldig naiv counter i statusbaren som viser hvor lang tid du har på deg. I tillegg gir den deg en notification dersom det er 30 minutter igjen av ølsalget. Noen måtte bare gjøre det, ingen årsak.

NB: Tar ikke høyde for helligdager og dager med egne regler. Feel free til å lage PR.

<img src=./img/img.png>

### Dependencies

* MacOS
* Python 3.10
* Rumps: https://github.com/jaredks/rumps
* Py2App: https://py2app.readthedocs.io/en/latest/

### Kom i gang
* ```git clone https://github.com/jonassundseth/olsalg.git```
* Lag venv [frivillig]: ```python3 -m venv venv```
* ```pip3 install -r requirements.txt```


### Kjøre programmet
```
python3 main.py
```

## Stand alone app
For å generere en app som kan startes av hvilken som helst luring:
```
python3 setup.py py2app --emulate-shell-environment
```
Boom: Appen ligger i ```dist/```

For optimal effekt: legg app-filen i Applications-folderet