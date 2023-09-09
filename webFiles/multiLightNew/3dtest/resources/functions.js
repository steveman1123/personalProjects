
//populate light strand with lights
function popuLights(numLights) {
  var lightArray = new Array();
/*
  //use this to generate random lights
  var yScale = maxSize*0.8; //leave some buffer room on top and bottom
  var y,x,z,red,gre,blu,a;
  for (var i=0;i<numLights;i++) {
    //assign semi-random coords and colors - x and z depend on y coord, makes triangular shape
    //change this later to accept positions/colors from json file
    y = Math.floor(yScale*Math.random()-yScale/2);
    x = Math.floor((y+canvas.height/2)*Math.random()-(y+canvas.height/2)/2);
    z = Math.floor((y+canvas.height/2)*Math.random()-(y+canvas.height/2)/2);
    red = Math.floor(255*Math.random());
    gre = Math.floor(255*Math.random());
    blu = Math.floor(255*Math.random());
    a = Math.random();

    lightArray.push(new Light(x, y, z, red, gre, blu, a)); //add light to strand
    //alert(lightArray[i].x);
  }
*/
  lightArray = JSON.parse(document.getElementById('jsonData').value);
  return lightArray;
}


function loadFile(filePath) {
  var result = null;
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.open("GET", filePath, false);
  xmlhttp.send();
  if (xmlhttp.status==200) {
    result = xmlhttp.responseText;
  }
  return result;
}


//set tree angle - current
function setAngles() {
  treeRad = parseInt(document.getElementById('angle').value)/180*Math.PI; //get tree rotation from input, convert to rads
}

//set ctx background color
function setCtxBackground(hexColor) {
  ctx.clearRect(0, 0, canvas.width, canvas.height); //clear canvas
  ctx.fillStyle=hexColor; //set color
  ctx.fillRect(0,0,canvas.width, canvas.height); //draw color
}

//convert x,z coords to radian (cartesian to cylindrical)
function xz2rad(x,z) {
  return {
    r: Math.sqrt(Math.pow(x, 2)+Math.pow(z, 2)),
    theta: Math.sign(x)*Math.acos(z/r)
  };
}

//convert radian to x,z coords (cartesian to cylindrical)
function rad2xz(r,theta) {
  return {
    x: r*Math.sin(theta),
    z: r*Math.cos(theta)
  };
}

//draw tree lights on canvas
function drawLights() {
  //loop thru light strand
  var lightX = 0;
  for (var i=0;i < lights.length;i++) {
    //obtain cylindrical coords from x,z coords
    r = xz2rad(lights[i].x,lights[i].z).r;
    lightRad = xz2rad(lights[i].x,lights[i].z).theta+treeRad; //add change in the tree's input angle

    //set x,z coords from cyl coords updated from tree angle
    lightX = rad2xz(r,lightRad).x;
    lights[i].dispZ = rad2xz(r,lightRad).z;
    //change transparency as lights move
    ctx.fillStyle = "rgba("+lights[i].r+", "+lights[i].g+", "+lights[i].b+", "+(lights[i].dispZ+r)/(2*r)+")";
    //if light on backside, set to white border, else hide border
    if(lights[i].dispZ<0 || (lights[i].r<50 && lights[i].g<50 && lights[i].b<50)) {
      ctx.strokeStyle = "rgba(255,255,255,0.5)";
    } else {
      ctx.strokeStyle = "rgba(0,0,0,0)";
    }
    ctx.beginPath(); //start drawing
    ctx.arc(lightX+canvas.width/2, lights[i].y+canvas.height/2, lightSize, 0, 2*Math.PI); //draw the light
    //ctx.fillText(lights[i].dispZ+", "+lights[i].z,10,10*i); //use this for debugging

    ctx.stroke(); //outline
    ctx.fill(); //inside
    ctx.closePath(); //finish drawing
  }
}


//light constructor class
//each light needs an index, x/y/z coord, and color
function Light(x, y, z, r, g, b, a) {
  // check if value exists, else set to 0
  this.x = x || 0; //x coord
  this.y = y || 0; //y coord
  this.z = z || 0; //z coord
  this.r = r || 0; //red
  this.g = g || 0; //green
  this.b = b || 0; //blue
  this.a = a || 1; //alpha
  this.dispZ = this.z; //z value to sort by (not used by server, only on client side
}


