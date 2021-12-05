//#include wifi

//VARIABLES
  // flame stuff
const int FLAMENUM = 1; //number of flames there will be
int pilotEyes[FLAMENUM] = {A1}; //pilot flame eye pins
int pilotLights[FLAMENUM] = {8}; //pilot starter pins
int pilotSolenoids[FLAMENUM] = {6}; //pilot solenoid pins

int mainSolenoids[FLAMENUM] = {1}; //main solenoid pins

/*
  //ir stuff
int inGateLED = A0; //in-gate LED
int inGateSense = 02; //in-gate sensor
int approachLED = A1; //gate-approach LED
int approachSense = A2; //gate-approach sensor

  //deco LED stuff
int flashLED = 0; //flashing LEDs
int stripLED = 0; //strips of LEDs
*/

//FUNCTIONS
//pause the program for t ms
void waitMillis(int t);

//sets pilotIsOut to 1 if the data from flame eye is off
void checkIfOut();

//try relighting any pilot lights that are out
//if it's still out, try again, and if that doesn't work, let the user know
void tryRelight();

//set the main flame output strength and duration (on and off, in ms)
void setFlames(int tOn, int tOff);

//0-->1255, 1000's is if someone is in the gate, 0-->255 is gate approach dist
int getIRData();
