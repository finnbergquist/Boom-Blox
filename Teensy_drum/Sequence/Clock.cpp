#include "Clock.h"

Clock::Clock(int BPM, int max_steps) {
    this->BPM = BPM;
    this->max_steps = max_steps;
    this->Step = 0;
    //time is is millis
    this->init_time = millis();
    this->step_interval = 60000 / BPM;
    this->total_time = step_interval * max_steps;
}

void Clock::start_clock() {
  this->init_time = millis();
  this->elapsed_time = 0;
}

void Clock::stop_clock() {
  this->elapsed_time = 0;
  this->Step = 0;
}



int Clock::getBPM() {
    return this->step_interval;
}

int Clock::getStep() {
    //get the time and check if 
    Step = this->getTime() / this->step_interval;
    if (Step >= max_steps) {
      Step = 0;
      start_clock();
    }
    
    return Step;
}

int Clock::getTime() {
  this->elapsed_time = millis() - init_time;
  return this->elapsed_time;
}

bool Clock::change() {
  return (Step != getStep());

}
