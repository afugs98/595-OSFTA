#include "Timer.hpp"

Timer::Timer() {
    // Set default onTime and offTime (e.g., 6 PM to 6 AM)
    onTime = std::time(nullptr); // Placeholder for actual time setting
    offTime = std::time(nullptr); // Placeholder for actual time setting
}

bool Timer::checkStatus(const std::time_t& currentTime) {
    return (currentTime >= onTime && currentTime < offTime);
}

void Timer::setOnTime(std::time_t newOnTime) {
    onTime = newOnTime;
}

void Timer::setOffTime(std::time_t newOffTime) {
    offTime = newOffTime;
}
