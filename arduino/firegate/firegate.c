/* Steven Williams
 * Local Firegate Controller
 * Jul 15 2018
 */

#include "sensors.h"
#include "functions.h"


void setup() {
  for(int i=0;i<FLAMENUM;i++) {
    pinMode(pilotEyes[i],INPUT);
    pinMode(pilotLights[i],OUTPUT);
    pinMode(pilotSolenoids[i],OUTPUT);
    pinMode(mainSolenoids[i],OUTPUT);
  }
}


void loop() {
  //get data from wifi
  //data will consist of:
    //which pilot to ignite
    //which flame to set off at what strength
    //OR
    //which pre-programmed configuration

  //send data over wifi
  //data will consist of:
    //which pilot is out


}
