from DatetimeUtils import CommonUtils

class Formatter:
    def __init__(self):
        pass

    def running_html(self, running_data, metadata):
        return f"""
        <h3 class="section-title">Running ({running_data['formatted_date']})</h3> 
        <div style="text-align: center; margin-bottom: 20px;">
        <img src="{metadata['mapUrl']}" alt="Running Map" style="max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 8px; display: block; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            </div>
        <div style="text-align: left; margin-bottom: 20px;">
        <h2 style="font-weight: bold; color: #00bfa5;">Streak: {metadata['streak']} Days</h2>
    </div>
        <table style="width:100%; border-collapse: collapse; text-align: left;">
            <tr>
                <th style="border-bottom: 1px solid #ddd; padding: 8px;">Metric</th>
                <th style="border-bottom: 1px solid #ddd; padding: 8px;">Value</th>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Activity Name</strong></td>
                <td style="padding: 8px;">{running_data['activity_name']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Start Time</strong></td>
                <td style="padding: 8px;">{running_data['formatted_start_time']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Distance</strong></td>
                <td style="padding: 8px;">{running_data['distance']:.2f} km</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Duration</strong></td>
                <td style="padding: 8px;">{running_data['duration']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Average Pace</strong></td>
                <td style="padding: 8px;">{running_data['avg_pace']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Best Pace</strong></td>
                <td style="padding: 8px;">{running_data['max_pace']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Calories Burned</strong></td>
                <td style="padding: 8px;">{running_data['calories']} kcal</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Avg HR</strong></td>
                <td style="padding: 8px;">{running_data['avg_hr']} bpm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Max HR</strong></td>
                <td style="padding: 8px;">{running_data['max_hr']} bpm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Avg Cadence</strong></td>
                <td style="padding: 8px;">{running_data['avg_cadence']} spm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Max Cadence</strong></td>
                <td style="padding: 8px;">{running_data['max_cadence']} spm</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Stride Length</strong></td>
                <td style="padding: 8px;">{running_data['stride_length']} m</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Training Effect</strong></td>
                <td style="padding: 8px;">{running_data['training_effect']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Training Load</strong></td>
                <td style="padding: 8px;">{running_data['training_load']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Ground Contact Time</strong></td>
                <td style="padding: 8px;">{running_data['ground_contact_time']}</td>
            </tr>
            <tr>
                <td style="padding: 8px;"><strong>Shoes</strong></td>
                <td style="padding: 8px;">{metadata['gear']}</td>
            </tr>
        </table>
        """

    def running_text(self, running_data, metadata):
        return f"""
Running ({running_data['formatted_date']})
=========================
Streak: {metadata['streak']} Days
{running_data['activity_name']}
{running_data['formatted_start_time']}
Distance: {running_data['distance']:.2f} kms
Duration: {running_data['duration']}
Avg Pace: {running_data['avg_pace']}
Best Pace: {running_data['max_pace']}
Calories: {running_data['calories']} kcal
Avg HR: {running_data['avg_hr']} bpm
Max HR: {running_data['max_hr']} bpm
Avg Cadence: {running_data['avg_cadence']} spm
Max Cadence: {running_data['max_cadence']} spm
Stride Length: {running_data['stride_length']} m
Training Effect: {running_data['training_effect']}
Training Load: {running_data['training_load']}
Ground Contact Time: {running_data['ground_contact_time']}
Shoes: {metadata['gear']}
"""

    def sleep_html(self, sleep_data):
        return f"""
            <h3 class="section-title">Sleep ({sleep_data['formatted_date']})</h3>
            <table class="data-table">
                <tr><th>Overall Sleep Summary</th></tr>
                <tr><td>You slept for {sleep_data['total_time']}, from {sleep_data['from_']} to {sleep_data['to_']}</td></tr>
                <tr><td>Score: <span class="score">{sleep_data['sleep_score']} ({sleep_data['quality']})</span></td></tr>
                <tr><td>Feedback: <span class="score">{sleep_data['Sleep Feedback']}</span></td></tr>
            </table>
            <table class="data-table">
                <tr><th>Sleep Stages</th><th>Quality</th><th>Time</th><th>Score</th><th>Optimal</th></tr>
                <tr><td>REM Sleep</td> <td>{sleep_data['REM_Quality']}</td><td>{sleep_data['REM_Time']}</td><td>{sleep_data['REM_Score']}</td><td>{sleep_data['REM_Optimal']}</td></tr>
                <tr><td>Light Sleep</td> <td>{sleep_data['Light_Quality']}</td><td>{sleep_data['Light_Time']}</td><td>{sleep_data['Light_Score']}</td><td>{sleep_data['Light_Optimal']}</td></tr>
                <tr><td>Deep Sleep</td> <td>{sleep_data['Deep_Quality']}</td><td>{sleep_data['Deep_Time']}</td><td>{sleep_data['Deep_Score']}</td><td>{sleep_data['Deep_Optimal']}</td></tr>
                <tr><td>Awake</td> <td>{sleep_data['Awake_Quality']}</td><td>{sleep_data['Awake_Time']}</td><td>{sleep_data['Awake_Score']}</td><td>{sleep_data['Awake_Optimal']}</td></tr>
            </table>
            <table class="data-table">
                <tr><th>Additional Metrics</th></tr>
                <tr><td>Avg Sleep Stress</td> <td>{sleep_data['Average_Sleep_Stress']}</td></tr>
                 <tr><td>Battery Change</td> <td>{sleep_data['Body Battery Change']}</td></tr>
                 <tr><td>Resting HR</td> <td>{sleep_data['Resting Heart Rate']}</td></tr>
                 <tr><td>Restlessness Level</td> <td>{sleep_data['Restlessness Level']}</td></tr>
            </table>
            """
    
    def sleep_text(self, sleep_data):
        return f"""
Sleep ({sleep_data['formatted_date']})
=========================
You slept for {sleep_data['total_time']}, from {sleep_data['from_']} to {sleep_data['to_']}.
Score: {sleep_data['sleep_score']} ({sleep_data['quality']})
Feedback: {sleep_data['Sleep Feedback']}
Sleep Stages:
-------------
REM: {sleep_data['REM_Quality']},{sleep_data['REM_Time']},{sleep_data['REM_Score']} [{sleep_data['REM_Optimal']}]
Light: {sleep_data['Light_Quality']},{sleep_data['Light_Time']},{sleep_data['Light_Score']} [{sleep_data['Light_Optimal']}]
Deep: {sleep_data['Deep_Quality']},{sleep_data['Deep_Time']},{sleep_data['Deep_Score']} [{sleep_data['Deep_Optimal']}]
Awake: {sleep_data['Awake_Quality']},{sleep_data['Awake_Time']},{sleep_data['Awake_Score']} [{sleep_data['Awake_Optimal']}]
Additional Metrics:
-------------------
Avg Sleep Stress: {sleep_data['Average_Sleep_Stress']}
Battery Change: {sleep_data['Body Battery Change']}
Resting HR: {sleep_data['Resting Heart Rate']}
Restlessness Level: {sleep_data['Restlessness Level']}
"""

    def body_stats_html(self, body_stats_data):
        return f"""
            <h3 class="section-title">Health ({body_stats_data['formatted_date']})</h3>
            <table class="data-table">
                <tr><th>Total Calories</th><td>{body_stats_data['Total kcal']}</td></tr>
                <tr><th>Active Calories</th><td>{body_stats_data['Active kcal']}</td></tr>
                <tr><th>Total Steps / Goal</th><td>{body_stats_data['Total Steps / Goal']}</td></tr>
                <tr><th>Distance</th><td>{round(body_stats_data['Distance']/1000,2)} kms</td></tr>
                <tr><th>Highly Active Duration</th><td>{body_stats_data['Highly Active Duration']}</td></tr>
                <tr><th>Moderate Intensity Duration</th><td>{body_stats_data['Moderate Intensity Minutes']} Minutes</td></tr>
                <tr><th>Floors Up</th><td>{body_stats_data['Floors Up']}</td></tr>
                <tr><th>Floors Down</th><td>{body_stats_data['Floors Down']}</td></tr>
                <tr><th>Heart Rate (Min/Resting/Max)</th><td>{body_stats_data['Heart Rate - Min/Resting/Max']}</td></tr>
                <tr><th>Last Seven Days Avg RHR</th><td>{body_stats_data["Last Seven Days Avg RHR"]}</td></tr>
                <tr><th>Average Stress</th><td>{body_stats_data['Avg Stress']}</td></tr>
                <tr><th>Max Stress</th><td>{body_stats_data["Max Stress"]}</td></tr>
                <tr><th>Blood Oxygen (SpO2)</th><td>{body_stats_data['Blood Oxygen (SpO2)']}</td></tr>
            </table>
            """

    def newsletterEmailFormatterHtml(self, sleep_data, body_stats_data):
        try:
            message = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.5">
                 <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    width: 100%;
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    border-radius: 8px;
                    margin-top: 20px;
                }}
                .header {{
                    background-color: #0073e6;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    border-radius: 8px 8px 0 0;
                }}
                .content {{
                    padding: 20px;
                }}
                .section {{
                    margin-bottom: 30px;
                }}
                .section-title {{
                    font-size: 1.4em;
                    margin-bottom: 10px;
                    color: #0073e6;
                }}
                .stats {{
                    margin-bottom: 20px;
                    border-top: 1px solid #ddd;
                    padding-top: 10px;
                }}
                .footer img {{
                    max-width: 100%;
                    width: 100%;
                    height: auto; 
                    margin-top: 10px;
                }}

                .footer {{
                    text-align: center;
                    color: #777;
                    font-size: 0.9em;
                    padding: 10px;
                    border-top: 1px solid #ddd;
                    margin-top: 20px;
                }}
                .data-table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-bottom: 20px;
                }}
                .data-table th,
                .data-table td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;
                    background-color: #fff;
                }}
                .data-table th {{
                    color: #333;
                }}
                .score {{
                    font-weight: bold;
                }}
            </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h2>Garmin Statistics</h2>
                    </div>
                    <div class="content">
                        <div class="section">
                            <h3 class="section-title">Sleep Data for {sleep_data['formatted_date']}</h3>
                            <div class="stats">
                                <table class="data-table">
                                    <tr>
                                        <th>Overall Sleep Summary</th>
                                    </tr>
                                    <tr>
                                        <td>You slept for {sleep_data['total_time']}, from {sleep_data['from_']} to {sleep_data['to_']}</td>
                                    </tr>
                                    <tr>
                                        <td>Score: <span class="score">{sleep_data['sleep_score']} ({sleep_data['quality']})</span></td>
                                    </tr>
                                </table>

                                <table class="data-table">
                                    <tr>
                                        <th>Sleep Stages</th>
                                    </tr>
                                    <tr>
                                        <td><strong>REM Sleep:</strong></td>
                                        <td>{sleep_data['REM_Quality']}</td>
                                        <td>{sleep_data['REM_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['REM_Score']} Optimal: {sleep_data['REM_Optimal']}</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Light Sleep:</strong></td>
                                        <td>{sleep_data['Light_Quality']}</td>
                                        <td>{sleep_data['Light_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['Light_Score']} Optimal: {sleep_data['Light_Optimal']}</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Deep Sleep:</strong></td>
                                        <td>{sleep_data['Deep_Quality']}</td>
                                        <td>{sleep_data['Deep_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['Deep_Score']} Optimal: {sleep_data['Deep_Optimal']}</span></td>
                                    </tr>
                                    <tr>
                                        <td><strong>Awake:</strong></td>
                                        <td>{sleep_data['Awake_Quality']}</td>
                                        <td>{sleep_data['Awake_Time']}</td>
                                        <td>Score: <span class="score">{sleep_data['Awake_Score']} Optimal: {sleep_data['Awake_Optimal']}</span></td>
                                    </tr>
                                </table>

                                <div class="section">
                                    <div class="section-title">Additional Details</div>
                                    <div class="section-content">
                                        <p>Average Sleep Stress: {sleep_data['Average_Sleep_Stress']}</p>
                                        <p>Battery Change: {sleep_data['Body Battery Change']}</p>
                                        <p>Resting Heart Rate: {sleep_data['Resting Heart Rate']}</p>
                                        <p>Restlessness Level: {sleep_data['Restlessness Level']}</p>
                                        <p>Restless moments: {sleep_data['Restless moments']}</p>
                                        <p>Sleep Feedback: {sleep_data['Sleep Feedback']}</p>
                                    </div>
                                </div>
                            </div>

                            <div class="stats">
                                <h3 class="section-title">Body Statistics for {body_stats_data['formatted_date']}</h3>
                                <table class="data-table">
                                    <tr>
                                        <th>Total kcal</th>
                                        <td>{body_stats_data['Total kcal']}</td>
                                    </tr>
                                    <tr>
                                        <th>Active kcal</th>
                                        <td>{body_stats_data['Active kcal']}</td>
                                    </tr>
                                    <tr>
                                        <th>Total Steps / Goal</th>
                                        <td>{body_stats_data['Total Steps / Goal']}</td>
                                    </tr>
                                    <tr>
                                        <th>Distance</th>
                                        <td>{body_stats_data['Distance']}</td>
                                    </tr>
                                    <tr>
                                        <th>Highly Active Duration</th>
                                        <td>{body_stats_data['Highly Active Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Active Duration</th>
                                        <td>{body_stats_data['Active Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Sedentary Duration</th>
                                        <td>{body_stats_data['Sedentary Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Moderate Intensity Minutes</th>
                                        <td>{body_stats_data['Moderate Intensity Minutes']}</td>
                                    </tr>
                                    <tr>
                                        <th>Vigorous Intensity Minutes</th>
                                        <td>{body_stats_data['Vigorous Intensity Minutes']}</td>
                                    </tr>
                                    <tr>
                                        <th>Intensity Minutes Goal Status</th>
                                        <td>{body_stats_data['Intensity Minutes Goal Status']}</td>
                                    </tr>
                                    <tr>
                                        <th>Floors Up</th>
                                        <td>{body_stats_data['Floors Up']}</td>
                                    </tr>
                                    <tr>
                                        <th>Floors Down</th>
                                        <td>{body_stats_data['Floors Down']}</td>
                                    </tr>
                                    <tr>
                                        <th>Heart Rate - Min/Resting/Max</th>
                                        <td>{body_stats_data['Heart Rate - Min/Resting/Max']}</td>
                                    </tr>
                                    <tr>
                                        <th>Last Seven Days Avg Resting Heart Rate</th>
                                        <td>{body_stats_data['Last Seven Days Avg Resting Heart Rate']}</td>
                                    </tr>
                                    <tr>
                                        <th>Average Stress</th>
                                        <td>{body_stats_data['Average Stress']}</td>
                                    </tr>
                                    <tr>
                                        <th>Max Stress Level</th>
                                        <td>{body_stats_data['Max Stress Level']}</td>
                                    </tr>
                                    <tr>
                                        <th>Stress Duration</th>
                                        <td>{body_stats_data['Stress Duration']}</td>
                                    </tr>
                                    <tr>
                                        <th>Blood Oxygen (SpO2)</th>
                                        <td>{body_stats_data['Blood Oxygen (SpO2)']}</td>
                                    </tr>
                                </table>
                            </div>
                        </div>
                    </div>
                    <div class="footer">
                    <p>Have a great day!</p>
                    <img src="https://lh3.googleusercontent.com/pw/AP1GczMyn-jztxA6E7Va572D3c8r00tPo7PpT35tkpYqLez72sDBLXai3ZXQJEc9doLAWUGjdgkq4846yU1p3-vzDYMCvHIqYzfQ9OlONFhzeLW3DCzSggOW9RDXsntkNHvLe251U7CbQ4q2Lepast7mWo0=w808-h278-s-no" alt="Garmin Statistics" style="max-width:100px;width:100%;height:auto;margin-top:10px;">
                </div>

                </div>
            </body>
            </html>
            """
        except Exception as e:
            message = f"<p>No Data Available: {e}</p>"
            print(message)
        return message

    def formatWeatherDataHtmlTableEmail(self,data_list, day_list, name, location):
        html_content = '''<html>
        <head>
        <style>
        body { font-family: Arial, sans-serif; background-color: #f0f8ff; }
        .container { max-width: 800px; margin: 20px auto; padding: 20px; background-color: #fff; box-shadow: 0 0 10px rgba(0,0,0,0.1); border-radius: 10px; }
        .weather-card { border: 1px solid #ccc; border-radius: 5px; padding: 15px; margin-bottom: 20px; background-color: #f9f9f9; }
        .weather-header { font-size: 20px; font-weight: bold; margin-bottom: 10px; color: #333; }
        .weather-details { margin-left: 15px; }
        .weather-details p { margin: 5px 0; }
        .weather-details ul { list-style-type: none; padding: 0; }
        .weather-details ul li { margin-bottom: 5px; }
        .summary { color: #1e90ff; font-weight: bold; }
        .temp { color: #2e8b57; }
        .sunrise-sunset { color: #ffa500; }
        .wind { color: #4682b4; }
        .uv-index { color: #ff6347; }
        .greeting { background-color: #1e90ff; color: #fff; padding: 10px; border-radius: 5px; margin-bottom: 20px; }
        table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        tr:nth-child(even) { background-color: #f9f9f9; }
        tr:nth-child(odd) { background-color: #fff; }
        </style>
        </head>
        <body>
        '''

        html_content += f'''<div class="container">
        <div class="greeting">
        <h2 style="margin-top: 0;">Weather Report</h2>
        <h3 style="margin-top: 0;">Good Morning, {str(name).title()}</h3>
        <p>Weather Forecast for Today at<br><b>{str(location).title()}</b></p>
        </div>
        '''

        html_content += '<div class="weather-card">\n'
        html_content += f'<div class="weather-header">{CommonUtils().timestamp_to_date(data_list["dt"])}</div>\n'
        html_content += '<div class="weather-details">\n'
        html_content += f'<p class="summary">Summary: {data_list["summary"]}</p>\n'
        html_content += '<table>\n'
        html_content += '<tr><th>Sunrise</th><th>Sunset</th><th>Temp Day</th><th>Temp Night</th><th>Feels Like Day</th><th>Feels Like Night</th><th>Humidity</th><th>Wind</th><th>UV Index</th></tr>\n'
        html_content += f'<tr><td class="sunrise-sunset">{CommonUtils().timestamp_to_datetime(data_list["sunrise"])}</td>'
        html_content += f'<td class="sunrise-sunset">{CommonUtils().timestamp_to_datetime(data_list["sunset"])}</td>'
        html_content += f'<td class="temp">{data_list["temp"]["day"]} °C</td>'
        html_content += f'<td class="temp">{data_list["temp"]["night"]} °C</td>'
        html_content += f'<td class="temp">{data_list["feels_like"]["day"]} °C</td>'
        html_content += f'<td class="temp">{data_list["feels_like"]["night"]} °C</td>'
        html_content += f'<td>{data_list["humidity"]} %</td>'
        html_content += f'<td class="wind">{data_list["wind_speed"]} m/s, {data_list["wind_deg"]}°</td>'
        html_content += f'<td class="uv-index">{data_list["uvi"]}</td></tr>\n'
        html_content += '</table>\n'
        html_content += '</div>\n'
        html_content += '</div>\n'

        html_content += '<div class="weather-card">\n'
        html_content += '<div class="weather-header">Hourly Forecast For Next 24 Hours</div>\n'
        html_content += '<div class="weather-details">\n'
        html_content += '<table>\n'
        html_content += '<tr><th>Time</th><th>Summary</th><th>Temp</th><th>Feels Like</th><th>Humidity</th><th>Wind</th><th>UV Index</th><th>Clouds (% of sky)</th></tr>\n'
        for hour in day_list:
            html_content += f'<tr><td>{CommonUtils().timestamp_to_time(hour["dt"])}</td>'
            html_content += f'<td class="summary">{hour["weather"][0]["description"].title()}</td>'
            html_content += f'<td class="temp">{hour["temp"]} °C</td>'
            html_content += f'<td class="temp">{hour["feels_like"]} °C</td>'
            html_content += f'<td>{hour["humidity"]} %</td>'
            html_content += f'<td class="wind">{hour["wind_speed"]} m/s, {hour["wind_deg"]}°</td>'
            html_content += f'<td class="uv-index">{hour["uvi"]}</td>'
            html_content += f'<td class="uv-index">{hour["clouds"]}%</td></tr>\n'
        html_content += '</table>\n'
        html_content += '</div>\n'
        html_content += '</div>\n'

        html_content += '''<p> Have a nice day! </p><p> <em> Location not correct? Reply to this mail with correct location. </em> </p>'''
        html_content += '</div>\n'
        html_content += '</body>\n</html>'

        return html_content
    
    def redditPostsEmailFormatter(self,posts):
        body = ''''''
        for post in posts:
            post_body = ''
            post_body += f'<div><strong>{post.author}</strong></div>\n'
            if post.is_video:
                post_body += f'<p><h3>{post.title} [VIDEO]</h3></p>\n'
            else:
                post_body += f'<p><h3>{post.title}</h3></p>\n'        
            if post.selftext:
                post_body += f'<p>{post.selftext}</p>\n'
            if hasattr(post, 'preview') and 'images' in post.preview:
                all_images = [x['source'] for x in post.preview['images']]
                for image in all_images:
                    post_body += f'<img src="{image["url"]}" alt="Post Image">\n'
            post_body += f'<p>Upvotes: {post.ups} Comments: {post.num_comments}</p>'        
            if post.is_video:
                post_body += f"<br><a class='watch-video-btn' href='https://reddit.com{post.permalink}'> Watch Video</a>"
            else:
                post_body += f"<br><a class='watch-video-btn' href='https://reddit.com{post.permalink}'> See on Reddit</a>"        
            post_body += '</div>\n'
            post_body += "<hr>"
            body += post_body
        body += "<p>Wishing you a wonderful day!</p>"
        return body
