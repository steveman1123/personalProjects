
//TODO: this is depreciated
function readTextFile(file) {
  var output = "";
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", file, false);
  rawFile.onreadystatechange = function () {
    if(rawFile.readyState === 4) {
      if(rawFile.status === 200 || rawFile.status === 0) {
        var allText = rawFile.responseText;
        output = JSON.parse(allText);
      }
    }
  };
  rawFile.send(null);
  return output;
}

function updateWeather() {

  //TODO: get coords based on external IP, then get gridpoints, then get weather (could also get geocoding via http://www.geoplugin.net/php.gp?ip={external-ip} get coords from there, then get gridpoints and city/state)
  //https://weather-gov.github.io/api/gridpoints
  //gridpoints = readTextFile("https://api.weather.gov/points/{lat},{lon}")
  /*
  coords, gridid, gridpoints:
  cedar rapids: (41.97, -91.67) DVN (30,86)
  phoenix: (33.49, -112.05) PSR (160,60)
  nyc: (40.71, -74.01) OKX (33, 35)
  LA: (34.05, -118.25) LOX (115,45)
  */

  gridid = "PSR"
  gridx = "160";
  gridy = "60";

  var weather = readTextFile("https://api.weather.gov/gridpoints/"+gridid+"/"+gridx+","+gridy+"/forecast");
  weather = weather['properties']['periods'];

  document.getElementById("weatherList").innerHTML = "";

  sectionNum = 5;

  for(i=0;i<sectionNum;i++){
    wSection = document.createElement('div'); //section to put weather data in
    wTime = document.createElement('div');
    forecast = document.createElement('div');

    wSection.className = 'wSection';
    wTime.className = 'wTime';
    forecast.className = 'forecast';

    document.getElementById("weatherList").appendChild(wSection);
    document.getElementsByClassName("wSection")[i].appendChild(wTime);
    document.getElementsByClassName("wSection")[i].appendChild(forecast);

    document.getElementsByClassName("wSection")[i].style.color="rgb("+(255*(1-i/sectionNum))+","+(255*(1-i/sectionNum))+","+(255*(1-i/sectionNum))+")";

    document.getElementsByClassName('wTime')[i].innerHTML = weather[i]['name'];
    document.getElementsByClassName('forecast')[i].innerHTML = weather[i]['detailedForecast'];
  }
}

function updateQuote() {
  var quotes = readTextFile('./quotes.json');
  var quote = quotes[parseInt(Math.random()*quotes.length)];
  var author = quote[1];
  quote = quote[0];
  document.getElementById("quote").innerHTML = quote;
  document.getElementById("author").innerHTML = author;
}

function updateCompliment() {
  var cs = readTextFile('./compliments.json');
  var c = cs[parseInt(Math.random()*cs.length)];
  document.getElementById("compliment").innerHTML = c;
}

function time() {
  var today = new Date();
  var hh = addZero(today.getHours());
  var mm = addZero(today.getMinutes());
  var ss = addZero(today.getSeconds());
  var yyyy = today.getYear()+1900;
  var mo = addZero(today.getMonth()+1);
  var dd = addZero(today.getDate());

  document.getElementById("clock").innerHTML = hh+":"+mm+":"+ss;
  document.getElementById("date").innerHTML = yyyy+"-"+mo+"-"+dd;

  if(!parseInt(hh+mm+ss)) { updateQuote(); } //update the quote at midnight
}

function addZero(i) {
  if(i<10) {
    i = "0" + i;
  }
  return i;
}

document.onload = updateWeather();
document.onload = updateQuote();
document.onload = updateCompliment();
document.onload = time();
window.setInterval(updateWeather,60*60*1000); //update every hour
window.setInterval(updateCompliment,6*60*60*1000); //update every 6 hours
window.setInterval(updateQuote,24*60*60*1000); //update every day
window.setInterval(time, 500); //update time every half second
