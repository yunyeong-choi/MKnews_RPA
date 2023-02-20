import pandas as pd

def df2html(news_top10):
    '''
    불러온 뉴스 데이터프레임{newsdb2df}의
    {news_top10}을 html으로 저장하는 함수
    input : news_top10
    output : news_html(html테이블)

    뉴스기사 링크 활성화를 위해 escape문을 조정함(escape=False)
    '''

    news_top10['url'] = '<a target="_blank" href='+news_top10['url']+'>'+news_top10['url']+'</a>'
    news_top10.to_html('today_mk_Best.html',header=True, index=True, justify='center',border=2,escape=False) #가운데정렬 및 열공간, 헤더, 인덱스 지정
    print('뉴스 데이터프레임 html으로 저장 성공!')
    
    news_html=open('today_mk_Best.html',encoding='utf-8').read() #로컬에 저장한 html테이블 불러오기
    
    # 불러온 news_html 파일 꾸며서 'mknews_best10.html'로 저장 
    HTMLFILE = open('mknews_best10.html', 'w') # 비어있는 html파일 만들기
    HTML_1 = """
    <h1 style="color:brown; text-align:center"> 매일경제 인기뉴스 Top10 </h1>
    """
    news_html_3 = news_html.replace('<table border="2" class="dataframe">', '<table style="border:0; cellpadding:2; height:400; font-size:20; bordercolor:white; class:dataframe">')#table line
    news_html_3 = news_html_3.replace('<td>','<td bgcolor=#FDEEDC>')#table color #cellpadding셀간격
    news_html_3 = news_html_3.replace('<th>','<th  height="20" bgcolor=#E38B29>') #header,index color

  
    # HTML 과 만들어둔 HTML TABLE 결합
    ALL_HTML = HTML_1 + news_html_3 #html 뉴스 테이블 

    # 꾸민 html파일 저장 : mknews_best10.html
    HTMLFILE.write(ALL_HTML)
    
    print('뉴스 테이블 html 불러오기 성공!')

    return ALL_HTML
    

if __name__=='__main_ _':
  df2html(news_top10)
