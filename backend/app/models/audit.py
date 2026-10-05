from pydantic import BaseModel
from typing import Optional


class Ingredient(BaseModel):
    name: str
    normalized_name: Optional[str] = None
    code: Optional[str] = None


class Nutrition(BaseModel):
    serving_size: Optional[str] = None
    calories: Optional[float] = None
    protein_g: Optional[float] = None
    carbohydrates_g: Optional[float] = None
    sugar_g: Optional[float] = None
    fat_g: Optional[float] = None
    sodium_mg: Optional[float] = None


class Product(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None


class FSSAI(BaseModel):
    number: Optional[str] = None


class PackageInformation(BaseModel):
    product: Product
    ingredients: list[Ingredient]
    nutrition: Nutrition
    fssai: FSSAI
    claims: list[str]
    raw_text: Optional[str] = None