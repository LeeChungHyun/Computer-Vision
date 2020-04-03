#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;
using namespace cv;
/*레이블링 응용해서 bounding box만들기*/
void labeling_stats()
{
	Mat src = imread("keyboard.bmp", IMREAD_GRAYSCALE);

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	Mat bin;
	threshold(src, bin, 0, 255, THRESH_BINARY | THRESH_OTSU);//src영상을 오츠 알고리즘으로 이진화 하고 bin에 저장

	Mat labels, stats, centroids;
	int cnt = connectedComponentsWithStats(bin, labels, stats, centroids);//bin영상에 레이블링 수행하고 각 객체 영역의 통계정보 추출한다.

	Mat dst;
	cvtColor(src, dst, COLOR_GRAY2BGR);//3채널로 변경하고 dst에 저장한다.

	for (int i = 1; i < cnt; i++) {
		int* p = stats.ptr<int>(i);//흰색 객체 영역에만 for문 수행한다.

		if (p[4] < 20) continue;//객체검출의 개수가 20개보다 작으면 잡음으로 간주하고 무시한다.

		rectangle(dst, Rect(p[0], p[1], p[2], p[3]), Scalar(0, 255, 255));//바운딩 박스(노랑색으로 했다.)
	}


	imshow("src", src);
	imshow("dst", dst);

	waitKey();
	destroyAllWindows();
}

int main() {
	labeling_stats();
	return 0;
}