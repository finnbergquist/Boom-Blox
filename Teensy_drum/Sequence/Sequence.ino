#include "Sequencer.h"


Sequencer sequence(5, 4);

void setup(){
    Serial.begin(9600);
}

void loop() {

    Serial.println(sequence.getBPM());
    delay(100);

}
