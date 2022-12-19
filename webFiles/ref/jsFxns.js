
//return a random RRGGBB hex color
function getRandColor() {
  chars = '0123456789ABCDEF';
  randCol = '#';
  for(j=0;j<6;j++) {
    randCol += chars[Math.floor(Math.random()*chars.length)];
  }
  return randCol;
}


//delete a row of a table element given the delete button is inside a table cell
function delRow(e) {
  e.parentNode.parentNode.parentNode.removeChild(e.parentNode.parentNode);
}

//add a table row to the end of the table
function addRow() {
  var tableElem = document.getElementById('table');
  var row = tableElem.insertRow(tableElem.firstElementChild.children.length);
  var cell = row.insertCell(0);
  cell.innerHTML = 'cell 1';
  cell = row.insertCell(1);
  cell.innerHTML = 'cell 2';
}

