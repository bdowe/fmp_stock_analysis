import pandas as pd
import requests as re
import config


def get_stats(ticker: str) -> pd.DataFrame:
    api_key = config.fmp['api_key']
    ticker = ticker.upper()

    resp_is = re.get(f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit=120&apikey={api_key}').json()
    resp_is = pd.DataFrame(resp_is, columns=['date', 'revenue', 'netIncome', 'operatingIncome'])

    resp_bs = re.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit=120&apikey={api_key}').json()
    resp_bs = pd.DataFrame(resp_bs, columns=['date', 'totalStockholdersEquity', 'totalLiabilities', 'longTermDebt'])

    resp_cf = re.get(f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit=120&apikey={api_key}').json()
    resp_cf = pd.DataFrame(resp_cf, columns=['date', 'dividendsPaid'])
    resp_cf['dividendsPaid'] = -resp_cf['dividendsPaid']

    df = resp_is.merge(resp_bs, on='date').merge(resp_cf, on='date')

    df['Equity+Dividends'] = df['totalStockholdersEquity'] + df['dividendsPaid']
    
    df['roe'] = df['netIncome'] / df['totalStockholdersEquity']
    df['roic'] = df['netIncome'] / (df['totalStockholdersEquity'] + df['longTermDebt'])

    cols = ['revenue', 'netIncome', 'operatingIncome', 'Equity+Dividends']
    cols_yoy = [col + '_yoy' for col in cols]

    df[cols_yoy] = (df[cols] - df[cols].shift(-1)) / abs(df[cols].shift(-1))

    return df



    
        
