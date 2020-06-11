fake_db = {
    '/company/history': {
        'page_title':'Company history',
        'page_details':'details about company history',
    },
    '/company/employees': {
        'page_title':'Our Team',
        'page_details':'details about company employees',
    },
}

def get_page(url:str) -> dict:
    if not url:
        return {}

    url = url.strip().lower
    url = '/' + url('/')

    page = fake_db.get(url, {})
    return page