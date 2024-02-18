#ifndef SENSOR_H
#define SENSOR_H

class Sensor {
public:
    Sensor();
    void setAmbientLight(float lightLevel);  // Declaration for setAmbientLight
    float getAmbientLight() const;

private:
    float ambientLight;
};

#endif // SENSOR_H
