from __future__ import annotations

from api.module1 import routes as routes1
from api.module2 import routes as routes2
from fastapi import FastAPI

description = """
# INFORMATION

Describe what you API is supposed to be used to do.
"""

openapi_tags = [
    routes1.openapi_tag,
    routes2.openapi_tag,
]

app = FastAPI(
    title="TODO APP",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Author",
        "url": "https://www.foo.com/contact/",
        "email": "author@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=openapi_tags,
)

app.include_router(routes1.router)
app.include_router(routes2.router)
