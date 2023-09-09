//infinity mirror LED strip using ws2811 and atmega328 chips

#include <FastLED.h>
#define LED_PIN     4
#define LED_TYPE    WS2811
#define COLOR_ORDER GRB
#define NUM_LEDS    84

CRGB leds[NUM_LEDS];

const int potPin= A0; //set potentiometer pin
const int buttonPin = 2; //set pushbutton pin

float readValue;  // Use this variable to read Potentiometer
int reading; //running value of button state (before debouncing)

#define FRAMES_PER_SECOND  240
#define MaxRead  1023 //max read value from pot
#define MinRead  0
#define MaxBrightness  255 //max brightness - can be set to dimmer if we wish
#define MinBrightness  0

unsigned char set_brightVal; //value to store scaled brightness value

int buttonState; //the user's idea of whether the button is pressed or not
int lastButtonState = LOW; // the previous reading from the input pin - this includes the bounce

unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled
unsigned short debounceDelay = 50;    // the debounce time in ms; increase if output flickers


uint8_t gHue = 0; // rotating "base color" used by many of the patterns
uint8_t gCurrentPatternNumber = 0; // Index number of which pattern is current


void setup() {
  delay(3000); // 3 second delay for recovery
  
  // tell FastLED about the LED strip configuration
  FastLED.addLeds<LED_TYPE,LED_PIN,COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  FastLED.clear();
  pinMode(potPin, INPUT);  //set potPin to be an input
  pinMode(buttonPin, INPUT);
  //Serial.begin(9600);      // turn on Serial Port
}

//declare list type and list of functions
typedef void (*SimplePatternList[])();
//the order of this list will be the order of the output when the button is pressed
SimplePatternList gPatterns = { rainbow, blocksRainbow, fadeRainbow, blockSolid, blueLoop, twoLoop, fourLoop, breatheRed, breathePurple, breatheRndColor, sinelon, clk, strobe, strobeRed, blockStrobe, purple, white };
//SimplePatternList gPatterns = { fourLoop }; //use this line to test individual patterns

void loop() {
  gPatterns[gCurrentPatternNumber]();
  reading = digitalRead(buttonPin); //read button state
  readValue = analogRead(potPin);  //Read the voltage on the Potentiometer

  //scale pot input to brightness value
  set_brightVal = (unsigned char) ((((readValue - MinRead) / (MaxRead - MinRead))* (MaxBrightness - MinBrightness)) + MinBrightness);

  //set minimum brightness value - just turn it off if it's too dim
  if (set_brightVal < 3){ set_brightVal = 0; }
  if (set_brightVal > 250){ set_brightVal = 255; }
  
  FastLED.setBrightness(set_brightVal); //update brightness value
  FastLED.show(); // send the 'leds' array out to the actual LED strip
  FastLED.delay(1000/FRAMES_PER_SECOND); // insert a delay to keep the framerate modest

  // If the button state changed, reset debounce timer
  if (reading != lastButtonState) { lastDebounceTime = millis(); }
  if ((millis() - lastDebounceTime) > debounceDelay) { //wait for debounce to finish
    if (reading != buttonState) { //if actual button state has changed
      buttonState = reading;
      if (buttonState == HIGH) { //button is pressed
        FastLED.clear();
        nextPattern();
      }
    }
  }
  lastButtonState = reading; //save button state
  EVERY_N_MILLISECONDS(20) { gHue++; } //change base hue color every 20 millis
}

#define ARRAY_SIZE(A) (sizeof(A) / sizeof((A)[0]))

// add one to the current pattern number, wrap around at the end
void nextPattern() {
  gCurrentPatternNumber = (gCurrentPatternNumber + 1) % ARRAY_SIZE(gPatterns);
}


// Blend one CRGB color toward another CRGB color by a given amount.
// Blending is linear, and done in the RGB color space.
// This function modifies 'cur' in place.
//https://forum.arduino.cc/t/fastled-fade-single-leds-from-color-to-a-target-color/547013
CRGB fadeTowardColor( CRGB& cur, const CRGB& target, uint8_t amount)
{
  nblendU8TowardU8( cur.red,   target.red,   amount);
  nblendU8TowardU8( cur.green, target.green, amount);
  nblendU8TowardU8( cur.blue,  target.blue,  amount);
  return cur;
}

// Helper function that blends one uint8_t toward another by a given amount
void nblendU8TowardU8( uint8_t& cur, const uint8_t target, uint8_t amount)
{
  if( cur == target) return;
  
  if( cur < target ) {
    uint8_t delta = target - cur;
    delta = scale8_video( delta, amount);
    cur += delta;
  } else {
    uint8_t delta = cur - target;
    delta = scale8_video( delta, amount);
    cur -= delta;
  }
}




//patterns

