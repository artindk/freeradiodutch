# FreeRadio - dodatek dla NVDA

FreeRadio to dodatek radia internetowego dla czytnika ekranu NVDA. Jego głównym celem jest łatwy dostęp do tysięcy internetowych stacji radiowych. Cały interfejs i wszystkie funkcje zaprojektowano z myślą o pełnej dostępności w NVDA.

## Katalog Radio Browser

FreeRadio używa otwartej bazy [Radio Browser](https://www.radio-browser.info/) jako katalogu stacji. Radio Browser to bezpłatny katalog zarządzany przez społeczność, zawierający ponad 50 000 internetowych stacji radiowych z całego świata. Nie wymaga rejestracji ani konta, a jego API jest otwarte dla wszystkich. Każda stacja zawiera adres, kraj, gatunek, język i informacje o przepływności; stacje są sortowane również według głosów użytkowników. FreeRadio łączy się z API przez serwery lustrzane w Niemczech, Holandii i Austrii; jeśli jeden serwer jest niedostępny, automatycznie przełącza się na następny.

## Dodawanie stacji do Radio Browser

Jeśli szukanej stacji nie ma w katalogu Radio Browser, możesz dodać ją samodzielnie na stronie [https://www.radio-browser.info/add](https://www.radio-browser.info/add). Konto nie jest potrzebne.

Wypełnij formularz na tej stronie:

- **Stream URL** *(wymagane)* - bezpośredni adres URL strumienia audio, kończący się na przykład na `.mp3`, `.aac`, `.ogg` lub podobnie. Nie jest to adres strony internetowej stacji, tylko surowy adres strumienia, który można wkleić do odtwarzacza multimedialnego. Większość stacji publikuje go na swojej stronie albo w sekcji "Słuchaj na żywo".
- **Station name** *(wymagane)* - nazwa stacji, która ma pojawić się w katalogu.
- **Homepage** - adres strony internetowej stacji.
- **Country and language** - wybierz kraj i język nadawania z list rozwijanych.
- **Tags** - słowa kluczowe gatunku lub tematu, rozdzielone przecinkami, na przykład `news`, `jazz`, `classical`. Są używane do wyszukiwania i filtrowania.
- **Logo URL** - bezpośredni link do obrazu logo stacji, jeśli jest dostępny.

Po wysłaniu stacja zostanie sprawdzona i dodana do publicznego katalogu. Po zaakceptowaniu pojawi się automatycznie w wyszukiwaniu i listach krajów FreeRadio, ponieważ katalog jest odświeżany z aktywnego API.

## Wymagania

- NVDA 2024.1 lub nowszy
- Windows 10 lub nowszy
- Połączenie z internetem

## Instalacja

Pobierz plik `.nvda-addon`, naciśnij na nim Enter i uruchom NVDA ponownie, gdy pojawi się taka prośba.

## Skróty klawiszowe

Wszystkie skróty można zmienić w menu NVDA -> Preferencje -> Zdarzenia wejścia -> FreeRadio. Skróty działają z dowolnego miejsca, niezależnie od aktywnego okna.

| Skrót | Funkcja | Opis |
|---|---|---|
| `Ctrl+Win+R` | Otwórz przeglądarkę stacji | Otwiera okno przeglądarki, jeśli jest zamknięte, albo przenosi je na wierzch, jeśli jest już otwarte. |
| `Ctrl+Win+P` | Wstrzymaj / wznów | Wstrzymuje aktualną stację, jeśli gra; wznawia ją, jeśli jest wstrzymana. Jeśli nic nie gra, uruchamia ostatnią stację albo otwiera listę ulubionych, zależnie od ustawienia. Dwukrotne szybkie naciśnięcie przechodzi bezpośrednio do wybranej karty. Trzykrotne naciśnięcie może wywołać osobną akcję, zależnie od ustawienia. |
| `Ctrl+Win+S` | Stop | Całkowicie zatrzymuje aktualną stację i resetuje odtwarzacz. |
| `Ctrl+Win+->` | Następna ulubiona | Przechodzi do następnej stacji na liście ulubionych. Po dojściu do końca wraca na początek listy. |
| `Ctrl+Win+<-` | Poprzednia ulubiona | Przechodzi do poprzedniej stacji na liście ulubionych. Na początku listy skacze na jej koniec. |
| `Ctrl+Win+Up` | Głośniej | Zwiększa głośność o 5; maksimum to 200. |
| `Ctrl+Win+Down` | Ciszej | Zmniejsza głośność o 5; minimum to 0. |
| `Ctrl+Win+V` | Dodaj do ulubionych | Dodaje aktualnie odtwarzaną stację do listy ulubionych. Informuje, jeśli stacja już jest na liście. |
| `Ctrl+Win+I` | Informacje o stacji | Odczytuje nazwę aktualnie odtwarzanej stacji. Naciśnij dwa razy, aby pokazać szczegóły, takie jak kraj, gatunek i przepływność, w oknie dialogowym. Naciśnij trzy razy, aby skopiować informacje o aktualnym utworze, czyli metadane ICY, do schowka, jeśli są dostępne; jeśli metadanych nie ma, rozpoczyna rozpoznawanie muzyki przez Shazam. Naciśnij cztery razy, aby wymusić rozpoznawanie muzyki, gdy metadane ICY są błędne. |
| `Ctrl+Win+M` | Kopia dźwięku | Kopiuje bieżący strumień równolegle na dodatkowe urządzenie wyjściowe audio. Ponowne naciśnięcie zatrzymuje kopiowanie. |
| `Ctrl+Win+E` | Nagrywanie natychmiastowe | Naciśnij raz, aby rozpocząć nagrywanie bieżącej stacji; naciśnij ponownie, aby zatrzymać. Naciśnij **dwa razy**, aby rozpocząć **nagrywanie utworu** - plik otrzyma nazwę bieżącego utworu, a nagrywanie zatrzyma się automatycznie po zmianie utworu. Dwukrotne naciśnięcie podczas aktywnego nagrywania utworu zatrzyma je wcześniej. Odtwarzanie trwa bez przerwy we wszystkich trybach nagrywania. Funkcja jest dostępna tylko dla stacji nadających metadane ICY. |
| `Ctrl+Win+W` | Otwórz folder nagrań | Otwiera w Eksploratorze plików folder z nagraniami. |
| *(nieprzypisane)* | Przełącz wyciszenie powiadomień | Przełącza ustawienie Wycisz powiadomienia w locie. Przypisz skrót w menu NVDA -> Preferencje -> Zdarzenia wejścia -> FreeRadio. |

Skróty następnej i poprzedniej stacji poruszają się tylko po liście ulubionych; nie działają z listą wszystkich stacji. Gdy fokus znajduje się na liście w oknie przeglądarki, lewa i prawa strzałka pełnią tę samą funkcję - zobacz Skróty w oknie dialogowym.

## Przeglądarka stacji

FreeRadio dodaje też podmenu **FreeRadio** do menu Narzędzia NVDA. Można z niego bezpośrednio otworzyć przeglądarkę stacji i ustawienia FreeRadio.

Okno otwierane skrótem `Ctrl+Win+R` zawiera pięć kart: Wszystkie stacje, Ulubione, Nagrywanie, Timer i Polubione utwory. Między kartami można przełączać się skrótem `Ctrl+Tab`.

Po otwarciu karty Wszystkie stacje automatycznie ładowanych jest 1000 najczęściej głosowanych stacji z Radio Browser. Wybranie kraju z listy rozwijanej aktualizuje listę i pokazuje stacje z tego kraju. Pisanie w polu wyszukiwania natychmiast uruchamia pełne wyszukiwanie w całej bazie Radio Browser, jednocześnie po nazwie, kraju i gatunku.

Lista **Urządzenie wyjściowe** na dole okna przeglądarki, poza kartami, zawiera wszystkie urządzenia audio rozpoznane przez BASS. Wybranie urządzenia natychmiast przekierowuje na nie dźwięk i zapisuje wybór na stałe; to samo urządzenie będzie użyte automatycznie w następnej sesji. Jeśli wybrane urządzenie nie jest podłączone, dodatek sam wraca do domyślnego urządzenia systemowego. Ta kontrolka działa tylko wtedy, gdy aktywny jest backend BASS.

Kontrolki **Głośność** (0-200) i **Efekty** w tym samym obszarze można zmieniać w dowolnej chwili, gdy okno jest otwarte. Z listy efektów można jednocześnie włączyć Chorus, Kompresor, Przesterowanie, Echo, Flanger, Gargle, Pogłos, EQ: wzmocnienie basu, EQ: wzmocnienie sopranów i EQ: wzmocnienie wokalu; zmiany są natychmiast stosowane do aktywnego strumienia. Te kontrolki działają w pełni tylko przy aktywnym backendzie BASS.

Gdy włączony jest co najmniej jeden efekt EQ, dla każdego aktywnego pasma pojawia się **kontrolka wzmocnienia**. Wzmocnienie można ustawić od -15 dB do +15 dB; wartości domyślne to bas +9 dB, soprany +9 dB i wokal +6 dB. Kontrolki są widoczne tylko dla aktualnie zaznaczonych pasm EQ i znikają automatycznie po odznaczeniu efektu. Wartości wzmocnienia są zapisywane globalnie i przywracane w następnej sesji.

Przycisk **Odtwórz/Wstrzymaj** również znajduje się na dole okna. Jeśli nic nie gra, uruchamia zaznaczoną stację; jeśli stacja już gra, wstrzymuje odtwarzanie.

Po zaznaczeniu stacji na liście przycisk **Szczegóły stacji** pokazuje informacje takie jak kraj, język, gatunek, format, przepływność, strona internetowa i adres URL strumienia w osobnym oknie. Każde pole znajduje się w osobnym, tylko do odczytu, polu tekstowym; można przechodzić między nimi Tabem i skopiować wszystkie informacje naraz przyciskiem **Kopiuj wszystko do schowka**. Ten przycisk jest dostępny na kartach Wszystkie stacje i Ulubione.

### Skróty w oknie dialogowym

Poniższe klawisze działają tylko wtedy, gdy aktywne jest okno Przeglądarka stacji.

### Klawisze funkcyjne

| Skrót | Funkcja | Opis |
|---|---|---|
| `F1` | Pomoc | Otwiera plik pomocy dodatku w domyślnej przeglądarce. Najpierw szukana jest pomoc w aktywnym języku NVDA; jeśli jej nie ma, otwierana jest wersja domyślna. |
| `F2` | Co jest odtwarzane | Odczytuje aktualnie odtwarzaną stację i nazwę utworu. Dwukrotne naciśnięcie pokazuje szczegóły, takie jak kraj, gatunek i przepływność, w oknie dialogowym. Trzykrotne naciśnięcie kopiuje informacje o utworze, czyli metadane ICY, do schowka, jeśli są dostępne; jeśli ich nie ma, uruchamia rozpoznawanie muzyki przez Shazam. Czterokrotne naciśnięcie wymusza rozpoznawanie muzyki przy błędnych metadanych ICY. |
| `F3` | Poprzednia stacja | Przechodzi do poprzedniej stacji na karcie Wszystkie stacje lub Ulubione i natychmiast rozpoczyna odtwarzanie. Na początku listy skacze na jej koniec. |
| `F4` | Następna stacja | Przechodzi do następnej stacji na karcie Wszystkie stacje lub Ulubione i natychmiast rozpoczyna odtwarzanie. Na końcu listy wraca na początek. |
| `F5` | Ciszej | Zmniejsza głośność o 5, minimum 0. |
| `F6` | Głośniej | Zwiększa głośność o 5, maksimum 200. |
| `F7` | Wstrzymaj / wznów | Wstrzymuje, jeśli stacja gra; wznawia, jeśli odtwarzanie jest wstrzymane i media są załadowane. |
| `F8` | Stop | Całkowicie zatrzymuje aktualną stację i resetuje odtwarzacz. |
| `F9` | Zmień nazwę | Otwiera dialog zmiany nazwy dla stacji z fokusem na karcie Ulubione. |

### Skróty listy i nawigacji

| Skrót | Funkcja | Opis |
|---|---|---|
| `->` | Następna stacja | Gdy fokus jest na liście Wszystkie stacje lub Ulubione, przechodzi do następnej stacji i odtwarza ją natychmiast. Na końcu listy wraca na początek. |
| `<-` | Poprzednia stacja | Gdy fokus jest na liście Wszystkie stacje lub Ulubione, przechodzi do poprzedniej stacji i odtwarza ją natychmiast. Na początku listy skacze na koniec. |
| `Enter` | Odtwórz | Gdy fokus jest na liście Wszystkie stacje lub Ulubione, natychmiast odtwarza zaznaczoną stację. Przełącza na zaznaczoną stację nawet wtedy, gdy inna już gra. |
| `Space` | Odtwórz / wstrzymaj | Wstrzymuje, jeśli stacja gra; w przeciwnym razie rozpoczyna odtwarzanie zaznaczonej stacji. |
| `Ctrl+Tab` | Następna karta | Przełącza na następną kartę: Wszystkie stacje -> Ulubione -> Nagrywanie -> Timer -> Polubione utwory. |
| `Ctrl+Shift+Tab` | Poprzednia karta | Przełącza na poprzednią kartę. |
| `Escape` | Ukryj | Ukrywa okno; dodatek nadal odtwarza w tle. |

### Skróty głośności

| Skrót | Funkcja | Opis |
|---|---|---|
| `Ctrl+Up` | Głośniej | Zwiększa głośność o 5. Działa tylko wtedy, gdy okno przeglądarki jest otwarte. |
| `Ctrl+Down` | Ciszej | Zmniejsza głośność o 5. Działa tylko wtedy, gdy okno przeglądarki jest otwarte. |

### Skróty Alt

| Skrót | Funkcja | Opis |
|---|---|---|
| `Alt+R` | Przejdź do pola wyszukiwania | Przenosi fokus do pola wyszukiwania. Radio Browser przeszukuje tekst z tego pola jednocześnie po nazwie, kraju i gatunku. |
| `Alt+V` | Dodaj / usuń ulubioną | Dodaje zaznaczoną stację do ulubionych; usuwa ją, jeśli jest już na liście. |
| `Alt+1` | Wszystkie stacje | Przełącza na kartę Wszystkie stacje. |
| `Alt+2` | Ulubione | Przełącza na kartę Ulubione. |
| `Alt+3` | Nagrywanie | Przełącza na kartę Nagrywanie. |
| `Alt+4` | Timer | Przełącza na kartę Timer. |
| `Alt+5` | Polubione utwory | Przełącza na kartę Polubione utwory. |
| `Alt+K` | Zamknij | Zamyka okno; dodatek nadal odtwarza w tle. |

## Ulubione

Lista ulubionych to osobista kolekcja stacji zapisywana na stałe. Aby dodać stację, zaznacz ją na liście i naciśnij przycisk Dodaj do ulubionych albo użyj skrótu `Alt+V`. Ten sam skrót usuwa stację, która już jest na liście.

Ulubione można odtwarzać skrótami `Ctrl+Win+->` i `Ctrl+Win+<-`; działają one nawet wtedy, gdy okno przeglądarki nie jest otwarte.

Aby usunąć stację z listy ulubionych, zaznacz ją i naciśnij przycisk **Usuń stację** albo klawisz `Delete`. Po usunięciu fokus i zaznaczenie automatycznie przechodzą na następną stację na liście. Jeśli usunięto ostatnią stację, fokus przechodzi na poprzednią. Jeśli lista stanie się pusta, fokus przechodzi na przycisk Odtwórz.

### Zmiana kolejności ulubionych

Po zaznaczeniu stacji na karcie Ulubione naciśnij `przecinek`, aby wejść w tryb przenoszenia - usłyszysz sygnał. Przejdź strzałkami do pozycji docelowej, a następnie naciśnij `przecinek` ponownie. Stacja zostanie umieszczona w wybranym miejscu, a nowa kolejność zapisana natychmiast. Ponowne naciśnięcie przecinka w tej samej pozycji anuluje przenoszenie.

### Dodawanie własnej stacji

Aby dodać stację, której nie ma w Radio Browser, użyj przycisku Dodaj własną stację. W wyświetlonym dialogu wpisz nazwę stacji i adres URL strumienia, aby dodać ją bezpośrednio do ulubionych. Własne stacje można odtwarzać i przenosić tak samo jak pozostałe ulubione.

### Profil audio stacji

Karta Ulubione zawiera dwa przyciski do zarządzania ustawieniami audio dla konkretnej stacji:

**Zapisz profil audio dla tej stacji** - zapisuje bieżący poziom głośności, aktywne efekty (chorus, EQ itd.) oraz wartości wzmocnienia EQ jako profil przypisany do konkretnej stacji. Za każdym razem, gdy ta stacja zacznie grać, zapisane ustawienia głośności, efektów i wzmocnień zostaną zastosowane automatycznie, zastępując ustawienia globalne.

**Wyczyść profil audio** - usuwa zapisany profil audio zaznaczonej stacji. Po wyczyszczeniu stacja wraca do globalnych ustawień głośności, efektów i wzmocnień EQ. Przycisk jest aktywny tylko wtedy, gdy zaznaczona stacja ma zapisany profil.

Oba przyciski znajdują się pod listą ulubionych i są aktywne tylko po zaznaczeniu stacji na liście.

## Rozpoznawanie muzyki

Trzykrotne naciśnięcie `Ctrl+Win+I` uruchamia rozpoznawanie muzyki przez Shazam dla aktualnie odtwarzanego strumienia. Rozpoznawanie zaczyna się tylko wtedy, gdy nie są dostępne metadane ICY, czyli informacje o utworze nadawane przez stację; jeśli metadane są dostępne, zostaną zamiast tego skopiowane do schowka.

Rozpoznawanie działa tak: krótka próbka audio jest przechwytywana ze strumienia przy użyciu ffmpeg, stosowany jest algorytm odcisku audio Shazama, a wynik wysyłany jest na serwery Shazama. Jeśli rozpoznawanie się powiedzie, NVDA odczyta tytuł utworu, wykonawcę, album i rok wydania oraz automatycznie skopiuje je do schowka. Jeśli opcja **Zapisuj polubione utwory do pliku tekstowego** jest włączona, wynik zostanie też dopisany do `likedSongs.txt`.

**Informacja dźwiękowa:** dwa rosnące sygnały oznaczają start rozpoznawania, a dwa opadające sygnały jego koniec. Krótki sygnał jest odtwarzany co 2 sekundy, gdy proces trwa.

**Wymaganie:** potrzebny jest `ffmpeg.exe`. Plik `ffmpeg.exe` umieszczony w folderze dodatku zostanie użyty automatycznie; jeśli znajduje się gdzie indziej, ścieżkę można ustawić w Ustawieniach. Pobierz ffmpeg ze strony [ffmpeg.org](https://ffmpeg.org/download.html).

## Kopia dźwięku

Skrót `Ctrl+Win+M` kopiuje aktualnie odtwarzany strumień na drugie urządzenie wyjściowe audio równocześnie z głównym odtwarzaniem. Przydaje się to do słuchania na dwóch różnych urządzeniach jednocześnie, na przykład przez głośniki i słuchawki.

Po pierwszym naciśnięciu pojawia się dialog wyboru z listą dostępnych urządzeń wyjściowych. Po wybraniu urządzenia rozpoczyna się kopiowanie, a główne odtwarzanie trwa bez przerwy. Ponowne naciśnięcie skrótu zatrzymuje kopiowanie.

**Przykłady użycia:**

- **Głośniki + słuchawki** - pozwól drugiej osobie słuchać tej samej audycji w słuchawkach, podczas gdy Ty słuchasz przez głośniki komputera.
- **Konfiguracja nagrywania** - skieruj główne wyjście na głośniki, a drugie na zewnętrzny rejestrator albo interfejs audio.
- **Kilka pomieszczeń** - odtwarzaj równocześnie przez głośnik Bluetooth i wbudowany głośnik; bez dodatkowego oprogramowania.
- **Monitorowanie zdalne** - podczas udostępniania ekranu albo pracy przez zdalny pulpit strumień może być słyszany po obu stronach.

> **Uwaga:** kopia dźwięku jest dostępna tylko wtedy, gdy aktywny jest backend BASS. Zmiana głośności podczas aktywnego kopiowania aktualizuje oba wyjścia jednocześnie.

## Nagrywanie

Nagrania są domyślnie zapisywane w `Documents\FreeRadio Recordings\`. Nazwa pliku zawiera nazwę stacji albo tytuł utworu w trybie nagrywania utworu oraz czas rozpoczęcia nagrywania. Folder nagrań można w dowolnej chwili zmienić w menu NVDA -> Preferencje -> Ustawienia -> FreeRadio -> **Folder nagrań**. Ponieważ silnik nagrywania łączy się bezpośrednio ze strumieniem, dźwięk jest zapisywany na dysku tak, jak został odebrany - bez przetwarzania i ponownego kodowania; jakość nagrania jest identyczna z jakością nadawania.

**Nagrywanie natychmiastowe:** podczas odtwarzania stacji naciśnij `Ctrl+Win+E` raz. Naciśnij ponownie, aby zatrzymać. Odtwarzanie trwa bez przerwy.

**Nagrywanie utworu:** naciśnij `Ctrl+Win+E` **dwa razy** szybko, gdy gra stacja nadająca metadane ICY. Nagrywanie rozpoczyna się natychmiast i otrzymuje nazwę bieżącego tytułu. Po zmianie utworu nagrywanie zatrzymuje się automatycznie, a NVDA ogłasza zapisaną nazwę pliku. Jeśli chcesz zakończyć wcześniej, naciśnij `Ctrl+Win+E` dwa razy ponownie. Jeśli bieżąca stacja nie nadaje metadanych ICY, nagrywanie utworu jest niedostępne i NVDA o tym poinformuje.

**Nagrywanie zaplanowane:** otwórz kartę Nagrywanie w przeglądarce. Wybierz stację z ulubionych, wpisz godzinę rozpoczęcia w formacie GG:MM i czas trwania w minutach, a następnie wybierz tryb nagrywania:

- **Nagrywaj podczas słuchania** - odtwarza i nagrywa jednocześnie. Backend odtwarzania uruchamiany jest w kolejności priorytetów BASS -> VLC -> PotPlayer -> Windows Media Player.
- **Tylko nagrywaj** - nagrywa cicho w tle bez wyjścia audio; silnik nagrywania łączy się bezpośrednio ze strumieniem.

Jeśli podana godzina już minęła, nagranie zostanie zaplanowane na następny dzień. NVDA ogłasza rozpoczęcie i zakończenie nagrywania.

## Timer

Otwórz kartę Timer w przeglądarce stacji (`Alt+4`). Można dodać dwa typy timerów:

**Alarm - uruchom radio:** automatycznie zaczyna odtwarzać wybraną stację z ulubionych o wskazanej godzinie. Wybierz stację i wpisz czas w formacie GG:MM.

**Uśpienie - zatrzymaj radio:** zatrzymuje odtwarzanie o wskazanej godzinie. Po uruchomieniu timera głośność jest stopniowo zmniejszana przez 60 sekund, zanim odtwarzanie zostanie zatrzymane. Nie trzeba wybierać stacji; wystarczy wpisać czas.

Dla obu typów, jeśli podana godzina już minęła, akcja zostanie zaplanowana na następny dzień. Oczekujące timery są widoczne na karcie; zaznacz jeden i naciśnij przycisk Usuń wybrany timer, aby go anulować.

## Ustawienia

Poniższe opcje można skonfigurować w menu NVDA -> Preferencje -> Ustawienia -> FreeRadio:

| Opcja | Opis |
|---|---|
| Urządzenie wyjścia audio (backend BASS) | Ustawia urządzenie wyjścia audio dla odtwarzania radia. Lista zawiera wszystkie urządzenia zgodne z BASS w systemie oraz opcję "Domyślne systemowe". Zmiany są stosowane natychmiast po zapisaniu; jeśli wybrane urządzenie zostanie odłączone, dodatek automatycznie wróci do domyślnego urządzenia systemowego i ogłosi zmianę. Opcja działa tylko wtedy, gdy używany jest backend BASS. |
| Głośność | Ustawia początkową głośność dodatku (0-200). Zmiany wykonane podczas odtwarzania skrótami `Ctrl+Win+Up` / `Ctrl+Win+Down` są również odzwierciedlane tutaj. |
| Domyślny efekt audio | Ustawia efekt audio stosowany przy starcie NVDA albo rozpoczęciu odtwarzania stacji. Wybrany efekt odpowiada liście Efekty w przeglądarce stacji. Opcja działa tylko z backendem BASS. |
| Wzmocnienie EQ (bas / soprany / wokal) | Ustawia poziom wzmocnienia w dB dla każdego pasma EQ (-15 do +15). Wartości obowiązują, gdy odpowiedni efekt EQ jest aktywny, i są zapisywane globalnie. Nadpisania dla pojedynczej stacji można zapisać przyciskiem **Zapisz profil audio** na karcie Ulubione. Opcja działa tylko z backendem BASS. |
| Sposób przełączania stacji (backend BASS) | Kontroluje zachowanie podczas przełączania między stacjami. **Natychmiastowe przełączenie** (domyślne) od razu zatrzymuje poprzednią stację przed uruchomieniem nowej. **Krótkie płynne przejście (1 sekunda)** i **Normalne płynne przejście (2 sekundy)** uruchamiają nową stację bez przerwy, a potem stopniowo wyciszają poprzednią w tle, gdy nowy strumień zostanie potwierdzony jako aktywny. Przy ustawieniu Natychmiastowe przełączenie nie ma wpływu na wydajność. Dostępne tylko z backendem BASS. |
| Wznów ostatnią stację przy starcie NVDA | Gdy włączone, ostatnio odtwarzana stacja jest automatycznie uruchamiana przy każdym starcie NVDA. |
| Automatycznie ogłaszaj zmiany utworów (metadane ICY) | Gdy włączone, NVDA automatycznie odczytuje nową nazwę utworu za każdym razem, gdy zmieni się na stacji nadającej metadane ICY. Pierwszy utwór jest ogłaszany również natychmiast po przełączeniu na nową stację. Domyślnie wyłączone. |
| Wycisz powiadomienia | Gdy włączone, NVDA nie ogłasza zmian stacji, zmian stanu odtwarzania (odtwórz, pauza, stop) ani zdarzeń nagrywania (rozpoczęte, zatrzymane, zakończone). Komunikaty błędów, informacje o ulubionych, wyniki rozpoznawania muzyki i powiadomienia aktualizacji nie są wyciszane. Można też przełączać w locie przez nieprzypisane zdarzenie wejścia. Domyślnie wyłączone. |
| Zapisuj polubione utwory do pliku tekstowego | Gdy włączone, informacje o utworze skopiowane do schowka trzykrotnym naciśnięciem `Ctrl+Win+I` są też dopisywane do `Documents\FreeRadio Recordings\likedSongs.txt`. Jeśli metadane ICY nie są dostępne, do tego samego pliku zapisany zostaje wynik rozpoznawania przez Shazam. Domyślnie wyłączone. |
| Gdy Ctrl+Win+P zostanie naciśnięty bez aktywnego odtwarzania | Określa, co stanie się po naciśnięciu skrótu, gdy nic nie gra: uruchomienie ostatniej stacji albo otwarcie listy ulubionych. |
| Gdy Ctrl+Win+P zostanie naciśnięty dwa razy | Wybiera akcję po dwukrotnym szybkim naciśnięciu skrótu: nic nie rób, otwórz listę ulubionych, otwórz kartę nagrywania albo otwórz kartę timera. Gdy wybrane jest "nic nie rób", pierwsze naciśnięcie reaguje natychmiast, bez opóźnienia. |
| Gdy Ctrl+Win+P zostanie naciśnięty trzy razy | Wybiera akcję po trzykrotnym szybkim naciśnięciu skrótu: nic nie rób, otwórz listę ulubionych, otwórz wyszukiwanie stacji, otwórz kartę nagrywania albo otwórz kartę timera. |
| Sprawdzaj aktualizacje automatycznie | Gdy włączone, przy każdym starcie NVDA działa w tle sprawdzanie aktualizacji; jeśli zostanie znaleziona nowa wersja, pojawi się powiadomienie. Gdy wyłączone, automatyczne sprawdzanie jest zatrzymane, ale ręczne nadal działa. |
| Ścieżka do ffmpeg.exe | Ścieżka do `ffmpeg.exe` używanego do rozpoznawania muzyki. Jeśli pozostanie pusta, automatycznie użyty zostanie `ffmpeg.exe` z folderu dodatku. |
| Ścieżka do VLC | Jeśli VLC nie jest zainstalowany albo znajduje się w nietypowym miejscu, można tutaj wpisać pełną ścieżkę do pliku wykonywalnego. |
| Ścieżka do wmplayer.exe | Wpisz tutaj ścieżkę do Windows Media Playera, jeśli jest potrzebna. |
| Ścieżka do PotPlayera | Jeśli PotPlayer znajduje się w nietypowym miejscu, można tutaj wpisać jego ścieżkę. |
| Folder nagrań | Ustawia folder, w którym zapisywane są nagrania. Jeśli pozostanie pusty, używana jest domyślna lokalizacja `Documents\FreeRadio Recordings\`. Przycisk Przeglądaj pozwala wybrać folder interaktywnie. Zmiany działają natychmiast po zapisaniu. |
| Wyłącz sprawdzanie połączenia internetowego przed odtwarzaniem | Zalecane dla użytkowników, u których występuje opóźnienie przed rozpoczęciem odtwarzania stacji. Przydatne również, gdy DNS jest blokowany. |

## Wyciszanie powiadomień

Gdy w ustawieniach włączone jest **Wycisz powiadomienia**, NVDA wycisza następujące automatyczne komunikaty:

- nazwa stacji po rozpoczęciu odtwarzania nowej stacji;
- zmiany stanu odtwarzania: odtwórz, pauza, stop;
- zdarzenia nagrywania: rozpoczęte, zatrzymane, zakończone (nagrania natychmiastowe, utworów i zaplanowane);
- komunikaty o zmianie utworu ICY, nawet gdy włączone jest też **Automatycznie ogłaszaj zmiany utworów**.

Celowo **nie** są wyciszane: komunikaty błędów, informacje o ulubionych (dodano / już na liście), wyniki rozpoznawania muzyki i powiadomienia aktualizacji.

Ustawienie można przełączyć w menu NVDA -> Preferencje -> Ustawienia -> FreeRadio albo natychmiast w dowolnym momencie przez nieprzypisane zdarzenie wejścia (przypisz je w menu NVDA -> Preferencje -> Zdarzenia wejścia -> FreeRadio). Po przełączeniu NVDA odczyta raz "Powiadomienia wyciszone" albo "Powiadomienia włączone", aby potwierdzić zmianę.

## Automatyczne ogłaszanie zmian utworów

Gdy w ustawieniach włączona jest opcja **Automatycznie ogłaszaj zmiany utworów**, FreeRadio sprawdza w tle strumień metadanych ICY aktywnej stacji mniej więcej co 5 sekund. Po zmianie utworu nowy tytuł jest automatycznie odczytywany przez NVDA - bez naciskania klawiszy.

Po przełączeniu na nową stację pierwsza informacja o utworze jest ogłaszana zaraz po nawiązaniu połączenia. Jeśli przełączysz na stację, która nie nadaje metadanych ICY, system pozostanie cichy, a informacje z poprzedniej stacji nie będą powtarzane.

Funkcja jest domyślnie wyłączona i można ją przełączyć w menu NVDA -> Preferencje -> Ustawienia -> FreeRadio.

## Polubione utwory

Gdy włączona jest opcja **Zapisuj polubione utwory do pliku tekstowego**, informacje o utworze skopiowane do schowka trzykrotnym naciśnięciem `Ctrl+Win+I` są także dopisywane w kolejnych wierszach do `Documents\FreeRadio Recordings\likedSongs.txt`.

Na stacjach nadających metadane ICY tytuł utworu i wykonawca są zapisywane bezpośrednio. Na stacjach bez metadanych ICY do tego samego pliku zapisywany jest wynik rozpoznawania przez Shazam - oba źródła używają jednej listy. Plik jest tworzony automatycznie, jeśli nie istnieje; każdy wpis jest dopisywany na końcu, a poprzednie wpisy nie są usuwane.

## Karta Polubione utwory

Karta **Polubione utwory** w przeglądarce stacji pokazuje wszystkie utwory zapisane w `likedSongs.txt`. Lista jest automatycznie ponownie wczytywana z pliku przy każdym otwarciu karty.

Wybranie utworu z listy włącza następujące akcje:

- **Odtwórz w Spotify:** próbuje otworzyć bezpośrednio aplikację Spotify na komputerze. Jeśli aplikacja nie jest zainstalowana, otwiera stronę Spotify i automatycznie zaczyna odtwarzać pierwszy wynik.
- **Odtwórz w YouTube (`Alt+O`):** wyszukuje wybrany utwór w YouTube i otwiera wyniki w domyślnej przeglądarce.
- **Usuń (`Alt+M`):** usuwa wybrany utwór z `likedSongs.txt` i aktualizuje listę. Klawisz `Delete` również uruchamia ten przycisk, gdy fokus jest na liście.
- **Odśwież (`Alt+E`):** ponownie wczytuje listę z pliku.

Przyciski Spotify, YouTube i Usuń są aktywne tylko wtedy, gdy na liście wybrany jest rzeczywisty utwór.

## Odtwarzanie

Dodatek wybiera backend odtwarzania w następującej kolejności priorytetów:

1. **BASS** - domyślny i główny backend. Nie wymaga osobnej instalacji; jest dołączony do dodatku. BASS wysyła dźwięk bezpośrednio do stosu audio Windows i pojawia się w mikserze głośności Windows jako niezależne źródło audio o nazwie "pythonw.exe", oddzielone od NVDA. Oznacza to, że dźwięk FreeRadio płynie całkowicie osobnym kanałem niż mowa NVDA: radio nie zanika, nie miesza się i nie jest zależne od ustawień audio NVDA, gdy NVDA mówi. Użytkownik może regulować głośność radia niezależnie od NVDA w mikserze głośności Windows. Obsługuje HTTP, HTTPS i większość osadzonych formatów strumieni. Kopia dźwięku jest dostępna tylko z tym backendem.
2. **VLC** - przejmuje odtwarzanie, jeśli BASS zawiedzie. Jest automatycznie szukany w typowych lokalizacjach instalacji, folderach profilu użytkownika i w systemowym PATH.
3. **PotPlayer** - używany, jeśli VLC nie zostanie znaleziony. Jest automatycznie szukany w typowych lokalizacjach instalacji.
4. **Windows Media Player** - używany jako ostatnia możliwość; wymaga zainstalowanego komponentu WMP w systemie.

## Sprawdzanie aktualizacji

FreeRadio automatycznie sprawdza nowe wersje przez GitHuba.

**Sprawdzanie automatyczne:** działa cicho w tle 15 sekund po starcie NVDA. Jeśli zostanie znaleziona nowa wersja, pojawi się powiadomienie; jeśli nie, nie pojawia się żaden komunikat.

**Sprawdzanie ręczne:** można uruchomić na żądanie z menu NVDA -> Narzędzia -> FreeRadio -> **Sprawdź aktualizacje...**. Przy ręcznym uruchomieniu wynik jest ogłaszany nawet wtedy, gdy wersja jest aktualna.

**Gdy znajdzie się aktualizacja:** pojawia się dialog z numerem nowej wersji i wersją zainstalowaną.

- Jeśli w wydaniu GitHuba jest dostępny bezpośrednio pobieralny plik `.nvda-addon`, pojawia się przycisk **Pobierz i zainstaluj**. Po potwierdzeniu plik jest pobierany w tle, NVDA ogłasza rozpoczęcie pobierania, a następnie automatycznie otwiera własny ekran instalacji NVDA.
- Jeśli nie ma bezpośredniego linku pobierania, pojawia się przycisk **Otwórz stronę**, który otwiera stronę wydania GitHuba w domyślnej przeglądarce.

**Aby wyłączyć automatyczne sprawdzanie:** wyłącz opcję **Sprawdzaj aktualizacje automatycznie** w menu NVDA -> Preferencje -> Ustawienia -> FreeRadio.

## Licencja

GPL v2
