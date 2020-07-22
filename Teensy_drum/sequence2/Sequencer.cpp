#include "Sequencer.h"
#include "Drum_channel.h"

Sequencer::Sequencer(int BPM, int max_steps, int note_duration, int num_channels) {
    //BPM, loop length and note duration
    this->BPM = BPM;
    this->max_steps = max_steps;
    this->duration = note_duration;
    this->num_channels = num_channels;
    this->Step = -1;
    //time is is millis
    this->init_time = millis();
    this->step_interval = (60000 / BPM) / duration;
    this->total_time = step_interval * max_steps;
}

void Sequencer::start_clock() {
  this->init_time = millis();
  this->elapsed_time = 0;
}

void Sequencer::stop_clock() {
  this->elapsed_time = 0;
  this->Step = 0;
}


int Sequencer::getBPM() {
    return this->step_interval;
}

int Sequencer::getChannels() {
    return this->num_channels;
}

int Sequencer::getStep() {
    //get the time and check if 
    Step = this->Check() / this->step_interval;
    if (Step >= max_steps) {
      Step = 0;
      start_clock();
    }
    
    return Step;
}

int Sequencer::Check() {
  this->elapsed_time = millis() - init_time;
  return this->elapsed_time;
}

bool Sequencer::change() {
  return (Step != getStep());

}

void Sequencer::add_instrument(Drum_channel new_channel) {
  channels[curr_channel] = new_channel;
  curr_channel++;
}

Drum_channel Sequencer::get_instrument(int index) {
  return channels[index];
}

bool Sequencer::inst_On(int inst) {
  return (get_instrument(inst).On(getStep()) == 1);
  
}

const char* Sequencer::getSound(int inst) {
  return get_instrument(inst).getSound();
}
