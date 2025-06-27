Fiare din Beci - Magazin Online de Replici Istorice
Fiare din Beci este o aplicație web completă, construită cu Django, ce servește drept magazin online și portofoliu pentru replici de săbii și arme istorice forjate manual. Platforma permite utilizatorilor să vizualizeze produsele, să plaseze comenzi și să interacționeze cu meșterul, în timp ce administratorul poate gestiona cu ușurință inventarul, comenzile și conținutul site-ului.

Întreaga aplicație este containerizată folosind Docker și orchestrată cu Docker Compose pentru a asigura un mediu de dezvoltare și producție consistent și izolat.

Livrabilele Proiectului
Această secțiune conține detaliile solicitate pentru predarea proiectului de licență.


Pași de Compilare, Instalare și Lansare a Aplicației
Deoarece aplicația este containerizată cu Docker, pașii de "compilare" și "instalare" sunt gestionați automat de Docker Compose. Procesul este următorul:

Cerințe Preliminare
Docker: Platforma de containerizare. Descarcă Docker Desktop

Docker Compose: Unealta pentru definirea și rularea aplicațiilor multi-container (inclusă în Docker Desktop).

Git: Pentru a clona repository-ul.

Pașii de Rulare
Clonați Repository-ul:

git clone https://github.com/VictorJude046/Licenta.git
cd Licenta

Construiți și Porniți Aplicația (Compilare și Lansare):
Această singură comandă va construi imaginea Docker (echivalentul compilării), va crea volumele necesare și va porni toate serviciile (web, bază de date).

docker-compose up --build

(Flag-ul --build este esențial la prima rulare).

Aplicați Migrațiile Bazei de Date:
După ce containerele au pornit, deschideți un nou terminal și rulați comanda pentru a crea structura bazei de date.

docker-compose exec website python manage.py migrate

Creați un Cont de Administrator:
Pentru a accesa panoul de administrare, creați un superuser.

docker-compose exec website python manage.py createsuperuser

Accesați Aplicația:
Aplicația este acum complet funcțională.

Website Public: http://localhost:8000

Panou de Administrare: http://localhost:8000/admin/

Tehnologii Utilizate
Backend
Python: Limbajul de programare principal.

Django: Cadrul web pentru construirea aplicației.

PostgreSQL: Sistemul de gestionare a bazei de date.

Pillow: Biblioteca Python pentru procesarea imaginilor.

Frontend
HTML5 & CSS3: Structura și stilizarea paginilor web.

JavaScript: Pentru funcționalități interactive, cum ar fi slideshow-ul de imagini.

Bootstrap 5: Cadrul CSS pentru design responsiv și componente UI.

Font Awesome: Pentru iconițe.

Google Fonts: Pentru fonturi personalizate.

Mediu de Rulare
Docker: Pentru containerizarea aplicației.

Docker Compose: Pentru orchestratea serviciilor (web, bază de date).
