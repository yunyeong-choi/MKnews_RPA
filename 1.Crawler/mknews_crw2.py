#크롤링 모듈만들기
import requests
from bs4 import BeautifulSoup

#카테고리별로 11개 인기뉴스 페이지 가져오기
#크롤링 함수 만들기
#for문으로 110개 기사 가져오는 동안 id_num으로 인덱스 110개 만들기
def best_To_Tuple()->bool:
    '''

  크롤링 결과를 출력하는 함수
   : DB저장을 위해 튜플로 반환 [(),()...]
  ---------------------------------------

  crawling_date : 크롤링한 날짜(%Y-%m-%d %H:%M)

  category_name :  11개의 뉴스 카테고리
  (뉴스종합, 경제, 기업, 사회, 국제, 부동산,
   증권, 정치, IT과학, 문화, 스포츠)  

   ranking: 순위 (1~10위) 

   title : 기사제목
   
   top10_url : 뉴스기사 링크

   register_date : '등록일' 뉴스기사 등록일

  -------------------------------------


    '''

    top10_categories = ['all','economy','business','society','world','realestate','stock',
 'politics','it','culture','sports']

    result=[]
    for i in range(11):
        main_url='https://www.mk.co.kr/news/ranking/'
        category_url=top10_categories[i]
        tot_category_url=main_url+category_url
        res=requests.get(tot_category_url)
        soup=BeautifulSoup(res.content,'html.parser')
        category_name=soup.select_one(".nav_link.tab_item.is_active").text.strip()
        top10_news= soup.select(".popular_top_node.news_node.col.col_x5")
        
        #여러 파일 요청시 파일명 중복 가능->크롤링한 날짜 및 시간 받아오기
        #date=soup.select_one('#datepicker')['value'] #str ->'오늘, 현재, 지금' 뉴스만 크롤링할 것이므로 불필요할듯.


    #인기뉴스 10개씩 가져오기    
        ranking=0 #순위 기본값 지정
        for news in top10_news:
            #1~10 순위 ranking(int) 생성
            ranking+=1
            
            title= news.select_one(".news_ttl").text #기사 제목
            
            top10_url=news.select_one(".news_item.type_thumb")['href'] #기사 url
            # 기사url 활성화를 위해 http없을 경우, http삽입
            if top10_url.startswith('http'):
                top10_url=top10_url
            else :
                top10_url='http:'+top10_url

            news_res=requests.get(top10_url) #개별기사 url 파싱
            news_soup=BeautifulSoup(news_res.content,'html.parser')
            #description=news_soup.select_one(".news_cnt_detail_wrap").text.strip()#기사내용->본 rpa프로젝트에선 불필요.
            register_date=news_soup.select_one('.registration dd').text.strip()#기사 등록일 <dd>태그

            
            #오늘날짜,시간활용해서 추출일시 추출(2시간마다 실시간 인기뉴스 변동되므로)
            from datetime import datetime
            today_date=datetime.today()
            crawling_date=today_date.strftime('%Y-%m-%d %H:%M')
            
            temp=(ranking,crawling_date,category_name,title,top10_url,register_date)
            result.append(temp)
            

    print('크롤링 성공!')
    print('크롤링한 날짜는 '+ crawling_date +' 입니다.')
 

    return result

if __name__=='__main_ _':
  best_To_Tuple()