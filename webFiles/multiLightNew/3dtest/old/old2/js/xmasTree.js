/* TODO:
 * - click to change color of element
 * - click/drag to change color
 * - right click to turn off
 * - get position/color data from json file
 * - save light data to json file (to send to lights)
 * - get image from file, map to tree (cone), then parse down to lights
 * - allow multi select for sliding animations
 */


var ctx, canvas; //context and canvas
var treeRad = 0, prevTreeRad = 0; //tree rotation angle in rads, also previously obtained angle
var r, lightRad; //radius and angle of light relative to tree angle=0
var maxSize = 500; //max canv side size (always square)
var numLights = 250; //number of lights on strand
var lights = new Array(); //light strand

if(screen.width<maxSize)
  maxSize = screen.width-5;
var lightSize = maxSize/60; //radius of light
var yScale = maxSize*0.8; //leave some buffer room on top and bottom

var x,y,z,r,g,b,a; //index, coords and color of individual light - just assign random values for now


function setup() {
  canvas = document.getElementById('canv');
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
  setInterval(run, 20); //run continuously every 20ms
}

function run() {
  prevTreeRad = treeRad; //store prev tree angle
  treeRad = parseInt(document.getElementById('angle').value)/180*Math.PI; //get tree rotation from input, convert to rads

  //if autospin is enabled, override user input
  if(document.getElementById('spin').checked) {
    prevTreeRad=0;
    treeRad=0.01;
  }

  ctx.clearRect(0, 0, canvas.width, canvas.height); //clear canvas
  ctx.fillStyle="black";
  ctx.fillRect(0,0,canvas.width, canvas.height);

  lights.sort(sort_by('z',false)); //sort from back to front

  //loop thru light strand
  for (var i=0;i < lights.length;i++) {
    //obtain cyl coords from x,z coords
    r = Math.sqrt(Math.pow(lights[i].x, 2)+Math.pow(lights[i].z, 2));
    //set angle as starting angle plus the change in the tree's input angle
    lightRad = (Math.sign(lights[i].x))*Math.acos(lights[i].z/r)+treeRad-prevTreeRad;

    //set x,z coords from cyl coords updated from tree angle
    lights[i].x = r*Math.sin(lightRad);
    lights[i].z = r*Math.cos(lightRad);

    //change transparency as lights move
    ctx.fillStyle = "rgba("+lights[i].r+", "+lights[i].g+", "+lights[i].b+", "+(lights[i].z+r)/(2*r)+")";

    ctx.strokeStyle = "#fff";


    ctx.beginPath(); //start drawing
    ctx.arc(lights[i].x+canvas.width/2, lights[i].y+canvas.height/2, lightSize, 0, 2*Math.PI); //draw the light
    ctx.fill(); //inside, user stroke() for outline
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
  var key = primer ? function(x) {
    return primer(x[field]);} : function(x) {return x[field];};
    reverse = !reverse ? 1 : -1;
    return function (a, b) { return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
  };
};



function showCoords(event) {
  var x = event.clientX;
  var y = event.clientY;
  var coords = "X coords: " + x + ", Y coords: " + y;
  alert(coords);
}