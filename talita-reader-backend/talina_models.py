from dataclasses import dataclass, field
from decimal import Decimal

@dataclass
class TalinaExtremityResultDTO:
    fat_porcentage: Decimal = field(default=None)
    fat_mass: Decimal = field(default=None)
    fat_free_porcentage: Decimal = field(default=None)
    fat_free_mass: Decimal = field(default=None)
    muscle_mass: Decimal = field(default=None)
    fat_score: str = field(default=None)
    muscle_score: str = field(default=None)
    total_mass: Decimal = field(default=None)

@dataclass
class TalinaSegmentalResultsDTO:
    left_leg: TalinaExtremityResultDTO = field(default=None)
    right_leg: TalinaExtremityResultDTO = field(default=None)
    left_arm: TalinaExtremityResultDTO = field(default=None)
    right_arm: TalinaExtremityResultDTO = field(default=None)
    trunk: TalinaExtremityResultDTO = field(default=None)
    leg_balance: str = field(default=None)
    arm_balance: str = field(default=None)

@dataclass
class TalinaDesirableDTO:
    min_weight: Decimal = field(default=None)
    max_weight: Decimal = field(default=None)
    min_fat_porcentage: Decimal = field(default=None)
    max_fat_porcentage: Decimal = field(default=None)
    min_fat_mass: Decimal = field(default=None)
    max_fat_mass: Decimal = field(default=None)
    min_bmi: Decimal = field(default=None)
    max_bmi: Decimal = field(default=None)

@dataclass
class TalinaMeasuresDTO:
    chest: Decimal = field(default=None)
    high_waist: Decimal = field(default=None)
    low_waist: Decimal = field(default=None)
    high_hip: Decimal = field(default=None)
    low_hip: Decimal = field(default=None)
    right_arm: Decimal = field(default=None)
    lef_arm: Decimal = field(default=None)
    legs: Decimal = field(default=None)

@dataclass
class TalinaResultsDTO:
    weight: Decimal = field(default=None)
    body_mass_index: Decimal = field(default=None)
    body_fat: Decimal = field(default=None)
    body_fat_mass: Decimal = field(default=None)
    body_fat_category: str = field(default=None)
    fat_free_mass: Decimal = field(default=None)
    viceral_fat_rating: Decimal = field(default=None)
    water_porcentage: Decimal = field(default=None)
    water_mass: Decimal = field(default=None)
    muscle_mass: Decimal = field(default=None)
    muscle_mass_score: str = field(default=None)
    leg_muscle_score: int = field(default=None)
    bone_mass: Decimal = field(default=None)
    smi_score: Decimal = field(default=None)
    smi_score_label: str = field(default=None)
    protein: Decimal = field(default=None)
    basal_metabolic_rate: Decimal = field(default=None)
    basal_metabolic_rate_label: str = field(default=None)
    metabolic_age: Decimal = field(default=None)
    daily_calorie_intake: Decimal = field(default=None)
    physique_rating: str = field(default=None)
    segmentalInfo: TalinaSegmentalResultsDTO = field(default=None)
    desirableData: TalinaDesirableDTO = field(default=None)
    comments: str = field(default=None)
    measures: TalinaMeasuresDTO = field(default=None)

@dataclass
class TalinaDataDTO:
    id: str = field(default=None)
    date: str = field(default=None)
    name: str = field(default=None)
    age: int = field(default=None)
    gender: str = field(default=None)
    height: Decimal = field(default=None)
    results: TalinaResultsDTO = field(default=None)