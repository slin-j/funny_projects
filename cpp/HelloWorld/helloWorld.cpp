#include <iostream> 
#include <vector>
#include <time.h>
using namespace std;

int main()
{
    vector<string> asdf;

    
    asdf.push_back("h");
    asdf.push_back("allo"); 

    string st = "hallo velo";
    string st2 = "hallo";


    cout << st << endl;

    for(string i : asdf)
        cout << i << endl;

    return 0;
}