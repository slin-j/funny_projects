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

int main()
{
    vector vec1(100,100);

    string input;

    int ff[10] = {1,2,3,4,5,6,7,8,9,10};

    for (auto &&i : ff)
    {
        cout << i <<endl;
    }
    
    //cout << *ff; 

    cout << "x:" << vec1.x << "y:" << vec1.y << endl;

    cin >> input;
    
    int f = input.find(' ');

    cout << "in:" << input << "find:" << f << endl;

    return 0;
}