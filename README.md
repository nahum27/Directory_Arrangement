# Directory_Arrangement

> 볼링 영상이 어느덧 4000개에 달하였고 흩어져 있던 영상들을 정리하기 위해 만들었음.



**정리전 상황 **

![볼링영상_자동화_정리](https://user-images.githubusercontent.com/30791788/83547056-9edb1480-a53c-11ea-91c0-be457f46d25a.png)



> **3,957개의 정리 되지 않은 동영상들이 정신을 어지럽게 만든다.** 



**정리 후**

![정리후](https://user-images.githubusercontent.com/30791788/83548820-5cff9d80-a53f-11ea-810d-a5f60859a7a8.png)



> **정리 후 100개의 폴더에 파일들이 날짜에 맞게 옮겨 졌다.  앞으로 나의 볼링 영상 분석에 큰 도움을 줄 것이다**





### Usage

> workspace : 정리할 경로 입력
>
> sep : 파일이름의 패턴을 확인 하여 구분자 입력
>
> - ex) 20200601_124502.mp4 -> 구분자를 '_'로 설정시 20200601은 디렉토리 명이 된다. 
>
> **directory_arrangement([정리할 경로], [구분자])** 



### Def 설명

- make_directory

  > 폴더를 생성할 directory 명을 리스트로 받아 directory를 일괄 생성 한다.

- make_path

  > source 경로와(파일위치\파일명) 이동할 경로(move_path)를 생성한다

- list_file_move

  > dictionary의 key에 value는 list로 key는 move_path가 되고 value는 옮겨질 파일이 되어 정리를 실행한다. 

- directory_arrangement

  >    process를 실행하는 함수이다.
  >
  > 1. 구분자를 전달 받아 파일 패턴에 맞게 dictionary 생성
  > 2. 디렉토리 생성
  > 3. 파일 이동

- py 실행

  > work_space 설정 : 정리할 경로를 설정한다.
  >
  > sep 설정 : 패턴에 맞게 구분자를 설정한다. 



### To-Do

> 파일 TYPE, 용량에 따른 분류
>
> 병렬 실행
>
> 기계 학습으로 인한 다양한 정리 되지 않은 폴더 자동 정리. 하위 탐색 부터 자동 디렉토리명 생성 및 파일 이동



> **PS 혹시 먼저 정리 하신 분이 계시거나 아이디어를 얻었다면 같이 생각을 공유 하면서 성장하면 좋겠습니다.** 
