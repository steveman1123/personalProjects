<?php

$url = "https://stocksunder1.org/";

$t = file_get_contents($url);

//var_dump($t);

$table = explode('<table',explode('</table>',$t)[5])[1];
$rows = explode('<tr>',$table);

for($i=0;$i<sizeof($rows);$i++) {
  $rows[$i] = explode('<td>',$rows[$i]);
  for($j=0;$j<sizeof($rows[$i]);$j++) {
    $rows[$i][$j] = preg_replace('',"",$rows[$i][$j]);
  }
}

var_dump($rows);
