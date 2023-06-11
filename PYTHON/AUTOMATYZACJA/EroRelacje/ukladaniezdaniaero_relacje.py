import time
import random
#ukladanie zdania do relacji insta,fb


poczatek = ["Seksi", "Seksowna", "Przepiękna", "Urocza", "Piękna", "Ładna", "Atrakcyjna", "Wyjątkowa", "Niegrzeczna","Milutka","Zjawiskowa","Czarująca","Fascynująca","Niezwykła","Olśniewająca","Zachwycająca","Porywająca","Namiętna"]
#link do relacji https://randki5minut.mobirisesite.com/


imiona = ['Maria', 'Anna', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Barbara', 'Krystyna', 'Ewa', 'Teresa', 'Joanna',
          'Magdalena', 'Zofia', 'Jadwiga', 'Danuta', 'Monika', 'Elżbieta', 'Halina', 'Beata', 'Irena', 'Dorota',
          'Bożena', 'Renata', 'Aleksandra', 'Marta', 'Janina', 'Kamila', 'Kinga', 'Wanda', 'Natalia', 'Karolina',
          'Patrycja', 'Mariola', 'Klaudia', 'Julia', 'Grażyna', 'Paulina', 'Helena', 'Aneta', 'Agata', 'Dominika',
          'Iwona', 'Weronika', 'Jolanta', 'Kornelia', 'Katarzyna', 'Sabina', 'Milena', 'Anita', 'Blanka', 'Alicja',
          'Adriana', 'Ewelina', 'Marlena', 'Katarzyna', 'Agata', 'Oliwia', 'Maja', 'Róża', 'Marta', 'Katarzyna',
          'Aleksandra', 'Marzanna', 'Patrycja', 'Renata', 'Sylwia', 'Agnieszka', 'Elżbieta', 'Joanna', 'Aniela',
          'Wioletta', 'Kamila', 'Katarzyna', 'Dagmara', 'Nina', 'Paula', 'Martyna', 'Łucja', 'Dominika', 'Justyna',
          'Adrianna', 'Izabela', 'Klaudia', 'Joanna', 'Ewelina', 'Olga', 'Aleksandra', 'Karina', 'Katarzyna', 'Inga',
          'Alicja', 'Karolina', 'Katarzyna', 'Marta', 'Anita', 'Katarzyna', 'Angelika', 'Natasza', 'Ilona', 'Natalia',
          'Martyna', 'Jagoda', 'Karolina', 'Daria', 'Katarzyna', 'Anita', 'Natalia', 'Katarzyna', 'Katarzyna', 'Marta',
          'Adrianna', 'Barbara', 'Paula', 'Patrycja', 'Magdalena', 'Kamila', 'Monika', 'Magdalena', 'Marta', 'Katarzyna',
          'Klaudia', 'Ewa', 'Weronika', 'Iwona', 'Ewelina', 'Aleksandra', 'Agnieszka', 'Kamila', 'Joanna', 'Sandra',
          'Natalia', 'Martyna', 'Katarzyna', 'Monika', 'Ewa', 'Patrycja', 'Anita', 'Aleksandra', 'Beata', 'Małgorzata',
          'Aleksandra', 'Monika', 'Jolanta', 'Karolina', 'Katarzyna', 'Zuzanna', 'Monika', 'Marta', 'Weronika',
          'Aleksandra', 'Katarzyna','Alicja', 'Oliwia', 'Emilia', 'Natalia', 'Nikola', 'Antonina', 'Lena', 'Nina', 'Iwona', 'Adrianna','Anastazja', 'Wanda', 'Lilia', 'Liwia', 'Gabriela', 'Julita', 'Martyna', 'Miriam', 'Lidia', 'Daria',
          'Ewelina', 'Maja', 'Agnieszka', 'Aurelia', 'Iga', 'Jagna', 'Sara', 'Sonia', 'Ludmiła', 'Kamila',
          'Roksana', 'Róża', 'Aurelia', 'Czesława', 'Elena', 'Lila', 'Maryla', 'Nadia', 'Renata', 'Wioletta',
          'Amanda', 'Apolonia', 'Celina', 'Izabela', 'Lea', 'Leila', 'Ligia', 'Lilia', 'Marlena', 'Mia']

