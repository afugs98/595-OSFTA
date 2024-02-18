#include "Light.hpp"

Light::Light() : isOn(false), brightness(0) {}

void Light::turnOn() {
    isOn = true;
}

void Light::turnOff() {
    isOn = false;
}

void Light::setBrightness(int level) {
    if (level >= 0 && level <= 100) {
        brightness = level;
    }
}

bool Light::isLightOn() const {
    return isOn;
}

int Light::getBrightness() const {
    return brightness;
}
