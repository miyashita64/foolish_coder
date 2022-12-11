#include "FeeCalculator.h"

int FeeCalculator::calcFee(int old){
    if(old >= 60){
        return 500;
    }
    else if (old >= 19)
    {
        return 800;
    }
    else if (old >= 13)
    {
        return 500;
    }
    return 0;
}