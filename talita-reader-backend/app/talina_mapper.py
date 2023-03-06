from talina_models import TalinaDataDTO, TalinaResultsDTO, TalinaSegmentalResultsDTO, TalinaExtremityResultDTO, TalinaDesirableDTO, TalinaMeasuresDTO
from decimal import Decimal
import re

# Procesa el objeto principal
def process_data(pdfText: str) -> TalinaDataDTO:
    splitedText = pdfText.split("\n")

    response = TalinaDataDTO()
    response.name = splitedText[0]
    response.id = splitedText[1]
    response.age = get_number(splitedText[2])[0]
    response.gender = remove_numbers(splitedText[2])
    response.height = get_height(splitedText[3])
    response.date = splitedText[4]
    response.results = process_results(splitedText)

    return response

# Procesa el objeto de resultados
def process_results(splitedText: list) -> TalinaResultsDTO:
    response = TalinaResultsDTO()
    index_start = find_first_lb(splitedText)

    if(index_start > 0):
        response.weight = get_number(splitedText[index_start])[0]
        response.body_mass_index = get_number(splitedText[index_start + 1])[0]
        response.body_fat = get_number(splitedText[index_start + 2])[0]
        response.body_fat_mass = get_number(splitedText[index_start + 3])[0]
        response.body_fat_category = splitedText[index_start + 4]
        response.fat_free_mass = get_number(splitedText[index_start + 5])[0]
        response.viceral_fat_rating = get_number(splitedText[index_start + 6])[0]
        response.water_porcentage = get_number(splitedText[index_start + 7])[0]
        response.water_mass = get_number(splitedText[index_start + 8])[0]
        response.muscle_mass = get_number(splitedText[index_start + 9])[0]
        response.muscle_mass_score = splitedText[index_start + 10]
        response.leg_muscle_score = get_number(splitedText[index_start + 11])[0]
        response.bone_mass = get_number(splitedText[index_start + 12])[0]
        response.smi_score = get_number(splitedText[index_start + 13])[0]
        response.smi_score_label = remove_numbers(splitedText[index_start + 13])
        response.protein = get_number(splitedText[index_start + 14])[0]
        response.basal_metabolic_rate = get_number(splitedText[index_start + 15])[0]
        response.basal_metabolic_rate_label = remove_numbers(splitedText[index_start + 16])
        response.metabolic_age = get_number(splitedText[index_start + 17])[0]
        response.daily_calorie_intake = get_number(splitedText[index_start + 18])[0]
        response.physique_rating = splitedText[index_start + 19]
        response.segmentalInfo = process_segmental_results(splitedText, index_start + 20)
        response.desirableData = process_desirable_results(splitedText,  index_start + 50)
        response.comments = joinElementsByIdex(splitedText, 6, index_start)
        response.measures = processMeasures(response.comments)

    return response

# Procesa el objeto TalinaSegmentalResultsDTO
def process_segmental_results(splitedText: list, index_start: int) -> TalinaSegmentalResultsDTO:
    response = TalinaSegmentalResultsDTO()
    
    response.left_leg = process_extremity_results(splitedText, index_start)
    response.right_leg = process_extremity_results(splitedText, index_start + 1)
    response.left_arm = process_extremity_results(splitedText, index_start + 2)
    response.right_arm = process_extremity_results(splitedText, index_start + 3)
    response.trunk = process_extremity_results(splitedText, index_start + 4)
    response.leg_balance = calculate_balance(response.left_leg.fat_mass, response.right_leg.fat_mass)
    response.arm_balance = calculate_balance(response.left_arm.fat_mass, response.right_arm.fat_mass)
   
    return response

#Procesa una extremidad TalinaExtremityResultDTO
def process_extremity_results(splitedText: list, index_start: int) -> TalinaExtremityResultDTO:
    response = TalinaExtremityResultDTO()

    response.fat_porcentage = float(get_number(splitedText[index_start])[0])
    response.fat_mass = float(get_number(splitedText[index_start + 5])[0])
    response.fat_free_mass = float(get_number(splitedText[index_start + 10])[0])
    response.muscle_mass = float(get_number(splitedText[index_start + 15])[0])
    response.fat_score = splitedText[index_start + 20]
    response.muscle_score = splitedText[index_start + 25]

    # Calculadas
    response.fat_free_porcentage = round(100 - response.fat_porcentage, 2)
    response.total_mass = round(response.fat_mass + response.fat_free_mass, 2)

    return response

# Procesa la seccion de deseables
def process_desirable_results(splitedText: list, index_start: int) -> TalinaDesirableDTO:
    response = TalinaDesirableDTO()

    weight = get_number(splitedText[index_start])
    response.min_weight = float(weight[0])
    response.max_weight = float(weight[1])

    body_fat_porcentage = get_number(splitedText[index_start + 1])
    response.min_fat_porcentage = float(body_fat_porcentage[0])
    response.max_fat_porcentage = float(body_fat_porcentage[1])

    body_fat_mass = get_number(splitedText[index_start + 2])
    response.min_fat_mass = float(body_fat_mass[0])
    response.max_fat_mass = float(body_fat_mass[1])

    bmi = get_number(splitedText[index_start + 3])
    response.min_bmi = float(bmi[0])
    response.max_bmi = float(bmi[1])

    return response

################## PROCESAR DATOS DE CABECERA ##################

# Obtiene numero de una cadena
def get_number(text : str) -> list:
    pattern = re.compile(r"\d+\.?\d*")
    matches = pattern.findall(text)

    return matches

# Obtiene la altura y la cambia a CM
def get_height(text : str) -> Decimal:
    matches = get_number(text)

    feetsToInches = float(matches[0]) * 12
    totalInches = feetsToInches + float(matches[1])

    return totalInches * 2.54

# Devuelve cadena de texto sin numeros ni espacios
def remove_numbers(string: str) -> str:
    string = re.sub(r"\d+", "", string)

    return string.strip()

################## PROCESAR DATOS DE RESULTADOS ##################

# Devuelve la primera cadena con un lb para conocer inicio de resultados
def find_first_lb(lst: list) -> int:

    for i, item in enumerate(lst):
        if isinstance(item, str) and "lb" in item:
            return i

    return -1

# Devuelve el lado mas pesado. Balanced si esta balanciado
def calculate_balance(leftSide : Decimal, rightSide: Decimal) -> str:
    if (leftSide == rightSide):
        return "Balanced"
    
    if(leftSide > rightSide):
        return "Left"
    
    return "Right"

# Unifica varios elementos del array en uno solo
def joinElementsByIdex(splitedData: list, init_index: int, end_index: int) -> str:
    return "".join(splitedData[init_index:end_index])

# Procesa las medidas a traves de comentarios (si es posible)
def processMeasures(comments: str) -> TalinaMeasuresDTO:
    response = TalinaMeasuresDTO()

    measures = comments.split(",")

    if (len(measures) == 8):
        response.chest = float(get_number(measures[0])[0])
        response.high_waist = float(get_number(measures[1])[0])
        response.low_waist = float(get_number(measures[2])[0])
        response.high_hip = float(get_number(measures[3])[0])
        response.low_hip = float(get_number(measures[4])[0])
        response.right_arm = float(get_number(measures[5])[0])
        response.lef_arm = float(get_number(measures[6])[0])
        response.legs = float(get_number(measures[7])[0])

    return response