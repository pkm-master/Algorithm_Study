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
|4주차|02.27 - 03.04| [# 2578](https://www.acmicpc.net/problem/2578) |[# 2527](https://www.acmicpc.net/problem/2527)| [# 17281](https://www.acmicpc.net/problem/17281)
|5주차|03.05 - 03.11| [# 10157](https://www.acmicpc.net/problem/10157) |[# 10158](https://www.acmicpc.net/problem/10158)| [# 10163](https://www.acmicpc.net/problem/10163)
|6주차|03.12 - 03.18| [# 12100](https://www.acmicpc.net/problem/12100) |[# 15683](https://www.acmicpc.net/problem/15683)| [# 17471](https://www.acmicpc.net/problem/17471)
|7주차|03.19 - 03.25| [# 17779](https://www.acmicpc.net/problem/17779) |[# 16637](https://www.acmicpc.net/problem/16637)| [# 16235](https://www.acmicpc.net/problem/16235)
|8주차|03.26 - 04.01| [# 17472](https://www.acmicpc.net/problem/17472) |[# 15685](https://www.acmicpc.net/problem/15685)| [# 14503](https://www.acmicpc.net/problem/14503)
|9주차|04.02 - 04.08| [# 21610](https://www.acmicpc.net/problem/21610) |[# 20057](https://www.acmicpc.net/problem/20057)| [# 21611](https://www.acmicpc.net/problem/21611)
|10주차|04.09 - 04.15| [# 20056](https://www.acmicpc.net/problem/20056) |[# 20058](https://www.acmicpc.net/problem/20058)| [# 17144](https://www.acmicpc.net/problem/17144)
|11주차|04.16 - 04.22| [# 17406](https://www.acmicpc.net/problem/17406) |[# 15684](https://www.acmicpc.net/problem/15684)| [# 17136](https://www.acmicpc.net/problem/17136)
|13주차|04.30 - 05.06| [# 14889](https://www.acmicpc.net/problem/14889) |[# 16236](https://www.acmicpc.net/problem/16236)| [# 19237](https://www.acmicpc.net/problem/19237)
|14주차|05.07 - 05.13| [# 14502](https://www.acmicpc.net/problem/14502) |[# 17141](https://www.acmicpc.net/problem/17141)| [# 17142](https://www.acmicpc.net/problem/17142)

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
