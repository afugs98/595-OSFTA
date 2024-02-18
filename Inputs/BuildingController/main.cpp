#include <iostream>
#include "BuildingManager.hpp"

/**
 * @id BuildingManager
 * @failure-probability 0.03
 * @dependencies [BuildingManger]
 */


int main() {
    // Create a Building Manager instance
    BuildingManager manager;

    // Simulate managing the building
    // This could be expanded to run in a loop, respond to user input, or be scheduled
    manager.manageBuilding();

    std::cout << "Building lights have been updated based on the current settings." << std::endl;

    return 0;
}