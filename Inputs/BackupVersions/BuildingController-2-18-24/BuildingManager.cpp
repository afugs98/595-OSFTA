#include "BuildingManager.hpp"

BuildingManager::BuildingManager() {
    // Initialize with some default light controllers
    controllers.push_back(LightController());
}

void BuildingManager::manageBuilding() {
    for (auto& controller : controllers) {
        controller.updateLights();
    }
}
