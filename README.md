
# Proctor : openCV 기반 비대면 시험 감독 웹사이트


## 📌 서비스 소개



- COVID-19 로 인한 비대면 활동이 보편화 되면서, 온라인 시험 내 부정행위 역시 증가하는 것을 막기 위해 만들게 되었어요.

- 대리 시험 , 화면 이탈, 멀티 디바이스를 통한 컨닝 등 부정행위를 막고 공정한 시험을 치르기 위한 부정행위 검출 및 감독 시스템 입니다.

- 응시자의 웹 카메라를 이용해 부정행위를 감독합니다.

- 전자기기 및 사람 수, 눈동자 방향, 얼굴 방향 각도를 탐지하고, 관리자에게 카카오톡 알림 서비스를 보냅니다.


## 📌 주요 기능

<p align="center">
  <img src="https://github.com/HyunnS2/Proctor/assets/105518951/c7d58fdb-38af-4d3f-9bf4-ec0c2c79262e">
</p>


##### 회원가입 및 로그인
- 관리자와 응시자로 구분하여 회원가입 및 로그인
- 카카오톡 로그인

##### 시험 생성
- 관리자 로그인 시 시험 생성 가능


##### 시험 응시
- 응시자 로그인 시 시험 목록을 확인하고 본인의 시험 응시 가능


##### 부정행위 탐지
- 부정행위 탐지 시, 해당 화면이 바로 캡쳐되며, 관리자에게 실시간 카카오톡 알림
- 시험 후 관리자는 시험 목록 , 응시자 , 시험 시간 , 부정행위 목록을 확인 및 검색 가능
- 응시자는 촬영된 부정행위 이미지를 통해 이의 제기 게시판을 활용해 이의 가능


## 📌 사용 기술

- Django
- openCV
- YoloV3
- Dlib , mediapipe
- MySQL


##  📌 서비스 이미지

관리자 - 시험 추가

<p style="width:500px">
	<img src="https://github.com/HyunnS2/Proctor/assets/105518951/f91ca704-fe94-44b0-903b-633a39fab5b7">
</p>

응시자 - 시험 목록 확인 및 입장

<p style="width:300px"><img src = ""https://github.com/HyunnS2/Proctor/assets/105518951/5af88232-82ae-41de-9279-de1ad3006fdd></p>

<p>
    <img src = "https://github.com/HyunnS2/Proctor/assets/105518951/6baf91a8-1dc0-4e4c-b592-faff8b27be4c">
    
</p>
