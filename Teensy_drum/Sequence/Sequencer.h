
#ifndef SEQUENCER_H
#define SEQUENCER_H

#include <Arduino.h>

class Sequencer {

  private:      
    int BPM;
    int Steps;
    

    
    
  public:
    Sequencer(int BPM, int Steps);
    int getBPM();
    int getSteps();
    int setBPM(int BPM);
    int setSteps(int Steps);

    
};

#endif
