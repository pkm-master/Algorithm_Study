# 11기 대전 2반 알고리즘 스터디

- SSAFY 11기 대전 2반 알고리즘 스터디입니다. 
- 주마다 풀이하는 문제 수는 문제의 난이도나 멤버들의 성장에 따라 변화할 수 있습니다.
- 현재 단계에서는 1주일에 3문제씩 진행합니다.
- 코드 리뷰와 문의는 MM으로 진행합니다.


## Members

|[![pkm-master](https://avatars.githubusercontent.com/u/156387263)](https://github.com/pkm-master)|[![gimhaen](https://avatars.githubusercontent.com/u/156387355)](https://github.com/gimhaen)|[![Psunmin](https://avatars.githubusercontent.com/u/81965009)](https://github.com/Psunmin)|[![pkm-master](https://avatars.githubusercontent.com/u/156387247)](https://github.com/cadetbluee)|
|:---:|:---:|:---:|:---:|
pkm-master|gimhaen|Psunmin|cadetbluee|
[![Dingurur](https://avatars.githubusercontent.com/u/155876321)](https://github.com/BYULNA-YUJINJANG)|[![baek-yak](https://avatars.githubusercontent.com/u/156387334)](https://github.com/baek-yak)|[![Ongyeom](https://avatars.githubusercontent.com/u/156387292)](https://github.com/Ongyeom)|
Dingurur|baek-yak|온겸|

## 문제 선정 기준
- 3개의  silver 등급 문제로 구성됩니다.
- 멤버들의 성장에 따라 문제 선정 기준은 변화할 수 있습니다.
  



## 참여 방법

### 기본 세팅

1. git clone을 통해 proejct 파일 받기
   ```bash
   git clone https://github.com/pkm-master/algorithm_study.git
   ```

2. Branch 생성
   ```bash
   git branch [브랜치명] master

   # exmaple
   # git branch pkm-master master
   ```

3. Branch로 이동하기
   ```bash
   git checkout [브랜치명]

   # example
   # git checkout pkm-master
   ```
4. ID로 된 폴더 생성
   ```bash
   mkdir [your_ID]

   # exmaple 
   # mkdir pkm-master
   ```

### 

### commit message 양식
   ```bash
   git commit -m "[your_ID] week[n]"

   # example
   # git commit -m "pkm-master week1" 
   ```

### 파일 이름 양식

파일 이름은 다음과 같은 양식을 따릅니다.

|Default word|Problem number|fail or success|
|------|---|---|
|problem| 푼 문제의 ID number|풀었는지, 풀지 못하였는지 여부|

- exmaple : 1024번 문제를 풀었을 경우 해당 파일의 이름
    ```python
    problem_1024_success.py
    ```
  




## 문제리스트

|주차|날짜|문제 1|문제 2|문제 3|
|:----:|:------:|:---:|:---:|:---:|
|1주차|02.06 - 02.12| [# 2669](https://www.acmicpc.net/problem/2669) |[# 2635](https://www.acmicpc.net/problem/2635)| [# 1463](https://www.acmicpc.net/problem/1463)
|2주차|02.13 - 02.19| [# 2628](https://www.acmicpc.net/problem/2628) |[# 1244](https://www.acmicpc.net/problem/1244)| [# 2149](https://www.acmicpc.net/problem/2149)
|3주차|02.20 - 02.26| [# 2116](https://www.acmicpc.net/problem/2116) |[# 2304](https://www.acmicpc.net/problem/2304)| [# 2559](https://www.acmicpc.net/problem/2559)


## Directory 구조
```MarkDown 
ALGORITHM_STUDY
├─name 1
│  └─week1
│       └─problem_{number1}_{success/fail}.py
│       └─problem_{number2}_{success/fail}.py
│       └─problem_{number3}_{success/fail}.py
│  └─ ...
├─ ... 
│  
└─name n
   └─week1
   └─week2
   └─ ...

```
