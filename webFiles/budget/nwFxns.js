
function addLA() {
  var elem = document.createElement('tr');
  elem.innerHTML = '<td><input type="text" placeholder="Asset Name"></td><td><input type="text" placeholder="Amount"></td><td><input type="text" placeholder="Liability Name"></td><td><input type="text" placeholder="Amount"></td><td><button class="trash" value="la'+Date.now()+'" onclick="delRow(this);"><div class="trashPic"></div></td>';
  document.getElementById('laTable').appendChild(elem);
}

function addStock() {
  now = Date.now();
  var elem = document.createElement('tr');
  elem.innerHTML = '<td><input type="text" placeholder="Ticker Symbol" id="stockSym"></td><td id="stockVal"></td><td><input type="text" placeholder="Shares Held"></td><td><button class="trash" value="stock'+now+'" onclick="delRow(this);"><div class="trashPic"></div></td>';
  document.getElementById('stocks').appendChild(elem);
}
