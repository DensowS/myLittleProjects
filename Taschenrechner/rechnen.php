<?php

#POST von der HTML Seite in php POST Array speichern
#$_POST[] -> von der HTML Seite über form Methode POST gesendet

if (!empty($_POST["submit"])) {
    # Zahl 1, Zahl 2 und Operator aus dem POST Array holen
    $_zahl1 = $_POST["zahl1"];
    $_zahl2 = $_POST["zahl2"];
    $_operator = $_POST["operator"];

    # Berechnungen
    if ($_operator == "+") {
        // bcadd: Methode in PHP (zahl1, zahl2, Anzahl Nachkommastellen)
        $ergebnis = bcadd($_zahl1, $_zahl2, is_int($_zahl1 + $_zahl2) ? 0 : 2);
        echo $_zahl1 . $_operator . $_zahl2 . "=" . $ergebnis;
    } else if ($_operator == "-") {
        // bcsub: Methode in PHP (zahl1, zahl2, Anzahl Nachkommastellen)
        $ergebnis = bcsub($_zahl1, $_zahl2, is_int($_zahl1 - $_zahl2) ? 0 : 2);
        echo $_zahl1 . $_operator . $_zahl2 . "=" . $ergebnis;
    } else if ($_operator == "*") {
        // bcmul: Methode in PHP (zahl1, zahl2, Anzahl Nachkommastellen)
        $ergebnis = bcmul($_zahl1, $_zahl2, is_int($_zahl1 * $_zahl2) ? 0 : 2);
        echo $_zahl1 . $_operator . $_zahl2 . "=" . $ergebnis;
    } else if ($_operator == "/" && $_zahl2 != 0) // Division durch 0 nicht erlaubt
    {
        // bcdiv: Methode in PHP (zahl1, zahl2, Anzahl Nachkommastellen)
        $ergebnis = bcdiv($_zahl1, $_zahl2, is_int($_zahl1 / $_zahl2) ? 0 : 2);
        echo $_zahl1 . $_operator . $_zahl2 . "=" . $ergebnis;
    } else {
        echo "Fehler: Division durch 0 nicht erlaubt.";
    }
}

?>