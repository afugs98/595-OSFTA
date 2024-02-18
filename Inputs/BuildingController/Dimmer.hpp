#ifndef DIMMER_H
#define DIMMER_H

class Dimmer {
public:
    Dimmer();
    void increase();
    void decrease();
    int getLevel() const;

private:
    int level;
};

#endif // DIMMER_H
