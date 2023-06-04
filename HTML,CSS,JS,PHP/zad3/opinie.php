<!DOCTYPE html>
<head>

<link rel="stylesheet" href="styl3.css">
<title>Opinie klientów</title>


<?php
$dane = mysqli_connect("localhost", "root", "",
"hurtownia");

if ($dane->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully";









?>


</head>

<body>

<div class="baner">
<h1>Hurtownia spożywcza</h1>

</div>

<div class="glowny">
<h2>Opinie naszych klientów</h2>



<?php
$polecenie1 = mysqli_query($dane ,"SELECT zdjecie, imie, opinia FROM klienci JOIN opinie ON
klienci.id = klienci_id WHERE Typy_id=2 OR Typy_id=3;");

while($wiersz2 = mysqli_fetch_row($polecenie1)){
  echo ("
  $wiersz2[0]<br>
  $wiersz2[2]<br>
  $wiersz2[1]<p>

");
}


?>

</div>

<div class="stopka1">
<h3>Współpracują z nami</h3>
<a href="http://sklep.pl">Sklep 1</a>

</div>

<div class="stopka2">


<h3>Nasi top klienci</h3>
<ol>
<?php

$polecenie2 = mysqli_query($dane ,"SELECT imie, nazwisko, punkty FROM klienci ORDER BY punkty DESC
LIMIT 3;");

while($wiersz2 = mysqli_fetch_row($polecenie2)){
  echo ("
  <li>$wiersz2[0] $wiersz2[1], $wiersz2[2] pkt</li>


");

}


mysqli_close($dane);
?>
</ol>

</div>

<div class="stopka3">
<h3>Skontaktuj się</h3>
<p>telefon:111222333
</div>

<div class="stopka4">
<h3>Autor:00000000</h3>
</div>


</body>