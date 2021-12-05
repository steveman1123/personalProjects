/*This game is meant for a 2 x whatever ascii screen,
   two 'C' chars represent the player, and '|' chars represent
   the obsticles. The screen starts with just the player,
   then as time goes on the course gradually fills with more
   obsticles until it reaches a certain frequency
*/

#include <Wire.h>
#include "rgb_lcd.h"

//declare vars here
bool up;
bool dn;
const int PLAYER_POS = 2; //x coord of player position
const int UP_BUTT = 12; //pin for up/yes button
const int DN_BUTT = 13; //pin for down/no button
const char PLAYER = 'C'; //player character
const char OBST = '|'; //obsticle character;
bool iscollision = false; //tests for if an OBST occupies a PLAYER char
int score = 0; //counts how many obsticles the player passed
const int lcdH = 2; //lcd height
const int lcdW = 16; //lcd width
bool player_pos[lcdH][lcdW];
const int pXpos = 2; //position in the x coord for the player to be placed
bool obst_pos[lcdH][lcdW];
int SMOOTH_SEC = 10; //in microseconds
bool new_obst[2][1];


//probably need to import screen library
void setup() {
  lcd.begin(lcdW,lcdH);
  pinMode(UP_BUTT, INPUT);
  pinMode(DN_BUTT, INPUT);
}

//smooths the input data from a digital source
bool smoothInput(int pin) {
  double out = 0;
  for(int s=0; s=SMOOTH_SEC-1; s++) {
    out += digitalRead(pin);
  }
  out = output/SMOOTH_SEC;
  if(out<0.5) {
    return false;
  } else {
    return true;
  }
}

//shifts array to the left 1, and appends an array
bool array[][] shiftArray(bool arrayToShift[lcdH][lcdW], bool arrayToAppend[lcdH][1]) {
  for(i=0;i<lcdH;i++) {
    for(j=0;j<lcdW;j++) {
      if(j==lcdW-1) {
        arrayToShift[i][j] = arrayToAppend[i][1];
      } else {
        arrayToShift[i][j] = arrayToShift[i][j];
      }
    }
  }
  return arrayToShift[][];
}

//display a char given boolean array of whether it should be there or not
void lcdPrintArray(bool arrayToDisp[lcdH][lcdW], char charToDisp) {
  for(i=0;i<lcdH;i++) {
    for(j=0;j<lcdW;j++) {
      lcd.setCursor(j,i);
      if(arrayToDisp[i][j]) {
        lcd.print(charToDisp);
      } else {
        lcd.print(' ');
      }
    }
  }
  return null;
}

//test for equivilent 'true' array elements, in this case it means it's a collision
bool testForCollision(bool array1[lcdH][lcdW], bool array2[lcdH][lcdW]) {
  for(i=0;i<lcdH;i++) {
    for(j=0;j<lcdW;j++) {
      if(array1[i][j]&&array2[i][j]) {
        return true;
      } else {
        return false;
      }
    }
  }
}

//this loop runs forever
void loop() {
  int startTime = millis();
  while (!iscollision) {

    //if a tick occurs (n number per second, increases as score increases), not sure if this works
    if((millis()-startTime) % (999-score) > 2) {
    
      //test if an OBST should occur, increases probability as score increases
      randomSeed(analogRead(5));
      int prob = score;
      if(prob>999) { prob = 999; }
      int tester = random(0,prob+1);
      bool obstCreated = ((prob%10<2)); //not actually sure if this whole part works well
      
      //set new obst Y pos
      if(obstCreated) { new_obst[random(0,1)][0] = 1; }
      
      //get smoothed user input
      up = smoothInput(UP_BUTT);
      dn = smoothInput(DN_BUTT);
      
      //change player being up or down
      if(up) {
        player_pos[0][pXpos] = 1;
        player_pos[1][pXpos] = 0;
      } else if(dn) {
        player_pos[0][pXpos] = 0;
        player_pos[1][pXpos] = 1;
      } else {
        player_pos[0][pXpos] = 1;
        player_pos[1][pXpos] = 1;
      }
      
      //move all OBST to the left 1
      obst_pos = shiftArray(obst_pos, new_obst);
      //clear & refresh screen (show PLAYER and OBST only on true's of respective arrays
      lcd.clear();
      lcdPrintArray(obst_pos, OBST);
      lcdPrintArray(player_pos, PLAYER);
      
      //test if collision
      isCollision = testForColl(player_pos, obst_pos);
    }
  }
  
    //prompt to play again
    lcd.clear();
    lcd.print(Aw, you just lost! Score: "score"); //these print statements will need more stuff like setCursor
    lcd.print("Play again?");
    memset up;
    memset dn;
    //wait for input
    while(!up||!dn) {
      up = smoothInput(UP_BUTT);
      dn = smoothInput(DN_BUTT);
    }
    if(dn) { exit(0); }
}


