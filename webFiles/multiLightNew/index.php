<?php
/* Steven Williams
 * 5/2019
 *
 */

/*
this page is meant to be for the user to use a click-and-drag interface to turn on lights,
as well as a file uploader and providing a text input option
user uses a radio button to select which type they wish to input (file, text, individual, or pre-programmed)


todo:
-add save option for pattern - done
-add ctrl click for color select
-add delete pattern option
-get position data from json file
-set up 3d interface
*/

//number of lights on the tree
$numLights = 250;
//file containing json data of lights currently on tree
$dataFile = './resources/lights.txt';
//folder to save user patterns into
$saveFolder = "./savedLights/";

//this file contains the functions used in the rest of the programs
include "./resources/functions.php";

$lightData = keysStartWith($_POST,"lightData"); //isolate lightdata from other data


//get the function - should be: update, save, load, auto,
switch(keysStartWith($_POST,"function")["function"]){
  case "update":
    saveJsonFile($lightData,$dataFile); //save lightData to dataFile
    updateTree();
    break;
  case "save":
    //ensure file isset and has a length>0, else set as "blank"
    $file2save = "blank";
    if(isset($_POST['saveFile'])) {
      //echo "<script>alert(".strlen($_POST['saveFile']).");</script>";
      if(strlen($_POST['saveFile'])>0) { $file2save = sanitizeData($_POST['saveFile']); }
    }

    saveJsonFile($lightData,$dataFile); //save only lightData to dataFile

    saveJsonFile($lightData, $saveFolder.$file2save); //save to file
    break;
  case "load":
    $file2load = "blank";
    if(isset($_POST['loadFile'])) {
      if(strlen($file2load)>0) { $file2load = sanitizeData($_POST['loadFile']); }
    }
    $lightData = readJsonFile($saveFolder.$file2load);
    saveJsonFile($lightData,$dataFile);
    break;
  case "auto":
    break;
  default:
    break;
}

//read $dataFile into array
$lightData = readJsonFile($dataFile);




//start html display
?>
<!DOCTYPE html>

<html>
  <head>
    <title>Happy Holidays!</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="./resources/tree.png" />
    <link type="text/css" rel="stylesheet" href="./resources/home.css" />
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script type="text/javascript" src="./resources/functions.js"></script>
  </head>
  <body onmousedown="mousedown();" onmouseup="mouseup();">

    <p><?php echo $function['function'];?></p>

    <p id="title">Enter a color to color the lights. Click to color, right click or double click to turn off</p>
    <p>Choose a Color: <input type="color" name="color" id="color" onchange="updateColorText();" value="#ff0000" autofocus> #<input type="text" name="colorText" id="colorText" maxlength="6" onkeypress="this.onchange();" onpaste="this.onchange();" oninput="this.onchange();" onchange="updateColor();" value="ff0000"></p>
    <form method="post">
      <form method="post">
      <div id="tree" oncontextmenu="return false;">
<?php
//display lights in triagular pattern

$i = $numLights-1; //allows botom right light to be index 0, top light is last light in strand
$numRows = ceil(-0.5+sqrt(2*($numLights)+.25)); //determines the number of rows needed for a triangle (with num elements in a row=row number) given the number of lights

//loop through rows
for($j=0;$j<$numRows;$j++) {
  $k = 0; //index of light in a row (0=leftmost, j=rightmost)
  //loop through lights per row
  while($k<=$j && $i>=0) {
    //check if light color value exists
    if(isset($lightData['lightData'.$i])) {
      $val = $lightData['lightData'.$i];  //if light exists, set color val to data
    } else {
      $val = "000";  //if it doesn't exist, set value to black
    }

    //display light div and hidden input data
?>
      <div class="light" onmousedown="mousedown();" onclick="changeColor(this);" oncontextmenu="clearBack(this);" ondblclick="clearBack(this);" id="light<?php echo $i; ?>" style="background-color: #<?php echo $val;?>;"></div>
      <input type="hidden" id="lightData<?php echo $i; ?>" name="lightData<?php echo $i; ?>" value="<?php echo $val;?>">
<?php
    $i--; //incriment light down
    $k++; //incriment light in row up - might have to change
  }
  echo "<br>\n"; //new line
}
?>
      </div>
      <p><?php echo $file2load;?></p>
      <p><button value="update" type="submit" name="function" class="button">Update Tree</button></p>

      <p style="font-size: 11pt;">There are <?php echo $numLights;?> lights in <?php echo $numRows;?> rows on this tree.</p>


        <p style="line-height: 200%;">Save Pattern: <input type="text" maxlength="16" pattern="[A-Za-z0-9 ]{1,16}" id="saveFile" name="saveFile" title="Name must be letters and numbers only"> <button name="function" value="save" class="button" type="submit">Save and Update Tree</button></p>
      </form>
      <p>Saving with the same name as another pattern will update that pattern</p>
    </form>

    <div id="fileList">
      <p>Saved Patterns:</p><br>
      <form method="post">
        <input type="hidden" value="load" name="function">
    <?php
    $files = preg_grep('/^([^.])/', scandir($saveFolder)); //remove hidden files/dirs
    foreach($files as $e) {
      $e = pathinfo($e, PATHINFO_FILENAME);
?>
      <p><input type="submit" value="<?php echo $e; ?>" name="loadFile" class="fileInput"></p>
<?php
    }
    ?>
      </form>
    </div>
    <p><a href="./3dtest/">Check out the 3D version underway!</a></p>
    <div id="credits">Made with &lt;3 by Senior Design Group 10 - 2019</div>
  </body>
</html>