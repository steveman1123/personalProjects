
function addXtn() {
  var elem = document.createElement('tr');
  elem.innerHTML = '<td><input type="text" placeholder="Date"></td><td><input type="text" placeholder="Account"></td><td><input type="text" placeholder="Amount"></td><td><input type="text" placeholder="Reason"></td><td><button class="trash" value="xtn'+Date.now()+'" onclick="delRow(this);"><div class="trashPic"></div></button></td>';
  document.getElementById('xtnList').appendChild(elem);
}
