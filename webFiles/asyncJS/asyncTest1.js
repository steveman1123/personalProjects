
//example async function - https://www.freecodecamp.org/news/async-await-in-javascript/
async function example() {
  disp("declaring promise");
  let promise = new Promise((resolve, reject) => { setTimeout(() => resolve("done!"), 3000) });

  disp("awaiting promise as result...\n");
  let result = await promise; // wait until the promise resolves (*)

  disp(result); // "done!"
}



//standard sync execution of baking cake example
function synccake() {
disp("setting up environment");
let ing = []
let batterMade = false;

let ovenTemp = 20;
let cakeBaked = false;

setTimeout(()=>{
disp("gathering ingredients");
ing = ["eggs","milk","flour"];
disp(ing);
},500);

setTimeout(()=>{
disp("making batter");
batterMade = (ing.length>0);
disp(batterMade);
},1000);

setTimeout(()=>{
disp("warming oven");
if(batterMade) {
  while(ovenTemp<150) {
    ovenTemp += 10;
    disp(ovenTemp);
  }
}
},2000);

setTimeout(()=>{
if(batterMade && ovenTemp>=150) {
  disp("baking cake");
  cakeBaked = true;
}
},3000);

setTimeout(()=>{
if(cakeBaked) {
  disp("ready to eat!\n");
}
},4000);

}



//async execution of baking cake example
async function asynccake() {
  disp("setting up environment");
  let ing = []
  let batterMade = false;

  let ovenTemp = 20;
  let cakeBaked = false;

  let ingReady = new Promise((resolve,reject)=>{
    setTimeout(()=>{
      disp("gathering ingredients");
      ing = ["eggs","milk","flour"];
      disp(ing);
    },500);
    resolve(true)});
  
   
  let batterMade = new Promise((resolve,reject)=>{
    setTimeout(()=>{
      disp("making batter");
      let ingReady = await ingReady;
      if(ing.length>0) {
        batterMade=true;
      }
    },2000);
    resolve(batterMade)});
  
  /*
  let ovenTemp = new Promise((resolve,reject)=>{
    setTimeout(()=>{
      disp("warming oven");
      batterMade = await batterMade;
      if(batterMade) {
        while(ovenTemp<150) {
          ovenTemp += 10;
          disp(ovenTemp);
        }
      }
    },2000);
    resolve(ovenTemp)});
  */
}

//disp("attempting example async");
//example();


//disp("baking sync cake")
//synccake();

disp("baking async cake");
asynccake();
