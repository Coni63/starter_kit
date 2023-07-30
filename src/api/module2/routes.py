from __future__ import annotations

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status


url_prefix = "module2"
openapi_tag = {
    "name": "Module 2",
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
async def get_all_items() -> list[dict]:
    all_objects = [{"n": i} for i in range(10)]
    return all_objects


@router.get("/{id}", tags=[openapi_tag["name"]])
async def get_item_by_id(id: int) -> dict:
    return {"n": id}


@router.post("/create/", tags=[openapi_tag["name"]], status_code=status.HTTP_201_CREATED)
async def read_item(new_item: int) -> dict:
    valid = new_item % 2 == 0
    if valid:
        return {"n": new_item}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="ERROR",
    )


@router.put("/update/{id}", tags=[openapi_tag["name"]], status_code=status.HTTP_200_OK)
async def update_item(id: int, new_item: int) -> dict:
    valid = new_item % 2 == 0
    if valid:
        return {"n": new_item}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="ERROR",
    )


@router.patch("/update/{id}", tags=[openapi_tag["name"]], status_code=status.HTTP_200_OK)
async def patch_item(id: int, new_item: int) -> dict:
    valid = new_item % 2 == 0
    if valid:
        return {"n": new_item}
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="ERROR",
    )


@router.delete("/detele/{id}", tags=[openapi_tag["name"]], status_code=status.HTTP_200_OK)
async def delete_item(id: int, new_item: int) -> bool:
    new_item += 1
    return True