//a blue dot with a tail that goes in a loop along the strand
void blueLoop() {
  fadeToBlackBy(leds, NUM_LEDS, 15);
  byte pos = (millis()/100)%NUM_LEDS; //needs to be tested - will start at a "random" position, then will increase an index every 100ms
  CRGB dotCol = CRGB(0,255,128);
  fadeTowardColor(leds[(pos+2)%NUM_LEDS],dotCol,32);
  fadeTowardColor(leds[(pos+1)%NUM_LEDS],dotCol,64);
  fadeTowardColor(leds[pos],dotCol,128);
}

//like blueLoop, but with 2 dots offset of different colors
void twoLoop() {
  CRGB colList[] = {
    CRGB(0,255,128),
    CRGB(255,0,16)
  };

  fadeToBlackBy(leds, NUM_LEDS, 15);
  //init the position
  byte posList[2]; //TODO: make this dependent on the length of colList (must know how many bytes in CRGB and do sizeof(colList)/bytesPerCRGB
  for(byte p=0;p<sizeof(posList);p++) {
    //set the positions
    posList[p] = (millis()/100+p*NUM_LEDS/sizeof(posList))%NUM_LEDS;
    //show the colors (fade them in for smoother transitions
    fadeTowardColor(leds[(posList[p]+2)%NUM_LEDS],colList[p],32);
    fadeTowardColor(leds[(posList[p]+1)%NUM_LEDS],colList[p],64);
    fadeTowardColor(leds[posList[p]],colList[p],128);
  }
}

//like 2 loop, but with 4 dots offset of different colors
void fourLoop() {
  fadeToBlackBy(leds, NUM_LEDS, 15); //fade things to black

  //set the colors
  CRGB colList[] = {
     CRGB(0,255,128), //light blue
     CRGB(0,64,255), //green
     CRGB(255,0,16), //red orange
     CRGB(127,192,127) //white-ish
  };

  //init the position
  byte posList[4]; //TODO: make this dependent on the length of colList (must know how many bytes in CRGB and do sizeof(colList)/bytesPerCRGB
  for(byte p=0;p<sizeof(posList);p++) {
    //set the positions
    posList[p] = (millis()/100+p*NUM_LEDS/sizeof(posList))%NUM_LEDS;
    //show the colors (fade them in for smoother transitions
    fadeTowardColor(leds[(posList[p]+2)%NUM_LEDS],colList[p],32);
    fadeTowardColor(leds[(posList[p]+1)%NUM_LEDS],colList[p],64);
    fadeTowardColor(leds[posList[p]],colList[p],128);
  }
}

//color order is RBG
void red() { fill_solid(leds, NUM_LEDS, CRGB(255,0,0)); }
void orange() { fill_solid(leds, NUM_LEDS, CRGB(255,0,32)); }
void yellow() { fill_solid(leds, NUM_LEDS, CRGB(255,0,128)); }
void green() { fill_solid(leds, NUM_LEDS, CRGB(0,0,255)); }
void blue() { fill_solid(leds, NUM_LEDS, CRGB(0,255,0)); }
void indigo() { fill_solid(leds, NUM_LEDS, CRGB(32,127,32)); }
void purple() { fill_solid(leds, NUM_LEDS, CRGB(100,127,0)); }
void white() { fill_solid(leds, NUM_LEDS, CRGB(255,255,255)); }

// a colored dot sweeping back and forth, with fading trails
void sinelon() {
  fadeToBlackBy(leds, NUM_LEDS, 20);
  uint16_t pos = beatsin16(6, 0, NUM_LEDS-1 );
  leds[pos] += CHSV( gHue, 255, 192);
}

//makes the strip a rainbow
void rainbow() {
  fill_rainbow(leds, NUM_LEDS, gHue, 7); // FastLED's built-in rainbow generator
}

//fades the whole strip slowly through the rainbow
void fadeRainbow() {
  fill_solid(leds, NUM_LEDS, CHSV((millis()/100)%256, 255, 192)); //change color every 10s (denominator should be 10000) (max hue value is 255 for fastLED)
}

//flashes white at 31.25Hz (50% DC at 32ms)
void strobe() {
  char isOn = (millis()/32)%2;
  fill_solid(leds, NUM_LEDS, CRGB(255*isOn,255*isOn,255*isOn));
}

//flashes red at 31.25Hz (50% DC at 32ms)
void strobeRed() {
  char isOn = (millis()/32)%2;
  fill_solid(leds, NUM_LEDS, CRGB(255*isOn,0,0));
}

//purple dot makes a full circle along the strand every minute - one jump every second
void clk() {
  if(NUM_LEDS>=60){
    byte pos = NUM_LEDS * (millis()/1000 % 60)/60.0; //scale ms to sec and # of lights in strip (so dot goes around strip in 1 min)
    
    leds[(pos+1)%NUM_LEDS] = CRGB(100,127,0); //set teh next light to be on (scale to be on the strip)
    leds[pos] = leds[pos+1]; //set this dot to be on
    fadeToBlackBy(leds, NUM_LEDS, 10); //leave a little bit of a trail (might just fade out)
  } else {
    fill_solid(leds, NUM_LEDS, CRGB(100,127,0)); //flash whole strip if the strip has less than 60 lights 
    fadeToBlackBy(leds, NUM_LEDS, 25); //leave a little bit of a trail (might just fade out)
  }
  
}

