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
해당 xml 파일은 c:/opencv/source/data/haarcascades에 위치해 있습니다.*/
void detect_face()
{
	Mat src = imread("tott.jpg");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	CascadeClassifier classifier("haarcascade_frontalface_default.xml");

	if (classifier.empty()) {
		cerr << "XML load failed!" << endl;
		return;
	}

	vector<Rect> faces;
	classifier.detectMultiScale(src, faces);

	for (Rect rc : faces) {
		rectangle(src, rc, Scalar(255, 0, 255), 2);
	}

	imshow("src", src);

	waitKey(0);
	destroyAllWindows();
}

void detect_eyes()
{
	Mat src = imread("tott.jpg");

	if (src.empty()) {
		cerr << "Image load failed!" << endl;
		return;
	}

	CascadeClassifier face_classifier("haarcascade_frontalface_default.xml");
	CascadeClassifier eye_classifier("haarcascade_eye.xml");

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
			circle(faceROI, center, eye.width / 2, Scalar(255, 0, 0), 2, LINE_AA);
		}
	}

	imshow("src", src);

	waitKey(0);
	destroyAllWindows();
}
