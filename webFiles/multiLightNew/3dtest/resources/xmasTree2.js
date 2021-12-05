/* TODO:
 * - don't change actual x,z values
 * - right click to turn off
 * - get position/color data from json file
 * - save light data to json file (to send to lights)
 * - get image from file, map to tree (cone), then parse down to lights
 * - allow multi select for sliding animations
 */



//global variables
var treeRad = 0; //tree rotation angle in rads, also previously obtained angle
var r = 0;
var lightRad = 0; //radius and angle of light relative to tree angle=0
var numLights = 250; //number of lights on strand
var lights = new Array(); //light strand
var lightColor = document.getElementById('colorText').value; //color to draw with
var maxSize = 500; //max canv side size (always square)
if(screen.width<maxSize) //if screenWidth is smaller than maxWidth
  maxSize = screen.width-5; //then set the max size to be slightly smaller than screenWidth
var lightSize = maxSize/50; //radius of light
var canvas = document.getElementById('canv');
var ctx = canvas.getContext('2d');
var mouseBtn = 0;
var rect = canvas.getBoundingClientRect();
var imgStartX = imgStartY = 5; //starting point for the image
var imgX = imgY = 0; //pixels from the top left of the canvas to the top left of the image
var startX = startY = dx = dy = 0;


function setup() {
  canvas.width = maxSize;
  canvas.height = maxSize;
  lights = popuLights(numLights);
  //TODO: redo event functions to handle touch/mouse events better - ie sense a touch, detect single, double, long, run appropriate fxn
  canvas.addEventListener("dblclick",clearLight,false);
  canvas.addEventListener("contextmenu",clearLight,false);
  canvas.addEventListener("click",onMouseover,false);
  canvas.addEventListener("mousedown",clickDn,false);
  canvas.addEventListener("mouseup",clickUp,false);
  canvas.addEventListener("mousemove",mouseMove,false);
  canvas.addEventListener("touchmove",onMouseover,false);
  canvas.addEventListener("touchstart",onMouseover,false);
  //canvas.addEventListener("touchend",onMouseover,false);

  updateAngleText();

  //TODO: this should be changed so that it only runs when needed
  //ie only when user inputs something (rotation, drawing, img upload, etc
  setInterval(run, 20); //run continuously every 20ms
}

function clickDn(e) {
  e.preventDefault();
  startX = e.clientX; startY = e.clientY; //global click coords
  imgStartX = imgX; imgStartY = imgY; //img coords
  mouseBtn = e.which;
}

function clickUp(e) {
  e.preventDefault();
  mouseBtn = 0;
}

function mouseMove(e) {
  e.preventDefault();
  if(mouseBtn==1) {
    dx = e.clientX-startX;
    dy = e.clientY-startY;
    onMouseover(e);
  } else if(mouseBtn==3) {
    clearLight(e);
  }
}

/* on mousdn
 * get which btn
 * if left - mouseOver
 * if right - clear
 * else nothing
 *
 * on mousup
 * unset mouseisdn
 *
 * on touch
 * short touch - mouseOver
 * long touch - clear
 * touchMove - mouseOver
 */



//function to run continuously
function run() {
  setAngles(); //get tree angle from input
  setCtxBackground("#000000"); //set background color
  lights.sort(sort_by('dispZ',false)); //sort lights from back to front
  drawLights(); //draw lights on canvas
  dispImage();
}
