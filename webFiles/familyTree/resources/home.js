var canvas = document.getElementById("canvas");
var ctx = canvas.getContext('2d');

canvas.height = 0.98*window.innerHeight;
canvas.width = 0.45*window.innerWidth;

var cw = canvas.width;
var ch = canvas.height;

function setup() {

  canvas.addEventListener("dblclick",addMember,false);
  //canvas.addEventListener("contextmenu",,false);
  canvas.addEventListener("click",selectMember,false);
  //canvas.addEventListener("mousedown",,false);
  //canvas.addEventListener("mouseup",,false);
  //canvas.addEventListener("mousemove",mouseMove,false);
  //canvas.addEventListener("touchmove",mosueMove,false);
  //canvas.addEventListener("touchstart",,false);

  setInterval(run,500);
}

var rw = 75;
var rh = 50;

function run() {
  ctx.beginPath();
  ctx.fillStyle = "#ccc";
  ctx.fillRect(0,0,cw,ch);
  ctx.closePath();
  ctx.beginPath();
  ctx.strokeStyle = "#f00";
  ctx.lineWidth = 5;
  ctx.strokeRect(cw/2-rw/2,ch/2-rh/2,rw,rh);
  ctx.closePath();
  ctx.beginPath();
  ctx.fillStyle = "#000";
  ctx.fillText("You",cw/2,ch/2);
  ctx.textAlign = "center";
  ctx.closePath();
}



function addMember() {
/*
  if within drawing boundry {
    if not within another member {
      add rectangle //may need to shift other members to add room for the new one
      pop up with name (first, last, middle), birth day, death day, major occupations, document upload
      if confirm in popup {
        add data to csv line with unique identifier
      } else {
        prompt (really cancel changes?), remove rectangle, text
      }
    }
  }

*/
}

function selectMember() {
/*
  if click is within member box {
    center box, highlight box border, populate input fields
  }

*/
}
