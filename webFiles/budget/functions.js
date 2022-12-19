function save() {
  alert("Saved");
}

function load() {
  //https://www.html5rocks.com/en/tutorials/file/dndfiles/
  alert("file loaded: ");
  alert(document.getElementById("loadFile").value);
}

function addXtn() {

  document.getElementById('xtnList').innerHTML += '<tr><td><input type="text" placeholder="Date"></td><td><input type="text" placeholder="Account"></td><td><input type="text" placeholder="Amount"></td><td><input type="text" placeholder="Reason"></td><td><button class="trash" value="xtn'+Date.now()+'" onclick="delXtn(this.value);"><div class="trashPic"></div></button></td></tr>';
}

function delXtn(rowNum) {
  alert("Removed "+rowNum);
}

function addLA() {
  document.getElementById('laTable').innerHTML += '<tr><td><input type="text" placeholder="Asset Name"></td><td><input type="text" placeholder="Amount"></td><td><input type="text" placeholder="Liability Name"></td><td><input type="text" placeholder="Amount"></td><td><button class="trash" value="la'+Date.now()+'" onclick="delLA(this.value);"><div class="trashPic"></div></td></tr>';
}

function delLA(rowNum) {
  alert("Removed "+rowNum);
}

function addStock() {
  document.getElementById('stocks').innerHTML += '<tr><td><input type="text" placeholder="Ticker Symbol" id="stockSym"></td><td id="stockVal"></td><td><input type="text" placeholder="Shares Held"></td><td><button class="trash" value="stock'+Date.now()+'" onclick="delStock(this.value);"><div class="trashPic"></div></td></tr>';
}

function delStock(rowNum) {
  alert("Removed "+rowNum);
}

function addMoExpense() {
  document.getElementById('moExp').innerHTML += '<tr><td><input type="text" placeholder="Name"></td><td><input type="text" placeholder="Amount"></td><td><button class="trash" value="moExp'+Date.now()+'" onclick="delMoExpense(this.value);"><div class="trashPic"></div></td></tr>';
}

function delMoExpense(rowNum) {
  alert("Removed "+rowNum);
}

function addWkExpense() {
  document.getElementById('wkExp').innerHTML += '<tr><td><input type="text" placeholder="Name"></td><td><input type="text" placeholder="Amount"></td><td><button class="trash" value="wkExp'+Date.now()+'" onclick="delWkExpense(this.value);"><div class="trashPic"></div></td></tr>';
}

function delWkExpense(rowNum) {
  alert("Removed "+rowNum);
}

function updateBudget() {
  var hrRate = parseFloat(document.getElementById('hrRate').value);
  var hrPerWk = parseFloat(document.getElementById('hrPerWk').value);
  var wkPerCh = parseFloat(document.getElementById('wkPerCh').value);
  var retRate = parseFloat(document.getElementById('retRate').value)/100;
  var taxRate = parseFloat(document.getElementById('taxRate').value)/100;

  var grossPerCh = hrRate*hrPerWk*wkPerCh;
  var expPerCh = grossPerCh*(1-retRate-taxRate);
  var expPerWk = expPerCh/wkPerCh;
  var expPerMo = 4*expPerWk;

  document.getElementById('grossPerCh').innerHTML = "$"+grossPerCh.toFixed(2);
  document.getElementById('expPerCh').innerHTML = "$"+expPerCh.toFixed(2);
  document.getElementById('expPerWk').innerHTML = "$"+expPerWk.toFixed(2);
  document.getElementById('expPerMo').innerHTML = "$"+expPerMo.toFixed(2);
}