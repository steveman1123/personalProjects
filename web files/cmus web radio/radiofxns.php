<?php

if(array_key_exists("cmd",$_POST)) {
  switch($_POST['cmd']) {
    case "prev":
      echo "back";
      //exec("cmus-remote something"); //exec cmus cmd
      break;
    case "pp":
      echo "play/pause";
      //exec("cmus-remote something"); //exec cmus cmd
      break;
    case "next":
      echo "forward";
      //exec("cmus-remote something"); //exec cmus cmd
      break;
    default:
      var_dump($_POST);
  }
} elseif(array_key_exists("vol",$_POST)) {
  $vol = min(max((int)$_POST['vol'],0),100); //ensure vol is between 0 and 100
  echo "vol set to $vol";
  //exec("cmus-remote vol $vol"); //exec cmus cmd
} else {
  var_dump($_POST);
}

?>
