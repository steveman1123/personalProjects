int minPin = A0;
int maxPin = A5;


void setup() {
  Serial.begin(9600);
  for(int i=minPin;i<=maxPin;i++) { pinMode(i,INPUT); }
}


void loop() {
  for(int i=minPin;i<=maxPin;i++) {
    Serial.print(digitalRead(i));
    Serial.print(", ");
  }
  Serial.println("");
}

