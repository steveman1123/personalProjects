/* Steven Williams
 * Remote Firegate Controller
 * Jul 16 2018
 */

#include "functions.h"

const int FLAMENUM = 0; //number of flames - should be 5
int warnPins[FLAMENUM] = {}; //warning light pins
int startPilot[FLAMENUM] = {}; //hold to turn on light, release to turn off
int flameStrength[FLAMENUM] = {}; //analog potentiometer, only active when singProg is on single
const int PROGBTNNUM = 8;
int miscBtns[PROGBTNNUM] = {}; //buttons for single or pre-programmed
int singProg = 0; //swt to change btw single flame or preprogrammed

char txDat = 0; //data to send
char rxDat = 0; //data to get

int rxActivePin = 0;
int rxPin = 0;
int txActivePin = 0;
int txPin = 0;


void setup() {
  for(int i=0;i<FLAMENUM;i++) {
  pinMode(warnPins[i],OUTPUT); //warning lights
  pinMode(startPilot[FLAMENUM],INPUT);//activate pilot lights - digital
  pinMode(flameStrength[i],OUTPUT);//flame strength - analog
  }
  //btns for pre-programmable displays/single flames
  for(int i=0;i<PROGBTNNUM;i++) {
    pinMode(miscBtns[i],INPUT);
  }
  pinMode(singProg,INPUT);//switch between single or pre-programmed
}


void loop() {
  //send data over wifi
  //data will consist of:
    //which pilot to ignite
    //which flame to set off at what strength
    //OR
    //which pre-programmed configuration

  //get data from wifi
  //data will consist of:
    //which pilot is out
  rxDat = get_data(rxActivePin,rxPin);

  send_data(txDat,txActivePin,txActivePin);

}
