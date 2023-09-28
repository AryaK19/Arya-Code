#include<iostream>
#include<math.h>
using namespace std;


class Point{
    int x, y;
    public:
        Point(int a, int b){
            x = a;
            y = b;
        }
        friend void distPoints(Point,Point);

        void displayPoint(){
            cout<<"The point is ("<<x<<", "<<y<<")"<<endl;
        }

};

void distPoints(Point a ,Point b){
    int dist = pow(pow((a.x - b.x),2) + pow((a.y - b.y),2),0.5);
    cout<<"The Distance Between the Points is "<<dist<<endl;
    

}

int main(){
    Point p(0, 1);
    p.displayPoint();

    Point q(0, 6);
    q.displayPoint();
    distPoints(p,q);
    return 0;
}
