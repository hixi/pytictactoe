from pathlib import Path
from starlette.responses import HTMLResponse


# templates = Jinja2Templates(directory=Path('web_api/templates'))
# 
# async def homepage(request):
#     return templates.TemplateResponse('index.html', {'request': request})


async def homepage(request):
    index_page = Path('web_api/templates/index.html')
    with open(index_page, 'r') as page:
        content = page.read()
    return HTMLResponse(content)
