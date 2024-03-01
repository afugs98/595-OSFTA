#include "LightController.hpp"


/**
 * @id LightController
 * @failure-probability 0.1
 * @dependencies [Light, Dimmer, Sensor, Timer]
 */

LightController::LightController() {
    // Initialize with some default lights, dimmers, timers, sensors
    lights.push_back(Light());
    dimmers.push_back(Dimmer());
    timers.push_back(Timer());
    sensors.push_back(Sensor());
}

void LightController::updateLights() {
    for (auto& light : lights) {
        // Example logic: if timer is on and ambient light is low, turn on the light
        auto currentTime = std::time(nullptr);
        if (timers[0].checkStatus(currentTime) && sensors[0].getAmbientLight() < 0.5f) {
            light.turnOn();
            light.setBrightness(dimmers[0].getLevel());
        } else {
            light.turnOff();
        }
    }
}
