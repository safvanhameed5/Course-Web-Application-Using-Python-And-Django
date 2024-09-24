import json
from django.shortcuts import render
from django.http import Http404


def load_courses():
    with open('../mycourse/api/get_all_courses_API_response.json') as f:
        return json.load(f)


def load_course_details(course_id):
    with open('../mycourse/api/get_course_detail_API_response.json') as f:
        details = json.load(f)
        # Compare as string if course_id is an integer in JSON
        if str(details['course_id']) == str(course_id):
            return details['videos']
    return None  # Return None if course_id does not match


def course_list(request):
    data = load_courses()
    courses = data.get('courses', [])
    return render(request, 'main/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    data = load_courses()
    courses = data.get('courses', [])
    videos = load_course_details(course_id)

    if videos is None:
        raise Http404("Course not found.")

    # Add course_id to the context
    return render(request, 'main/course_detail.html', {
        'videos': videos,
        'course_id': course_id,  # Pass course_id to the template
        'courses': courses
    })
