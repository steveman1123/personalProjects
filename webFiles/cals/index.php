<?php


?>

<!DOCTYPE html>

<html>
  <head>
    <title>Food Tracker</title>
    <meta name="description" content="This site is intended to allow the user to track their nutritional intake">
    <link rel="stylesheet" type="text/css" href="./resources/cals.css">
    <link rel="shortcut icon" href="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <div class="wrapper">
      <div class="inputs">
        <p>Track your calories and nutrition</p>
        <p>See <a href="https://health.gov/dietaryguidelines/2015/guidelines/appendix-2/" target="_blank">this table</a> for how many calories you should intake.</p>
        <table>
          <tr><td>Date:</td><td><input type="date" id="date" autofocus></td></tr>
          <tr><td>Name of Food:</td><td><input type="text" id="foodName"></td></tr>
          <tr><td>Number of Calories:</td><td><input type="number" id="cals"></td></tr>
        </table>
        <p><button onclick="addItem();">Add Item</button></p>
        <p><button onclick="saveAs();">Save Data</button><input type="file" id="file" onchange="load();"></p>
        <h3>Quick Links</h3>
        <fieldset id="bmicalc"><legend>BMI Calculator</legend>
          <p><input type="number" id="height" step="0.01" placeholder="height (m)" onchange="calcBMI();"><input type="number" id="weight" step="0.1" placeholder="weight (kg)" onchange="calcBMI();"><input disabled id="bmi" placeholder="BMI"></p>
        </fieldset>
      </div>
      <div id="foodList">
        <div class="foodItem"><div>Date</div><div>Food Item</div><div>Calories</div></div>
      </div>
    </div>
  </body>
</html>

<script>
  function addItem() {
    document.getElementById("foodList").innerHTML += '<div class="foodItem"><div>'+document.getElementById("date").value+'</div><div>'+document.getElementById("foodName").value+'</div><div>'+document.getElementById("cals").value+'</div></div>';
  }

  function saveAs() {
    data2save = document.getElementById("foodList").innerHTML;
    today = new Date();
    fileName = "calories--"+today.getFullYear()+(today.getMonth()+1)+(today.getDate()<10 ? "0" : "")+today.getDate()+".txt";
    var a = document.createElement("a");
    document.body.appendChild(a);
    a.style = "display: none";
    var blob = new Blob([data2save], {type: "text/plain"}),
        url = window.URL.createObjectURL(blob);
    a.href = url;
    a.download = fileName;
    a.click();
    window.URL.revokeObjectURL(url);
  }

  function load() {
    var file = document.getElementById('file').files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
      document.getElementById('foodList').innerHTML = e.target.result;
    };
    reader.readAsText(file);
	}


  function calcBMI() {
    h = document.getElementById("height").value;
    w = document.getElementById("weight").value;
    var bmi = Math.round(w/Math.pow(h,2)*100)/100;
    if(bmi<18.5) {bmi += " - underweight";}
    if(bmi>=18.5 && bmi<25) {bmi += " - healthy";}
    if(bmi>=25) {bmi += " - overweight";}

    document.getElementById("bmi").value = bmi;
  }
</script>