from __future__ import annotations

from app.{{cookiecutter.module_name}}.application.use_cases import basic_application
from app.{{cookiecutter.module_name}}.domain.item import Item
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status

url_prefix = "{{cookiecutter.module_name}}"
openapi_tag = {
    "name": "{{cookiecutter.module_title}}",
    "description": "Manage todos - CRUD operations",
    "externalDocs": {
        "description": "Items external docs",
        "url": "https://fastapi.tiangolo.com/",
    },
}

router = APIRouter(
    prefix=f"/{url_prefix}",
    tags=[openapi_tag["name"]],
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=[openapi_tag["name"]])
def get_all_items() -> list[dict]:
    return basic_application.get_all_items()


@router.get("/{id}", tags=[openapi_tag["name"]])
def get_item_by_id(id: int) -> dict:
    return basic_application.get_item_by_id(id)


@router.post("/create/", tags=[openapi_tag["name"]], status_code=status.HTTP_201_CREATED)
def create_item(item: Item) -> dict:
    try:
        return basic_application.create_item(item)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.put("/update/{id}", tags=[openapi_tag["name"]], status_code=status.HTTP_200_OK)
def update_item(id: int, new_item: Item) -> dict:
    try:
        return basic_application.update_item(id, new_item)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.patch("/update/{id}", tags=[openapi_tag["name"]], status_code=status.HTTP_200_OK)
def patch_item(id: int, new_item: Item) -> dict:
    try:
        return basic_application.patch_item(id, new_item)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete("/detele/{id}", tags=[openapi_tag["name"]], status_code=status.HTTP_200_OK)
def delete_item(id: int) -> bool:
    return basic_application.delete_item(id)
