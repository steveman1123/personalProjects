
//physical:
//pilot solenoid
//pilot flame eye
//pilot starter
//main solenoid

//logical:
//pilot supposed to be lit - changes with button press
//number of flames - constant
//duration of mains to be on - cnages with button press

const int FLAMENUM = 1;
bool supposedtobelit[FLAMENUM] = {1}; //is the pilot supposed to be on? - changes with button presses

int flameEyes[FLAMENUM] = {A0};
int pilotLighter[FLAMENUM] = {A5};
int pilots[FLAMENUM] = {A4};
int mains[FLAMENUM] = {A3};

int remoteButton = A1; //remote button to activate pilot... TODO: change this when more pins are available

void setup() {
  //set input pins
  for(int i=0;i<FLAMENUM;i++) {
    pinMode(flameEyes[i], INPUT);
  }
  //set output pins
  for(int i=0;i<FLAMENUM;i++) {
    pinMode(pilotLighter[i], OUTPUT);
    pinMode(pilots[i], OUTPUT);
    pinMode(mains[i], OUTPUT);
  }
  Serial.begin(9600);
}


unsigned int pilotLighterStartTime = 0; //time used for keeping pilotLighters active
int pilotLighterTimeout = 5000; //ms to timeout the pilot lighters
unsigned int pilotStartTime = 0; //time used for keeping pilots active
int pilotTimeout = 10000; //ms to time out the pilots

void loop() {
  //if the remote button is pressed
  if(digitalRead(remoteButton)) {
    btnPress(supposedtobelit);
  }
  
  supposedtobelit[FLAMENUM-1] = !digitalRead(A2);
  
  //if the timeout occurs, turn off all pilots
  testTimeout();
  
  
  
}

//set which flames are supposedtobelit based on which button is pressed




//function to run if a button is pressed
void btnPress(bool supposedtobelit2[FLAMENUM]) {
  //if flameEyes[i] is 0 & flame [i] is supposed to be lit, ensure that it is, or time out
  //in english: if the flame is out, and it's supposed to be there, and it's within the timeout time, then keep the lighter on until the flame is there or it times out
  //if it times out, send data to the operator
  for(int i=0;i<FLAMENUM;i++) {
    if(!digitalRead(flameEyes[i]) & supposedtobelit2[i]) {
      digitalWrite(pilots[i], 1); //open pilots[i] (pilot solenoid) if supposedtobelit
      digitalWrite(pilotLighter[i], 1); //turn on pilotLighter[i] if supposedtobelit
      
      pilotLighterStartTime = millis(); //initiate start of time
      while((millis()<=pilotLighterStartTime+pilotLighterTimeout) & !digitalRead(flameEyes[i])) {} //wait while below timeout and flame is not there
      delay(500); //keep on for extra 0.5 seconds, just in case
      digitalWrite(pilotLighter[i], 0); //turn off the pilotLighter
      
      //if it timed out and the flame is still out, close the solenoid and send a signal to the operator
      if((millis()>(pilotLighterStartTime+pilotLighterTimeout)) & !digitalRead(flameEyes[i])) {
        digitalWrite(pilots[i], 0); //close pilot solenoid
        Serial.println(i); //send data
      }
    }
  }

  //turn on mains if supposed to be lit and the pilotLight is active
  for(int i=0;i<FLAMENUM;i++) {
    if(digitalRead(flameEyes[i]) & supposedtobelit2[i]) {
      digitalWrite(mains[i], 1);
    }
  }
  //while the remote button is pressed
  while(digitalRead(remoteButton)) {}
  //turn off all mains
  for(int i=0;i<FLAMENUM;i++) {
    digitalWrite(mains[i], 0);
  }
  pilotStartTime = millis(); //re-start timeout timer
}


//if the timeout occurs, turn off all pilots
void testTimeout() {
  if(millis()>(pilotStartTime+pilotTimeout)) {
    for(int i=0;i<FLAMENUM;i++) {
      digitalWrite(pilots[i], 0);
    }
  }
}


