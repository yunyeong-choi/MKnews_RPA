### MKnews_RPA : 매일경제 인기뉴스 RPA 패키지
-  <`22 SESAC 실무 프로젝트 기반 금융데이터 분석가 양성 과정> 내 RPA 프로젝트
<br>

#### :newspaper: 프로젝트 설명
> - 수행기간 : 2022.09.01 ~ 2022.09.23 (총 3주) <br>
> - 참여인원 : 개인 <br>
> - 기획의도 : **크롤링**한 뉴스들에 대한 **이메일 발송 자동화**와 유저가 원하는 카테고리별 뉴스에 대한 **텔레그램 발송 자동화**를 하나의 파이프라인으로 구현하고자 함 <br>
> - 활용 데이터 : 매일경제 웹 사이트 내 오늘의 인기뉴스 페이지 (https://www.mk.co.kr/news/ranking)
> - 활용 도구 및 언어 :![python badge](https://img.shields.io/badge/-Python-%23F7DF1E?style=plastic-square&logo=Python&logoColor=ffdd54&color=3776AB) ![mysql badge](https://img.shields.io/badge/-%20MySQL-%23F7DF1E?style=plastic-square&logo=mysql&logoColor=white&color=0F3460) ![AWS badge](https://img.shields.io/badge/-%20AWS%20ec2-%23F7DF1E?style=plastic-square&logo=amazonaws&logoColor=EF5B0C&color=FEF9A7) ![AWS badge](https://img.shields.io/badge/-%20AWS%20RDS-%23F7DF1E?style=plastic-square&logo=amazonaws&logoColor=EF5B0C&color=FEF9A7)
<p align="center">
<img src="https://user-images.githubusercontent.com/68022088/220157056-c146c785-823b-4b1c-8e6b-a387e3ff2595.png"  width="600" height="400" />
</p>
<br>

#### :mag: 패키지 구조
> **main2.py** : 메인 모듈<br><br>
> :one: Crawler : 데이터 크롤링 함수 &rightarrow; **mknews_crw2.py** <br>
> :two: DB_Load : DB 생성 및 추출 후 데이터프레임으로 출력하는 함수 &rightarrow; **dbTodf.py** <br>
> :three: RPA 
> - 데이터프레임을 html 테이블로 저장하는 함수 &rightarrow; **save_html2.py**
> - 저장한 html 테이블 파일을 이메일로 전송하는 함수 &rightarrow; **email_sender.py**
> - 저장한 html 테이블 파일 또는 원하는 카테고리별 뉴스 목록을 텔레그램으로 전송하는 함수 &rightarrow;
