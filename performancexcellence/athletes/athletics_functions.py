from competitions.models import Competition, CompetitionEvent
from django.db.models import Max, Case, When, Value, CharField, Q, F
from django.db.models.functions import Coalesce
from django.db.models import OuterRef, Subquery
from django.db.models import Max, Case, When, Value, CharField, Q, F
from django.db.models.functions import Coalesce, Substr
from competitions.models import Competition, CompetitionEvent
from datetime import date, timedelta
from datetime import datetime
import pandas as pd
from wellness.models import WellnessDaily

def progression_by_year(athlete_id, event_name):
    # Retrieve the data from the database
    all_results = Competition.objects.filter(athlete=athlete_id)
    event = CompetitionEvent.objects.get(event_name=event_name)
    # Convert querysets to DataFrames
    results_df = pd.DataFrame(list(all_results.values()))
    events_df = pd.DataFrame([event.__dict__])
    # Perform a left join to combine the two DataFrames based on 'event' column
    df = results_df.merge(events_df, left_on='event_id', right_on='id', how='inner')
    df = df[((df.competition_wind <= 2.0) & (df.wind_direction == '+')) | (df.wind_direction == '-')]
    # Select specific columns after the join
    selected_columns = ["event_name", "competition_result", "wind_direction", "competition_wind", "competition_date"]
    df = df[selected_columns]
    # Convert competition_date to datetime format
    df['competition_date'] = pd.to_datetime(df['competition_date'])
    
    # Extract year from competition_date and add it as a new column
    df['year'] = df['competition_date'].dt.year

    # Determine whether to use max() or min() based on the event type
    results_in_meters_or_points = ["ShotPut", "Discus", "Hammer", "Javelin", "LongJump", "HighJump", "PoleVault", "TripleJump", "Heptathlon", "Decathlon", "Octathlon"]
    if event_name in results_in_meters_or_points:
        aggregated_df = df.groupby(["event_name", "year"])["competition_result"].max().reset_index()
    else:
        aggregated_df = df.groupby(["event_name", "year"])["competition_result"].min().reset_index()

    # Convert DataFrame to dictionary
    result_dict = {}
    for index, row in aggregated_df.iterrows():
        event = row['event_name']
        year = row['year']
        result = row['competition_result']

        if event not in result_dict:
            result_dict[event] = {'years': [], 'results': []}
        
        result_dict[event]['years'].append(year)
        result_dict[event]['results'].append(result)
    # Print the final dictionary
    return result_dict

def personal_bests(athlete_id):
    best_results = (
        Competition.objects.filter(athlete_id=athlete_id)
        .exclude(Q(wind_direction='+') & Q(competition_wind__gt=2.0))
        .values('event')
        .annotate(
            max_competition_result=Max(Case(
                When(
                    Q(wind_direction='+') | Q(competition_wind__lte=2.0),
                    then=F('competition_result')
                ),
                default=Value(None),
                output_field=CharField(),
            ))
        )
    )
    
    competition_results_valid = (
        Competition.objects.filter(athlete_id=athlete_id)
        .filter(
            Q(wind_direction='+') & Q(competition_wind__lte=2.0) |
            Q(competition_result=Subquery(best_results.filter(event=OuterRef('event')).values('max_competition_result')))
        )
        .values('event', 'competition_name', 'competition_local', 'competition_date', 'competition_result', 'wind_direction', 'competition_wind')
    )

    # Create a dictionary to store the best result for each event_name
    best_results_dict = {}
    for record in competition_results_valid:
        event_name = CompetitionEvent.objects.get(id=record['event']).event_name
        if event_name not in best_results_dict or record['competition_result'] < best_results_dict[event_name]['competition_result']:
            best_results_dict[event_name] = record
    
    # Convert the dictionary values to a list
    records_list = list(best_results_dict.values())
    
        # Add event_name to each dictionary
    for record in records_list:
        event_id = record['event']
        event_name = CompetitionEvent.objects.get(id=event_id).event_name
        record['event_name'] = event_name

    return records_list

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



