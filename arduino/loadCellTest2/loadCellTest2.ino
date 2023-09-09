/* Steven Williams
    18.11.2015
   __|``|__|``|__|``|__|``|__
   read clock data from a load cell and interpret it as a weight
*/

void setup() {
  pinMode(3, INPUT);
  Serial.begin(9600);
}

const int LENGTH = 20;   //# of data pts, ~16
short arrayhi[LENGTH];
short arraylo[LENGTH];
unsigned long start;
int n;
int hi;
int lo;
const int INTERVAL = 50; //# of milliseconds of read time

void loop() {
  memset (arrayhi, 0, LENGTH); //clear arrays to avoid carrying previous data over
  memset (arraylo, 0, LENGTH);
  n = 0;
  start = millis(); //set start time point
  //read
  while ((millis() - start) < INTERVAL) {
    hi = 0;
    lo = 0;
    while (digitalRead(7) == 0) { lo++; } //length of low signal
    while (digitalRead(7) == 1) { hi++; } //length of high signal
    n++;
    if (hi > 0 && hi <= LENGTH) { arrayhi[hi - 1] = arrayhi[hi - 1] + hi; } //add new hi val to arrayhi
    if (lo > 0 && lo <= LENGTH) { arraylo[lo - 1] = arraylo[lo - 1] + lo; } //add new lo val to arraylo
  }
/*
  //average the numbers over the whole
  for (int i = 0; i < LENGTH; i++) {
    arrayhi[i] = (short) arrayhi[i] / n;
    arraylo[i] = (short) arraylo[i] / n;
  }
*/
  //disp arrayhi
  Serial.print("Hi:  ");
  for (int i = 0; i < LENGTH; i++) {
    Serial.print(arrayhi[i]);
    Serial.print("  ");
  }
  Serial.print("     ");

  //disp arraylo
  Serial.print("Lo:  ");
  for (int i = 0; i < LENGTH; i++) {
    Serial.print(arraylo[i]);
    Serial.print("  ");
  }
  Serial.println();
}
