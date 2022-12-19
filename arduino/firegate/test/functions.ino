//for functions that can be used in broad scenarios

//get nth bit of a char
bool getBit(char x, unsigned short n) {
  return 0b1 & (x >> n);
}

//sets the nth bit of a char to 1 or 0
char setBit(char c, bool b, unsigned short n) {
  return (0b1 << n) | c;
}

//pause the program for t ms
void waitMillis(int t) {
  unsigned int startTime = millis();
  while(millis() < (startTime+t)) {}
}

const int TIME2WAIT = 1; //time duration of 1 bit - should be 1 for actual transfer, increase to ~500 for testing
//sends 1 byte of data across a pin
//turn on startLine, send data over dataLine, turn off startLine
void send_data(char data, int startLine, int dataLine) {
  digitalWrite(startLine,HIGH);
  for(int i=0;i<8;i++) {
    digitalWrite(dataLine,getBit(data, i));
    waitMillis(TIME2WAIT);
  }
  digitalWrite(startLine, LOW);
}

//if pin 1 is high,
char get_data(int startLine, int dataLine) {
  if(digitalRead(startLine)) {
    unsigned char bitPos = 0; //0->7
    char output = 0;
    int startTime = millis();
    //8 is the size of a char type
    while(digitalRead(startLine)|(bitPos<8)) {
      //number of bits to shift is dependant on wait time
      bitPos = (millis()-startTime)/TIME2WAIT;
      output = output | (digitalRead(dataLine) << bitPos);
    }
    return output;
  }
  return 0;
}
