# Hello there!

## Disclaimer:
Jeg fik ikke sat det op med docker, men kørte en mysql database på en local apache server (med XAMPP).
Derfor skal der sættes en tom MySQL database op et sted før det kan køre.

## Korte kommentare knyttet til nogle af delopgaverne:
---------------------
- Python modulet ligger i rodstien sammen med manage.py og denne readme ( getmodule.py ). Den henter kun 440 cat facts som umiddelbart virker til at være maximum. Jeg tjekker for dublicate data og prøvede at hente 500 random facts flere gange og gemme dem seperat for at tjekke dem imod hindanden, men efter at fjerne dublicates endte jeg altid med max 440. Hvis man kalder API'et med amount=500 for man også kun 440 ud. Der er en anden stig for user submittet facts som havde 173 facts heller ikke inkluderede, da jeg generelt fandt kvaliteten af disse facts lavere. 
- Docker nåede jeg ikke, jeg prøvede kort men løb ind i problemer med oprette en database
med en bruger som havde adgang fra andre steder end localhost, og indså jeg ikke ville have tid til det.
- Jeg lavede en model med kun text og id felter, hvis det var noget jeg arbjede videre med
ville jeg nok have udvidet modellen så den kunne have mere funktionalitet i fremtiden
- Django management kommandoen er fundet under catfacts\cats\management\commands\getcatfacts.py
Jeg ville gerne have sørget for at håndtere duplicate data i databasen, men nåede det ikke. Hvis man kører **python manage.py getcatfacts** flere gange nu, smider den dataen ind igen on igen, så der er chance for at vise det samme fact 2 gange. 
- Viewet findes i cats\views.py
---------------------

## Installation
 
For at installere skal du have git, python3 og pip

Åben commandolinien og gå et sted hen hvor du vil have det.

1. kør **git clone https://github.com/s154674/catfacts.git**

2. Find **catfacts/setting.py** og åben den i en text editor og skift database værdier ud

3. gå tilbage til den yderste **catfacts** mappe

4. **mkvirtualenv navn**

5. **pip install -r requirements.txt** (hvis den brokker sig over MySQL, download en whl fil fra
https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient som du kan bruge, og pip install den istedet)

6. **python manage.py migrate**

7. **python manage.py getcatfacts** (Hvis den giver dig No module named 'requests' så kør en pip install requests først)

8. **python manage.py runserver**

Du burde nu se dette:

Performing system checks...

... 

Starting development server at **http://127.0.0.1:8000/**
Quit the server with CTRL-BREAK


Du kan nu gå til **localhost:8000/cats/** og se 10 random catfacts der opdateres når du klikker Refresh




