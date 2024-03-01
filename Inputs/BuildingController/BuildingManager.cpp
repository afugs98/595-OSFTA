#include "BuildingManager.hpp"


/**
 * @id BuildingManager
 * @failure-probability 0.01
 * @dependencies [LightController]
 */

BuildingManager::BuildingManager() {
    // Initialize with some default light controllers
    controllers.push_back(LightController());
}

void BuildingManager::manageBuilding() {
    for (auto& controller : controllers) {
        controller.updateLights();
    }
}
