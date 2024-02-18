# Compiler settings
CXX = g++
CXXFLAGS = -Wall -std=c++11

# Project files
SOURCES = main.cpp Light.cpp Dimmer.cpp Timer.cpp Sensor.cpp LightController.cpp BuildingManager.cpp
OBJECTS = $(SOURCES:%.cpp=build/%.o)
EXECUTABLE = build/BuildingLightSystem

# Build directory
BUILDDIR = build

# Default target
all: $(BUILDDIR) $(EXECUTABLE)

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

$(EXECUTABLE): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $@

# Rule for compiling source files
build/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up
clean:
	rm -rf $(BUILDDIR)

# Run the program
run: all
	./$(EXECUTABLE)
