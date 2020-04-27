#include "opencv2/opencv.hpp"
#include <iostream>
/*harr알고리즘을 이용한 얼굴 및 눈 검출 프로그램입니다*/
using namespace cv;
using namespace std;

//얼굴과 눈 검출을 위한 함수를 따로 만들었습니다.
void detect_face();
void detect_eyes();

//main문은 단순 함수 호출 기능만 부여합니다.
int main()
{
	detect_face();
	detect_eyes();

	return 0;
}

/*얼굴 검출 함수입니다.
1.이미지를 imread시킨다==>visual studio로 할 때, 이미지와 xml파일들은 해당 프로젝트 폴더에 옮기셔야 합니다.

2. xml을 불러들인다==>해당xml 파일들은 haarcascade의 전면 얼굴(frontalface_default)과 눈(eye)에 대한 내용이 들어있습니다. 이는 opencv에서 제공해주므로 따로 만들 필요가 없습니다.
해당 xml 파일은 c:/opencv/source/data/haarcascades에 위치해 있습니다.

3. 입력 영상 image에서 다양한 크기의 객체 사각형 영역을 검출합니다(detectMultiScale). Rect클래스를 이용해 벡터 타입으로 모든 사각형 정보를 저장합니다.
*/
void detect_face()
{
	Mat src = imread("tott.jpg");
	
	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}
	//CascadeClassifier classifier.load("");으로도 표현 가능합니다.
	CascadeClassifier classifier("haarcascade_frontalface_default.xml");

	//에러문
	if (classifier.empty()) {
		cerr << "XML load failed!" << endl;
		return;
	}
	//src에서 얼굴 영상을 검출하여 faces에 저장합니다.
	vector<Rect> faces;
	classifier.detectMultiScale(src, faces);

	//사각형 영역을 청록색으로 표시합니다. rgb값을 변경해도 무방.
	for (Rect rc : faces) {
		rectangle(src, rc, Scalar(255, 255, 0), 2);
	}

	imshow("src", src);

	waitKey(0);
	destroyAllWindows();
}
/*눈 영역을 검출합니다. 전체적인 코드는 위와 비슷합니다.
1. 먼저 얼굴의 위치를 찾은 후에 눈 위치를 찾는 방식으로 진행했습니다.
2. 입력 영상에서 검출한 사각형 얼굴 영역의 부분 영상을 추출하여 faceROI에 저장합니다.
3. faceROI에서 눈을 검출합니다.
4. 검출한 눈의 중앙에 원을 그립니다.*/
void detect_eyes()
{
	Mat src = imread("lena.jpg");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	CascadeClassifier face_classifier("haarcascade_frontalface_default.xml");
	CascadeClassifier eye_classifier("haarcascade_eye.xml");

	//에러문 
	if (face_classifier.empty() || eye_classifier.empty()) {
		cerr << "XML load failed!" << endl;
		return;
	}

	vector<Rect> faces;
	face_classifier.detectMultiScale(src, faces);

	for (Rect face : faces) {
		rectangle(src, face, Scalar(255, 0, 255), 2);

		Mat faceROI = src(face);
		vector<Rect> eyes;
		eye_classifier.detectMultiScale(faceROI, eyes);

		for (Rect eye : eyes) {
			Point center(eye.x + eye.width / 2, eye.y + eye.height / 2);
			circle(faceROI, center, eye.width / 2, Scalar(0, 0, 255), 2, LINE_AA);//빨간색 원
		}
	}

	imshow("src", src);

	waitKey(0);
	destroyAllWindows();
}
