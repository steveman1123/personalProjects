/* Steven Williams
 * 15.11.2015
 * PROGRAM OBJECTIVE:
 * retrieve values from a load sensor in the form of a clock signal
 * and interpret it as a readable mass quantity
 */

void setup() {
  // for defining digital reads
  pinMode(3, INPUT);
  pinMode(7, INPUT);
  Serial.begin(9600);
}
  /*
  int counter = 0;
  int numLoop = 20;
  */
  int hi = 0;
  int lo = 0;
  int prevVal = 0;
  int val = 0;
  const int ELEMS = 10;
  int valsLo[ELEMS];
  int valsHi[ELEMS];
  int valsSum;
  float avgLo;
  float avgHi;
    
void loop() {
  /* displays raw timer data
  if (counter%numLoop == 0) {
    if(Serial.available() > 0) {
      Serial.print("Pin 7: ");
      Serial.println(digitalRead(7));
      Serial.print("Pin 8: ");
      Serial.println(digitalRead(8));
      Serial.println(" ");
      delay(20);
    }
  }
  */
  
  val = digitalRead(7);
  
  if (val>0) {
    hi++;
  } else {
    lo++;
  }
  int level = 6;
  
  if (val>prevVal) { //rising edge
    if (lo>level) {
    Serial.print("Time lo: ");
    Serial.println(lo);
    }
    /*
    valsSum = 0;
    for(int i=0;i<ELEMS;i++) { //append newest low length to lo array
      if (i==ELEMS-1){
        valsLo[i] = lo;
      } else {
        valsLo[i] = valsLo[i+1];
      }
      valsSum += valsLo[i];
      
    }
    avgLo = valsSum/ELEMS;
    */
    lo = 0;
  } else if(val<prevVal) { //falling edge
    if (hi>level) {
    Serial.print("Time Hi: ");
    Serial.println(hi);
    }
    /*
    valsSum = 0;
    for(int i=0;i<ELEMS;i++) { //append newest high length to hi array
      if (i==ELEMS-1){
        valsHi[i] = hi;
      } else {
        valsHi[i] = valsHi[i+1];
      }
      valsSum += valsHi[i];
    }
    /*
    Serial.println(hi);
    Serial.println(valsSum);
    delay(1000);
    avgHi = valsSum/ELEMS;
    */
    hi = 0;
  }
  /*
  if (avgHi < 5.0) {
      Serial.print("avgHi: ");
      Serial.println(avgHi);
  }
  if (avgLo < 5.0) {
      Serial.print("avgLo: ");
      Serial.println(avgLo);
  }
  */
  prevVal = val;
}

