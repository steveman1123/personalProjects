//https://www.youtube.com/watch?v=670f71LTWpM

/*
//nested setTimeouts "callback hell"
setTimeout(()=> {
  disp("1");
  setTimeout(()=> {
    disp("2");
    setTimeout(()=> {
      disp("3");
    },1000);
  },1000);
},1000);
*/

/*
//error first callback
//make sure that we're always prepared to catch errors
//promises are the next iteration of that idea
//promises always need a resolve and reject
let myPromise = new Promise((resolve, reject)=> {
  const rand = Math.floor(Math.random()*2); // random 1 or 0
  if(rand === 0) {
    resolve();
  } else {
    reject();
  }
});

//how it can be resolved/rejected (in the wild)
myPromise
  .then(()=> disp("success")) //resolve
  .catch(()=> disp("oof")); //reject
*/

//https://javascript.info/fetch

/*
let response = await fetch("./test.json");
disp(response.ok);
if (response.ok) { // if HTTP-status is 200-299
  // get the response body (the method explained below)
  let json = await response.text();
  alert(json);
} else {
  alert("HTTP-Error: " + response.status);
}
*/

//fetch returns a promise
let url = 'http://192.168.1.102/ip.php';
fetch(url)
  .then(response => response.text())
  .then(data => disp(data))
  .catch(disp("err - "+response.status));

