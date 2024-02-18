#ifndef LIGHTCONTROLLER_H
#define LIGHTCONTROLLER_H

#include "Light.hpp"
#include "Dimmer.hpp"
#include "Timer.hpp"
#include "Sensor.hpp"
#include <vector>

class LightController {
public:
    LightController();
    void updateLights();

private:
    std::vector<Light> lights;
    std::vector<Dimmer> dimmers;
    std::vector<Timer> timers;
    std::vector<Sensor> sensors;
};

#endif // LIGHTCONTROLLER_H
