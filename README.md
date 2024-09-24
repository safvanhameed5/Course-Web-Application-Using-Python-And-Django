# Course-Web-Application-Using-Python-And-Django

## Overview
This project is a simple Django web application designed to display a list of courses and the details of each course's videos. It utilizes two JSON files to simulate API responses for fetching course information and videos for a selected course.

## Features
- **Course List Page**: Displays the available courses using data from `get_all_courses_API_response.json`. Users can filter the courses using the provided facets and select a course to view its details.
- **Course Detail Page**: Displays a list of videos for the selected course using data from `get_course_detail_API_response.json`. Users can play a video by selecting it.

## Pages
1. **Course List Page**:
   - Shows all available courses.
   - Implements filters for courses based on the facets provided in the JSON response.
   - Clicking on a course redirects the user to the Course Detail page.

2. **Course Detail Page**:
   - Displays the course’s videos.
   - Allows the user to select and play videos from the list.

