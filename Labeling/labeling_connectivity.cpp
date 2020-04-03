#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;
/*영상 레이블링에서 픽셀의 연결 관계
1. 4-방향 연결성
2. 8-방향 연결성
*/
void labeling_basic() {
	uchar data[] = {
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,1,1,0,0,0,0,
		0,0,0,0,0,1,0,0,0,0,
		0,0,0,0,0,1,0,1,1,0,
		0,0,1,1,1,0,0,0,1,0,
		0,1,0,0,0,0,0,0,1,0,
		0,1,0,0,0,0,1,1,0,0,
		0,0,1,1,1,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
	};//uchar 자료형 배열 data를 픽셀 데이터로 사용하는 임시 Mat객체생성


	Mat src = Mat(10, 10, CV_8UC1, data) * 255;//n*n크기의 이진 영상, 모든 원소에 255곱한 결과 src에 저장한다.

	Mat labels;
	int cnt = connectedComponents(src, labels, 8);//image, label, connectivity순으로(4 또는 8)
	//지금은 8-방향 연결성 방식으로 접해본다.

	cout << "src:\n" << src << endl;
	cout << "labels:\n" << labels << endl;
	cout << "number of label:" << cnt << endl;
}

int main() {
	labeling_basic();
	return 0;
}