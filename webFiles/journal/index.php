<?php
//password to access the entries
$pass = "rectalgia";

//ensure proper time zone
date_default_timezone_set('America/Chicago');

//var_dump($_POST);

//location of the entries
$entriesFile = "./entries.json";

?>
<!DOCTYPE HTML>
<html>
  <head>
    <title>Daily Journal</title>
    <link rel="stylesheet" type="text/css" href="./journal.css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
<?php
//if a password is set or if the date and entry are set
if((array_key_exists("pass",$_POST) and $_POST['pass']==$pass) or (array_key_exists('date',$_POST) and array_key_exists("entry",$_POST))) {
  //load the entries
  if(is_file($entriesFile)) {
    $entries = json_decode(file_get_contents($entriesFile),true);
  } else {
    $entries = array();
  }

  //if data is present, write to the file
  if(array_key_exists("date",$_POST) and array_key_exists("entry",$_POST)) {
    //TODO: clean up inputs
    $entries[$_POST['date']] = $_POST['entry'];
    //write to file
    $savestatus = file_put_contents($entriesFile,json_encode($entries));
    if($savestatus) {
      echo "<p style=\"color: green;\">Saved entry</p>";
    } else {
      echo "<p style=\"color: red;\">Error saving entry. Try Again.</p>";
    }
  }

  if(array_key_exists('date',$_GET)) {
    $displayeddate = $_GET['date'];
  } else {
    $displayeddate = date("Y-m-d");
  }
  if(array_key_exists($displayeddate,$entries)) {
    $displayedentry = $entries[$displayeddate];
  } else {
    $displayedentry = "Today I ";
  }
?>
    <form name="journalEntry" method="post">
      <input name="date" type="date" value="<?php echo $displayeddate; ?>" disabled="disabled">
      <br>
      <p>What did you do today?</p>
      <textarea name="entry" autofocus><?php echo $displayedentry; ?></textarea>
      <br>
      <button type="submit">Done</button>
    </form>
    <p>Note: if the date is of a previous entry, it will overwrite it</p>
    <p><b>Previous Entries</b></p>
    <?php foreach(array_keys($entries) as $k) { echo "<p><a href=\"?date=$k\">$k</a></p>"; } ?>
<?php } else { ?>
    <form name="pw" method="post">
      <p id="passline">Password: <input name="pass" type="password" autofocus><button type="submit" >Submit</button></p>
<?php } ?>
  </body>
</html>