//make green blips of some on some off, march around
void blips() {
  unsigned short startIndex = millis()/500 % NUM_LEDS; //increase every 500ms  
  unsigned short on = 5;
  unsigned short off = 2;
  fill_solid(leds, NUM_LEDS,CRGB(0,0,255)); //set everything to green
  for(char j=0;j<NUM_LEDS/(on+off);j++){
    for(short i=0;i<off;i++) {
      leds[(i+j*(on+off)+startIndex)%NUM_LEDS] = CRGB(0,0,0);
    }
  }
}

//fade fom black to red and back
void breatheRed() {
  byte freq = 3; //frequency in bpm
  CRGB curColor = CRGB(beatsin8(freq, 0, 255),0,0); //color is always red, but beats
  fill_solid(leds,NUM_LEDS,curColor);
}

void breathePurple() {
  byte freq = 3; //frequency in bpm
  CRGB curColor = CRGB(beatsin8(freq, 5, 100),beatsin8(freq,5,127),0); //color is always purple, but beats
  fill_solid(leds,NUM_LEDS,curColor);
}

//fade from black to a constant rainbow color
//TODO: delay for a short period when off and when at full? Or find another way to slow it down
CRGB tgtColor = CRGB(0,0,0);
void breatheRndColor() {
  if(leds[0]==CRGB(0,0,0)) { //if leds are off, then change the tgt color
    tgtColor = CRGB(random(0,255),random(0,255),random(0,255));
  } else if(leds[0]==tgtColor) { //else if the leds are the tgt color, then the tgt to off
    tgtColor = CRGB(0,0,0);
  }
  for(byte i=0;i<NUM_LEDS;i++) {
    fadeTowardColor(leds[i],tgtColor,1);
  }
}

//TODO
//random points that blip in and fade out
void drops() {
  byte ptList[6]; //number of points 
  
}


//wave that moves left to right and back again
void slosh() {
  
}

//steve's mirror has 3 blocks in it - these functions color only those blocks
//these are the locations of the blocks (extracted from leds array in setup)
const char blockLength = 11; //number of leds per block
unsigned char block1pos = 9;
unsigned char block2pos = 31;
unsigned char block3pos = 62;

CRGB blockCol = CRGB(0,0,0); //solid color for the blocks
CRGB rimCol = CRGB(0,0,0); // solid color for the rim

//perform the rainbow function just on the blocks
void blocksRainbow() {
  for(char i=0;i<blockLength;i++){
    leds[block1pos+i] = CHSV(gHue+i*7,255,192);
    leds[block2pos+i] = CHSV(gHue+i*7+100,255,192);
    leds[block3pos+i] = CHSV(gHue+i*7+200,255,192);
  }
}

//set each block as it's own solid color
void blockSolid() {
  for(char i=0;i<blockLength;i++){
    leds[block1pos+i] = CHSV(gHue,255,192);
    leds[block2pos+i] = CHSV(gHue+100,255,192);
    leds[block3pos+i] = CHSV(gHue+200,255,192);
  }
}


//strobe the blocks as one color, and the rest as another, alternating every so often
void blockStrobe() {
  CRGB c1 = CRGB(255,255,255);
  CRGB c2 = CRGB(255,0,0);
  byte blkFreq = 32; //in ms - eg 32=31.25Hz (since 1/32ms=31.25Hz)
  byte rimFreq = 32; //in ms - eg 32=31.25Hz (since 1/32ms=31.25Hz)
  //TODO: set the swap time to change as a random number (btw 0.5 and 5 seconds)
  byte swapTime = 2; //in seconds, swap the colors every {swapTime} seconds

  bool blockOn = (millis()/blkFreq)%2; //set the block to be on or off
  bool rimOn = (millis()/rimFreq)%2; //set the rim to be on or off
  
  //swap the colors
  if(((millis()/1000)/swapTime)%2) {
    blockCol = c1;
    rimCol = c2;
  } else {
    blockCol = c2;
    rimCol = c1;
  }
  
  //fill the whole strip (including the blocks)
  fill_solid(leds, NUM_LEDS, CRGB(rimCol.r*rimOn,rimCol.g*rimOn,rimCol.b*rimOn));
  //overwrite the blocks with their color
  for(char i=0;i<blockLength;i++){
    leds[block1pos+i] = CRGB(blockCol.r*blockOn,blockCol.g*blockOn,blockCol.b*blockOn);
    leds[block2pos+i] = CRGB(blockCol.r*blockOn,blockCol.g*blockOn,blockCol.b*blockOn);
    leds[block3pos+i] = CRGB(blockCol.r*blockOn,blockCol.g*blockOn,blockCol.b*blockOn);
  }
}

//waves that eminate at random frequencies away from two boxes (currently have speakers on them, should look like the waves are coming from the speakers)
void waves() {
  
}
