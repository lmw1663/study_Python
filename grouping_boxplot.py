import pandas as pd
import numpy as np
import featuretools as ft

# CSV 파일의 URL (GitHub raw 버전 링크 사용)
url = "https://raw.githubusercontent.com/WillKoehrsen/automated-feature-engineering/master/walk_through/data/loans.csv"

# CSV 파일을 데이터프레임으로 읽기
loans = pd.read_csv(url)

loans['loan_start'] = pd.to_datetime(loans['loan_start'], format='%Y-%m-%d')
loans['loan_end'] = pd.to_datetime(loans['loan_end'], format='%Y-%m-%d')
loansDf = pd.DataFrame(loans)

# Create new entityset
es = ft.EntitySet(id='clients')
print(loansDf.head())
print(loansDf.dtypes)
# clients DataFrame을 Entity로 변환하여 EntitySet에 추가
#es.add_dataframe(dataframe_name='clients', dataframe=loansDf, index='loan_id',time_index="loan_start")

print(es)
