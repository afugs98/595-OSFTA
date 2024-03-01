#include "Sensor.hpp"

/**
 * @id Sensor
 * @failure-probability 0.05
 * @dependencies []
 */

Sensor::Sensor() : ambientLight(0.0f) {}

void Sensor::setAmbientLight(float lightLevel) {
    ambientLight = lightLevel;
}

float Sensor::getAmbientLight() const {
    return ambientLight;
}
