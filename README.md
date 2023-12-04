# SmartSensor-Python

## 프로젝트 개요
노인 분들이 넘어졌을 때 이를 감지하는 스마트 홈캠을 위한 Python 기반의 낙상 감지 알고리즘입니다. 이 프로젝트는 아두이노와 YOLO v8 라이브러리를 활용하여 실시간으로 넘어짐 상황을 감지하고, 보호자에게 알립니다.

## 시작하기 전에
이 프로젝트는 Python 3.9를 사용하며, 가상환경에서 작업하는 것을 권장합니다.

## 설치 방법

### 가상환경 설정 및 활성화

1. 가상환경 생성:
   ```bash
   python -m venv .venv
   ```

2. 가상환경 활성화:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### 필요한 패키지 설치

이 프로젝트의 모든 의존성은 `requirements.txt`에 명시되어 있습니다. 다음 명령어로 필요한 모든 패키지를 설치할 수 있습니다:

```bash
pip install -r requirements.txt
```
