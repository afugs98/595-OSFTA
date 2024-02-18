#ifndef LIGHT_H
#define LIGHT_H

class Light {
public:
    Light();
    void turnOn();
    void turnOff();
    void setBrightness(int level);

    bool isLightOn() const;  // Declaration for isLightOn
    int getBrightness() const;  // Declaration for getBrightness


private:
    bool isOn;
    int brightness;
};

#endif // LIGHT_H
