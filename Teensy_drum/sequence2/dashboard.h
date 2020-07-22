#ifndef Dashboard_h
#define Dashboard_h

#include <Audio.h>
#include <Bounce.h>


//two buttons on particular pins 
int DEBOUCE_TIME = 15;

class dashboard {
  public:
    Bounce play_button = Bounce(2, DEBOUNCE_TIME);
    Bounce stop_button = Bounce(3, DEBOUNCE_TIME);
    Bounce record_button = Bounce(4, DEBOUNCE_TIME);  
    dashboard();
       
}
