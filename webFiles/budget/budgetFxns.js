
function addMoExpense() {
  var elem = document.createElement('tr');
  elem.innerHTML = '<td><input type="text" placeholder="Name"></td><td><input type="text" class="moExp" oninput="updateBudget();" placeholder="Amount"></td><td><button class="trash" value="moExp'+Date.now()+'" onclick="delRow(this);"><div class="trashPic"></div></td>';
  document.getElementById('moExp').appendChild(elem);
}

function addWkExpense() {
  var elem = document.createElement('tr');
  elem.innerHTML = '<td><input type="text" placeholder="Name"></td><td><input type="text" oninput="updateBudget();" placeholder="Amount" class="wkExp"></td><td><button class="trash" value="wkExp'+Date.now()+'" onclick="delRow(this);"><div class="trashPic"></div></td>';
  document.getElementById('wkExp').appendChild(elem);
}

function updateBudget() {
  var isSal = document.getElementById('wageType').checked; //is a salary

  var payRate = 0; //pay rate - either salary or hourly
  var hrPerWk = 0; //hours worked/wk
  var wkPerCh = parseFloat(document.getElementById('wkPerCh').value)||0; //weeks per paycheck
  var retRate = parseFloat(document.getElementById('retRate').value)/100||0; //amt saved for retirement out of paycheck
  var taxRate = parseFloat(document.getElementById('taxRate').value)/100||0; //tax rate on income

  if(isSal) {
    document.getElementById('salRateRow').setAttribute('style','display: all;');
    document.getElementById('hrRateRow').setAttribute('style','display: none;');
    document.getElementById('hpwRow').setAttribute('style','display: none;');
    payRate = document.getElementById('salRate').value / 2080||0;
    hrPerWk = 40;
  } else {
    document.getElementById('salRateRow').setAttribute('style','display: none;');
    document.getElementById('hrRateRow').setAttribute('style','display: all;');
    document.getElementById('hpwRow').setAttribute('style','display: all;');
    payRate = document.getElementById('hrRate').value;
    hrPerWk = document.getElementById('hrPerWk').value;
  }

  var grossPerCh = payRate*hrPerWk*wkPerCh;
  var expPerCh = grossPerCh*(1-retRate-taxRate);
  var expPerWk = expPerCh/wkPerCh||0;
  var expPerMo = 4*expPerWk;

  document.getElementById('grossPerCh').innerHTML = "$"+grossPerCh.toFixed(2);
  document.getElementById('expPerCh').innerHTML = "$"+expPerCh.toFixed(2);
  document.getElementById('expPerWk').innerHTML = "$"+expPerWk.toFixed(2);
  document.getElementById('expPerMo').innerHTML = "$"+expPerMo.toFixed(2);

  var moExpList = document.getElementsByClassName('moExp');
  var wkExpList = document.getElementsByClassName('wkExp');
  var moExp = 0;
  var wkExp = 0;

  for(i=0;i<moExpList.length;i++) { moExp += parseFloat(moExpList[i].value) || 0; }
  for(i=0;i<wkExpList.length;i++) { wkExp += parseFloat(wkExpList[i].value) || 0; }

  var remaining = expPerMo-moExp-4*wkExp;
  document.getElementById("remaining").innerHTML = "$"+remaining.toFixed(2);

}