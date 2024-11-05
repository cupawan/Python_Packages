import os
import pytz
import datetime
from datetime import timedelta
from garminconnect import Garmin
from collections import defaultdict
from Boto3Toolkit import Boto3Utils
from DatetimeUtils import CommonUtils
import logging

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

class GarminAPI:
    def __init__(self):
        self.today = datetime.date.today()
        self.api = self.setUpGarmin()
        self.login  = self.api.login()
        self.today_c_date = self.today.strftime("%Y-%m-%d")
        self.yesterday = self.today - timedelta(days = 1)
        self.yesterday_c_date = self.yesterday.strftime("%Y-%m-%d")
        self.utils = CommonUtils()
        
    def setUpGarmin(self):
        try:
            api = Garmin(os.environ["MyEmailAddress"], os.environ["MyGarminPassword"])
        except Exception as e:
            print(f"Error logging in Garmin API: {e}")
            api = None
        return api

    def getSleepStats(self):
        try:
            logger.info("Fetching Sleep Statistics from Garmin")
            sleep_data = self.api.get_sleep_data(self.today_c_date)
            sleep_dict = defaultdict(lambda:0)
            calendar_date = sleep_data['dailySleepDTO']['calendarDate']
            date_object = datetime.datetime.strptime(calendar_date, '%Y-%m-%d')
            formatted_date = date_object.strftime('%a, %d %b %y')
            sleep_score = sleep_data['dailySleepDTO']['sleepScores']['overall']['value']
            total_duration = sleep_data['dailySleepDTO']['sleepScores']['totalDuration']['qualifierKey'].title()
            total_sleep_seconds = sleep_data['dailySleepDTO']['sleepTimeSeconds']
            avg_sleep_stress = sleep_data['dailySleepDTO']['avgSleepStress']
            awake_count = sleep_data['dailySleepDTO']['sleepScores']['awakeCount']['qualifierKey'].title()
            awake_seconds = sleep_data['dailySleepDTO']['awakeSleepSeconds']
            awake_value = sleep_data['dailySleepDTO']['awakeCount']
            awake_start = int(sleep_data['dailySleepDTO']['sleepScores']['awakeCount']['optimalStart'])
            awake_end = int(sleep_data['dailySleepDTO']['sleepScores']['awakeCount']['optimalEnd'])
            rem_percentage = sleep_data['dailySleepDTO']['sleepScores']['remPercentage']['qualifierKey'].title()
            rem_value = sleep_data['dailySleepDTO']['sleepScores']['remPercentage']['value']
            rem_seconds = sleep_data['dailySleepDTO']['remSleepSeconds']
            rem_start = int(sleep_data['dailySleepDTO']['sleepScores']['remPercentage']['optimalStart'])
            rem_end = int(sleep_data['dailySleepDTO']['sleepScores']['remPercentage']['optimalEnd'])
            light_seconds = sleep_data['dailySleepDTO']['lightSleepSeconds']
            light_percentage = sleep_data['dailySleepDTO']['sleepScores']['lightPercentage']['qualifierKey'].title()
            light_value = sleep_data['dailySleepDTO']['sleepScores']['lightPercentage']['value']
            light_start = int(sleep_data['dailySleepDTO']['sleepScores']['lightPercentage']['optimalStart'])
            light_end = int(sleep_data['dailySleepDTO']['sleepScores']['lightPercentage']['optimalEnd'])
            restlessness = sleep_data['dailySleepDTO']['sleepScores']['restlessness']['qualifierKey'].title()
            restless_moments_count = sleep_data['restlessMomentsCount']
            deep_seconds = sleep_data['dailySleepDTO']['deepSleepSeconds']
            deep_percentage = sleep_data['dailySleepDTO']['sleepScores']['deepPercentage']['qualifierKey'].title()
            deep_value = sleep_data['dailySleepDTO']['sleepScores']['deepPercentage']['value']
            deep_start = int(sleep_data['dailySleepDTO']['sleepScores']['deepPercentage']['optimalStart'])
            deep_end = int(sleep_data['dailySleepDTO']['sleepScores']['deepPercentage']['optimalEnd'])
            body_battery_change  = sleep_data['bodyBatteryChange']
            resting_heartrate = sleep_data['restingHeartRate']
            feedback = sleep_data['dailySleepDTO']['sleepScoreFeedback']
            ist = pytz.timezone('Asia/Kolkata')
            sleep_start_ts = sleep_data['dailySleepDTO']['sleepStartTimestampGMT']/1000
            sleep_end_ts = sleep_data['dailySleepDTO']['sleepEndTimestampGMT']/1000
            sleep_start = datetime.datetime.fromtimestamp(sleep_start_ts).astimezone(ist).strftime("%H:%M")
            sleep_end = datetime.datetime.fromtimestamp(sleep_end_ts).astimezone(ist).strftime("%H:%M")
            sleep_dict = {
                'formatted_date': formatted_date,'total_time' : self.utils.seconds_to_hm(total_sleep_seconds),'from_' : sleep_start,'to_' : sleep_end,'sleep_score' : f"{sleep_score}/100",'quality' : total_duration,'REM_Quality' : rem_percentage,'REM_Time' : self.utils.seconds_to_hm(rem_seconds),'REM_Score' : rem_value,'REM_Optimal' : f"{rem_start}-{rem_end}",'Light_Quality' : light_percentage,'Light_Time' : self.utils.seconds_to_hm(light_seconds),'Light_Score' : light_value,'Light_Optimal' : f"{light_start}-{light_end}",'Deep_Quality' : deep_percentage,'Deep_Time' : self.utils.seconds_to_hm(deep_seconds),'Deep_Score' : deep_value,'Deep_Optimal' : f"{deep_start}-{deep_end}",'Awake_Quality' : awake_count,"Awake_Time" : self.utils.seconds_to_hm(awake_seconds),"Awake_Score" : awake_value,"Awake_Optimal" : f"{awake_start}-{awake_end}","Average_Sleep_Stress" : int(avg_sleep_stress),"Body Battery Change" : body_battery_change,"Resting Heart Rate" : resting_heartrate,"Restlessness Level" : restlessness,"Restless moments" : restless_moments_count,"Sleep Feedback" : feedback.title().replace('_',' ')
                }
            logger.info("Generated Sleep Statistics Data Successfully")
            return sleep_dict
        except Exception:
            logger.error("[Sleep]: No Sleep Data Found")
            raise 
    
    def getYesterdayBodyStats(self):
        try:
            logger.info(f"Fetching Body Statistics for {self.yesterday_c_date}")
            garmin_body_stats = self.api.get_stats_and_body(self.yesterday_c_date)
            date_object = datetime.datetime.strptime(garmin_body_stats['calendarDate'], '%Y-%m-%d')
            formatted_date = date_object.strftime('%a, %d %b %y')
            d = {
                "formatted_date" : formatted_date,
                "Total kcal": int(garmin_body_stats['totalKilocalories']),
                "Active kcal": int(garmin_body_stats['activeKilocalories']),
                "Total Steps / Goal": f"{garmin_body_stats['totalSteps']} / {garmin_body_stats['dailyStepGoal']}",
                "Distance": garmin_body_stats['totalDistanceMeters'],
                "Highly Active Duration": self.utils.seconds_to_hm(garmin_body_stats['highlyActiveSeconds']),
                "Active Duration": self.utils.seconds_to_hm(garmin_body_stats['activeSeconds']),
                "Sedentary Duration": self.utils.seconds_to_hm(garmin_body_stats['sedentarySeconds']),
                "Moderate Intensity Minutes": garmin_body_stats['moderateIntensityMinutes'],
                "Vigorous Intensity Minutes": garmin_body_stats['vigorousIntensityMinutes'],
                "Floors Up": int(garmin_body_stats['floorsAscended']),
                "Floors Down": int(garmin_body_stats['floorsDescended']),
                "Heart Rate - Min/Resting/Max": f"{garmin_body_stats['minHeartRate']} / {garmin_body_stats['restingHeartRate']} / {garmin_body_stats['maxHeartRate']}",
                "Last Seven Days Avg RHR": garmin_body_stats['lastSevenDaysAvgRestingHeartRate'],
                "Avg Stress": garmin_body_stats['averageStressLevel'],
                "Max Stress": garmin_body_stats['maxStressLevel'],
                "Stress Duration": self.utils.seconds_to_hm(garmin_body_stats['stressDuration']),
                "Blood Oxygen (SpO2)": garmin_body_stats['averageSpo2']
                }        
            logger.info("Generated Body Statistics Data Successfully")
            return d
        except Exception:
            logger.error("[Body]: No Body Statistics Found")
            raise
    
    def getTodayBodyStats(self):
        stats = self.api.get_stats_and_body(self.today_c_date)
        return stats

    def getActivitiesByDateRange(self, start_date, end_date):
        data = self.api.get_activities_by_date(startdate=start_date, enddate=end_date)
        return data
    
    def getActivitiesForDate(self, fordate):
        data = self.api.get_activities_fordate(fordate = fordate)
        return data
    
    def getActivityById(self, activity_id):
        data = self.api.get_activity(activity_id = activity_id)
        return data

    def getActivityDetailsById(self, activity_id):
        data = self.api.get_activity(activity_id = activity_id)
        return data

    def getGearForActivityId(self,activity_id):
        data = self.api.get_activity_gear(activity_id=activity_id)
        return data[0]['customMakeModel']
    
    def getLastActivity(self):
        data = self.api.get_last_activity()
        return data
    
    def getYesterdayActivity(self):
        data = self.api.get_activities_fordate(fordate = self.yesterday_c_date)
        return data
    
    def getProgressSummaryBetweenDates(self, start_date, end_date):
        data = self.api.get_progress_summary_between_dates(startdate= start_date, enddate= end_date)
        return data
    
    def getUserSummary(self, cdate):
        data = self.api.get_user_summary(cdate)
        return data
    
    def getRunningData(self):
        d = defaultdict(lambda:0)
        metadata = defaultdict(lambda:0)
        logger.info("Fetching Running Data")
        data = self.getActivitiesForDate(self.today_c_date)
        if not data:
            raise KeyError
        metadata['device_name'] = self.getPrimaryTrainingDevice()[0]
        metadata['device_image'] = self.getPrimaryTrainingDevice()[1]
        for i in data['ActivitiesForDay']['payload']:
            if i['activityType']['typeKey'] == "running":
                activity_id = i['activityId']
                data = self.getActivityById(activity_id)
                metadata['profile_image'] = data['metadataDTO']['userInfoDto']['profileImageUrlMedium']
                metadata['user_name'] = data['metadataDTO']['userInfoDto']['fullname']
                metadata['location_name'] = data.get('locationName', 'Unknown Location')
                metadata['gear'] = self.getGearForActivityId(activity_id=activity_id)
                d["activity_name"] = data['activityName']
                d["activity_type"] = data['activityTypeDTO']['typeKey'].title()
                d["user_name"] = data['metadataDTO']['userInfoDto']['fullname']
                d["profile_image"] = data['metadataDTO']['userInfoDto']['profileImageUrlMedium']
                d["location_name"] = data.get('locationName', 'Unknown Location')
                start_time = data['summaryDTO'].get('startTimeLocal', None)
                d["formatted_start_time"] = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.%f").strftime("%a, %d %b %Y at %H:%M %p") if start_time else "Unknown Time"
                d["formatted_date"] = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.%f").strftime("%a, %d %b %y") if start_time else "Unknown Date"
                d["distance"] = data['summaryDTO'].get('distance', 0) / 1000
                d["duration"] = self.utils.seconds_to_hm(data['summaryDTO'].get('duration', 0))
                d["avg_pace"] = CommonUtils().convert_speed_mps_to_minkm(data['summaryDTO'].get('averageSpeed', 0))
                d["max_pace"] = CommonUtils().convert_speed_mps_to_minkm(data['summaryDTO'].get('maxSpeed', 0))
                d["calories"] = data['summaryDTO'].get('calories', 0)
                d["avg_hr"] = data['summaryDTO'].get('averageHR', 0)
                d["max_hr"] = data['summaryDTO'].get('maxHR', 0)
                d["avg_cadence"] = int(data['summaryDTO'].get('averageRunCadence', 0))
                d["max_cadence"] = int(data['summaryDTO'].get('maxRunCadence', 0))
                d["training_effect"] = data['summaryDTO'].get('trainingEffectLabel', "Not Available")
                d["ground_contact_time"] = round(data['summaryDTO'].get('groundContactTime',0),1)
                d['stride_length'] = round(data['summaryDTO'].get('strideLength',0)/100,2)
                d['verticalRatio'] = data['summaryDTO'].get('verticalRatio',0)
                d['training_load'] = round(data['summaryDTO']['activityTrainingLoad'],2)
                d['is_PR'] = data['metadataDTO']['personalRecord']
                return d, metadata, activity_id
            else:
                logger.error("[Running]: No Running Data Found")
                raise

    def getRunningStreak(self, streakStart= "2024-8-1"):
        logger.info("Fetching Run Streak")
        activities = self.api.get_activities_by_date(streakStart, self.today_c_date)
        running_activity_dates = []        
        for activity in activities:
            if activity['activityType']['typeKey'] == 'running':
                activity_date = datetime.datetime.strptime(activity['startTimeLocal'], "%Y-%m-%d %H:%M:%S")
                running_activity_dates.append(activity_date.date())        
        running_activity_dates.sort(reverse=True)
        streak = 0
        current_date = datetime.date.today()        
        for run_date in running_activity_dates:
            if run_date == current_date:
                streak += 1
            elif run_date == current_date - datetime.timedelta(days=1):
                day_flag = True
                streak += 1
                current_date -= datetime.timedelta(days=1)
            else:
                break
        logger.info(f"Your Run Streak is {streak} Days.")
        return streak, day_flag
           
    def getPrimaryTrainingDevice(self):
        device = self.api.get_primary_training_device()
        return device['WearableDevices']['deviceWeights'][0]['displayName'],\
            device['WearableDevices']['deviceWeights'][0]['imageUrl']
    
    def getMapImage(self, activity_id):
        activity_details = self.api.get_activity_details(activity_id)
        polyline = activity_details['geoPolylineDTO']['polyline']
        coordinates = [(i['lat'], i['lon']) for i in polyline]
        path = "|".join([f"{lat},{lon}" for lat, lon in coordinates])
        map_url = f"{os.environ["GoogleMapsApiPath"].replace("=//","://")}{path}&key={os.environ["GoogleApiKey"]}"
        return map_url

    