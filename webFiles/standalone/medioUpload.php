<!DOCTYPE html>

<?php

$pass = "moist"; //file upload password


if(key_exists("vidFiles",$_FILES) and sizeof($_FILES['vidFiles']['name'])>0) {
  //TODO: ensure file types are only mp4, reject all others
  //display the files received page
  var_dump($_FILES);

} else { //display the expected page
  
?>

<html>
  <head>
    <title>Medio Upload</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      html, body {
        width: 100%;
        height: 100%;
        text-align: center;
        font-family: sans-serif;
        margin: 0;
      }
      #error {
        color: red;
      }
      p {
        width: 50%;
        text-align: center;
        margin: 5 auto;
      }
      
      @media screen and (max-width: 640px){
        p {
          width: 90%;
        }
      }
      body {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
      }
    </style>
  </head>
    <body>
  <?php
  if(key_exists("passwd",$_POST) and strcmp($_POST["passwd"],$pass)==0) {
    ?>
    <p>This is for video uploading for the Movies section of the site. <a href="mailto:smw1109@protonmail.com">hmu</a> if you want to add something to another part of the site</p>
      <form method="post" enctype="multipart/form-data">
        <input type="file" name="vidFiles[]" id="vidFiles" multiple accept="video/mp4" autofocus>
        <input type="submit" value="Go" name="submit">
      </form>
    <?php
  } else { //passwd either not set or is incorrect
    if(key_exists("passwd",$_POST)) {
      ?>
    <p id="error">Incorrect Password</p>
      <?php
    }
    ?>
    <p>Password Required:</p>
    <form method="post">
      <input type="password" name="passwd" id="passwd" autofocus>
    </form>
    <?php
  }
  ?>
  </body>
</html>
<?php
}
?>
