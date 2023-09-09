/* TODO:
 * - click to change color of element
 * - click/drag to change color
 * - right click to turn off
 * - get position/color data from json file
 * - save light data to json file (to send to lights)
 * - get image from file, map to tree (cone), then parse down to lights
 * - allow multi select for sliding animations
 * - refactor to be more processor efficient (event driven, not timer driver)
 */


var ctx, canvas; //context and canvas
var treeRad = 0, prevTreeRad = 0; //tree rotation angle in rads, also previously obtained angle
var r, lightRad; //radius and angle of light relative to tree angle=0
var maxSize = 500; //max canv side size (always square)
var numLights = 500; //number of lights on strand
var lights = new Array(); //light strand
var lightColor = document.getElementById('colorText').value; //color to draw with

if(screen.width<maxSize)
  maxSize = screen.width-5;
var lightSize = maxSize/50; //radius of light
var yScale = maxSize*0.8; //leave some buffer room on top and bottom
canvas = document.getElementById('canv');

var x,y,z,r,g,b,a; //index, coords and color of individual light - just assign random values for now



function setup() {

  ctx = canvas.getContext('2d');

  canvas.height = maxSize;
  canvas.width = maxSize;

  //populate light strand with lights
  for (var i=0;i<numLights;i++) {
    //assign semi-random coords and colors - x and z depend on y coord, makes triangular shape
    //change this later to accept positions/colors from json file
    y = Math.floor(yScale*Math.random()-yScale/2);
    x = Math.floor((y+canvas.height/2)*Math.random()-(y+canvas.height/2)/2);
    z = Math.floor((y+canvas.height/2)*Math.random()-(y+canvas.height/2)/2);
    r = Math.floor(255*Math.random());
    g = Math.floor(255*Math.random());
    b = Math.floor(255*Math.random());
    a = Math.random();

    lights.push(new Light(i, x, y, z, r, g, b, a)); //add light to strand
  }

  //TODO: redo event functions to handle touch/mouse events better - ie sense a touch, detect single, double, long, run appropriate fxn
  canvas.addEventListener("contextmenu",clearLight, false);
  canvas.addEventListener("dblclick", clearLight, false);
  canvas.addEventListener("touchmove",onMouseover, false);
  canvas.addEventListener("touchstart",onMouseover, false);
  canvas.addEventListener("click", onMouseover,false);
  canvas.addEventListener("mousedown", onMouseover,false);  
  //canvas.addEventListener("touchmove",onMouseover, false);

  //TODO: this should be changed so that it only runs when needed
  //ie only when user inputs something (rotation, drawing, img upload, etc
  setInterval(run, 20); //run continuously every 20ms
}


//TODO: separate processes into individual fxns
function run() {
  prevTreeRad = treeRad; //store prev tree angle
  treeRad = parseInt(document.getElementById('angle').value)/180*Math.PI; //get tree rotation from input, convert to rads
/*
  //if autospin is enabled, override user input
  if(document.getElementById('spin').checked) {
    prevTreeRad=0;
    treeRad=0.01;
  }
*/


  ctx.clearRect(0, 0, canvas.width, canvas.height); //clear canvas
  ctx.fillStyle="black";
  ctx.fillRect(0,0,canvas.width, canvas.height);

  lights.sort(sort_by('z',false)); //sort from back to front

  //loop thru light strand
  for (var i=0;i < lights.length;i++) {
    //obtain cylindrical coords from x,z coords
    r = Math.sqrt(Math.pow(lights[i].x, 2)+Math.pow(lights[i].z, 2));
    //set angle as starting angle plus the change in the tree's input angle
    lightRad = (Math.sign(lights[i].x))*Math.acos(lights[i].z/r)+treeRad-prevTreeRad;

    //set x,z coords from cyl coords updated from tree angle
    lights[i].x = r*Math.sin(lightRad);
    lights[i].z = r*Math.cos(lightRad);

    //change transparency as lights move
    ctx.fillStyle = "rgba("+lights[i].r+", "+lights[i].g+", "+lights[i].b+", "+(lights[i].z+r)/(2*r)+")";
    //if light on backside, set to white border, else hide border
    if(lights[i].z<0 || (lights[i].r<50 && lights[i].g<50 && lights[i].b<50)) {
      ctx.strokeStyle = "rgba(255,255,255,0.5";
    } else {
      ctx.strokeStyle = "rgba(0,0,0,0)";
    }
    ctx.beginPath(); //start drawing
    ctx.arc(lights[i].x+canvas.width/2, lights[i].y+canvas.height/2, lightSize, 0, 2*Math.PI); //draw the light

    //ctx.fillText(lights[i].x+", "+lights[i].y,10,10*i);

    ctx.stroke(); //outline
    ctx.fill(); //inside
    ctx.closePath(); //finish drawing
  }
}


