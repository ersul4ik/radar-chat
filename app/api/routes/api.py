from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from core import config
from services.charts import create_radar_chart
from services.extract import extract_data_from_file

router = APIRouter(prefix="/v1")


@router.get(
    "/chart",
    name="chars:get-data",
    response_class=HTMLResponse,
)
async def get_chart():
    data = extract_data_from_file(config.TECH_RADAR_FILE_PATH)
    chart_html = create_radar_chart(data)
    html_content = f"""
    <html>
        <head>
            <title>Radar Chart</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
        <body>
            <h1>Radar Chart</h1>
            {chart_html}
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
