var now = 0;


function save() {
  alert("Saved");
}

function load() {
//https://stackoverflow.com/questions/31746837/reading-uploaded-text-file-contents-in-html
  var fileToLoad = document.getElementById("loadFile").files[0];

  var fileReader = new FileReader();
  fileReader.onload = function(fileLoadedEvent){
    var textFromFileLoaded = fileLoadedEvent.target.result;
    document.getElementById("list").innerHTML = textFromFileLoaded;
  };
  fileReader.readAsText(fileToLoad, "UTF-8");
}

function delRow(rowNum) {
  var del = confirm("Are you sure you want to delete that?");
  if(del) {
    rowNum.parentNode.parentNode.parentNode.removeChild(rowNum.parentNode.parentNode);
  }
}

//fxn to run on page load
function init() {
  updateBudget();
}