<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Breathing Exercises</title>
<style>
body,html {
  background-color: black;
  font-family: sans-serif;
  padding: 12px;
  color: white;
}
body * {
  font-size: 14pt;
}

a {
  color: #2af;
  text-decoration: none;
}

</style>
  </head>
  <body>
    <h1>Breathing Exercises</h1>

<?php
//specify files to exclude
$exclude = ['.','..',"./index.php"];
$dir = "./";

$files = preg_grep('/^([^.])/', scandir($dir)); //remove hidden files/dirs

foreach($files as $e) { //loop through files
  $link = $dir.$e;
  if(!in_array($link,$exclude)) {
    echo "<p><a href='./$e'>".basename($e,".html")."</a></p>";
  }
}
?>

  </body>
</html>
