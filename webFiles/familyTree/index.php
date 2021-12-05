<?php
$localroot = $_SERVER['DOCUMENT_ROOT']; //location of this file as seen by the server
$root = str_replace("\\","/",substr(getcwd(),strlen($localroot)));  //location of this file as seen by the public

?>

<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8">
    <meta name="description" content="A user friendly family tree maker">
    <title>Family Tree Maker</title>
    <link rel="stylesheet" type="text/css" href="./resources/home.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body onload="setup();">
    <div id="canvDiv">
      <canvas id="canvas">Your Browser does not support html5 Canvas. Please update to a newer version.</canvas>
    </div>
    <div id="inputs">
      <p><input id="familyName" placeholder="familyName"><input id="firstName" placeholder="First Name"><input id="middleNames" placeholder="Middle Name(s)"></p>
      <p>Birth date <input type="date" id="birthDate"> Death date <input type="date" id="deathDate"></p>
      <p><textarea id="occupations" placeholder="Occupations"></textarea></p>
      <p><textarea id="notes" placeholder="Notes"></textarea></p>
      <div id="files">
        <p>Add some relavant files (birth certificates, medical records, etc)</p>
        <input type="file" multiple>
      </div>
    </div>
  </body>
</html>
<script type="text/javascript" src="./resources/home.js"></script>