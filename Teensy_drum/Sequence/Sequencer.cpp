#include "Sequencer.h"

Sequencer::Sequencer(int BPM, int Steps) {
  this->BPM = BPM;
  this->Steps = Steps;
}
int Sequencer::getBPM() {
  return this->BPM;
}

int Sequencer::getSteps() {
  return this->Steps;
}

int Sequencer::setBPM(int BPM) {
  this->BPM = BPM;
}

int Sequencer::setSteps(int Steps) {
  this->Steps = Steps;
}