//light constructor class
//each light needs an index, x/y/z coord, and color
function Light(n, x, y, z, r, g, b, a) {
  // check if value exists, else set to 0
  this.n = n || 0;
  this.x = x || 0;
  this.y = y || 0;
  this.z = z || 0;
  this.r = r || 0;
  this.g = g || 0;
  this.b = b || 0;
  this.a = a || 1;
}


//sort array by element, forward or reverse
var sort_by = function(field, reverse, primer){
  var key = primer ? function(x) {return primer(x[field]);} : function(x) {return x[field];};
    reverse = !reverse ? 1 : -1;
    return function (a, b) { return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
  };
};



//TODO: grab color from inputs
function onMouseover(e) {
  e.preventDefault();
  if (typeof e.clientX !== 'undefined') {
    //alert('defined');
    touchObj = e;
  } else {
    //alert('undef');
    touchObj = e.changedTouches[0];
  }
    
  var rect = canvas.getBoundingClientRect();
  var mx = parseInt(touchObj.clientX) - rect.left - (rect.right-rect.left)/2;
  var my = parseInt(touchObj.clientY) - rect.top - (rect.bottom-rect.top)/2;
//alert(lightColor);
  for(var i=0;i<lights.length;i++) {
    if ((mx-lights[i].x)*(mx-lights[i].x)+(my-lights[i].y)*(my-lights[i].y) < Math.pow(lightSize,2) && lights[i].z>0) {
      lights[i].r = hex2rgb(lightColor).r;
      lights[i].g = hex2rgb(lightColor).g;
      lights[i].b = hex2rgb(lightColor).b;
    }
  }

}


function clearLight(e) {
  e.preventDefault();
  touchObj = e.changedTouches[0];
  var rect = canvas.getBoundingClientRect();
  var mx = parseInt(touchObj.clientX) - rect.left - (rect.right-rect.left)/2;
  var my = parseInt(touchObj.clientY) - rect.top - (rect.bottom-rect.top)/2;


  for(var i=0;i<lights.length;i++) {
    if ((mx-lights[i].x)*(mx-lights[i].x)+(my-lights[i].y)*(my-lights[i].y) < Math.pow(lightSize,2) && lights[i].z>0) {
      lights[i].r = "0";
      lights[i].g = "255";
      lights[i].b = "0";
    }
  }
}

function handleTouch(e) {
  //handle touch events (tap, long tap, dbl tap)
  
}



//set color input value to colorText value 
function updateColor() { 
  document.getElementById("color").value = "#"+document.getElementById("colorText").value;
  lightColor = document.getElementById('colorText').value;
} 

//set colortext value to color input value 
function updateColorText() { 
  document.getElementById("colorText").value = document.getElementById("color").value.substring(1); 
  lightColor = document.getElementById('colorText').value;
} 


function hex2rgb(hex) { 
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? { 
    r: parseInt(result[1], 16), 
    g: parseInt(result[2], 16), 
    b: parseInt(result[3], 16) 
  } : null; 
}