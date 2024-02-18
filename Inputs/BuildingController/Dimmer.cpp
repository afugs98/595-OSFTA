#include "Dimmer.hpp"

Dimmer::Dimmer() : level(50) {}

void Dimmer::increase() {
    if (level < 100) {
        level++;
    }
}

void Dimmer::decrease() {
    if (level > 0) {
        level--;
    }
}

int Dimmer::getLevel() const {
    return level;
}
