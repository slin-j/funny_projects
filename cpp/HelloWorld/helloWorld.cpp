#include <iostream> 
using namespace std;

class vector
{
    public:
        float x;
        float y;

    vector(float x_val, float y_val)
    {
        x = x_val;
        y = y_val;
    }
};

void test(string* str)
{
    cout << "func:" << *str << endl;
}

int main()
{
    vector vec1(100,100);

    string input = "slin";
    string* p_in = &input;
    test(p_in);
    cout << *p_in << endl;

    return 0;
}