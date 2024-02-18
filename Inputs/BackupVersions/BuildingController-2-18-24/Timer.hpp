#ifndef TIMER_H
#define TIMER_H

#include <ctime>

class Timer {
public:
    Timer();
    bool checkStatus(const std::time_t& currentTime);
    void setOnTime(std::time_t newOnTime);  // Declaration for setOnTime
    void setOffTime(std::time_t newOffTime);  // Declaration for setOffTime

private:
    std::time_t onTime;
    std::time_t offTime;
};

#endif // TIMER_H