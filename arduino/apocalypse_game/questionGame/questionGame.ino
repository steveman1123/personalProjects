#include <stdio.h>
#include <Wire.h>
#include "rgb_lcd.h"
#include <CurieBLE.h>

rgb_lcd lcd;
const int powerLButt = 1;
const int lButt = A0;
const int rButt = A1;
const int vibPin = 4;
const int userPin =A2;
void loseSequence(int* wrong, boolean* exi){
    lcd.clear();
    lcd.print("Dude,");
    lcd.setCursor(0, 1);
    lcd.print("You just LOST");
    int r = random(0, 245);
    int g = random(0, 245);
    int b = random(0, 245);
    lcd.setRGB(r, g, b);
    *wrong=*wrong+1;
    delay(2000);
    lcd.setCursor(0, 0);
    *exi = true; 
    }
void winSequence(int* right, boolean* exi){
      lcd.clear();
      lcd.print("You Won!! :D !!");
      int r = random(0, 245);
      int g = random(0, 245);
      int b = random(0, 245);
      lcd.setRGB(r, g, b);
      *right=*right+1;
      digitalWrite(vibPin, 1);
      delay(2000);
      digitalWrite(vibPin, 0);
      *exi = true;    
}


String quests[] = {"Is Arduino real cool?", "Is grass green?", "Is anything real?", "No?", "Are you okay?", "Do you think?", "Is Walter cool?", "Do you even lift?", "Is the cake a lie?", "147+986=17", "163+236=399", "Was Cy the mascot in 1860?", "How many teeth do you have?", "Is Half Life 3 confirmed?", "Do pigs fly??", "Can you push both buttons?", "Do you have a name?", "Did you win?", "Did we win?", "Does the box vibrate?", "Can you stand on one leg?", "Is the answer always yes?", "Is SE a real major?" };
int ans[] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 };
const int questNUM = 23; //THIS MUST BE CHANGED IF THE QUESTION NUMBER IS CHANGED
int r = random(0, 245);
int g = random(0, 245);
int b = random(0, 245);


void setup() {
  randomSeed(analogRead(2));
  pinMode(powerLButt, OUTPUT);
  digitalWrite(powerLButt, HIGH);
  pinMode(rButt, INPUT);
  pinMode(lButt, INPUT);
  pinMode(vibPin, OUTPUT);
  lcd.begin(16, 2);
  lcd.setRGB(r, g, b);
  lcd.print("Are you ready to");
  lcd.setCursor(0, 1);
  lcd.print("play the question game?");
  lcd.setCursor(0, 0);
  delay(1500);
  lcd.clear();
}

int i = 0;
String topLine = "";
String botLine = "";
int right=0;
int wrong=0;
void loop() {
  
  int counter0; 
  i= random(0,22);
  lcd.clear();
  if (right>=10){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("DAMN");
    lcd.setCursor(0,1);
    lcd.print("You just keep Winning!!!!");
    lcd.setCursor(0,0);
    delay(1750);
    lcd.clear();
    lcd.print("You've gotten 10");
    lcd.setCursor(0,1);
    lcd.print("RIGHT! amazing");
    delay(1750);
    lcd.clear();
    right=0;
    
  }
  if (wrong>=10){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("DAMN u suck");
    lcd.setCursor(0,1);
    lcd.print(" GIVE UP!!!!");
    lcd.setCursor(0,0);
    delay(1750);
    lcd.clear();
    lcd.print("You've gotten 10");
    lcd.setCursor(0,1);
    lcd.print("WRONG! LOSER!"); 
    delay(1750);
    lcd.clear();
    wrong=0;
    }
    
  if (quests[i].length() > 16) {
    int j = 1;
    while (quests[i].charAt(quests[i].length() - j) != ' ') { j++; } 
    topLine = quests[i].substring(0, quests[i].length() - j);
    botLine = quests[i].substring(quests[i].length() - j + 1, quests[i].length());
  } else {
    topLine = quests[i];
    botLine = "";
  }
  lcd.setCursor(0, 0);
  lcd.print(topLine);
  lcd.setCursor(0, 1);
  lcd.print(botLine);

  //lcd.print(quests[i]);

  int lButtStatus = analogRead(lButt);
  int rButtStatus = analogRead(rButt);
  bool exi = false;
  while (!exi) {
    lButtStatus = analogRead(lButt);
    rButtStatus = analogRead(rButt);
    if( ans[i]==0){
       if (lButtStatus >1020) {
          winSequence(&right, &exi);
           }
       if (rButtStatus >1020) {
          loseSequence(&wrong, &exi); 
          }
       }
    if( ans[i]==1){   
       if (rButtStatus >1020) {
           winSequence(&right, &exi);
           right++;
           }
        if (lButtStatus >1020) {
           loseSequence(&wrong, &exi);
           wrong++;    
           }
       }
  }
  lcd.clear();
  lcd.print("wrong");
  lcd.print(wrong);
  delay(750);
  lcd.clear();
    lcd.print("right");
  lcd.print(right);
  delay(750);
  lcd.clear();
}
//  i++;
 /// if(i>questNUM-1){i=0;}
  


