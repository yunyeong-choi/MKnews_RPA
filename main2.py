

#매일경제 뉴스 최근 2시간이내 기준, 인기뉴스 크롤링
from mknews_crw2 import best_To_Tuple
#best_To_Tuple() #return result : 리스트안 튜플값
btt=best_To_Tuple()

#크롤링 결과 db저장 후 df생성
from dbTodf import newsdb2df 
newsdb2df(btt)#return news_top10 :데이터프레임

#df을 html 로 로컬에 저장 
from save_html2 import df2html
news=newsdb2df(btt)
HTML_tb=df2html(news) # return : html 파일생성 후 꾸민 html테이블 리턴 

#HTML->이메일 전송
from email_sender import send_mail 
RPA_MAIL=send_mail('tinggunj@naver.com',['tinggunj@gmail.com','tinggunj@naver.com'],
    subject='[매일경제 오늘의 인기뉴스!]', content='최근 2시간이내 인기뉴스 목록입니다.\n\n'+'\n'+HTML_tb,
    attachments=[r'C:\Users\Choi\workspace\sesac\project1_crawring\yycrawler_package\mknews_best10.html'])

#카테고리별 뉴스 url->telegram 전송


