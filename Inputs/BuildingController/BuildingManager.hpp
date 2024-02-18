#ifndef BUILDINGMANAGER_H
#define BUILDINGMANAGER_H

#include "LightController.hpp"
#include <vector>

class BuildingManager {
public:
    BuildingManager();
    void manageBuilding();

private:
    std::vector<LightController> controllers;
};

#endif // BUILDINGMANAGER_H
