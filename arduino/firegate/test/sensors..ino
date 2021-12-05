

//sets pilotIsOut to 1 if the data from flame eye is off
void checkIfOut() {
  for(int i=0;i<FLAMENUM;i++) {
    pilotIsOut[i] = digitalRead(pilotEyes[i]);
  }
}

//turn on a single pilot light flame at the flame-th pin for t ms
void pilotLighter(int flame, int t) {
  digitalWrite(pilotSolenoids[flame], HIGH); //ensure valve is open
  digitalWrite(pilotLights[flame], HIGH); //turn on lighter
  waitMillis(t); //pause for t ms
  digitalWrite(pilotLights[flame], LOW); //turn off lighter
  checkIfOut(); //update checked settings
}


//try relighting any pilot lights that are out
//if it's still out, try again, and if that doesn't work, let the user know
void tryRelight(int startLine, int dataLine) {
  checkIfOut();
  for(int i=0;i<FLAMENUM;i++) {
    if(pilotIsOut[i]) { //attempt 1
      pilotLighter(i, 50); //try relighting the pilot and update
      if(pilotIsOut[i]) { //attempt 2
        digitalWrite(pilotSolenoids[i], LOW); //close valve
        waitMillis(10); //give it time to close
        digitalWrite(pilotSolenoids[i], HIGH); //open valve
        pilotLighter(i, 50); //try relighting the pilot and update
        if(pilotIsOut[i]) { //give up and send data to remote
          send_data((char) i, startLine, dataLine); //send cable data
        }
      }
    }
  }
}



//set the main flame output strength and duration (on and off, in ms)
void setFlames(int tOn, int tOff) {
  //enable flame if value >0
  for(int i=0;i<FLAMENUM;i++) {
    if(strength[i]>0) { analogWrite(mainSolenoids[i], strength[i]); }
  }
  waitMillis(tOn); //wait for time to process
  //disable the flames
  for(int i=0;i<FLAMENUM;i++) {
    analogWrite(mainSolenoids[i], 0);
  }
  waitMillis(tOff); //wait for at least this time beforer firing again
}


//0-->1255, 1000's is if someone is in the gate, 0-->255 is gate approach dist
int getIRData() {
  return 1000*digitalRead(inGateSense)+analogRead(approachSense);
}
