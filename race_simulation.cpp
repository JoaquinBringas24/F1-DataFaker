#include <iostream>
using namespace std;

extern "C"
{
    double box_probability(double prob, int stint_laps, double rate)
    {
        return prob - (rate * stint_laps);
    };

    bool box_eval(double prob)
    {
        return (rand() % 100) > prob * 100;
    };

    double lap_time(double stint_laps, int distance, double velocity, double rate)
    {
        return distance / (velocity - rate * stint_laps);
    };
};
