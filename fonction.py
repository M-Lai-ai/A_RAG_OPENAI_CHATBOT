import requests
from typing import Optional, Dict, Union
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
FMP_API_KEY = os.getenv('FMP_API_KEY')

def get_stock_info(symbol: str) -> Dict[str, Union[str, float]]:
    """
    Obtient les informations détaillées d'une action.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        Dict: Informations détaillées sur l'action
    """
    base_url = "https://financialmodelingprep.com/api/v3/profile/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        
        data = response.json()
        if not data:
            return {"error": f"Aucune donnée trouvée pour {symbol}"}
        
        stock_data = data[0]
        return {
            "companyName": stock_data.get("companyName", "N/A"),
            "price": stock_data.get("price", "N/A"),
            "currency": stock_data.get("currency", "USD"),
            "exchange": stock_data.get("exchange", "N/A"),
            "industry": stock_data.get("industry", "N/A"),
            "description": stock_data.get("description", "N/A"),
            "sector": stock_data.get("sector", "N/A"),
            "ceo": stock_data.get("ceo", "N/A"),
            "website": stock_data.get("website", "N/A"),
            "marketCap": stock_data.get("mktCap", "N/A")
        }
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur lors de la requête API: {str(e)}"}

def search_stocks(query: str, limit: int = 10, exchange: str = "NASDAQ") -> List[Dict]:
    """
    Recherche des actions par nom ou symbole.
    
    Args:
        query (str): Terme de recherche
        limit (int): Nombre maximum de résultats
        exchange (str): Bourse spécifique
    
    Returns:
        List[Dict]: Liste des actions correspondantes
    """
    base_url = "https://financialmodelingprep.com/api/v3/search"
    
    try:
        response = requests.get(
            base_url,
            params={
                'query': query,
                'limit': limit,
                'exchange': exchange,
                'apikey': FMP_API_KEY
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la recherche: {str(e)}"}]

def get_stock_quote(symbol: str) -> Dict:
    """
    Obtient le cours actuel et les informations de base d'une action.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        Dict: Informations sur le cours de l'action
    """
    base_url = "https://financialmodelingprep.com/api/v3/quote/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        data = response.json()
        return data[0] if data else {"error": "Aucune donnée de cours trouvée"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur lors de la requête: {str(e)}"}

def get_stock_price_change(symbol: str) -> Dict:
    """
    Obtient les variations de prix sur différentes périodes.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        Dict: Variations de prix sur différentes périodes
    """
    base_url = "https://financialmodelingprep.com/api/v3/stock-price-change/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        data = response.json()
        return data[0] if data else {"error": "Aucune donnée de variation trouvée"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur lors de la requête: {str(e)}"}

def get_financial_statements(symbol: str, statement_type: str = "income", period: str = "annual") -> List[Dict]:
    """
    Obtient les états financiers d'une entreprise.
    
    Args:
        symbol (str): Symbole de l'action
        statement_type (str): Type d'état financier ('income', 'balance', 'cash')
        period (str): Période ('annual' ou 'quarter')
    
    Returns:
        List[Dict]: États financiers
    """
    statement_types = {
        "income": "income-statement",
        "balance": "balance-sheet-statement",
        "cash": "cash-flow-statement"
    }
    
    base_url = f"https://financialmodelingprep.com/api/v3/{statement_types.get(statement_type, 'income-statement')}/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={
                'period': period,
                'apikey': FMP_API_KEY
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

def get_key_metrics(symbol: str, period: str = "annual") -> List[Dict]:
    """
    Obtient les métriques clés d'une entreprise.
    
    Args:
        symbol (str): Symbole de l'action
        period (str): Période ('annual' ou 'quarter')
    
    Returns:
        List[Dict]: Métriques clés
    """
    base_url = "https://financialmodelingprep.com/api/v3/key-metrics/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={
                'period': period,
                'apikey': FMP_API_KEY
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

def get_financial_ratios(symbol: str, period: str = "annual") -> List[Dict]:
    """
    Obtient les ratios financiers d'une entreprise.
    
    Args:
        symbol (str): Symbole de l'action
        period (str): Période ('annual' ou 'quarter')
    
    Returns:
        List[Dict]: Ratios financiers
    """
    base_url = "https://financialmodelingprep.com/api/v3/ratios/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={
                'period': period,
                'apikey': FMP_API_KEY
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

def get_company_outlook(symbol: str) -> Dict:
    """
    Obtient une vue d'ensemble complète de l'entreprise.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        Dict: Vue d'ensemble de l'entreprise
    """
    base_url = "https://financialmodelingprep.com/api/v4/company-outlook/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur lors de la requête: {str(e)}"}

def get_stock_peers(symbol: str) -> List[str]:
    """
    Obtient la liste des entreprises similaires.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        List[str]: Liste des symboles d'entreprises similaires
    """
    base_url = "https://financialmodelingprep.com/api/v4/stock_peers/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        data = response.json()
        return data[0].get('peersList', []) if data else []
    except requests.exceptions.RequestException as e:
        return [f"Erreur lors de la requête: {str(e)}"]

def get_company_notes(symbol: str) -> List[Dict]:
    """
    Obtient les notes d'entreprise.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        List[Dict]: Notes d'entreprise
    """
    base_url = "https://financialmodelingprep.com/api/v4/company-notes/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

def get_key_executives(symbol: str) -> List[Dict]:
    """
    Obtient les informations sur les dirigeants clés.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        List[Dict]: Informations sur les dirigeants
    """
    base_url = "https://financialmodelingprep.com/api/v3/key-executives/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

def get_market_cap(symbol: str) -> Dict:
    """
    Obtient la capitalisation boursière actuelle.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        Dict: Capitalisation boursière
    """
    base_url = "https://financialmodelingprep.com/api/v3/market-capitalization/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        data = response.json()
        return data[0] if data else {"error": "Aucune donnée de capitalisation trouvée"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur lors de la requête: {str(e)}"}

def get_financial_growth(symbol: str, period: str = "annual") -> List[Dict]:
    """
    Obtient les métriques de croissance financière.
    
    Args:
        symbol (str): Symbole de l'action
        period (str): Période ('annual' ou 'quarter')
    
    Returns:
        List[Dict]: Métriques de croissance
    """
    base_url = "https://financialmodelingprep.com/api/v3/financial-growth/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={
                'period': period,
                'apikey': FMP_API_KEY
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

def get_company_score(symbol: str) -> Dict:
    """
    Obtient le score de l'entreprise.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        Dict: Score de l'entreprise
    """
    base_url = "https://financialmodelingprep.com/api/v4/score"
    
    try:
        response = requests.get(
            base_url,
            params={
                'symbol': symbol,
                'apikey': FMP_API_KEY
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur lors de la requête: {str(e)}"}

def get_dcf_analysis(symbol: str) -> Dict:
    """
    Obtient l'analyse DCF (Discounted Cash Flow).
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        Dict: Analyse DCF
    """
    base_url = "https://financialmodelingprep.com/api/v3/discounted-cash-flow/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        return response.json()[0] if response.json() else {"error": "Aucune donnée DCF trouvée"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Erreur lors de la requête: {str(e)}"}

def get_stock_news(symbol: str, from_date: str, to_date: str, page: int = 0) -> List[Dict]:
    """
    Obtient les actualités liées à l'action.
    
    Args:
        symbol (str): Symbole de l'action
        from_date (str): Date de début (YYYY-MM-DD)
        to_date (str): Date de fin (YYYY-MM-DD)
        page (int): Numéro de page
    
    Returns:
        List[Dict]: Actualités
    """
    base_url = "https://financialmodelingprep.com/api/v3/stock_news"
    
    try:
        response = requests.get(
            base_url,
            params={
                'tickers': symbol,
                'from': from_date,
                'to': to_date,
                'page': page,
                'apikey': FMP_API_KEY
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

def get_earnings_calendar(symbol: str) -> List[Dict]:
    """
    Obtient le calendrier des résultats.
    
    Args:
        symbol (str): Symbole de l'action
    
    Returns:
        List[Dict]: Calendrier des résultats
    """
    base_url = "https://financialmodelingprep.com/api/v3/historical/earning_calendar/"
    
    try:
        response = requests.get(
            f"{base_url}{symbol}",
            params={'apikey': FMP_API_KEY}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Erreur lors de la requête: {str(e)}"}]

SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

def google_search(query: str, domain: str = "google.com", country: str = "us", language: str = "en") -> Dict:
    """
    Effectue une recherche Google générale.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google',
        'q': query,
        'google_domain': domain,
        'gl': country,
        'hl': language
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_jobs_search(query: str, domain: str = "google.com") -> Dict:
    """
    Recherche des offres d'emploi sur Google Jobs.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_jobs',
        'google_domain': domain,
        'q': query
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_shopping_search(query: str, domain: str = "google.com") -> Dict:
    """
    Recherche des produits sur Google Shopping.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_shopping',
        'google_domain': domain,
        'q': query
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_news_search(language: str = "en", country: str = "us") -> Dict:
    """
    Recherche des actualités sur Google News.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_news',
        'hl': language,
        'gl': country
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_trends_search(query: str) -> Dict:
    """
    Recherche des tendances sur Google Trends.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_trends',
        'q': query
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_scholar_search(query: str, language: str = "en") -> Dict:
    """
    Recherche des articles académiques sur Google Scholar.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_scholar',
        'q': query,
        'hl': language
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_events_search(query: str, language: str = "en", country: str = "us") -> Dict:
    """
    Recherche des événements sur Google Events.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_events',
        'q': query,
        'hl': language,
        'gl': country
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_flights_search(
    departure: str,
    arrival: str,
    outbound_date: str,
    return_date: str,
    language: str = "en",
    country: str = "us"
) -> Dict:
    """
    Recherche des vols sur Google Flights.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_flights',
        'hl': language,
        'gl': country,
        'departure_id': departure,
        'arrival_id': arrival,
        'outbound_date': outbound_date,
        'return_date': return_date
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_hotels_search(
    query: str,
    check_in: str,
    check_out: str,
    language: str = "en"
) -> Dict:
    """
    Recherche des hôtels sur Google Hotels.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_hotels',
        'q': query,
        'hl': language,
        'check_in_date': check_in,
        'check_out_date': check_out
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def google_food_search(query: str, language: str = "en") -> Dict:
    """
    Recherche de nourriture sur Google Food.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'google_food',
        'q': query,
        'hl': language
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def apple_app_store_search(term: str, page: int = 0, num: int = 10) -> Dict:
    """
    Recherche des applications sur l'App Store d'Apple.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'apple_app_store',
        'term': term,
        'page': page,
        'num': num
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def youtube_search(query: str) -> Dict:
    """
    Recherche des vidéos sur YouTube.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'youtube',
        'search_query': query
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()

def ebay_search(query: str) -> Dict:
    """
    Recherche des produits sur eBay.
    """
    params = {
        'api_key': SERPAPI_API_KEY,
        'engine': 'ebay',
        '_nkw': query
    }
    
    response = requests.get('https://serpapi.com/search', params=params)
    return response.json()
    
# Mise à jour du dictionnaire des fonctions disponibles
functions_dict = {
    1: {
        "description": "Obtenir les informations détaillées d'une action",
        "parameters": {"symbol": "str - symbole de l'action (ex: AAPL)"},
        "function": get_stock_info
    },
    2: {
        "description": "Rechercher des actions par nom ou symbole",
        "parameters": {
            "query": "str - terme de recherche",
            "limit": "int - nombre max de résultats (défaut: 10)",
            "exchange": "str - bourse (défaut: NASDAQ)"
        },
        "function": search_stocks
    },
    3: {
        "description": "Obtenir le cours actuel d'une action",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_stock_quote
    },
    4: {
        "description": "Obtenir les variations de prix",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_stock_price_change
    },
    5: {
        "description": "Obtenir les états financiers",
        "parameters": {
            "symbol": "str - symbole de l'action",
            "statement_type": "str - type d'état ('income', 'balance', 'cash')",
            "period": "str - période ('annual' ou 'quarter')"
        },
        "function": get_financial_statements
    },
    6: {
        "description": "Obtenir les métriques clés",
        "parameters": {
            "symbol": "str - symbole de l'action",
            "period": "str - période ('annual' ou 'quarter')"
        },
        "function": get_key_metrics
    },
    7: {
        "description": "Obtenir les ratios financiers",
        "parameters": {
            "symbol": "str - symbole de l'action",
            "period": "str - période ('annual' ou 'quarter')"
        },
        "function": get_financial_ratios
    },
    8: {
        "description": "Obtenir la vue d'ensemble de l'entreprise",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_company_outlook
    },
    9: {
        "description": "Obtenir les entreprises similaires",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_stock_peers
    },
    10: {
        "description": "Obtenir les notes d'entreprise",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_company_notes
    },
    11: {
        "description": "Obtenir les informations sur les dirigeants",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_key_executives
    },
    12: {
        "description": "Obtenir la capitalisation boursière",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_market_cap
    },
    13: {
        "description": "Obtenir les métriques de croissance financière",
        "parameters": {
            "symbol": "str - symbole de l'action",
            "period": "str - période ('annual' ou 'quarter')"
        },
        "function": get_financial_growth
    },
    14: {
        "description": "Obtenir le score de l'entreprise",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_company_score
    },
    15: {
        "description": "Obtenir l'analyse DCF",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_dcf_analysis
    },
    16: {
        "description": "Obtenir les actualités de l'action",
        "parameters": {
            "symbol": "str - symbole de l'action",
            "from_date": "str - date de début (YYYY-MM-DD)",
            "to_date": "str - date de fin (YYYY-MM-DD)",
            "page": "int - numéro de page (défaut: 0)"
        },
        "function": get_stock_news
    },
    17: {
        "description": "Obtenir le calendrier des résultats",
        "parameters": {"symbol": "str - symbole de l'action"},
        "function": get_earnings_calendar
    },
    18: {
        "description": "Recherche Google générale",
        "parameters": {
            "query": "str - terme de recherche",
            "domain": "str - domaine Google (défaut: google.com)",
            "country": "str - code pays (défaut: us)",
            "language": "str - code langue (défaut: en)"
        },
        "function": google_search
    },
    19: {
        "description": "Recherche d'emplois Google Jobs",
        "parameters": {
            "query": "str - terme de recherche",
            "domain": "str - domaine Google (défaut: google.com)"
        },
        "function": google_jobs_search
    },
    20: {
        "description": "Recherche Google Shopping",
        "parameters": {
            "query": "str - terme de recherche",
            "domain": "str - domaine Google (défaut: google.com)"
        },
        "function": google_shopping_search
    },
    21: {
        "description": "Recherche Google News",
        "parameters": {
            "language": "str - code langue (défaut: en)",
            "country": "str - code pays (défaut: us)"
        },
        "function": google_news_search
    },
    22: {
        "description": "Recherche Google Trends",
        "parameters": {
            "query": "str - terme de recherche"
        },
        "function": google_trends_search
    },
    23: {
        "description": "Recherche Google Scholar",
        "parameters": {
            "query": "str - terme de recherche",
            "language": "str - code langue (défaut: en)"
        },
        "function": google_scholar_search
    },
    24: {
        "description": "Recherche Google Events",
        "parameters": {
            "query": "str - terme de recherche",
            "language": "str - code langue (défaut: en)",
            "country": "str - code pays (défaut: us)"
        },
        "function": google_events_search
    },
    25: {
        "description": "Recherche Google Flights",
        "parameters": {
            "departure": "str - aéroport de départ (code IATA)",
            "arrival": "str - aéroport d'arrivée (code IATA)",
            "outbound_date": "str - date aller (YYYY-MM-DD)",
            "return_date": "str - date retour (YYYY-MM-DD)",
            "language": "str - code langue (défaut: en)",
            "country": "str - code pays (défaut: us)"
        },
        "function": google_flights_search
    },
    26: {
        "description": "Recherche Google Hotels",
        "parameters": {
            "query": "str - terme de recherche",
            "check_in": "str - date d'arrivée (YYYY-MM-DD)",
            "check_out": "str - date de départ (YYYY-MM-DD)",
            "language": "str - code langue (défaut: en)"
        },
        "function": google_hotels_search
    },
    27: {
        "description": "Recherche Google Food",
        "parameters": {
            "query": "str - terme de recherche",
            "language": "str - code langue (défaut: en)"
        },
        "function": google_food_search
    },
    28: {
        "description": "Recherche Apple App Store",
        "parameters": {
            "term": "str - terme de recherche",
            "page": "int - numéro de page (défaut: 0)",
            "num": "int - nombre de résultats (défaut: 10)"
        },
        "function": apple_app_store_search
    },
    29: {
        "description": "Recherche YouTube",
        "parameters": {
            "query": "str - terme de recherche"
        },
        "function": youtube_search
    },
    30: {
        "description": "Recherche eBay",
        "parameters": {
            "query": "str - terme de recherche"
        },
        "function": ebay_search
    }
}
