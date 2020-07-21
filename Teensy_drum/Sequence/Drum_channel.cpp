#include "Drum_channel.h"


Drum_channel::Drum_channel(const char *inst_name, int max_steps) {
    this->inst_name = inst_name;
    this->max_steps = max_steps;


}

const char* Drum_channel::getSound() {
    return this->inst_name;
}

int Drum_channel::On(int index) {
    return this->steps[index];
}

void Drum_channel::set(int index, int val) {
  this->steps[index] = val;
}
