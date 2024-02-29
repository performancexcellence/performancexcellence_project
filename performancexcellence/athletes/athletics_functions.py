from competitions.models import Competition, CompetitionEvent
import pandas as pd
from datetime import date, datetime, timedelta
from django.db.models import Min, Max, Case, When
from django.db.models.functions import Cast
from django.db.models import DateTimeField
import datetime

def format_duration(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    seconds, centiseconds = divmod(seconds, 1)
    centiseconds = round(centiseconds, 2) * 100

    if minutes:
        formatted_duration = f"{int(minutes)}:{int(seconds):02d}.{int(centiseconds):02d}"
    else:
        formatted_duration = f"{int(seconds):02d}.{int(centiseconds):02d}"

    return formatted_duration

def get_competitions(athlete):
    competitions = Competition.objects.filter(athlete=athlete, competition_wind__lte=2.0)
    for competition in competitions:
        if competition.is_timing:
            # Convert to Duration
            competition.result = datetime.timedelta(seconds=float(competition.result))
        else:
            # Convert to float
            competition.result = float(competition.result)
    return competitions

def personal_bests(athlete_id):
    # Retrieve all events for the athlete
    events = CompetitionEvent.objects.all()
    competitions = get_competitions(athlete_id)

    # Create a dictionary to store the best result for each event
    best_results = {}

    for competition in competitions:
        event = competition.event
        if competition.is_timing:
            competition.result = format_duration(competition.result.total_seconds())
            # If the event is not in the dictionary or the new result is better, update the dictionary
            if event not in best_results or competition.result < best_results[event].result:
                best_results[event] = competition
        else:
            competition.result = competition.result
            # If the event is not in the dictionary or the new result is better, update the dictionary
            if event not in best_results or competition.result > best_results[event].result:
                best_results[event] = competition

    # Convert the dictionary values to a list
    best_competitions = list(best_results.values())

    return best_competitions


def get_progression(athlete_id, event_name, period):
    print(period)
    # Retrieve the specific event based on event_name
    event = CompetitionEvent.objects.get(event_name=event_name)

    # Filter results based on athlete and the specific event
    competitions_results = get_competitions(athlete_id)
    x_axis = []
    y_axis = []
    if period == 'Best By Year':
        # Get the best result of each year for the event
        array_results = []
        unique_years = set(result.date.year for result in competitions_results)
        for year in unique_years:
            best_result = competitions_results.filter(event=event, date__year=year).order_by('result').first()
            if best_result:
                array_results.append(best_result)

        # Order the array_results by date
        array_results = sorted(array_results, key=lambda x: x.date)
    else:
        array_results= []
        # Get all results of the year for the event
        results = competitions_results.filter(event=event)
        for result in results:
            if str(result.date.year) == str(period):
                array_results.append(result)
                x_axis.append(result.date.month)
    x_axis = []
    y_axis = []
    for result in array_results:
        x_axis.append(result.date.strftime("%Y-%m-%d"))
        result_converted = result.result
        y_axis.append(result_converted)

    return x_axis, y_axis


def wellness(wellness_registers):
    result_dict = {"weight": [], "mood": [], "stress": [], "sleep_quality": [], "soreness": [], "fatigue": [], "average": [], "registration_date": [], "hydration": [], "nutrition": [], "sleep_hours": []}
    try:
        # The `values()` method returns an iterator over the values of the dictionary, which is not iterable.
        # To iterate over the values of the dictionary, use `iter(wellness_registers.values())`.
        results_df = pd.DataFrame(list(iter(wellness_registers.values())))
        for index, row in results_df.iterrows():
            mood = row['mood']
            stress_levels = row['stress_level']
            sleep_quality = row['sleep_quality']
            muscle_soreness = row['muscle_soreness']
            fatigue = row['fatigue']
            nutrition = row['nutrition']
            hydration = row['hydration']
            weight = row['weight']
            sleep_hours = row['hours_sleep']
            registration_date = row['registration_date'].strftime("%Y-%m-%d")
            average = (mood + stress_levels + sleep_quality + muscle_soreness + fatigue + nutrition + hydration) / 7
            result_dict["mood"].append(mood)
            result_dict["stress"].append(stress_levels)
            result_dict["sleep_quality"].append(sleep_quality)
            result_dict["soreness"].append(muscle_soreness)
            result_dict["fatigue"].append(fatigue)
            result_dict["average"].append(average)
            result_dict["registration_date"].append(registration_date)
            result_dict["nutrition"].append(nutrition)
            result_dict["weight"].append(weight)
            result_dict["hydration"].append(hydration)
            result_dict["sleep_hours"].append(sleep_hours)
    except:
        pass
    return result_dict

def load(load_register):
    result_dict = {"load": [], "training_hours": [], "intensity": [], "registration_date": []}
    try:
        # The `values()` method returns an iterator over the values of the dictionary, which is not iterable.
        # To iterate over the values of the dictionary, use `iter(wellness_registers.values())`.
        results_df = pd.DataFrame(list(iter(load_register.values())))
        for index, row in results_df.iterrows():
            load = row['load']
            training_hours = row['training_hours']
            intensity = row['intensity']
            registration_date = row['registration_date'].strftime("%Y-%m-%d")
            result_dict["load"].append(load)
            result_dict["training_hours"].append(training_hours)
            result_dict["intensity"].append(intensity)
            result_dict["registration_date"].append(registration_date)
    except:
        pass
    return result_dict

def weekly_wellness(wellness_registers):
    results_df = pd.DataFrame(list(iter(wellness_registers.values())))

    # Convert the registration_date column to datetime format
    results_df['registration_date'] = pd.to_datetime(results_df['registration_date'])

    # Calculate the start of the week for each registration date
    results_df['week_start'] = results_df['registration_date'] - pd.to_timedelta(results_df['registration_date'].dt.dayofweek, unit='D')

    weekly_data = results_df.groupby('week_start')

    result_dict = {
        "weight": [],
        "mood": [],
        "stress": [],
        "sleep_quality": [],
        "soreness": [],
        "fatigue": [],
        "average": [],
        "week_start": [],
        "hydration": [],
        "nutrition": [],
        "sleep_hours": []
    }

    for week_start, group_data in weekly_data:
        mood_avg = group_data['mood'].mean()
        stress_avg = group_data['stress_level'].mean()
        sleep_quality_avg = group_data['sleep_quality'].mean()
        soreness_avg = group_data['muscle_soreness'].mean()
        fatigue_avg = group_data['fatigue'].mean()
        nutrition_avg = group_data['nutrition'].mean()
        hydration_avg = group_data['hydration'].mean()
        weight_avg = group_data['weight'].mean()
        sleep_hours_avg = group_data['hours_sleep'].mean()
        overall_avg = (mood_avg + stress_avg + sleep_quality_avg + soreness_avg + fatigue_avg + nutrition_avg + hydration_avg) / 7

        result_dict["mood"].append(mood_avg)
        result_dict["stress"].append(stress_avg)
        result_dict["sleep_quality"].append(sleep_quality_avg)
        result_dict["soreness"].append(soreness_avg)
        result_dict["fatigue"].append(fatigue_avg)
        result_dict["average"].append(overall_avg)
        result_dict["week_start"].append(week_start.strftime("%Y-%m-%d"))
        result_dict["nutrition"].append(nutrition_avg)
        result_dict["weight"].append(weight_avg)
        result_dict["hydration"].append(hydration_avg)
        result_dict["sleep_hours"].append(sleep_hours_avg)

    return result_dict

def weekly_load(load_registers):
    results_df = pd.DataFrame(list(iter(load_registers.values())))

    # Convert the registration_date column to datetime format
    results_df['registration_date'] = pd.to_datetime(results_df['registration_date'])

    # Calculate the start of the week for each registration date
    results_df['week_start'] = results_df['registration_date'] - pd.to_timedelta(results_df['registration_date'].dt.dayofweek, unit='D')

    weekly_data = results_df.groupby('week_start')

    result_dict = {
        "load": [],
        "intensity": [],
        "volume": [],
        "week_start": []

    }

    for week_start, group_data in weekly_data:
        intensity_avg = group_data['intensity'].mean()
        volume_sum = group_data['training_hours'].sum()

        result_dict["load"].append(intensity_avg*volume_sum)
        result_dict["intensity"].append(intensity_avg)
        result_dict["volume"].append(volume_sum)
        result_dict["week_start"].append(week_start.strftime("%Y-%m-%d"))

    return result_dict


def get_competitions_by_athlete(athlete_id):
    competitions = Competition.objects.filter(athlete=athlete_id)
    distinct_events = set()
    # Iterar sobre todas as competições
    for competition in competitions:
        # Adicionar o evento da competição ao set
        distinct_events.add(competition.event)

    # Retornar o set como um array
    return list(distinct_events)

def antropometric_function(antropometric_data):
    for data in antropometric_data:
        data.mg_somatorio = (
                data.prega_tricipal + data.prega_subescapular + data.prega_bicipal +
                data.prega_ilio_cristal + data.prega_supra_espinal + data.prega_abdominal +
                data.prega_coxa + data.prega_gemeo
        )
        data.peso_mg = round((data.body_fat*data.weight),2)
        data.mm_somatorio = (data.perimeter_relax_arm+ data.perimeter_strenght_arm+ data.perimeter_abdominal
                             +data.perimeter_hip+ data.perimeter_thigh)
        data.peso_mm = round((data.body_muscle*data.weight),2)
    return antropometric_data, antropometric_data.last()
