from fastapi import APIRouter, HTTPException, status
from beanie import PydanticObjectId
from typing import List
from models.contact import Contact, CreateContactModel, UpdateContactModel, PinContactModel

router = APIRouter(prefix="/api/contacts",tags=["Contacts"])

@router.get("/", response_model=List[Contact])

async def get_all_contacts():
    """ 获取所有联系人。"""
    contacts = await Contact.find_all().sort([("is_pinned", -1), ("name", 1)]).to_list()
    return contacts


@router.post("/", response_model=Contact, status_code=status.HTTP_201_CREATED)
async def add_contact(contact_data: CreateContactModel):
    """ 创建一个新联系人。 """
    # 将输入的 Pydantic 模型 转换为 数据库 Document 模型
    new_contact = Contact(**contact_data.model_dump())
    await new_contact.insert()
    return new_contact

@router.put("/{id}", response_model=Contact)
async def update_contact(id: PydanticObjectId,contact_update: UpdateContactModel):
    """ 根据 ID 更新一个已存在的联系人。 """
    # 1. 从数据库读取
    contact_to_update = await Contact.get(id)
    if not contact_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"ID 为 {id} 的联系人不存在。")

    update_data = contact_update.model_dump(exclude_none=True)

    await contact_to_update.update({"$set": update_data})

    updated_contact = await Contact.get(id)
    return updated_contact


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(id: PydanticObjectId):
    """根据 ID 删除一个联系人。"""

    contact_to_delete = await Contact.get(id)
    if not contact_to_delete: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"ID 为 {id} 的联系人不存在。")

    await contact_to_delete.delete()
    return None  # 204 No Content

@router.put("/{id}/pin", response_model=Contact)
async def toggle_pin_contact(id: PydanticObjectId, pin_data: PinContactModel):
    """ 专门用于切换联系人的置顶状态。 """
    contact_to_pin = await Contact.get(id)

    if not contact_to_pin:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"ID 为 {id} 的联系人不存在。"
        )

    # 更新置顶状态
    await contact_to_pin.update({"$set": {"is_pinned": pin_data.is_pinned}})

    updated_contact = await Contact.get(id)
    return updated_contact

@router.get("/groups", response_model=List[str])
async def get_all_groups():
    """ 获取所有不重复的、非空的分组名称列表。 """
    # distinct() 会返回一个包含所有 'group' 字段唯一值的列表
    all_groups = await Contact.distinct("group")


    # 过滤掉 None 或空字符串
    valid_groups = [group for group in all_groups if group]
    return valid_groups