wiek = [25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41]



hook = ["Przyszedłbyś ze mną poćwiczyć?","Chciałbyś mnie wymasować?","Chcesz się namiętnie porozciągać?","Co mnie myślisz?","Może się spotkamy?","Co byś zrobił ze mną sam na sam?","Chcesz spalić ze mną kalorie?","Czy byłbyś w stanie się skupić, gdybyś mnie zobaczył?","Czy znalazłby się ktoś, kto mógłby mi pomóc trenować w łózku","Czy jest któs kto mógłby mnie trenować w łóżku?","Jak spędził byś ze mną wolny czas?","Napijemy się razem kawy?","Spędzimy razem wieczór?","Jestem ładna dla ciebie?","Chcę, żebyś zawsze otaczał mnie ramionami","Uczyń mnie swoją księżniczką","Kto ma ochotę na kolację ze mną?","Co sądzisz o moim stroju?","Chcesz zobaczyć moją bieliznę?","co przychodzi ci do głowy, kiedy na mnie patrzysz?","Chcesz się ze mną spotkać?","Przyjdź i powiedz mi, o czym dzisiaj myślisz","Co mogę dla ciebie zrobic?","Czy moja figura jest w twoim typie?","Jakie jest twoje zdanie na temat mojego stroju?","Chodź tu i daj mi klapsa","Czy mogę być twoją małą niewolnicą","Może do mnie dołączysz?","Bardzo tęsknię za ciepłą pogoda 😩 A Wy?","Ocena od 1 do 10?","Chcesz trochę mnie?","Przytul się do mnie jeśli chcesz","Chcę, żeby ktoś mnie mocno przytulił","Chcesz spędzic ze mną czas ?","Z ubraniem czy bez,Co myślisz?","Ma ktoś ochotę mnie pomasować?","Zawsze możesz oprzeć się na moim ramieniu. albo nawet na mój soczysty tyłek","Napijemy się razem kawy?","Spędzimy razem wieczór?","Jestem ładna dla ciebie?","Chcę, żebyś zawsze otaczał mnie ramionami","Uczyń mnie swoją księżniczką","Kto ma ochotę na kolację ze mną?","Co sądzisz o moim stroju?","Spełnie twoje fantazje,jesteś chętny?","Chcesz zobaczyć moją bieliznę?","co przychodzi ci do głowy, kiedy na mnie patrzysz?","Chcesz się ze mną spotkać?","Przyjdź i powiedz mi, o czym dzisiaj myślisz","Co mogę dla ciebie zrobic?","Czy moja figura jest w twoim typie?","Jakie jest twoje zdanie na temat mojego stroju?","Chodź tu i daj mi klapsa","Spędzimy namiętnie wieczór?","Czy mogę być twoją małą niewolnicą?","Może do mnie dołączysz?","Bardzo tęsknię za ciepłą pogoda 😩 A Wy?","Ocena od 1 do 10?","Chcesz trochę mnie?","jeśli pozwolę, zrobisz mi niegrzeczne rzeczy?","Co byś zrobił gdybyś mnie zobaczył taką w twoim łóżku?","Lato musi przyjść wcześniej","pójdziesz za mną wszędzie i zagrasz ze mną w coś niegrzecznego?","Podoba ci się taki widok?","Chodź, zabaw się ze mną","jestem samotna, czy są jacyś faceci, którzy chcą porozmawiać z seksowną dziewczyną taką jak ja?","Czy lubisz to co widzisz?","Co jeśli poproszę cię o wylizanie mnie do czysta?","Jak w tym wyglądam?","Napijemy się razem wina?","Obejrzymy wspolnie film?","Chcesz zobaczyć, co jest pod ubraniem?"]





for i in range(1, 2):
    sentence = f"{random.choice(hook)} Przesuń w góre"
    print(sentence)

