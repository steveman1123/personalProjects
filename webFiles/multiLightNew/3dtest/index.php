<?php
$localroot = $_SERVER['DOCUMENT_ROOT'];
$root = substr(getcwd(),strlen($localroot));

/* TODO:
 * - ensure all post data is sanitized
 * - execute python code
 */

//file containing json data of lights currently on tree
$dataFile = './resources/lights.txt';
//folder to save user patterns into
$saveFolder = "./savedLights/";
//this file contains the functions used in the rest of the programs
include "./resources/functions.php";


$jsonData = $_POST['jsonData']; //receive json data

switch(keysStartWith($_POST,"function")["function"]){
  case "update":
    saveJsonFile($jsonData,$dataFile); //save jsonData to dataFile
    break;
  case "save":
    //ensure file isset and has a length>0, else set as "blank"
    $file2save = "blank";
    if(isset($_POST['saveFile'])) {
      //echo "<script>alert(".strlen($_POST['saveFile']).");</script>";
      if(strlen($_POST['saveFile'])>0) { $file2save = sanitizeData($_POST['saveFile']); }
    }
    if($file2save<>"blank") {
      saveJsonFile($jsonData,$dataFile); //save only jsonData to dataFile
      saveJsonFile($jsonData, $saveFolder.$file2save); //save to file
    } else {
      echo "<script>alert('Cannot save with that name.');</script>";
    }
    break;
  case "loadDelete": //load/delete selected file
    //TODO: add logic to determine if a file is to be deleted
    $file2load = "blank"; //init as "blank"
    $file2delete = "blank"; //init as "blank"
    if(isset($_POST['loadFile'])) { //if post data exists
      if(strlen($file2load)>0) { //if post data is>0 chars
        $file2load = sanitizeData($_POST['loadFile']); //sanitize and set
      }
    $jsonData = readJsonFile($saveFolder.$file2load); //read json into var
    saveJsonFile($jsonData,$dataFile); //save json data to tree file
    } elseif(isset($_POST['delete'])) { //if delete is the function
      $file2delete = $_POST['delete'];
      if(file_exists($saveFolder.$file2delete)) { //if the file exists
        if($file2delete<>"blank"){ //if it's not the blank template
          unlink($saveFolder.$file2delete);//delete it
        } else {
          echo "<script>alert('Cannot delete that pattern.');</script>";
        }
      }
    }
    break;
  default:
    break;
}

?>

<!DOCTYPE html>
<html>
  <head>
    <title>3D Test</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link type="text/css" rel="stylesheet" href="./resources/home.css" />
  </head>
  <body style="text-align: center; width: 100%; height: 100%; margin: 0;" onload="setup();">

    <br>
   <p>Choose a Color: <input type="color" name="color" id="color" onchange="updateColorText();" value="#ff0000" autofocus> #<input type="text" name="colorText" id="colorText" maxlength="6" onkeypress="this.onchange();" onpaste="this.onchange();" oninput="this.onchange();" onchange="updateColor();" value="ff0000"></p>
   <p><input type="checkbox" id="picker"> Use Color Picker</p>
    <p>Paste an Image URL <input type="text" id="imgURL" onpaste="this.onchange();" oninput="this.onchange();" onkeypress="this.onchange();" onload="this.onchange();" onchange="dispImage();"><span style="font-size: 10pt"> (file must be jpg, png, or bmp)</style></p>

    <canvas id="canv" oncontextmenu="return false;"></canvas>
    <p id="angleP"></p>
    <p><input type="range" style="width: 300px; height: 30px; border: solid black 1px;" min=-180 max=180 id="angle" oninput="updateAngleText();"></p>
    <form method="post">
      <input type="hidden" name="jsonData" id="jsonData" value='<?php echo readJsonFile($dataFile) ?>'>
      <button type="submit" onclick="setJsonData();" class="button" value="update" name="function">Update Tree</button>
      <div class="listWrap">
        <form method="post">
          <input type="text" name="saveFile" placeholder="Pattern Name">
          <button type="submit" class="button" value="save" name="function" onclick="setJsonData();">Save Tree Pattern</button>
        </form>
        <form method="post">
          <input type="hidden" name="function" value="loadDelete">
          <p>Saved Patterns</p>
          <div id="fileList" class="list">
<?php
      $files = preg_grep('/^([^.])/', scandir($saveFolder)); //remove hidden files/dirs
    foreach($files as $e) {
      $e = pathinfo($e, PATHINFO_FILENAME);
?>
            <p><button class="trash" name="delete" value="<?php echo $e; ?>" type="submit" onclick="return confirm('Are you sure you want to delete the pattern "<?php echo $e;?>"?');"><div class="trashPic"></div></button><input type="submit" name="loadFile" value="<?php echo $e; ?>" class="fileName"></p>
<?php } ?>
          </div>
        </form>
      </div>
    </form>

<br><p id="foot">Made with &lt;3 By Senior Design Group 10</p>
  </body>
</html>

<script type="text/javascript" src="./resources/functions.js"></script>
<script type="text/javascript" src="./resources/xmasTree2.js"></script>
