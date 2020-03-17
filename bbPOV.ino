#include <NeoPixelBus.h>
#include "graphics.h"
#define colorSaturation 128
#define IR 32

int numRot= 0;
int numDiv = 0;
int stateDiv = 0;
int spinstae = 1;
volatile unsigned long rotTime, timeOld, timeNow, opeTime, spinTime;

uint8_t loopcount=0;
uint8_t ListNow=0;
uint8_t delayFrames=2;
uint8_t SpinTimes=0;
#define looptimes 20

NeoPixelBus<DotStarBgrFeature, DotStarSpiMethod> strip(NUMPIXELS);
RgbColor black(0);

void setup() {
  
  Serial.begin(115200);
  pinMode(IR, INPUT);
   attachInterrupt(IR, RotCount, RISING );
     strip.Begin();
    strip.ClearTo(black);
    strip.Show();
}
void loop() {
 if(stateDiv == 1 && micros() - timeOld > rotTime / Div * (numDiv)){
    stateDiv = 0;
  }
  if(stateDiv == 0 && micros() - timeOld < rotTime / Div * (numDiv + 1)){
    stateDiv = 1;
    strip.ClearTo(black);
        for(int i = 0; i < NUMPIXELS; i++){
      strip.SetPixelColor(i, HtmlColor(pic[numRot][numDiv][i]));
    }
    strip.Show();
    
    numDiv++;
    if(numDiv >= Div ) numDiv = 0;
  }
}

void RotCount() {
  timeNow = micros();
  rotTime = timeNow - timeOld;
  timeOld = timeNow;

  SpinTimes++;
  
  if (SpinTimes>=delayFrames){
  numRot++;
  loopcount++;
  SpinTimes=0;
  
  if (loopcount<looptimes){
      if(numRot>=ShowList[ListNow+1])
      numRot=ShowList[ListNow];
    }
  else{
      loopcount=0;
      ListNow++;
      if(ListNow>=list)
        ListNow=0;
    }
  if (numRot >= Frame ){
    numRot = 0;
  }
  }
}
