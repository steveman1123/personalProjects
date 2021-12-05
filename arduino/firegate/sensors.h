//#include wifi

//VARIABLES
  // flame stuff
const int FLAMENUM = 0; //number of flames there will be
int pilotEyes[FLAMENUM] = {}; //pilot flame eye pins
int pilotLights[FLAMENUM] = {}; //pilot starter pins
bool pilotIsOut[FLAMENUM] = {}; //pilot lights that are out - start with all being out
int pilotSolenoids[FLAMENUM] = {}; //pilot solenoid pins
int mainSolenoids[FLAMENUM] = {}; //main solenoid pins
char strength[FLAMENUM] = {}; //flame strength (0=off, 255=full)


  //ir stuff
int inGateLED = 0; //in-gate LED
int inGateSense = 0; //in-gate sensor
int approachLED = 0; //gate-approach LED
int approachSense = 0; //gate-approach sensor

  //deco LED stuff
int flashLED = 0; //flashing LEDs
int stripLED = 0; //strips of LEDs

  //wifi stuff - may need to change down to 1 pin
const int WIFINUM = 0; //number of pins wifi shield uses
int wifiDataPins[WIFINUM] = {};//data pins
int wifiData[WIFINUM] = {};//data values



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