//sort array by element, forward or reverse
var sort_by = function(field, reverse, primer){
  var key = primer ? function(x) {return primer(x[field]);} : function(x) {return x[field];};
    reverse = !reverse ? 1 : -1;
    return function (a, b) { return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
  };
};


function onMouseover(e) {
  if(document.getElementById('picker').checked) {
    getColorOnOver(tapPoint(e).x,tapPoint(e).y);
  } else {
    colorLightsOnOver(tapPoint(e).x,tapPoint(e).y,lightColor);
  }
}

//define if mouse or touch event, then x,y postition of the tap
function tapPoint(e) {
  e.preventDefault();
  if (typeof e.clientX !== 'undefined') {
    touchObj = e; //mouse object
  } else {
    touchObj = e.changedTouches[0]; //touch object
  }

  //get tap position relative to canvas
  rect = canvas.getBoundingClientRect();
  var mx = parseInt(touchObj.clientX) - rect.left - (rect.right-rect.left)/2;
  var my = parseInt(touchObj.clientY) - rect.top - (rect.bottom-rect.top)/2;
  //document.getElementById('angleP').innerHTML = mx+", "+my;
  return {x:mx,y:my};
}

//if over a light, return color value of that light
function getColorOnOver(x,y) {

  var data = ctx.getImageData(x+maxSize/2,y+maxSize/2,1,1).data; //get data from pixel under mouse x,y
  //document.getElementById('angleP').innerHTML = data[0];
  document.getElementById('colorText').value=rgb2hex(data[0],data[1],data[2]); //set colorText value
  updateColor(); //sync color inputs
}


//color the lights under a touch/mouse if not under the image
function colorLightsOnOver(mx,my,hexColor){
  //document.getElementById('angleP').innerHTML = mx+", "+my;
  //if inside the image
  if(mx>imgX && mx<imgX+img.width && my>imgY && my<imgY+img.height) {
    imgX = dx+imgStartX; imgY = dy+imgStartY;
    document.getElementById('angleP').innerHTML = imgX+", "+imgY;
  } else { //outside the image
    for(var i=0;i<lights.length;i++) {
      r = xz2rad(lights[i].x,lights[i].z).r;
      lightRad = xz2rad(lights[i].x,lights[i].z).theta+treeRad;
      lightX = rad2xz(r,lightRad).x;
      lights[i].dispZ = rad2xz(r,lightRad).z;
      if ((mx-lightX)*(mx-lightX)+(my-lights[i].y)*(my-lights[i].y) < Math.pow(lightSize,2) && lights[i].dispZ>0) {
        lights[i].r = hex2rgb(hexColor).r;
        lights[i].g = hex2rgb(hexColor).g;
        lights[i].b = hex2rgb(hexColor).b;
      }
    }
  }
}

//set color to black
function clearLight(e) {
  colorLightsOnOver(tapPoint(e).x,tapPoint(e).y,'000000'); //set color to black
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

//convert hex color to rgb (hex of type #AABBCC)
function hex2rgb(hex) {
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
}

//convert individual color from 0-255 to 00-FF
function componentToHex(c) {
  var hex = c.toString(16);
  return hex.length == 1 ? "0" + hex : hex;
}
function rgb2hex(r,g,b) {
  return componentToHex(r)+componentToHex(g)+componentToHex(b);
}

var img = new Image();

//display an image on canvas - image from url
function dispImage() {
  /*
TODO:
add image addition, moving, resizing
add button press to upload image and update pattern
*/
  img.src = document.getElementById('imgURL').value; //load img from url
  img.crossOrigin = "anonymous"; //reference as anon - security feature
  ctx.drawImage(img,imgX+maxSize/2,imgY+maxSize/2); //show on canvas
//  document.getElementById('angleP').innerHTML = imgX+", "+imgY;
}

//set json data to input value to be posted
function setJsonData() {
  //alert(JSON.stringify(lights));
  document.getElementById('jsonData').value = JSON.stringify(lights);
}

//rotate selected images around tree
function rotateImages() {

}

//update the angle display
function updateAngleText() {
  document.getElementById('angleP').innerHTML = document.getElementById('angle').value+"&deg;";
}


//prompt and execute if the user wishes to actually delete a pattern
function toDelete(toBeDeleted) {
  var confirm = window.confirm("Are you sure you wish to delete "+toBeDeleted+"?"); //prompt to delete object
  if(confirm) {
    //delete object
    alert('deleted');
  } else {
    //don't delete
    alert('not deleted');
  }
}
