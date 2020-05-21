#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

//모폴로지 연산을 위한 데이터
int main() {
uchar data[] = {
		0,0,0,0,0,0,0,0,
		0,1,1,0,0,0,1,0,
		0,1,1,0,0,0,1,0,
		0,1,1,1,0,0,1,0,
		0,1,1,1,0,1,1,0,
		0,1,1,1,1,1,1,0,
		0,1,1,0,0,1,1,0,
		0,0,0,0,0,0,0,0
};
Mat src = Mat(8, 8, CV_8UC1, data);
cout << "src is\n" << src << endl;

Mat bin;
threshold(src, bin, 0, 1, THRESH_BINARY | THRESH_OTSU);

Mat mask = getStructuringElement(MORPH_CROSS, Size(3,3), Point(1,1));

Mat dst1, dst2;

erode(bin, dst1, mask, Point(-1, -1), 1);
dilate(bin, dst2, mask, Point(-1, -1), 1);

cout << "erode is\n" << dst1 << endl;
cout << "dilate is\n" << dst2 << endl;

Mat dst3, dst4;
morphologyEx(bin, dst3, MORPH_OPEN, mask);
morphologyEx(bin, dst4, MORPH_CLOSE, mask);

cout << "open is\n" << dst3 << endl;
cout << "close is\n" << dst4 << endl;

return 0;
}

